def fibosum(number):
    f1=0
    f2=1
    sum=0
    while (number>f2):
        sum=sum+f2
        a=f2
        f2=f2+f1
        f1=a
    print("sum=",sum)

def priming(number):
    for i in range(2,number):
        if (number%i == 0):
            print("your number is not prime")
            break
        else:
            print("your number is prime")
            break

def toBinary(number):
    binary = [0,0,0,0,0,0,0,0]
    i = 7
    while(i >= 0):
        binary[i] = number%2
        i = i-1
        number = number//2
    print(binary)

def main():
    N = int(input("Enter your number:"))
    fibosum(N)
    priming(N)
    toBinary(N)

main()
