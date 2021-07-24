# author : Snehashish Laskar
# email : snehashish.laskar@gmail.com
# LICENSE : Apache 2.0
# Project name : Site password hasher
"""
Objective of this project:

The Objective og this Project is to make passwords almost impossible to crack.
This program uses the art of cryptography and hashing to represent a password using 
just a hash which can be used as the password for a site

"""
# importing the hashing library
from hashlib import sha256

# Asking the user about which site the password is for
name_of_site = input("please enter the name of the site: \n")

# Defining the core function
def hashSite(text):
    # Joining the name of the site with a key word
    # The key word could be anything you want 
    name_of_site = ("MYKEYWORD"+text).encode()
    # Hashing the final string to form a strong and 
    # Almost impossible to crack password
    hash_for_this_site = "you can use the following password : "+ sha256(name_of_site).hexdigest()

    # returning the final result
    return hash_for_this_site

# Calling the function and printing out what it returns
print(hashSite(name_of_site))

