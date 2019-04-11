from antlr4 import *
from autogen.CymbolParser import CymbolParser
from autogen.CymbolVisitor import CymbolVisitor


class Type:
    VOID = "void"
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOLEAN = "boolean"


class CymbolCheckerVisitor(CymbolVisitor):
    id_values = {}

    def visitIntExpr(self, ctx: CymbolParser.IntExprContext):
        value = int(ctx.getText())
        return {'type': Type.INT, 'value': value}

    def visitStringExpr(self, ctx: CymbolParser.IntExprContext):
        value = ctx.getText()
        return {'type': Type.String, 'value': value}

    def visitFloatExpr(self, ctx: CymbolParser.FloatExprContext):
        value = float(ctx.getText())
        return {'type': Type.FLOAT, 'value': value}

    def visitBooleanExpr(self, ctx: CymbolParser.FloatExprContext):
        value = bool(ctx.getText())
        return {'type': Type.BOOLEAN, 'value': value}

    def visitVarDecl(self, ctx: CymbolParser.VarDeclContext):
        var_name = ctx.ID().getText()
        tyype = ctx.tyype().getText()
        print("tyype = " + tyype)

        if (tyype == Type.VOID):
            result = Type.VOID
            print("Mensagem de erro 1...")
            exit(1)
        else:
            if ctx.expr() != None:
                init = ctx.expr().accept(self)
                print("init = " + init["type"])
                if init != tyype:
                    print("Mensagem de erro 2...")
                    exit(2)

            result = tyype
            self.id_values[var_name] = tyype

        print("saved variable " + var_name + " of type " + tyype)
        return result

	def visitAddSubExpr(self, ctx: CymbolParser.AddSubExprContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        op = ctx.op.text

        if op == '+':
            result = left["value"] + right["value"]
        else:
            result = left["value"] - right["value"]

        print(result)
        return {'type': Type.INT, 'value': result}

    def visitMulDivExpr(self, ctx: CymbolParser.MulDivExprContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        op = ctx.op.text

        if op == '*':
            result = left["value"] * right["value"]
        else:
            result = left["value"] / right["value"]

        print(result)
        return {'type': Type.INT, 'value': result}
	
	def visitComparisonExpr(self, ctx: CymbolParser.ComparisonExprContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        op = ctx.op.text

        result = eval(str(left["value"]) + op + str(right["value"]))
        return {'type': Type.BOOLEAN, 'value': result}
	
	def visitEqExpr(self, ctx:CymbolParser.BoolExprContext):
        left = self.visit(ctx.expr()[0])
		right = self.visit(ctx.expr()[1])
		op = ctx.op.text

		if op == '==':
			result =  (left["value"] == right["value"])
		else:
			result = (left["value"] != right["value"])

		return {'type': Type.BOOLEAN, 'value': result}

    def aggregateResult(self, aggregate: Type, next_result: Type):
        return next_result if next_result != None else aggregate
