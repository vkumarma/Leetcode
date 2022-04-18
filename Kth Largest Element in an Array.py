class Heap:
    def __init__(self,size = 20000):
        self.cbt = [None] * size
        self.next_index = 0
    
    def insert(self,data):
        self.cbt[self.next_index] = data
        child_index = self.next_index
        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            parent = self.cbt[parent_index]
            child = self.cbt[child_index]
            if parent < child:
                self.cbt[parent_index] = child
                self.cbt[child_index] = parent
                child_index = parent_index
            else:
                break
        self.next_index += 1
                
    def remove(self):
        if self.next_index == 0:
            return None
        self.next_index -= 1
        to_remove = self.cbt[0]
        last_element = self.cbt[self.next_index]
        self.cbt[0] = last_element
        self.cbt[self.next_index] = to_remove # overwritten by insert
        parent_index = 0
        while parent_index < self.next_index:
            left_child_index = 2 * parent_index + 1
            right_child_index = 2 * parent_index + 2
            parent = self.cbt[parent_index]
            left_c = None
            right_c = None
            max_element = parent
            if left_child_index < self.next_index:
                left_c = self.cbt[left_child_index]
            if right_child_index < self.next_index:
                right_c = self.cbt[right_child_index]
            if left_c is not None:
                max_element = max(parent,left_c)
            if right_c is not None:
                max_element = max(max_element,right_c)
            if max_element == parent:
                break
            if max_element == left_c:
                self.cbt[left_child_index] = parent
                self.cbt[parent_index] = max_element
                parent_index = left_child_index
            
            elif max_element == right_c:
                self.cbt[right_child_index] = parent
                self.cbt[parent_index] = max_element
                parent_index = right_child_index
          
        return to_remove

def findKthLargest(nums, k):
    heap = Heap()
    count = 0
    for element in nums:
        heap.insert(element)
    
    while count != k:
        temp = heap.remove()
        count += 1
    return temp

print(findKthLargest([3,2,1,5,6,4],2)) # 5