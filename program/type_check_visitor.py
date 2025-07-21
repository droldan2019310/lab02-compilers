from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor
from custom_types import IntType, FloatType, StringType, BoolType

class TypeCheckVisitor(SimpleLangVisitor):

  def visitMulDiv(self, ctx: SimpleLangParser.MulDivContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for * or /: {} and {}".format(left_type, right_type))

  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
        return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
        raise TypeError("Unsupported operand types for + or -: {} and {}".format(left_type, right_type))
  
  def visitInt(self, ctx: SimpleLangParser.IntContext):
    return IntType()

  def visitFloat(self, ctx: SimpleLangParser.FloatContext):
    return FloatType()

  def visitString(self, ctx: SimpleLangParser.StringContext):
    return StringType()

  def visitBool(self, ctx: SimpleLangParser.BoolContext):
    return BoolType()

  def visitParens(self, ctx: SimpleLangParser.ParensContext):
    return self.visit(ctx.expr())

  def visitPower(self, ctx: SimpleLangParser.PowerContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
      return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
      raise TypeError(f"Unsupported operand types for ^: {left_type} and {right_type}")

  def visitMod(self, ctx: SimpleLangParser.ModContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))
    if isinstance(left_type, IntType) and isinstance(right_type, IntType):
      return IntType()
    else:
      raise TypeError(f"Unsupported operand types for %: {left_type} and {right_type}")

  def visitAddSub(self, ctx: SimpleLangParser.AddSubContext):
    left_type = self.visit(ctx.expr(0))
    right_type = self.visit(ctx.expr(1))

    if isinstance(left_type, StringType) or isinstance(right_type, StringType):
      if isinstance(left_type, StringType) and isinstance(right_type, StringType):
        return StringType()
      else:
        raise TypeError(f"Cannot add String and {type(right_type).__name__}")
    elif isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
      return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
    else:
      raise TypeError(f"Unsupported operand types for + or -: {left_type} and {right_type}")
