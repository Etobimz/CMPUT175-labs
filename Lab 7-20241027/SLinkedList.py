class SLinkedListNode:
    # an instance of this class is a node in a Single Linked List
    # a node has a reference to data and reference to next
    def __init__(self,initData,initNext):
        self.data = initData
        self.next = initNext
        
    def getNext(self):
        return self.next
    
    def getData(self):
        return self.data
    
    def setData(self,newData):
        self.data = newData
        
    def setNext(self,newNext):
        self.next = newNext


class SLinkedList:
    # an instance of this class is a Singly-Linked List object
    # it has reference to the first node in the list
    def __init__(self):
        self.head = None
        self.size = 0
         

    def add(self,item):
        # adds an item at the start of the list
        new_node = SLinkedListNode(item,None)
        new_node.setNext(self.head)
        self.head = new_node
        self.size = self.size + 1
        
    def append(self,item):
        # adds an item at the end of the list
        new_node = SLinkedListNode(item,None)
        current = self.head # Start the traversal
        if self.size == 0: # check if list is empty
            self.add(item)
        else:
            while (current.getNext()!=None):
                current= current.getNext() # traversing the list
            current.setNext(new_node)
            self.size = self.size +1


    def insert(self,pos,item):
        """
        function confirms the user input is valid and inserts 
        the input in the desired position in the linked list

        param;
        pos: postion to fix new input
        item; user data to be inserted
        
        """

        # confirms the list is not empty
        if self.getSize() < 0:
            print("Can't insert in an empty list")

        else:
            # checks and confirms the pos is an integer
            assert isinstance(pos, int), 'pos should be a an integer'
        
            # checks and confirms the pos is non negative
            assert pos >= 0 and pos <= self.getSize(), 'pos has to be a postive integer and less than list size' 


            # adds an item to the first index/ the start of the list 
            #  and if the list is empty, the node gets added to the first index too
            if pos == 0:
                self.add(item)

            # adds an item to the last index/ the end of the list
            elif pos == self.getSize():
                self.append(item)

            # checks and confirm the pos index is the middle and inserts the pos in the middle of the list 
            elif pos == self.getSize() // 2:
                #traverse until we get to the middle postion
                count = 0
                current = self.head

                while count < pos - 1:
                    current = current.getNext()
                    count += 1
                #  setting the new node to the postion
                new_middle_node = SLinkedListNode(item, current.getNext())
                current.setNext(new_middle_node)
                self.size = self.size + 1

            # if the position is not at midddle index or start or end
            else:
                count = 0 
                current = self.head

                # Traverse to the postion
                while count < pos - 1:
                    current = current.getNext()
                    count += 1

                # setting the new node to the postion
                new_node = SLinkedListNode(item, current.getNext())
                current.setNext(new_node)
                self.size = self.size + 1


    def remove(self,item):
        # remove the node containing the item from the list
        if self.size == 0:
            raise Exception('List is Empty')
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if not found:
            raise Exception('Item not in list')
        else:
            if previous == None: # the item is in the first node of the list
                self.head = current.getNext()
            else: # item is not in the first node
                previous.setNext(current.getNext())
            self.size = self.size -1
            
    def index(self,item):
        # finds the location of the item in the list
        if self.size == 0:
            raise Exception('List is empty')
        position = 0
        found = False
        current = self.head
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                position = position + 1
        if found:
            return position
        else:
            return 'Item not found'
        
    def pop(self):
        # removes the node from the end of the list and returns the item 
        if self.size == 0:
            raise Exception('List is empty')
        current = self.head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = None
        else:
            previous.setNext(None)
        self.size = self.size -1
        return current.getData()
    
    def __str__(self):
        # returns a string representation of the list
        current = self.head
        string = ''
        while current != None:
            string = string + str(current.getData())+'->'
            current = current.getNext()
        return string
    
    def getSize(self):
        return self.size

    
def main():
    # Testing Singly-Linked List
    slist = SLinkedList()
    slist.add(2)
    slist.add(4)
    slist.add('A')
    slist.append(77)
    slist.append(6)
    slist.append('Z')
    print('Original List:', slist.getSize(), 'elements')
    print(slist)
    print()
    slist.insert(0, 'start')
    print('After inserting the word start at position 0:', slist.getSize(), 'elements')
    print(slist)
    print()
    slist.insert(7, 'end')
    print('After inserting the word end at position 7:', slist.getSize(), 'elements')
    print(slist)
    print()
    slist.insert(4, 'middle')
    print('After inserting middle at position 4:', slist.getSize(), 'elements')
    print(slist)
    
    
if __name__=="__main__":
    main()
