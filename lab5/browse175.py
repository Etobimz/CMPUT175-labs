import os
from time import sleep
import stack

#----------------------------------------------------
# Lab 5 Problem B: BROWSE-175
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

os.system("")  # enables ANSI characters in terminal


def print_location(x, y, text):
    '''
    Prints text at the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
        - text (str): text to print
    Returns: N/A
    '''
    print ("\033[{1};{0}H{2}".format(x, y, text))

def clear_screen():
    '''
    Clears the terminal screen for future contents.
    Input: N/A
    Returns: N/A
    '''
    if os.name == "nt":  # windows
        os.system("cls")
    else:
        os.system("clear")  # unix (mac, linux, etc.)
        
def display_error(error):
    '''
    Displays an error message under the current site as specificed by "error".
    Input:
        - error (str): error message to display
    Returns: N/A
    '''
    move_cursor(0, 3)
    print("\033[6;31;40m{:^80}\033[0m".format(error))
    sleep(0.6)
    clear_screen()

def print_header():
    '''
    Prints the BROWSE-175 header.
    Input: N/A
    Returns: N/A 
    '''
    print("\033[0;32;40m{:^80}\033[0m".format("[ BROWSE-175 ]"))

def move_cursor(x, y):
    '''
    Moves the cursor to the specified location on the terminal.
    Input:
        - x (int): row number
        - y (int): column number
    Returns: N/A
    '''
    print("\033[{1};{0}H".format(x, y), end='')

def display_current_site(current):
    '''
    Displays the current site underneath the header.
    Input:
        - current (str): current site
    Returns: N/A
    '''
    print("\033[2;32;40m{:^80}\033[0m".format("Currently viewing: " + current))
    print("\033[4;30;40m{:^80}\033[0m".format(""))

def display_hint(message):
    '''
    Displays navigation hint message in the terminal.
    Input:
        - message (str): navigation hint message
    Returns: N/A
    '''
    print("\033[40;30;47m{:^80}\033[0m".format(message))

def display_buttons(back, fwd):
    '''
    Displays the navigational buttons at the top of the terminal.
    "(<) BACK" and "FORWARD (>)" labels should only be displayed
    if there are sites to go back or forward to.
    Input: 
        - back: stack of previous sites
        - fwd: stack of forward sites
    Returns: N/A
    '''
   # Check if the back stack has items
    if not back.isEmpty():
        back_label = "(<) BACK"  # Set the back label if items are available to go back to
    else:
        back_label = ""  # Leave back_label empty if there are no items in the back stack

    # Check if the forward stack has items
    if not fwd.isEmpty():
        fwd_label = "FORWARD (>)"  # Set the forward label if items are available to go forward to
    else:
        fwd_label = ""  # Leave fwd_label empty if there are no items in the forward stack

    # Print the buttons using the 80 char width alignment
    print(f"{back_label:<10}{'':^60}{fwd_label:>10}")

    

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
        print("\033[31mCannot go backward.")

    # Pause the script for 5 seconds before it ends
    sleep(2)

   
    
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
        print("\033[31mCannot go forward.")

    # Pause the script for 5 seconds before it ends
    sleep(2)


    return current


def main():
    HOME = 'www.cs.ualberta.ca'
    back = stack.Stack()
    fwd = stack.Stack()
    current = HOME
    quit = False

    while not quit:
        clear_screen()
        print_header()
        display_current_site(current)
        display_buttons(back, fwd)


        move_cursor(0, 20)
        display_hint("Use <, > to navigate, = to enter a URL, q to quit")
        print_location(5, 5, "Action: ")
        move_cursor(13, 5)
        action = input()
        if action == '=':
            current = goToNewSite(current, back, fwd)
        elif action == '<':
            current = goBack(current, back, fwd)
        elif action == '>':
            current = goForward(current, back, fwd)
        elif action == 'q':
            clear_screen()
            quit = True
        else:
            display_error('Invalid action!')
  

if __name__ == "__main__":
    main()