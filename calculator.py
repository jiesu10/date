#简易计算器加减乘除
def add(x, y):
    """加法"""
    return x + y

def subtract(x, y):
    """减法"""
    return x - y

def multiply(x, y):
    """乘法"""
    return x * y

def divide(x, y):
    """除法"""
    if y == 0:
        return "错误：除数不能为零！"
    return x / y

# 这是程序的入口，用来运行计算器
if __name__ == "__main__":
    print("欢迎使用简易Python计算器！")
    
    while True:
        print("\n请选择操作:")
        print("1. 加法")
        print("2. 减法")
        print("3. 乘法")
        print("4. 除法")
        print("5. 退出")

        choice = input("请输入你的选择 (1/2/3/4/5): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("请输入第一个数字: "))
                num2 = float(input("请输入第二个数字: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError:
                print("输入错误：请输入有效的数字。")

        elif choice == '5':
            print("感谢使用，再见！")
            break
        else:
            print("无效输入，请重新选择。")
