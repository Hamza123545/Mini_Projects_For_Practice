# simple even odd number min project



print("Welcome to the even odd simple project")

def even_odd_checker():
    while True:
        num = int(input("Enter a number or 0 to exit"))

        if num == 0:
            print("Good bye")
            break
        elif num % 2 ==0:
            print("This is an even number")
        else:
            print("this is an odd number")

even_odd_checker()
