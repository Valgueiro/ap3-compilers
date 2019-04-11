from antlr4 import *
from autogen.CymbolParser import CymbolParser
from autogen.CymbolVisitor import CymbolVisitor


class Type:
    VOID = "void"
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOLEAN = "boolean"

# Value/IDs = {'type':, 'value': }
# Params = {'type': , 'name':}
# Functions = {'type': , 'params'}

class CymbolCheckerVisitor(CymbolVisitor):
    id_values = {}
    functions = {}

    def visitFiile(self, ctx: CymbolParser.FiileContext):
        self.visitChildren(ctx)

    def visitIntExpr(self, ctx: CymbolParser.IntExprContext):
        return {'type': Type.INT}

    def visitStringExpr(self, ctx: CymbolParser.StringExprContext):
        return {'type': Type.STRING}

    def visitFloatExpr(self, ctx: CymbolParser.FloatExprContext):
        return {'type': Type.FLOAT}

    def visitBooleanExpr(self, ctx: CymbolParser.BooleanExprContext):
        return {'type': Type.BOOLEAN}

    def visitVarIdExpr(self, ctx: CymbolParser.VarIdExprContext):
        var_name = ctx.ID().getText()
        return self.id_values[var_name]

    def visitVarDecl(self, ctx: CymbolParser.VarDeclContext):
        var_name = ctx.ID().getText()
        tyype = ctx.tyype().getText()

        if (tyype == Type.VOID):
            result = Type.VOID
            print("Mensagem de erro 1...")
            exit(1)
        else:
            if ctx.expr() is not None:
                compatible = self.isCompatible(result['type'], tyype)[0]
                if not compatible:
                    print("Mensagem de erro 2...")
                    exit(2)
            out = {'type': tyype}
            self.id_values[var_name] = out

    def visitSignedExpr(self, ctx: CymbolParser.SignedExprContext):
        expr = self.visit(ctx.expr)

        if expr['type'] in [Type.INT, Type.FLOAT]:
            return {'type': expr['type']}
        else:
            print('error')  
        return 0

    def visitNotExpr(self, ctx: CymbolParser.NotExprContext):
        expr = self.visit(ctx.expr)

        if expr['type'] == Type.BOOLEAN:
            return {'type': Type.BOOLEAN}
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
        return {'type': Type.INT}

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

    def visitFuncDecl(self, ctx: CymbolParser.FuncDeclContext):
        return_type = ctx.tyype().getText()
        name = ctx.ID().getText()
        params = {}
        if ctx.paramTypeList() is not None:
            params = self.visit(ctx.paramTypeList())
        self.functions[name] = {'type': return_type, 'params': params}
         
    def visitParamTypeList(self, ctx: CymbolParser.ParamTypeListContext):
        params = []
        for param in ctx.paramType():
            params.append(self.visit(param))
        return params

    def visitParamType(self, ctx: CymbolParser.ParamTypeContext):
        return {'type': ctx.tyype().getText(), 'name': ctx.ID().getText()}

    def visitFunctionCallExpr(self, ctx: CymbolParser.FunctionCallExprContext):
        func_name = ctx.ID().getText()
        func = self.functions[func_name]
        params_types = []
        if ctx.exprList() is not None:
            params_types = self.visit(ctx.exprList())
        
        for index, param in enumerate(params_types):
            if func['params'][index]['type'] != param:
                print("Error: wrong params")
                return 0
        
        return {'type': func['type']}

    def visitExprList(self, ctx: CymbolParser.ExprListContext):
        expr_types = []
        for expr in ctx.expr():
            print(expr.getText())
            expr_types.append(self.visit(expr)['type'])
        print
        return expr_types

    def aggregateResult(self, aggregate: Type, next_result: Type):
        return next_result if next_result != None else aggregate

    def isCompatible(self, f_type, s_type):
        numbers_type = [Type.INT, Type.FLOAT]
        if f_type == s_type:
            return True, f_type
        elif f_type in numbers_type and s_type in numbers_type:
            return True, Type.FLOAT
        else:
            return False, None
            


