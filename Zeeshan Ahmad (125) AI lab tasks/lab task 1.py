def calculator(expression):
    try:
        result = eval(expression)
        return result
    except:
        return "Invalid Expression"

def main():
    print("Dynamic Calculator")
    while True:
        expression = input("Enter expression (or type 'exit' to quit): ")
        if expression.lower() == 'exit':
            print("Exiting...")
            break
        print("Result:", calculator(expression))

main()
