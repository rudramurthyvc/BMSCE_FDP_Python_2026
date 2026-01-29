while True:
    print("1 : Hello, 2: Bye , 3: Exit")

    ch = int(input("Press Enter to print pattern or type 'exit': "))
    if ch == 1:
        print("Hello")
    elif ch == 2:
        print("Bye BMS")
    elif ch == 3:
        print("exiting")
        break
    else:
        print("invalid input")