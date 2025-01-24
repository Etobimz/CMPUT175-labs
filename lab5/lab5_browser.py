#----------------------------------------------------
# Lab 5, Exercise 2: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

from stack import Stack

def getAction():
    '''
    Parameters: None
    Inputs: Function prompts the user to "enter = to enter a URL, < to go back, > to go forward, q to quit: "
    Returns: The users valid input
    '''

    #initilize the while loop used to keep asking the user for their input and breaks when user inputs 'q'
    user_input = '' #defining the user_input variable with a placeholder " "

    while user_input != 'q':
        user_input = input("\nPlease Enter = to enter a URL, < to go back, > to go forward, q to quit:  ")

        if user_input == '=':
           return "="
        elif user_input == '<':
           return '<'
        elif user_input == '>':
           return '>'
        elif user_input == 'q':
           return 'q'
        else:
            raise ValueError # raise a valueError that is caught by the try - exception block in the __main__ function
        
    return user_input
       

def goToNewSite(current, bck, fwd):
    '''
    This function is called when the user enters ‘=’ and types in their url
    
    Inputs: 
    current: The current site the user just enters 
    bck: a reference to the Stack holding the webpage addresses to go back to
    fwd; a reference to the Stack holding the webpage addresses to go forward to.

    Returns: the website the user just entered 
    ''' 
    bck.push(current)
    user_URL = input("Please enter URL you wish to go: ")
    current = user_URL # stores the user_input in the current var.


    return  current
    
 
    
def goBack(current, bck, fwd):
    '''
    This function is called when the user enters ‘<’
    
    Inputs: 
    current: The current site the user is currently viewing
    bck: a reference to the Stack holding the webpage addresses to go back to
    fwd; a reference to the Stack holding the webpage addresses to go forward to.

    Returns: the previous website before the current one and returns to the current if no previous page

    '''
    try:
        # We move the current page to forward stack before navigating back
        fwd.push(current)
        current = bck.pop() # Function to pop the last item in a stack and raises an IndexError if the stack is empty

    except IndexError: # catch the error raised in the pop method from the Stack class 
        print("Cannot go backward.")
    
    return current
    

def goForward(current, bck, fwd):
    '''
    This function is called when the user enters ‘>’

    Inputs: 
    current: The current site the user is currently viewing
    bck: a reference to the Stack holding the webpage addresses to go back to
    fwd; a reference to the Stack holding the webpage addresses to go forward to.

    Returns: the website in the next page
    '''
    try:
         # We move the current page to back stack before navigating foward
        bck.push(current)
        current = fwd.pop() # Function to pop the last item in a stack and raises an IndexError if the stack is empty

    except IndexError: # catch the error raised in the pop method from the Stack class 
        print("Cannot go forward.")
    return current

    
def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    back = Stack()
    forward = Stack()
    
    current = HOME
    quit = False
    
    while not quit:
        print('\nCurrently viewing', current)
        try: # try to run the getaction function and check if a valid input was enteered else except the value error
            action = getAction()
            
        except ValueError:  # Dont throw an error, just pop up a notice telling the user to enter a valid input
            print('Invalid Entry')

        else:
            if action == '=':
                current = goToNewSite(current, back, forward)
            elif action == '<':
                current = goBack(current, back, forward)
            elif action == '>':
                current = goForward(current, back, forward)
            elif action == 'q':
                quit = True
           
            
            
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()
    