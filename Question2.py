    
def leap_year(num):
    if(num % 100 == 0):
        if(num % 400 == 0):
            return 'Leap Year'
        return 'Not a Leap Year'
        
    if(num % 4 == 0):
        return 'Leap Year'


    else:
        return 'Not a Leap Year'


def main():
    num = int(input('Enter a number and I will determine whether it\'s a leap year or not: '))

    print(leap_year(num))



main()
