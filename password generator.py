# import string
# import random

# if __name__ == "__main__":
#     # Letter Sets
#     s1 = string.ascii_letters
#     s2 = string.digits
#     s3 = string.punctuation
#     service_name = input("Enter the site: ")
#     plen = int(input("Enter the password length: "))

#     # Combining all the sets
#     s = []
#     s.extend(list(s1))
#     s.extend(list(s2))
#     s.extend(list(s3))
#     # print(s)
#     random.shuffle(s)
#     # print (s)

#     print("Your password is: ")
#     print("".join(s[0:plen]))


#     # Saving the password in the file 
#     file = open("pass.txt" , "a")
#     file.write(f"\n{service_name} ; ")
#     file.write("".join(s[0:plen]))
#     file.close()

#     print("Password has been saved in the file.")


import string 
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)
    s3 = string.digits
    # print(s3)
    s4 = string.punctuation
    # print(s4)
    passwordLength = int(input("Enter password length:\n"))
    site_name = input("Enter your site: ")
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    print("Your password is: ")
    print("".join(s[0:passwordLength]))

    # Saving the password in the file 
    site_file = open("password.txt","a")
    site_file.write(f"\n{site_name}: ")
    site_file.write("".join(s[0:passwordLength]))
    site_file.close()

    print("Password has been saved in the file.")




