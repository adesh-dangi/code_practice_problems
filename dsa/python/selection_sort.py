class Sorting_class:
        
    def selection_sort(self,array:list)->list:
        """
        check for lowest value
           compare it if its lowest
           swap it with the first value
           O(n^2) : time
           O(1)   : space
        """
        size_n = len(array)
        for i in range(size_n):
            lowest_value_index = i
            for j in range(i+1, size_n):
                if array[lowest_value_index] > array[j]:
                    lowest_value_index = j
            array[i], array[lowest_value_index] = array[lowest_value_index], array[i]
        return array
    
    def bubble_sort(self, array:list) -> list:
        """
        iterate pick one value
           iterate from 2nd position
              compare with first value 
              if 2nd value smaller then swap with first
        O(n^2) : time (best O(n)=already sorted)
        O(1)   : space
        """
        changed=False
        for i in range(len(array)):
            for j in range(i+1, len(array)-2):
                # print(array[i], array[j], array)
                if array[i] > array[j]:
                    array[i],array[j] = array[j], array[i]
                    changed=True
            if changed:
                break
        return array
    

selection_sort = Sorting_class().bubble_sort   


# case1
a = [2,1,3,4,5,6,7,8,9,10]
print("before : ", a)
print("after : ", selection_sort(a))

#case2
a = [10,9,8,7,6,5,4,3,2,1]
print("before : ", a)
print("after : ", selection_sort(a))

#case3
a = [1,2,3,4,5,6,7,8,9,10]
print("before : ", a)
print("after : ", selection_sort(a))