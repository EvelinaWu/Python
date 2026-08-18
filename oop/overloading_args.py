class calculator():
   def add(self, *args):
      if len(args) == 2:
         x,y = args[0] + args[1]
         if isinstance(x, str) and isinstance(y, str):
            return f"字串串接結果：{x} - {y}"
          return f"數字相加結果：{x + y}"
        