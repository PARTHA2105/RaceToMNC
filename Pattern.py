class Solution:
    @staticmethod
    def PrintPattern():
        #Print Pattern1.
        """
        Docstring for PrintPattern 
        """
        for i in range(5):
            print("*" * 5)
            
        print("Print Pattern 2 - Triangle")
        for i in range(5):
            print("* " * (i+1)) 

        print("Print Patter 3 - Numberic triangle.")
        
        for i in range(5):
            print(*range(1,i+2))
        
        print("Print 4th Pattern")
        """
        1
        22
        333
        4444
        55555
        """
        for i in range(1,5+1):   
            for j in range(i):
                print(i,end=" ")
            print()
        #Print Patter 5
        """
        *****
        ****
        ***
        **
        *
        """
        for i in range(5, 0,-1):
            for j in range(i):
                print("*",end=" ")
            print()

        for i in range(5):
            print("* " *(5-i))

    #Pattern 6th
        for i in range(5):
            for j in range(1,5-i+1):
                print(j,end=" ")
            print()
    #Patter 7 
        for i in range(5):
            print(" " )  
            print("* " * (2*i+1))  

if __name__ =="__main__":
    Solution.PrintPattern()
