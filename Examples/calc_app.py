def main():
    while True:
        n1 = input("Enter First Number: ")
        try:
            n1 = float(n1)
            break
        except ValueError:
            print(f"{n1} is incorrect value")

    while True:
        n2 = input("Enter Second Number: ")
        try:
            n2 = float(n2)
            break
        except ValueError:
            print(f"{n2} is incorrect value")

    operator_signs = ["*", "/", "+", "-", "%"]
    while True:
        try:
            o = input("Enter Operator (*,/,+,-) : ")
            if o in operator_signs:
                break
            print(f"{o} not in (*,/,+,-) ")
        except Exception as e:
            print(e)

    print(f"Result of: {n1} {o} {n2} = ", eval(f"{n1} {o} {n2}"))


main()
