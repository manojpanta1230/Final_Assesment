#importing a string and sys module 
import string
import sys
#creating a function having a argumnets 
def ceaser_chiper(encrypted_text):
    """This will provide the key value for the shifted alphabets"""
    #creating a  empty dictionary
    decrypted_texts = {}
    #loop upto the range 
    for key in range(26):
        decrypted_text = ""
         #using for loop 
        for ch in encrypted_text:
            # If the character is not a letter, we can just add it to the decrypted text as is.
            if ch not in string.ascii_letters:
                decrypted_text += ch
                continue
            #check the order of character
            ch_num = ord(ch)
            #check whether the character is captial or not 
            if ch.isupper():
                # to find the right characters 
                ch_num = (ch_num - 65 - key) % 26 + 65
            else:
                #if the character is lower.New character is found by using this formula 
                ch_num = (ch_num - 97 - key) % 26 + 97
            decrypted_text += chr(ch_num)

        decrypted_texts[key] = decrypted_text
    # Now that we have a dictionary of all possible decrypted texts, we can look for clues to determine
    # which one is the correct decryption. For example, we might look for common English words or phrases.
    # In this example, we will just return the decrypted text that has the most lowercase "e" characters,
    # as "e" is the most common letter in the English language.
    i= max(decrypted_texts, key=lambda key: decrypted_texts[key].count("e"))
    decrypted_text = decrypted_texts[i]
   #print the key and decrypted text using string formating
    print(f"Key: {i}\nDecrypted Text: {decrypted_text}")

    return 
    
# Test the function with a sample encrypted string

if (len(sys.argv)) < 2: #check whether sys.argv is less than 2 or not 
    print("Error: Missing command-line argument.")

else:
    #taking filename  from sys module using the indexing 
    filename=sys.argv[1]
    try:#infinte Loop 
        #open the text file  in reading mode 
        txt_file = open(filename, "r")
        #read the conbtent of file
        data = txt_file.read()
        #read file is assigned with new_varaible 
        encrypted_text = data
        #key is assigned after the function calling
        key = ceaser_chiper(encrypted_text)
    # if there is no file in the folder .This will appear.
    except FileNotFoundError:
        print("Error: Cannot open",filename,"Sorry about that.")


