#----------------------------------------------------
# Lab 4: Web browser simulator
# Purpose of program:
#
# Author: 
# Collaborators/references:
#----------------------------------------------------

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
           print("Invalid entry.")
           
           
  


def goToNewSite(current, pages):
    '''

    Parameters:
    current - Current index of the page being viewed (int)
    pages - List of website addresses (list)

    Inputs:
    Prompts the user to enter a new website address

    Returns:
    Updated current index (int) pointing to the new site

    '''   
    new_url = input("Please enter a new URL: ")

    # Add the new URL to the list
    pages.append(new_url)

    # Return the index of the new URL (the last element in the list)
    # This will be assigned to `currentIndex` in `main()`
    return len(pages) - 1  # This new index is the new "current" index

    
    

    
def goBack(current, pages):
    '''
    Parameters:
    current - Current index of the page being viewed (int)
    pages - List of website addresses (list)

    Inputs:
    the  '<' key

    Returns: 
    the updated index of the page being viewed after going back.
    
    '''  
    if current > 0:  # Ensure we're not at the first page
        current -= 1  # Move back by one index
    else:
        print("Cannot go back.")
    return current  # Return the updated index





def goForward(current, pages):
    '''
    Parameters:
    current - Current index of the page being viewed (int)
    pages - List of website addresses (list)

    Inputs:
    the  '>' key

    Returns: 
    the updated index of the page being viewed after going foward.

    '''    
    #Check if there is a next page to move forward to
    if current < len(pages) -1:  # check if we are at the last index
        current += 1  # Move front by one index if we arent. That is move foward
    else:
        print("Cannot go forward.")
    return current  # Return the updated index
  

def main():
    '''
    Controls main flow of web browser simulator
    Inputs: N/A
    Returns: None
    '''    
    HOME = 'www.cs.ualberta.ca'
    websites = [HOME]
    currentIndex = 0
    quit = False
    
    while not quit:
        print('\nCurrently viewing', websites[currentIndex])
        action = getAction()
        
        if action == '=':
            currentIndex = goToNewSite(currentIndex, websites)
        elif action == '<':
            currentIndex = goBack(currentIndex, websites)
        elif action == '>':
            currentIndex = goForward(currentIndex, websites)
        elif action == 'q':
            quit = True
    
    print('Browser closing...goodbye.')    

        
if __name__ == "__main__":
    main()


   