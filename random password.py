import random 
import string

characters=list(string.ascii_letters + string.digits )
special_char=list("!@#$%^&*()")
# to include atleast one special character 
def generate_password():
     ps_length=int(input("How long you like your password to be?"))
     random.shuffle(characters)
     ps=[]
     c=random.randint(1,ps_length//3)
     print(c)
     for x in range(c):
          ps.append(random.choice(special_char))
     while c<ps_length:
          ps.append(random.choice(characters)) 
          c+=1    
     random.shuffle(ps) 
     ps="".join(ps)
     print(ps) 

option = input("Do you want to generate a password?(Yes/No)")

if option == "Yes":
     generate_password()
elif option =="No":
     print("program ended") 
     quit()
else:
     print("Invalid input, please enter (Yes/No) ")  
     quit()       
