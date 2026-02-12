def collatz_sequence(n):
    while(n!=1):
        print(n, end='->')
        if(n%2==0):
            n=n//2
        else:
            n=3*n+1
    print(1)

n=int(input())
collatz_sequence(n)
