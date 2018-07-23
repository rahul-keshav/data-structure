import sys
class Solution:
    # Write your code here
    def __init__(self):
        self.list_stack=[]
        self.list_queue=[]
        
    def pushCharacter(self,char1):
        self.list_stack.append(char1)
        
    def enqueueCharacter(self,char2):
        self.list_queue.append(char2)
        
    def popCharacter(self):		
        return self.list_stack.pop(-1)
        
    def dequeueCharacter(self):		
        return self.list_queue.pop(0)
		
        
 # read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")           