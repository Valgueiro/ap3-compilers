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

    def visitStringExpr(self, ctx: CymbolParser.StringExprContext):
        value = ctx.getText()
        return {'type': Type.STRING, 'value': value}

    def visitFloatExpr(self, ctx: CymbolParser.FloatExprContext):
        value = float(ctx.getText())
        return {'type': Type.FLOAT, 'value': value}

    def visitBooleanExpr(self, ctx: CymbolParser.BooleanExprContext):
        value = bool(ctx.getText())
        return {'type': Type.BOOLEAN, 'value': value}

    def visitVarIdExpr(self, ctx: CymbolParser.VarIdExprContext):
        var_name = ctx.ID.getText()
        return self.id_values[var_name]


    def visitVarDecl(self, ctx: CymbolParser.VarDeclContext):
        var_name = ctx.ID().getText()
        tyype = ctx.tyype().getText()

        if (tyype == Type.VOID):
            result = Type.VOID
            print("Mensagem de erro 1...")
            exit(1)
        else:
            if ctx.expr() != None:
                result = self.visit(ctx.expr())
                if result['type'] != tyype:
                    print("Mensagem de erro 2...")
                    exit(2)
                out = {'type': tyype, 'value': result['value']}
                self.id_values[var_name] = tyype

        return out

    def visitSignedExpr(self, ctx: CymbolParser.SignedExprContext):
        expr = self.visit(ctx.expr)
        op = ctx.op.text

        if expr['type'] in [Type.INT, Type.FLOAT]:
            value = expr['value']
            if op == '-':
                value *= -1
            return {'type': expr['type'], 'value': value}
        return 0

    def visitNotExpr(self, ctx: CymbolParser.NotExprContext):
        expr = self.visit(ctx.expr)

        if expr['type'] == Type.BOOLEAN:
            return {'type': Type.BOOLEAN, 'value': not expr['value']}
        return 0

    def visitComparisonExpr(self, ctx: CymbolParser.ComparisonExprContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        op = ctx.op.text

        result = eval(str(left["value"]) + op + str(right["value"]))
        return {'type': Type.BOOLEAN, 'value': result}

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

    def visitEqExpr(self, ctx: CymbolParser.EqExprContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        op = ctx.op.text

        if op == '==':
            result = (left["value"] == right["value"])
        else:
            result = (left["value"] != right["value"])

        return {'type': Type.BOOLEAN, 'value': result}

    def visitParenExpr(self, ctx: CymbolParser.ParenExprContext):
        return self.visit(ctx.expr())   
    
    def visitBoolExpr(self, ctx: CymbolParser.BoolExprContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        op = ctx.op.text

        if left['type'] == Type.BOOLEAN and right['type'] == Type.BOOLEAN:
            if op == '&&':
                result = left['value'] and right ['value']
            else:
                result = left['value'] or right ['value']
            return {'type': Type.BOOLEAN, 'value': result}
        return 0

    def aggregateResult(self, aggregate: Type, next_result: Type):
        return next_result if next_result != None else aggregate



