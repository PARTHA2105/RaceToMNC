def PrintNTime(count ,n):
    if(count==n): return 
    print("Partha")
    count+=1
    PrintNTime(count,n)        

print(PrintNTime(0,5))

#Print 1 to N using Recursion using Backtracking Approach: will print the reverse order.
#if you want normal then forward (Recursion)traacking just print it and call recursion.
def PrindValues(count ,n):
    if(count>n):return 
    PrindValues(count+1,n)
    print(count)

print (PrindValues(1,5))

#N to 1 using Recursion
"""
Backtracking builds solutions by exploring all options and undoing choices when needed. 
To print numbers from n down to 1 using backtracking, the function recursively calls 
itself with the previous number until it goes below 1. After reaching the base case, 
it prints the numbers while returning from the recursion.
This way, numbers are printed in ascending order because the print happens
after the recursive call during backtracking. The main difference from forward 
recursion is that printing occurs on the way back, not before the recursive call.

if n is. 4
print(count) print 1
funt(1,4)
base: when count > 4 then return
funt(2 , 4) print 2
funt(3,4) print 3
funt(4,4) = Base case excecute 

or 

Back Tracking
count>1

function (1,4)
print()
function (2,4)
print()
function(3,4)
print()
function(4,4)
print()


"""
def PrintNToOne(n):
    if(n<1) : return
    print(n)
    PrintNToOne(n-1)

print(PrintNToOne(5))
#Time complexity mostly O(N), Space complexity O(N) 


#Sum of first N Natural Numbers
def PrintNNumbers(num):
    if(num==1):return 1
    return (num+ PrintNNumbers(num-1))

print(PrintNNumbers(5))



#Sum of first N Natural Numbers
def FactorialNumbers(num):
    if(num==1):return 1
    return (num* FactorialNumbers(num-1))

print(FactorialNumbers(5))


def ReverseArray(array):
    array = array[::-1] #slicing.
    return print(" ".join(map(str, array)))

#Best solution
def ReverseArr(arr):
    val=[]
    length = len(arr)
    for i in range(length):
        lastdigt = arr[len(arr)-i-1]
        val.append(lastdigt)
    print(val)

def ReverseArrayMethod2(arr):
    val1= 0
    val2= len(arr)-1
    while(val1<val2):
        arr[val1],arr[val2]= arr[val2],arr[val1]
        val1+=1
        val2-=1

print(ReverseArray([5,4,3,2,1]))
print(ReverseArr([5,4,3,2,1]))
print(ReverseArrayMethod2([5,4,3,2,1]))


def CheckStringPalindrome(strval):
    
    n= len(strval)
    restults =""
    for i in range(n):
        restults+=strval[n-i-1]
    
    return restults==strval


print(CheckStringPalindrome("TAKE U FORWARD"))
print(CheckStringPalindrome("ABCDCBA"))

#Check given string are Palindrome using Recursion 
def CheckStringPalindromeRecursion(i,instr):

    if(i>=len(instr)//2):
        return True
    dd = instr[i]
    if(instr[i] != instr[len(instr)-i-1]):
        return False
    CheckStringPalindromeRecursion(i+1,instr)
    

print(CheckStringPalindromeRecursion(0,"madam"))


#Print Fibonacci Series up to Nth term
def fibonacci_list(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    
    fib = fibonacci_list(n - 1)
    fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci_list(4)) # return list 
#return the number:
# if(n<=1):return n
# last = fibonacci_list(n-1) 
# slast = fibonacci_list(n-2)
# return last+slast
    