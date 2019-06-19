# prime number 

def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True 
def generateprime(num):
    for i in range (2,num+1):
        if prime(i):
            print(i, end=" ")
    return
num=int(input())
generateprime(num)




#character sum
def charactersum(s):
    sum=0
    for i in range(0, len(s)):
        if s>=chr(97) and s<= chr(122) :
             sum= sum+(ord(s[i])-96)
    print(sum)
s=input(" ")
charactersum(s)