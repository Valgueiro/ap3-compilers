from antlr4 import *
from autogen.CymbolParser import CymbolParser
from autogen.CymbolVisitor import CymbolVisitor


class Type:
    VOID = "void"
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOLEAN = "boolean"


numbers_type = [Type.INT, Type.FLOAT]
# Value/IDs = {'type':}
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
            print("Error in VarDecl...")
            exit(1)
        else:
            if ctx.expr() is not None:
                result = self.visit(ctx.expr())
                canReceive = self.canReceive(tyype, result['type'])
                if not canReceive:
                    print("Error in VarDecl...")
                    exit(2)
            out = {'type': tyype}
            self.id_values[var_name] = out
    
    def visitAssignStat(self, ctx: CymbolParser.AssignStatContext):
        old_val = self.id_values[ctx.ID().getText()]
        new_val = self.visit(ctx.expr())

        if old_val['type'] != new_val['type']:
            print('Assign error')
            exit(3)

    def visitSignedExpr(self, ctx: CymbolParser.SignedExprContext):
        expr = self.visit(ctx.expr)

        if expr['type'] in [Type.INT, Type.FLOAT]:
            return {'type': expr['type']}
        else:
            print('Error in SignedExpr')
            exit(3)  
        return 0

    def visitNotExpr(self, ctx: CymbolParser.NotExprContext):
        expr = self.visit(ctx.expr)

        if expr['type'] == Type.BOOLEAN:
            return {'type': Type.BOOLEAN}
        else:
            print('Error in NotExpr')
            exit(3)  
        return 0

    def visitComparisonExpr(self, ctx: CymbolParser.ComparisonExprContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        
        if left['type'] == Type.BOOLEAN and right['type'] == Type.BOOLEAN:
            return {'type': Type.BOOLEAN}
        else:
            print('Error in ComparisonExpr')
            exit(3) 

    def visitMulDivExpr(self, ctx: CymbolParser.MulDivExprContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        compatible, result = self.isCompatible(left['type'], right['right'])

        if compatible and result in numbers_type:
            return {'type': result}
        else:
            print('Error in MulDiv')
            exit(3) 

    def visitAddSubExpr(self, ctx: CymbolParser.AddSubExprContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        compatible, result = self.isCompatible(left['type'], right['type'])

        if compatible:
            return {'type': result}
        else:
            print('Error in AddSub')
            exit(3) 

    def visitEqExpr(self, ctx: CymbolParser.EqExprContext):
        return {'type': Type.BOOLEAN}

    def visitParenExpr(self, ctx: CymbolParser.ParenExprContext):
        return self.visit(ctx.expr())   
    
    def visitBoolExpr(self, ctx: CymbolParser.BoolExprContext):
        left = self.visit(ctx.expr()[0])
        right = self.visit(ctx.expr()[1])
        compatible, result = self.isCompatible(left['type'], right['type'])

        if compatible and result == Type.BOOLEAN:
            return {'type': Type.BOOLEAN}
        else:
            print('Error in BoolExpr')
            exit(3) 

    def visitFuncDecl(self, ctx: CymbolParser.FuncDeclContext):
        return_type = ctx.tyype().getText()
        name = ctx.ID().getText()
        params = {}
        if ctx.paramTypeList() is not None:
            params = self.visit(ctx.paramTypeList())
        self.functions[name] = {'type': return_type, 'params': params}

        #define params variables
        for param in params:
            self.id_values[param['name']] = {'type': param['type']}

        returns = self.visitBlock(ctx.block())
        
        #remove params variables
        for param in params:
            del self.id_values[param['name']]
        if len(returns) == 0:
            if return_type != Type.VOID:
                print('expecting some return')
                exit(3)
        else:
            print('returns:')
            print(returns)
            for ret in returns:
                if not self.canReceive(return_type, ret['type']):
                    out = "TypeError: Wrong return type at line " + ret['line'] + " column " + ret['column']
                    out += ". Passed "+  ret['type'] + ", expected " + return_type + "."
                    print(out)
                    exit(3)
    #TO-DO: check multiple levels returns
    def visitBlock(self, ctx: CymbolParser.BlockContext):
        types = []
        for stat in ctx.stat():
            ret = self.visit(stat)
            if ret is not None:
                if not isinstance(ret, list):
                    ret = [ret]
                for r in ret:
                    if r not in types:
                        print(ret)
                        types.append(r)
        print(types)
        return types
    
    def visitIfStat(self, ctx: CymbolParser.IfStatContext):
        condition = self.visit(ctx.expr())
        if condition['type'] != Type.BOOLEAN:
            out = "TypeError: Wrong type at line " + str(ctx.start.line) + " column " + str(ctx.expr().start.column)
            out += ". Passed "+  condition['type'] + ", expected boolean."
            print(out)
            exit(3)
        
        return self.visit(ctx.ifElseExprStat())

    def visitReturnStat(self, ctx: CymbolParser.ReturnStatContext):
        val = self.visit(ctx.expr())
        val['line'] = str(ctx.expr().start.line)
        val['column'] = str(ctx.expr().start.column)
        return val

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
        
        if len(params_types) != len(func['params']):
            out = "ParamsError: Wrong number of parameters at line " + str(ctx.start.line) + " column " + str(ctx.start.column)
            out += ". Passed "+  str(len(params_types)) + ", expected " + str(len(func['params'])) + "."
            print(out)
            exit(3)

        for index, param in enumerate(params_types):
            if not self.canReceive(func['params'][index]['type'], param['type']):
                out = "TypeError: Wrong parameter passed at line " + param['line'] + " column " + param['column']
                out += ". Passed "+ param['type'] + ", expected " + func['params'][index]['type'] + "."
                print(out)
                exit(3)
        
        return {'type': func['type']}

    def visitExprList(self, ctx: CymbolParser.ExprListContext):
        expr_types = []
        for expr in ctx.expr():
            val = self.visit(expr)
            val['line'] = str(expr.start.line)
            val['column'] = str(expr.start.column)
            expr_types.append(val)
        return expr_types

    def aggregateResult(self, aggregate: Type, next_result: Type):
        return next_result if next_result != None else aggregate

    def isCompatible(self, f_type, s_type):
        if f_type == s_type:
            return True, f_type
        elif f_type in numbers_type and s_type in numbers_type:
            return True, Type.FLOAT
        else:
            return False, None
    
    def canReceive(self, dest_type, source_type):
        if dest_type == source_type:
            return True
        elif dest_type == Type.FLOAT and source_type == Type.INT:
            return True
        else:
            return False
            


