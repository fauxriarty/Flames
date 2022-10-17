import os

name1= input("Enter your name: ")
name2= input("Enter the name of the person you want to check your flames determined relationship with: ")

#removing the common characters:
s1=''.join(i for i in name1 if i not in name2 )
s2=''.join(i for i in name2 if i not in name1)
n=len(s1)+len(s2)




def flames(n):
    s= ['Friends', 'Lovers', 'Acquaintances', 'Marriage', 'Enemies', 'Siblings']

    while len(s)>1:
        if n%6!=0:
            t= n%6
            if t>len(s):
                t=t%len(s) -1
            else:
                t=t-1
        else:
            t = 5
        s.remove(s[t])
    print(s[0])


print("Calculating...")
os.system('cls')
print(f"\nYour relationship with {name2} is: ")
flames(n)



