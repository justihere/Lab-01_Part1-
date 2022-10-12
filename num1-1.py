import argparse 

def process(val_1, op, val_2):
    if op == "+":
        return val_1 + val_2
    elif op == "-":
        return val_1 - val_2
    elif op == "*":
        return val_1 * val_2
    elif op == "/":
        if val_2 == 0:
            print("can't divide by zero")
        return val_1 / val_2
            
    else:
        print("Invalid operator")
        exit()

if name == "__main__" :
    parser = argparse.ArgumentParser(description="Take two integer values - ")
    parser.add_argument("input_value_1", type=int,
                help="Give a positive integer value for 1st veriable")
    parser.add_argument("input_operator", type=str,
                help="Give an operator", choices=["+", "-", "*", "/"])
    parser.add_argument("input_value_2", type=int,
                help="Give a positive integer value for 2nd variable")

    input_args = parser.parse_args()
    val_1 = input_args.input_value_1
    val_2 = input_args.input_value_2
    operator = str(input_args.input_operator)


    print("{0} {1} = {2}".format(process(val_1, operator, val_2)))






