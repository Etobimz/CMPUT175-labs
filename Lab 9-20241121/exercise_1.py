import random
import time

#---------------------------------------#      
# Implement Recursive selection sort here. 

# n: size of array - index is index of starting element
def recursive_selection_sort(data, data_len, index = 0): 

    """
    function to sort numbers in a list in descending order

    param;
    data: list to be sorted

    data_len: list length

    index; int - current index being processed

    """
  
    # TODO-Remove pass and fill out the rest. 
    #You may use additional user_defined functions if required.
    
    # Set the base case 
    if index >= data_len - 1:
        return 
    
    # Find the index of the largest element in the unsorted part of the list

    biggest_no = index

    for i in range(index+1, data_len):
        if data[i] > data[biggest_no]:
            biggest_no = i
      
    # Swap the data 
    if biggest_no != index:
        temp = data[index]
        data[index] = data[biggest_no]
        data[biggest_no] = temp
          
    # Recursively calling selection sort function 
    recursive_selection_sort(data, data_len, index+1)


#---------------------------------------#
#Implement the Recursive merge sort here

def merge_sort(left_list, right_list):
    """
    Function to merge two sorted lists into a single sorted list in descending order.
    
    param:
        left_list (list): The first sorted sublist.
        right_list (list): The second sorted sublist.
    
    Returns:
        list: A merged sorted list in descending order.
    """
    merged_list = []
    i = 0  # Pointer for left_list
    j = 0  # Pointer for right_list

    # Merge the two lists by comparing their elements
    while i < len(left_list) and j < len(right_list):
        if left_list[i] > right_list[j]:  # Descending order comparison
            merged_list.append(left_list[i])
            i += 1
        else:
            merged_list.append(right_list[j])
            j += 1

    # Add remaining elements from left_list
    while i < len(left_list):
        merged_list.append(left_list[i])
        i += 1

    # Add remaining elements from right_list
    while j < len(right_list):
        merged_list.append(right_list[j])
        j += 1

    return merged_list


def recursive_merge_sort(data): 
    """
    Function to sort a list of numbers in descending order using recursive merge sort.

    param:
        data (list): The list to sort.
    
    Returns:
        list: The sorted list in descending order.
    """
    # Base case: A list of one or zero elements is already sorted
    if len(data) <= 1:
        return data

    # Find the middle of the list
    middle = len(data) // 2

    # Recursively sort the left and right halves
    left_list = recursive_merge_sort(data[:middle])
    right_list = recursive_merge_sort(data[middle:])

    # Merge the two sorted halves and return
    return merge_sort(left_list, right_list)

#---------------------------------------#
if  __name__== "__main__":
    # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
       
    # Calculate the execution time to sort a list of random numbers #
    random_list_ = random_list.copy()  # make a copy to save the unsorted list
    start_sel = time.time()
    recursive_selection_sort(random_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
    
    
    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    ascending_list_ = ascending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(ascending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in ascending order 
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))      
    
    
    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    descending_list_ = descending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(descending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))


#  The merge sort takes the least amount of time to sort items