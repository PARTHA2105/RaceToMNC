import math
#Given an integer N, return the number of digits in N.
#inputVal = int(input("Enter value:"))
#print("The count of digits is : ",len(inputVal))

#Brote solution approach 
# cot =0
# while(inputVal>0):
#     cot+=1
#     inputVal= inputVal//10 #remove the last digit from the number

# print(cot)

#Get the 
#optimal Solution
#Use Log of 10 log10(number) it will give you the count.

#while(inputVal>0):
#cot = int(math.log10(inputVal)+1) #math will run in the constant time of O(1) space complexity also O(1)

#print(cot)

#Extract Digit will exact all the digit from the given number.

#number%10 will retun the last digit of the number until less than zero.

"""Reverse the give number"""
num= 15064000
rev=0
while(num>0):
    digit = num%10
    num= num//10
    rev= rev*10+digit

print(rev)
#Time complexity = O(log10 N)
#space Complexity = O(1)

#check palindrome
def Palindrome(number):
    #Check if the number is Zero only then return false.
    if(number is 0):
        return False
    
    origNum=number
    revnumber= 0

    while(origNum>0):
        lastdigit = origNum%10
        origNum =origNum//10
        revnumber = revnumber*10+lastdigit

    return(number==revnumber)

print(Palindrome(121))

def FindGCDOfTwoNumber(number1, number2):
    gcd=0

    if(number1 == 0 and number2==0):
        return 0

    for i in range(1,min(number1,number2)+1):  #range(min(num1,num2),0,-1) -- Reverse until big  to 1
        if(number1%i ==0 and number2%i ==0):
            gcd=i
    
    return gcd

print((FindGCDOfTwoNumber(3,6))) #time complexity : O(min(nmuber1,number2)), O(1)


def EuclideanAlogorithm(num1,num2):
    
    """Euclidean Algorithm:
    The Euclidean Algorithm is a method for finding the greatest common divisor (GCD)
    of two numbers. It operates on the principle that the GCD of two numbers remains
    the same even if the smaller number is subtracted from the larger number.

    To find the GCD of n1 and n2 where n1 > n2:
    1. Repeatedly subtract the smaller number from the larger number until one of them becomes 0.
    2. Once one becomes 0, the other is the GCD of the original numbers.

    Example:
    n1 = 20, n2 = 15

    gcd(20, 15) = gcd(20 - 15, 15) = gcd(5, 15)
    gcd(5, 15)  = gcd(15 - 5, 5)  = gcd(10, 5)
    gcd(10, 5)  = gcd(10 - 5, 5) = gcd(5, 5)
    gcd(5, 5)   = gcd(5 - 5, 5)  = gcd(0, 5)

    Hence, return 5 as the GCD.
    """
    if(num2 ==0):
        return num1
    return(EuclideanAlogorithm(num2,num1%num2)) #Recursion O(log(min(num1,num2)))
    
    #'OR'

    # while(num1 != 0):
    #     temp = num1
    #     num1= num2% num1
    #     num2=temp
    # return num2

    
print(EuclideanAlogorithm(2,5))

def gcdOfOddEvenSums(n):

        sumOdd=n*n
        sumEven=n*(n+1)

                
        if(sumEven==0): return sumOdd
        
        while(sumEven !=0):
            temp= sumEven
            sumEven= sumOdd %sumEven
            sumOdd = temp

        return sumOdd

print(gcdOfOddEvenSums(4))


def CheckArmstrongNumber(orig):
    # An Armstrong number (also called a narcissistic number) is a number 
    # that is equal to the sum of its digits each raised to the power of the number of digits.
    
    num = orig
    if(num == 0):return 0
    count=0

    #Find the digit of the give number
    Totaldigit = int(math.log10(num)+1)

    while(num>0):
        #Get the each number from the given input.        
        digitNum = num%10
        
        #Add sum of each digit with multiply wit the total digit
        count+= int(math.pow(digitNum ,Totaldigit))
        #Remove the each digit from the orignal value
        num//=10
    
    return orig ==count

print(CheckArmstrongNumber(153))


"""
Print all Divisors of a given Number:

Problem Statement: Given an integer N, return all divisors of N.
A divisor of an integer N is a positive integer that divides N without 
leaving a remainder. In other words, if N is divisible by another 
integer without any remainder, then that integer is considered a divisor of N.
"""


def FindDivisors(num):
    divisors=[]
    for i in range(1,num+1): # optimize is use itreate (1, sqrt(n))  if( i != N//i) add n/i too
        if(num % i==0):
            divisors.append(i)
    
    return divisors

print(FindDivisors(32))


def FindPrimeNumber(num):

    cnt =0
    for i in range(1,int(math.sqrt(num)) +1):  #optimize is use itreate (1, sqrt(n))  if( i != N//i) increment n/i too
        
        if(num %i ==0):
            cnt+=1
            #If n is not a perfect square, count its reciprocal f
            if(num//i !=i):
                cnt+=1
    
    return cnt==2

print(FindPrimeNumber(2))

        



        
        

