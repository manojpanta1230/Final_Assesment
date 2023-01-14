#importing random module
import random
#lists of different string
CONSTANTS=["lived","aboard","test","valued","make","algorithm","Nepese","maoja","gobar","nepal","Uk",
"china","america","water","kitkat","nepaliba","manoj","newphew","Kathmandu","palpa","bhutan",
"seafood","china","bigmart","bhatbateni","bounty","nepalwo","ranimahal","shreenagar","goodday",
"britinian","happyhappy","makemy","boroplus","qwe","rty","yui","lodu","assdd","assdqwqwe",
"asaeeedd","asdsadaadadadaad","adada"]
list2=["apple","banana","mango","watermelon","masss","rice","rakshi","dal","abhat","kskais",
"mento","tarkali","happy","sad","emotiom","meat","bheda","mance","pritn","baby3","dharam",
"osho",'meditation',"workme","nepa","opa","fride","oven","make","computer","cpu","monitor"
,"processor","keyboard","mouse","kit","facewash","haves","manaas","asad"]
list3=["dog","cat","Gorilaa","Man","tiger","frog","crocodile","monkey","Rhinio","baag","bhal"
,"nepaligo","nepa","thai","croco","hamper","goofs","laptop","embeeded","system","Pubg",
"freefire","cos","verysoon","comingup","fifaworld","qatar","malysia","japan","england","beby","comeone",
"someone","evertthinh","anything","pyhton","mysql"]
print("Password Generator")
print("-------------------\n-------------------\n\n\n")
s=set()
# Start an infinite loop
while True:
    try:
        #get user input for number of passwords needed anr try to convert it to an integer
        needed_password=int(input("How many password are needed?:"))
        #check if input is within the specified range
        if (1<=needed_password<=24):
            
            #loop through the specified number of password
            for i in range(needed_password):
                #using choice method of random and choose random string from 3 lists
                a=random.choice(CONSTANTS)
                b=random.choice(list2)
                c=random.choice(list3)
                #print the password within the number 
                print(i+1,"--->",a+b+c)
                s.add(a+b+c)
            print(len(s))
            #break the loop 
            break
        else:
             #If the input is not within the specified range, print an error message
            print("Enter value between 1 and 24")
                
        
    except ValueError:
        # If the user input could not be converted to an integer
        print("Please Enter a Number String is not accpeted")
    

