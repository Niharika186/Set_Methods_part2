'''The elements which are same in both sets it will be removed'''
# a={1,2,3}
# b={3,5,6,7}
# a.difference_update(b)
# b.difference_update(a)
# print(a) # {1,2}
# print(b) # {5, 6, 7}

# a={5,6,7}
# a.copy()
# print(a) # {5,6,7}


'''we get the unique elements from both the sets'''
# a={5,10,15,20,25}
# b={10,20}
# a.symmetric_difference_update(b)
# print(a) # {5, 25, 15}
# b.symmetric_difference_update(a)
# print(b) # {5, 25, 15}

# a={2,4,6}
# b={3,6,9}
# a.intersection_update(b)
# b.intersection_update(a)
# print(a) # {6}
# print(b) # {6}

# x={11,22,33}
# x.remove(11) 
# print(x) # {33, 22}
# x.remove(44)
# print(x) # KeyError


'''Both the set should contain same element,the another set can contain less elements with same values,but it should not contain unique elements'''
# x={10,20,30,40}
# y={10,20}
# print(x.issuperset(y)) # True
# print(y.issuperset(x)) # False


