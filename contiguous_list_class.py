class List:
    def __init__(self, maximum):
        self.__begning = -1
        self.__ending = -1
        self.__maximum = maximum

    def __repr__(self):
        if self.isEmpty(): #if the list is empty returns an empty vector
            return '[]'
        else: #if the list is not empty, this formats and returns the content
            items = '['
            for i in range(self.__begning, self.__ending):
                items = items + "'" + str(self.vector[i]) + "'" + ", "
            items = items + "'" + str(self.vector[self.__ending]) + "'" + ']'
            return items

    def isEmpty(self):
        if self.__begning == -1 or self.__ending == -1: #checks if there is is something in the list
            return True
        else:
            return False
    
    def length(self):
        return self.__ending + 1 #returns the index of the ending plus 1, which is the length

    def get_index(self, item):
        for i in range(0, self.length()):
            if self.vector[i] == item:
                return i
        return False

    def get_item(self, index):
        if index >= 0 and index < self.length():
            return self.vector[index]
        return False

    def is_index_valid(self, index):
        if index >= self.__begning and index <= self.__ending + 1: #checks if it is a valid index to insert
            return True
        else:
            return False

    def insert(self, item, index=int):
        if self.length() < self.__maximum: #checks if there is free space in the list
            if self.isEmpty(): #if it is the first item to be inserted, do this
                if index == 0:
                    self.vector = [None]
                    self.vector[0] = item
                    self.__begning = 0
                    self.__ending = 0
                    return True
                else:
                    return False
            elif self.is_index_valid(index): #if it's not the first item and the index is valid, do this
                if [None] not in self.vector:
                    self.vector = self.vector + [None]
                for i in range(self.__ending, index -1, -1):
                    self.vector[i+1] = self.vector[i]
                self.vector[index] = item
                self.__ending = self.__ending + 1
                return True
            else:
                return False
        else:
            return False

    def remove(self, delete_this_index):
        if delete_this_index >= 0 and delete_this_index <= self.__ending: #checks if the index exists
            for i in range(delete_this_index, self.__ending):
                self.vector[i] = self.vector[i + 1] #delete the index by overscribing it
            self.vector[self.__ending] = [None]
            self.__ending = self.__ending - 1
            return True
        else:
            return False

    def empty_list(self):
        self.vector = [None]
        self.__begning = -1
        self.__ending = -1
