#importing random and sys module
import random
import sys
#checking  the condition using if....else
if (len(sys.argv)) < 2: #check whether sys.argv is less than 2 or not 
    print("Error: Missing command-line argument.")
else:
    filename = sys.argv[1] # assigning the filename
    try:
        f = open(filename, 'r') # Open the file with the name stored in the `filename` variable in read mode and assign the file object to `f`.
        d = open("new_student_gmail.txt", 'w')#open the file for writing the content
    # Read the contents of the file and strip any leading whitespace.
    # Split the contents by newline characters into a list called `a`.
        a = f.read().strip().split("\n")
    # Iterate over the list `a` with a for loop.
        for i in range(len(a)):
    # Split the current element of `a` by a comma and assign the resulting list to `content`.
            content = a[i].split(",")
    # Assign the second element of `content` (which should be a string of forenames) to the variable `forenames`.
            forenames = content[1]
    # Split `forenames` by spaces into a list called `names`.
            names = forenames.split()
     #using list comphersion  and using a loop joined with .
            initials = ".".join([forename[0].lower() for forename in names])
    # Split the first element of `content` (which should be a student ID) by a space and assign the resulting list to `student_id`.
            student_id = content[0].split(" ")[0]
    # Assign the second element of `student_id` (which should be a family name) to `family_name`.
    # Remove any non-alphabetic characters from `family_name` and convert it to lowercase.
            family_name = content[0].split(" ")[1]
            family_name = ''.join([c.lower() for c in family_name if c.isalpha()])
    # Initialize a list called `lists` that contains the integers from 0 to 9.
            lists = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   #Initialize a empty list and generate a random four number and join that number converting into string
            digits = [str(random.choice(lists)) for i in range(4)]
            new_digits = ''.join(digits)
     # Use string formatting to create an email address based on the variables `student_id`, `initials`, `family_name`, 
    # and `new_digits`, and assign it to the variable `email`.
            email = ("%s %s.%s%s@poppleton.ac.uk" %(student_id, initials, family_name, new_digits))       
    #write into the file 
            d.write("%s\n" % (email))
        print("File Created Successfully")
   #if user cannot input filename as argument
    except:
            print("Error: Cannot open",filename,"Sorry about that.")

