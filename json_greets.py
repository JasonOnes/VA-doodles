""" Possible page 1 user_name check using json? """

import json

def retrieve_user():
    """ Get the user_name if already made """
    user_name = input("Who is trying to enter!>> ")
    filename = '{}.json'.format(user_name)
    try:
        with open(filename) as file_object:
            user_name = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return user_name

def create_user():
    """ Makes a new json file for new user"""
    print("I don't think you've been here before.")
    user_name = input("And what, pray tell, is your name again? ")
    filename = '{}.json'.format(user_name)
    with open(filename, 'w') as file_object:
        json.dump(user_name, file_object)
    print("Okay, we'll remember you next time!")
    return user_name


def greet():
    """ Greet user at login and determine if they are already a user"""
    user_name = retrieve_user()
    if user_name:
        print("Alright, hope your excited to be back {}!".format(user_name))
        """ Insert security vetting """
        """continue through to page two"""
    else:
        user_name = create_user()
        """insert some security set up ie password"""
        """ continue to page two"""

if __name__ == '__main__':
    greet()
