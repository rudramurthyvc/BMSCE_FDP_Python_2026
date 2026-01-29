name = input("enter student name: ")

m1 = int(input("enter marks1: "))
m2 = int(input("enter marks2: "))
m3 = int(input("enter marks3: "))
m4 = int(input("enter marks4: "))
m5 = int(input("enter marks5: "))

if 0 <= m1 <= 100:
    if 0 <= m2 <= 100:
        if 0 <= m3 <= 100:
            if 0 <= m4 <= 100:
                if 0 <= m5 <= 100:
                    avg = (m1 + m2 + m3 + m4 + m5) / 5
                        print(f"{name} average marks is {avg}")

                        if avg >= 75:
                            print(f"{name} scored A grade")
                        elif avg >= 50:
                            print(f"{name} scored B grade")
                        elif avg >= 30:
                            print(f"{name} scored C grade")
                        else:
                            print(f"{name} Failed in semester")
                    else:
                        print("Enter marks between 0 to 100 only")
            else:
                print("invalid")
    else:print("invalid")
else:

