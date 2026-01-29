grade=input("enter the grade")
match grade:
    case "A":
        print("scored morethan 90")
    case "B":
        print("between 80 to 90")
    case "C":
        print("between 60 to 80")
    case "F":
        print("failed")
    case _:
        print("invalid")