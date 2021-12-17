import hashlib
import secrets
import base64
import json

def cracking_prefix(filename,hash_result,salt_in_base64URL_ascii):
    #This line will open the password file
   file_opening = open(filename)
   lines = 0
   #this for loop will take each password of the file and will generate the hash value for each entry. 
   for line in file_opening:
       lines = lines + 1
       password = line.strip()
       #The code will add a prefix salt and then will use the hashlib to generate the hashing value. 
       salt = base64.b64decode(salt_in_base64URL_ascii)
       salted_password =  salt + bytes(password, "utf-8")
       hashed = hashlib.sha1(salted_password)
       value = base64.b64encode(hashed.digest()).decode("ascii")
       #This condition will compare de original hash againts the hash generate by the password taken from the passwords file. 
       if value == hash_result :
           print("\nThe plain text password is: " + str(password) )
           break
           

   file_opening.close()

def cracking_postfix(filename,hash_result,salt_in_base64URL_ascii):
    #This line will open the password file
   file_opening = open(filename)
   lines = 0
   #this for loop will take each password of the file and will generate the hash value for each entry. 
   for line in file_opening:
       lines = lines + 1
       password = line.strip()
       #The code will add a prefix salt and then will use the hashlib to generate the hashing value.
       salt = base64.b64decode(salt_in_base64URL_ascii)
       salted_password =  salt + bytes(password, "utf-8")
       hashed = hashlib.sha1(salted_password)
       value = base64.b64encode(hashed.digest()).decode("ascii")
       ##This condition will compare de original hash againts the hash generate by the password taken from the passwords file. 
       if value == hash_result :
           print("\nThe plain text password is: " + str(password) )
           break


   file_opening.close()
   


def main():
    filename = "minipasswords.txt"
    print("\nWelcome to the cracking hashing program.\n")
    print("Please refer to the following document for the hashing process: https://developer.okta.com/blog/2021/03/05/ultimate-guide-to-password-hashing-in-okta  \n")
    print("If you used the code in the previous link to hash your password you should have an output similiar to this one: \n ")
    print( "\n" + "{" + "\n" 
    " algorithm: \"SHA-1\"," + "\n"
    " salt: \"WtAA0AREjKfKRDTCrskd9A==\", " + "\n"
    " saltOrder: \"POSTFIX\", " + "\n"
    " value: \"PrL6zaCRxFqduROMbABkZKphDUw=\" " + "\n" + "}" )
    print("\nPlease introduce the following information using the quotes as in the example output.")
    #Requesting information from the user
    salt_in_base64URL_ascii = input("\nPlease enter the salt value: ")
    salt_order = input("Please enter the salt order: ")
    hash_result = input("Please enter the hash value: ")
    hash_result = hash_result.lstrip('\"')
    hash_result = hash_result.rstrip('\"')
    #Selecting result depending the prefix order. 
    if salt_order == '"PREFIX"' :
        cracking_prefix(filename,hash_result,salt_in_base64URL_ascii)
    elif salt_order == '"POSTFIX"' :
        cracking_postfix(filename,hash_result,salt_in_base64URL_ascii)
    else  :
        print("The order value was incorrect please enter \"POSTFIX\" or \"PREFIX\" ")



if __name__ == "__main__":
    main()
