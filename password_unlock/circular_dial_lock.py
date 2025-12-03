class SingleNodeInLock:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class CircularDialedLock:
    def __init__(self, headValue=None):
        self.head = SingleNodeInLock(headValue)
        self.current = self.head

    def append_last(self, value):
        new_node = SingleNodeInLock(value)
        self.current.next = new_node
        new_node.previous = self.current
        self.current = new_node
        self.head.previous = self.current
        self.current.next = self.head

    def print_list(self, last_val):
        temp = self.head
        i = 0
        while i <= last_val:
            print(temp.value)
            print("Next:",temp.next.value)
            print("Previous:",temp.previous.value)
            temp = temp.next
            i=i+1
    def set_current(self, index):
        temp = self.head
        i = 0
        while i < index:
            temp = temp.next
            i=i+1
        self.current = temp

    def traverse_left(self, dials):
        temp = self.current
        i=0
        no_of_times_wrapped = 0
        while i < dials:
            temp = temp.previous
            if temp.value == 0:
                no_of_times_wrapped = no_of_times_wrapped + 1
            i=i+1
        self.current = temp
        return no_of_times_wrapped

    def traverse_right(self, dials):
        temp = self.current
        i=0
        no_of_times_wrapped = 0
        while i < dials:
            temp = temp.next
            if temp.value == 0:
                no_of_times_wrapped = no_of_times_wrapped + 1
            i=i+1
        self.current = temp
        return no_of_times_wrapped
