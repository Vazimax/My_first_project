def odd_even_project() :
    number = input("Enter a number :")
    while number != "x":

        try:
            number = int(number)
            if number%2 == 0 :
                print("It's an even number =)")
            else :
                print("It's an odd number :)")
        except ValueError:
            print("Please Enter a valid number")

        number = input("Enter a number again , and if you wanna exit press 'x' :")