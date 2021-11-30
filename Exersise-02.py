#Exercise-02
"""Write a function in Python which takes two sequences
as arguments and returns True if every element in a
sequence is also an element of second sequnce, else
False."""

def common_data(list1, list2):
    result = False
    for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result
             elif x != y:
                 result = False
                 return result
print(common_data([1,2,3,4,5], [1,2,3,4,5]))
print(common_data([1,2,3,4,5], [6,7,8,9,10]))
