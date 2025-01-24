class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self, initData, initNext, initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def search(self, item):
        current = self.__head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()

        return found

    def index(self, item):
        current = self.__head
        found = False
        index = 0

        while current != None and not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()
                index = index + 1

        if not found:
            index = -1

        return index

    def add(self, item):
        """
        adds the item to the start of the list
        param;
        item; user data to be inserted
        
        """
        new_node = DLinkedListNode(item,None,None)

         # adds to the start if the list was empty
        if self.__head == None:
            self.__head = new_node
            new_node.setPrevious(None)

        # adds to the start by replacing the first node at index 0 or first index if the list was nonempty
        elif self.__head != None:
            new_node.setNext(self.__head)
            self.__head.setPrevious(new_node)

            # update the head to point to new node
            self.__head = new_node

            new_node.setPrevious(None)
         
        # increase the list size
        self.__size += 1



    def remove(self, item):
        """
        removes the first element in the list that is equal to the item

        param;
        item; user data to be inserted 
        
        """
        
        current = self.__head
        previous = None
        found = False

        # traverse until we get the item that is equal to new item
        while current is not None and not found: #enables us to loop through without raising an error if item not found
            if current.getData() == item:
                found = True

                # head of the list
                if previous == None:
                    self.__head = current.getNext()

                # not head of the list
                else:
                    previous.setNext(current.getNext())

                # not the last item
                if current.getNext() != None:
                    current.getNext().setPrevious(previous)
        
                # last item in the list
                else:
                    self.__tail = previous


                # reduce the list size
                self.__size -= 1
              
            else:
                previous = current
                current = current.getNext()


    def append(self, item):
        """
        
        adds a new node to the tail of the list with item as its data

        param;
        item; user data to be inserted
        
        """

        new_node = DLinkedListNode(item,None,None)
        # if the list is empty
        if self.__head == None:
            self.__head = new_node
            new_node.setPrevious(None)
            
            
        # if the list is non empty
        elif self.__head != None:
            #traverse till the last index
            current = self.__head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(new_node)
            new_node.setPrevious(current)


        # Increment the size of the list after each append
        self.__size += 1
            


    def insert(self, pos, item):
        """
        function confirms the user input is valid and inserts 
        the input in the desired position in the linked list

        param;
        pos: postion to fix new input
        item; user data to be inserted

        """

        
        new_node = DLinkedListNode(item,None,None)

        # confirms the list is not empty
        if self.getSize() < 0:
            raise Exception('you cant insert in a empty list')


        # checks and confirms the pos is an integer
        elif type(pos) != int:
            raise Exception ('pos should be a an integer')

        # checks and confirms the pos is non negative
        elif pos < 0 or pos > self.getSize():
            raise Exception ('pos has to be a postive integer and less than list size')

        previous = None
        current = self.__head
        count = 0

        # adds an item to the first index/the start of the list for both empty and non empty list
        if pos == 0:
            self.add(item)

        # inserting at the end of the list
        elif pos == self.getSize():
            self.append(item)

        # inserting in the middle of the list
        elif pos == self.getSize() // 2:

            # Traverse until we get to the position to insert the item
            while count < pos - 1:
                current = current.getNext()
                count += 1

            #  setting the new node to the postion
            current.setNext(new_node)
            new_node.setPrevious(current)
            self.__size += 1

        # inserting anyhwere in the list not the start or end or middle
        else:
            # Traverse until we get to the position to insert the item
            while count < pos - 1:
                current = current.getNext()
                count += 1

            #  setting the new node to the postion
            current.setNext(new_node)
            new_node.setPrevious(current)
            self.__size += 1
     
        

    def pop1(self):
        # removes and returns the last item in the list
        if self.getSize() == 0:
            raise Exception('You cant remove from an empty list')
    
        prev = None
        current = self.__head

        # Traverse to the end of the list
        while current.getNext() is not None:
            prev = current
            current = current.getNext()

        # If there's only one element, reset head and tail to None
        if prev == None:
            self.__head = None
            self.__tail = None
        else:
            prev.setNext(None)
            self.__tail = prev  # Update the tail

        # Decrement the size and return the data of the removed node
        self.__size -= 1
        return current.getData()

    def pop(self, pos=None):
        #  removes and returns the item in the given position.
        if self.getSize() == 0:
            raise Exception('You cant remove from an empty list')
        
        # chechk if int
        elif pos is not None and type(pos) != int:
            raise Exception('pos should be an integer')
    
        # Check if pos is within the list's range
        elif pos is not None and (pos < 0 or pos >= self.getSize()):
            raise Exception('pos has to be a positive integer and less than list size')
        
        previous = None
        current = self.__head
        count = 0

        # removes the last item
        if pos == None:
            return self.pop1()

        # remove from the first index if only one element
        elif self.getSize() and pos == 0:
            return self.pop1()
        
        # remove from the first index if more than 1 element in list
        elif self.getSize() > 0 and pos == 0:
            self.__head = current.getNext
            self.setPrevious(None)
           
        # remove from anyhwere in the list not start or end
        while current is not None and count < pos:
            previous = current
            current = current.getNext()
            count += 1

        previous.setNext(current.getNext())

        # Update next node's previous pointer if it's not the last node
        if current.getNext():  
            current.getNext().setPrevious(previous)

        # Decrement the size and return the data of the removed node
        self.__size -= 1
        return current.getData()

    def searchLarger(self, item):
        """
        returns the position of the first element that is larger than the item

        param;
        item; user data
        
        """
        current = self.__head
        position = 0
    
        while current is not None:
            if current.getData() > item:
                return position
            current = current.getNext()
            position += 1

        return -1

    def getSize(self):
        return self.__size
        

    def getItem(self, pos):
        # Handle empty list case
        if self.getSize() == 0:
            raise Exception('Cannot get an item from an empty list')

        # Handle non-integer position
        if not isinstance(pos, int):
            raise Exception('Position should be an integer')

         # Adjust negative indices
        if pos < 0:
            pos += self.getSize() # More concise and Pythonic

        # Handle out-of-bounds indices *after* adjusting for negative indices
        if pos < 0 or pos >= self.getSize():
            raise Exception("Position out of range")

        #  traverse from the tail if closer to the end
        if pos > self.getSize() // 2: 
            current = self.__tail
            count = self.getSize() - 1
            while count > pos:
                current = current.getPrevious()
                count -= 1
        else: # Traverse from the head if closer to the beginning
            current = self.__head
            count = 0
            while count < pos:
                current = current.getNext()
                count += 1

        return current.getData()



    def __str__(self):
        # create the string representation of the linked list
        elements = []
        current_node = self.__head  

        while current_node is not None:
            elements.append(str(current_node.getData()))  # Collect node data values
            current_node = current_node.getNext()

        return " ".join(elements)  # Join with a space to match the expected output





def test():

    linked_list = DLinkedList()

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    linked_list.add("World")
    linked_list.add("Hello")

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) ==
               "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
    x = linked_list.pop(1)
    is_pass = (x == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    int_list2 = DLinkedList()

    for i in range(0, 10):
        int_list2.add(i)
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"

    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    for i in range(21, 23):
        int_list2.insert(0, i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
    x = int_list2.getSize()
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"

    int_list = DLinkedList()

    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    for i in range(0, 1000):
        int_list.append(i)
    correctOrder = True

    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"

    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False

    is_pass = correctOrder
    assert is_pass == True, "fail the test"

    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test"

    int_list.insert(7, 801)
    x = int_list.searchLarger(800)
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"

    x = int_list.getItem(-1)
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"

    if is_pass == True:
        print("=========== Congratulations! Your have finished exercise 2! ============")


if __name__ == '__main__':
    test()


