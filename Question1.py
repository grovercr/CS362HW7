


def Fizz(num):
    if(num % 3 == 0):
        print('Fizz')
        return 'Fizz'
    else:
        return None


def Buzz(num):
    if(num % 5 == 0):
        print('Buzz')
        return 'Buzz'
    else:
        return None



def main():
    for i in range(1,100):
        if(i % 3 == 0 and i % 5 == 0):
            Fizz(i)
            Buzz(i)

        elif(i % 3 == 0):
            Fizz(i)
        elif(i % 5 == 0):
            Buzz(i)
    
        else:
            print(i)

main()