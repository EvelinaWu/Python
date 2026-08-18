#0輸入,0輸出
def test():
    print("Hello, World")
    
#2 input,1 output
def mul(x, y):
    return x * y  

def add(x, y):
    return x + y  
  
def minus(x, y):
    return x - y  
  
def divide(x, y):
    if y == 0:
        return "Error: Division by zero"#除數不能為零
    return x / y
  
  
  #####################################
  
test()
test()
num1 = mul(3,4)
num2 = add(5,6) 
num3 = minus(10,2)
num4 = divide(2,3)
print(f"num1:{num1},num2: {num2}, num3: {num3}, num4: {num4}")