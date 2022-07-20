def Equal(num1,num2):
    return num1 == num2

# print(Equal(4, 3))

def not_equal(num1, num2):
    # if num1 != num2:
    #     print(True)
    # else:
    #     print(False)
    return num1 != num2

# print(not_equal(1,1))

def And(val1, val2):
    return val1 and val2

# print(And(True, False))    #> False
# print(And(True, True))     #> True
# print(And(False, True))    #> False
# print(And(False, False))   #> False

def not_or(val1, val2):
    return not val1 or val2

# print(not_or(True, False))    #> False
# print(not_or(True, True))     #> True
# print(not_or(False, True))    #> True
# print(not_or(False, False))   #> True

def length_list(list, val):
    return len(list) == val

# print(length_list([], 1))   #>  False
# print(length_list([], 0))   #>  True
# print(length_list([5, 2], 2))   #>  True
# print(length_list([1, 4, 3], 4))   #>  False
# print(length_list([0, 2, "i", 0.9], 4))   #>  True

def has_remainder(val1, val2):
    return val1 % val2 != 0

print(has_remainder(4, 2))   #>  False
print(has_remainder(57, 4))  #>  True
print(has_remainder(6, 3))   #>  False
print(has_remainder(81, 7))  #>  True
