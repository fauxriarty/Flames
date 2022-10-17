import os

l=['Friends','Lovers','Acquaintances','Marriage','Enemies','Siblings']

#removing the common characters:
s1=''.join(i for i in name1 if i not in name2 )
s2=''.join(i for i in name2 if i not in name1)

name1= input("Enter your name: ")
name2= input("Enter the name of the person you want to check your flames determined relationship with: ")

print("Calculating...")
os.system('cls')
print(f"Your relationship with {name2} is: ", flames(s1,s2))



