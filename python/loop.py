# this program is a mix of loop and condional structure
a=1
while(a!=6):
    print("don't repeat your self")
    a+=1
jeu_lance = True
print(" ")
while jeu_lance:
    choixMenu = input("> ")
    if choixMenu=="again":
        continue
    elif choixMenu=="quiet":
        break
    elif choixMenu=="hello":
        print("hello")
    else :
        print("repeat what you inputed is not availible")
        continue
    
    
    
    
sentence = "bonjour tout le monde :) !"
for letter in sentence:
    print(letter)
for i in range(0,5):
    print("hello")
choice = input("input your hello number > ")
if(choice==1):
    print("your choice is one")
elif(choice==2):
    print("your choice is two")
else:
    print("sorry we can't understand your choice")
