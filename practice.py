
"""
Docstring for practice
a= "leetcode"
b= "leeto"

c="sadbutsad"
d= "sad"

#retun the first occurance index.
def strStr(haystack, needle) -> int:
    if(needle in haystack):
        x= haystack.find(needle)
        return x
    return -1
print(strStr(c,d))
"""

#Basic Test:

"""
# Adult check for election.
age = int(input("Enter the age: ")) # input is the built in function to user can able to enter the age in the terminal.

if(age>=18):
    print("A person can able to vote")
else:
    print("He is not a eligible person to vote anyone.")


#Lets use multiple check to get the student grade.
stu_mark = int(input("Enter marks: "))

if stu_mark < 0 or stu_mark > 100:
    print("Invalid marks.")

elif stu_mark >= 90:
    print("Resulted grade is 'A+'")

elif stu_mark >= 80:
    print("Resulted grade is 'A'")

elif stu_mark >= 70:
    print("Resulted grade is 'B+'")

elif stu_mark >= 35:
    print("Resulted grade is 'B'")

else:
    print("Resulted grade is 'RA'")   # Re-Appear

"""
# let's consider a common problem: 
# given a number between 1 and 7, print the corresponding day of the week.
# Here's how we can use the switch statement for this task:

"""
day = int(input ("Enter value to find the day of the week: "))

match(day): #match case is available in python 3.11 and lower version .
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
"""
    

#Passing, Returning, and Assigning Strings
class Solution:
    # 'self' key when you are try to aceess instance of class then use ..this is common method .
    #like we can declare staticmethod to skip self key , ne need to create instance of class and also classMethod 
    @staticmethod
    def printMethod(inputstr): #if you are working with class then need to put self key from Getting arguments.
        new_str =inputstr #assign
        new_str +=" World"
        return new_str #return
    @staticmethod
    def printNumbers(count):
        for i in range(count):
            print(f"Current value is {i} printed")
            i+=1
    @staticmethod
    def FindFactorialValue(num):
        if(num==0 or num==1):
            return 1
        while(num>0):
            return  num * Solution.FindFactorialValue(num-1)

        

if __name__ == "__main__":
    #  printObj= Solution()
     inputStr="Hello" 
     #pass input string to the print method.
     res = Solution.printMethod(inputStr)
     res = Solution.printNumbers(10)
     res = Solution.FindFactorialValue(5)
     print(f"The factorial 5 is: {res} ")
    


