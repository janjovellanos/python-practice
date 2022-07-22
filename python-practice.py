# def Equal(num1,num2):
#     return num1 == num2

# # print(Equal(4, 3))

# def not_equal(num1, num2):
#     # if num1 != num2:
#     #     print(True)
#     # else:
#     #     print(False)
#     return num1 != num2

# # print(not_equal(1,1))

# def And(val1, val2):
#     return val1 and val2

# # print(And(True, False))    #> False
# # print(And(True, True))     #> True
# # print(And(False, True))    #> False
# # print(And(False, False))   #> False

# def not_or(val1, val2):
#     return not val1 or val2

# # print(not_or(True, False))    #> False
# # print(not_or(True, True))     #> True
# # print(not_or(False, True))    #> True
# # print(not_or(False, False))   #> True

# def length_list(list, val):
#     return len(list) == val

# # print(length_list([], 1))   #>  False
# # print(length_list([], 0))   #>  True
# # print(length_list([5, 2], 2))   #>  True
# # print(length_list([1, 4, 3], 4))   #>  False
# # print(length_list([0, 2, "i", 0.9], 4))   #>  True

# def has_remainder(val1, val2):
#     return val1 % val2 != 0

# # print(has_remainder(4, 2))   #>  False
# # print(has_remainder(57, 4))  #>  True
# # print(has_remainder(6, 3))   #>  False
# # print(has_remainder(81, 7))  #>  True


# def xor(val1, val2):
#     return val1^val2

# # print(xor(False, False))   #>  False
# # print(xor(True, False))   #>  True
# # print(xor(True, True)) #>  False
# # print(xor(5, 3))  #> 6
# # print(xor(8, 4))  #> 12
# # print(xor(2, 2))  #> 0
# # print(xor(1, 2))  #> 3
# # print(xor(4, 4))  #> 0

# # def de_morgans_law (val1, val2):
# #     return not val1 or not val2

# def de_morgans_law (val1, val2):
#     return not (val1 and val2)

# # print(de_morgans_law(True, True)) # False
# # print(de_morgans_law(True, False)) # True
# # print(de_morgans_law(False, False)) # True
# # print(de_morgans_law("", [])) # True
# # print(de_morgans_law(2, 2)) # False
# # print(de_morgans_law(2, 0)) # True


# # print('sent message!')

# # print('''a comment block
# # keep writing typing
# # testing testin slekrjselrtjse
# # lrjselrjlserjsler
# # je
# # k''')

# def concat_name(first_name, last_name):
#     return f'{first_name} {last_name}'

# # print(concat_name("First", "Last"))  #> "Last, First"
# # print(concat_name("John", "Doe"))    #> "Doe, John"
# # print(concat_name("Mary", "Jane"))   #> "Jane, Mary"


# # print('''
# # this
# # is
# # a

# # multiline
# # string
# # ''')

# # print('''this
# # is
# # a

# # multiline
# # string''')

# # print("What's up, doc?")

# # print('The poet used "day" to mean "life".')

# # print('The bunny said, "Let\'s go to the library."')

# num = 5
# str = "5"
# # print('num {0}, str {1}, equal? {2}'.format(num, str, num==str))

# # print(f'num {num}, str {str}, equal? {num==str}')

# def format_name(first, last):
#     return f"Hi, my name is {first} {last}"

# # print(format_name("Alex", "Ambrose"))  #> Hi, my name is Alex Ambrose
# # print(format_name("Amy", "Mayer"))     #> Hi, my name is Amy Mayer
# # print(format_name("Rick", "Morty"))    #> Hi, my name is Rick Morty

# def index_string(str):
#     return str[3:-1]

# # print(index_string("Alchemy"))     #> hem
# # print(index_string("Ridiculous"))  #> iculou
# # print(index_string("Serendipity")) #> endipit

# # string = 'hello'

# # string[0] = 'p'

# # print(string)

# def index_of(string, letter):
#     return string.lower().index(letter.lower())

# # print(index_of("Arm", "a"))  #> 0
# # print(index_of("Pie", "e"))  #> 2
# # print(index_of("Lucid", "i"))  #> 3
# # print(index_of("Obvious","u"))  #> 5

# def is_last_character_n(name):
#     return name[-1] == 'n'

# # print(is_last_character_n("Aiden"))  #> True
# # print(is_last_character_n("Piet"))   #> False
# # print(is_last_character_n("Bert"))   #> False
# # print(is_last_character_n("Dean"))   #> True

# def long_burp(num):
#     return 'Bu' + 'r'*num + 'p'

# # print(long_burp(3))  #> "Burrrp"
# # print(long_burp(5))  #> "Burrrrrp"
# # print(long_burp(9))  #> "Burrrrrrrrrp"

# def last_three(str, substr):
#     return str.lower().endswith(substr.lower())

# # print(last_three("Power", "wer"))  #> True
# # print(last_three("Application", "App"))   #> False
# # print(last_three("Raw", "raw"))   #> True
# # print(last_three("Bonjour", "OUR"))   #> True

# def is_palindrome(str):
#     reverse = ''.join(reversed(str))

#     return str == reverse


# # print(is_palindrome("kayak")) # True
# # print(is_palindrome("app"))  # False
# # print(is_palindrome("racecar")) # True
# # print(is_palindrome("valid")) # False


# def recursive_string(str):
#     if len(str) == 0:
#         return str

#     return recursive_string(str[1:]) + str[0]


# # print(recursive_string("civic")) # civic
# # print(recursive_string("refer")) # refer
# # print(recursive_string("string")) # gnirts
# # print(recursive_string("avocado")) # odacova
# # print(recursive_string("application")) # noitacilppa

# def addition(num1, num2):
#     return num1 + num2

# # print(addition(2, 3))   #> 5
# # print(addition(-3, -6)) #> -9
# # print(addition(7, 3))   #> 10


# # tiny number
# int1 = 5
# float1 = 5.0
# # small number
# int2 = 135
# float2 = 135.246
# # huge number known as `googol`
# int3 = 10**100
# float3 = 10.0**100

# # print('** FIVE **')
# # print(int1 == float1)
# # print(float1)


# # print('\n** GOOGOL **')
# # 2A: Print int3
# # 2B: Print float3
# # 2C: Print equality comparison (==) between int1 and float3
# # print(int3)
# # print(float3)
# # print(int3 == float3)

# # print(int2 % int1)
# # print(float2 % float1)
# # print(float2 % int1)
# # print(int2 % float1)
# # print(int2 % float1)

# def increment(num):
#     return num + 1

# # print(increment(0))   #> 1
# # print(increment(9))   #> 10
# # print(increment(-3))  #> -2

# def min2sec(min):
#     return min * 60

# # print(min2sec(5)) #> 300
# # print(min2sec(3)) #> 180
# # print(min2sec(2)) #> 120

# def how_many_legs(chickens, cows, pigs):
#     return (chickens * 2 ) + (cows *4) + (pigs *4)

# # print(how_many_legs(2, 3, 5))    #> 36
# # print(how_many_legs(1, 2, 3))    #> 22
# # print(how_many_legs(5, 2, 8))    #> 50

# def string_int(input):
#     return int(input)


# # print(string_int("6"))     #> 6
# # print(string_int("1000"))  #> 1000
# # print(string_int("12"))    #> 12


# def calculate_exponent(base, exponent):
#     return base ** exponent

# # print(calculate_exponent(5, 5))     #> 3125
# # print(calculate_exponent(10, 10))   #> 10000000000
# # print(calculate_exponent(3, 3))     #> 27

# def integer_division(num1, num2):
#     return num1 // num2

# # print(integer_division(5.0, 2))     #> 2.0
# # print(integer_division(10, 10))     #> 1
# # print(integer_division(60, 8.0))    #> 7.0
# # print(integer_division(5.0, 1.0))   #> 5.0
# # print(integer_division(8, 2))       #> 4


from cmath import exp
from tokenize import Name


def find_digit_amount(n):
  l = len(str(n))
  if n < 0:
    return l - 1
  return l



# print(find_digit_amount(123))           #> 3
# print(find_digit_amount(-56))           #> 2
# print(find_digit_amount(7154))          #> 4
# print(find_digit_amount(61217311514))   #> 11
# print(find_digit_amount(0))             #> 1

def perfect_square (num1, num2):
    if num2**2 == num1:
        return True
    else:
      return False


# print(perfect_square(15, 5)) #> False
# print(perfect_square(25, 5)) #> True
# print(perfect_square(81, 9)) #> True
# print(perfect_square(9, 2))  #> False

def recursive_fib(num):
    if num <= 1:
        return num
    else:
        return(recursive_fib(num-1) + recursive_fib(num-2))

# print(recursive_fib(1))     #> 1
# print(recursive_fib(2))     #> 1
# print(recursive_fib(4))     #> 3
# print(recursive_fib(6))     #> 8
# print(recursive_fib(12))    #> 144

def recursive_countdown(num):
    if num == 0:
        return
    else:
        print(num)
        return (recursive_countdown(num -1) )

# recursive_countdown(5) #> 5 4 3 2 1

def is_prime(num, i=2):
    if(num < 2):
        return True
    if(num == 2):
        return False
    if(num < i * i):
        return True

    return is_prime(num, i + 1)



#DAY 2
def divisible_by_five(num):
    return num % 5 == 0

# print(divisible_by_five(5))    #> True
# print(divisible_by_five(-55))  #> True
# print(divisible_by_five(37))   #> False

def calculate_exponent(base, exponent):
    return base ** exponent

# print(calculate_exponent(5, 5))     #> 3125
# print(calculate_exponent(10, 10))   #> 10000000000
# print(calculate_exponent(3, 3))     #> 27

def remainder(num1, num2):
    return num1 % num2

# print(remainder(1, 3))  #> 1
# print(remainder(3, 4))  #> 3
# print(remainder(5, 5))  #> 0
# print(remainder(7, 2))  #> 1

def first_before_second(string, char1, char2):
    if string.index(char1) < string.index(char2):
        return True
    else:
        return False

# print(first_before_second("a rabbit jumps joyfully", "a", "j"))
# # > True
# # Every instance of "a" occurs before every instance of "j".

# print(first_before_second("knaves knew about waterfalls", "k", "w"))
# #> True

# print(first_before_second("happy birthday", "a", "y"))
# #> False
# # The "a" in "birthday" occurs after the "y" in "happy".

# print(first_before_second("precarious kangaroos", "k", "a"))
# > False

x = 1
y = '1'
list1 = [1, 2]
list2 = [1, 2]
list3 = [2, 3]

# print(x == x)
# print(x == y)
# print(list1 == list2)
# print(list1 == list3)

# x = 1
# y = '1'
# list1 = [1, 2]
# list2 = [1, 2]
# a = 10
# b = 10
# word1 = 'cat'
# word2 = 'cat'
# obj1 = { 0: 'cat'}
# obj2 = { 0: 'cat'}

# print(x == x)
# print(x is x)

# print(x == y)
# print(x is y)

# print(list1 == list2)
# print(list1 is list2)

# print(a == b)
# print(a is b)

# print(word1 == word2)
# print(word1 is word2)

# print(obj1 == obj2)
# print(obj1 is obj2)

# def largest_perimeter(numsArr):
#         for i in range(len(numsArr)):


# Example 1
# try:
#     str = 'hello'
#     str[0] = 'm'
#     print(str)
# except(TypeError) as e:
#     print('Error: ', e)
# finally:
#     print('I happen regardless of any exceptions.')

# Example 2
# try:
#     print(word)
# except(NameError) as e:
#     print('Error: ', e)
# finally:
#     print('I happen regardless of any exceptions.')


# Write your solution here.
# def print_list(list):
#     for i in list:
#         print(i)


# lst1 = [1, 2, 5, 1429]
# lst2 = ['this', 'list', 'is', 'being', 'printed']
# lst3 = ['there', 'are', 2, 'data', 'types', 'being', 'printed']
# lst4 = [[1, 2], ['hello', 'from', 'within']]
# print_list(lst1)        # 1 2 5 1429
# print_list(lst2)        # this list is being printed
# print_list(lst3)        # there are 2 data types being printed
# print_list(lst4)        # [1, 2] ['hello', 'from', 'within']

# guest_list = ["George", "Anthony", "Susan", "Tiffany"]

# def check_membership(guest_name, guest_list):
#     if guest_name in guest_list:
#         return True
#     else:
#         return False


# print(check_membership("Sally", guest_list))        # False
# print(check_membership("Anthony", guest_list))      # True

# print("** Doubling Penny **")

# # How many times would a penny need to double to generate a million dollars?
# count = 0
# total = 0

# # STEP 2: Write the while loop

# while total < 1000000:
#     if total == 0:
#         total = 0.01
#     else:
#         total *= 2
#     count +=1


# print('Double', count, 'times')

# # How much money has been generated at that point?
# print('${:,}'.format(total))


# def is_valid_hex_code(code):
#     if code[0] == '#' and len(code) == 7:
#         for i in code:
#             print(i)
#             if((not i.isalpha) or (not int(i).isnumeric)):
#                 return False
#             else:
#                 return True


# import re
# def is_valid_hex_code(code):
#     match = re.search(r’^#(?:[0-9a-fA-F]{3}){1,2}$’, code)
#     if match:
#         return True
#     else:
#         return False

# print(is_valid_hex_code("#CD5C5C")) #> True
# # print(is_valid_hex_code("#EAECEE")) #> True
# # print(is_valid_hex_code("#eaecee")) #> True


# def seq_of_numbers(input):
#     for i in input:
#         if i == i+1:
#             pass
#         else:

# print(seq_of_numbers("1211"))
# # This is "one 1, one 2, two 1s"
# # Prints "111221"

# print(seq_of_numbers("111221"))
# # This is "three 1s, two 2s, and one 1"
# # Prints "312211"

# print(seq_of_numbers("31131211131221"))
# # This is "one 3, two 1s, one 3, one 1, one 2, three 1s,
# #    one 3, one 1, two 2s, and one 1"
# # Prints "13211311123113112211"

# def cap_space(word):
#     res = ''
#     for i in word:
#         if i.isupper():
#             res += ' ' + i.lower()
#         else:
#             res += i
#     return res


# print(cap_space("helloWorld"))     #> "hello world"
# # print(cap_space("iLoveMyTeapot"))  #> "i love my teapot"
# # print(cap_space("stayIndoors"))    #> "stay indoors"


# def char_count(char, string):
#     count = 0
#     for el in string:
#         if el == char:
#             count += 1
#     return count

# print(char_count("a", "App Academy"))         #> 1
# print(char_count("c", "Chamber of Secrets"))  #> 1
# print(char_count("b", "big fat bubble"))      #> 4

# def vowel_count(string):
#     vowelsArr = 'aeiouAEIOU'
#     count = 0
#     for char in string:
#         if char in vowelsArr:
#             count += 1;
#     return count

# print(vowel_count("App Academy"))         #> 4
# print(vowel_count("Coding Expert"))       #> 4
# print(vowel_count("Supreme"))             #> 3
# print(vowel_count("Chamber of Secrets"))  #> 5

# def add_upper(string):
#     res = ''
#     for char in string:
#         if(char.isupper()):
#             res += char
#     return res

# print(add_upper("ApPlE"))        #> APE
# print(add_upper("Coding"))       #> C
# print(add_upper("PIano"))        #> PI
# print(add_upper("SUPREME"))      #> SUPREME




# STEP 1 - Write a function named `welcome` that prints a welcome message

# welcome = lambda : print('welcome')

# # Step 2 - Write a function named `calc_sum` that
# #   - takes in two numbers and
# #   - returns their sum
# calc_sum = lambda num1, num2: num1 + num2

# # DO NOT EDIT - The guts of the program
# welcome()

# print(calc_sum(1,2), 'is 3?', calc_sum(1,2) == 3)
# print(calc_sum(-10,-2), 'is -12?', calc_sum(-10,-2) == -12)
# print(calc_sum(1.1,-2.2), 'is -1.1?', calc_sum(1.1,-2.2) == -1.1)
# print(calc_sum('a','b'), 'is ab?', calc_sum('a','b') == 'ab')
# print(calc_sum([1,2],[3,4]), 'is [1,2,3,4]?',
#       calc_sum([1,2],[3,4]) == [1,2,3,4])

# Write your code here.
# def sample_function(arg1, arg2, input ='default'):
#     return print(arg1, arg2, input)


# # sample_function(input = "asdf", "a", "b")      # ERROR
# # sample_function("asdf", input = "a", "b")      # ERROcleaR
# sample_function("asdf", "a", input = "b")      # VALID

# Write your code here.
# def string_multi_print(str):
#     return lambda int: print(str * int)

# # string_multi_print = lambda str: print(str)


# string_multi_print('hello ')(2)  # Prints "hello hello "
# string_multi_print('wahoo ')(3)  # Prints "wahoo wahoo wahoo "

#  OUR ATTEMPT
# Write your code here.
# def merge_sort(list):
#     # Call merge somewhere in here
#     if len(list) > 1:
#         first_half = merge_sort(list[:len(lst)//2])
#         second_half = merge_sort(list[len(lst)//2:])
#         return merge(first_half, second_half)
#     return list

# def merge(lower, upper):
#     i = j = 0
#     temp = []
#     while i < len(lower) or j < len(upper):
#         if i == len(lower):
#             temp.append(upper[j])
#             j+=1
#         elif j == len(upper):
#             temp.append(lower[i])
#             i+=1
#         elif lower[i] < upper[j]:
#             temp.append(lower[i])
#             i+=1
#         else:
#             temp.append(upper[j])
#             j+=1
#     return temp


# lst = [5, 2, 38, 91, 16, 427]

# sorted_lst = merge_sort(lst)        # Out of place solution
# print(sorted_lst)

# merge_sort(lst)                     # In place solution
# print(lst)

# This is an out-of-place solution, see if you can do this in-place if you
# hadn't previously done so!

# def merge_sort(list):
#     if len(list) > 1:
#         mid = len(list)//2
#         lower_half = merge_sort(list[:mid])
#         upper_half = merge_sort(list[mid:])
#         return merge(lower_half, upper_half)
#     return list

# def merge(lower, upper):
#     i = j = 0
#     temp = []
#     while i < len(lower) or j < len(upper):
#         if i == len(lower):
#             temp.append(upper[j])
#             j+=1
#         elif j == len(upper):
#             temp.append(lower[i])
#             i+=1
#         elif lower[i] < upper[j]:
#             temp.append(lower[i])
#             i+=1
#         else:
#             temp.append(upper[j])
#             j+=1
#     return temp


# list = [5, 2, 38, 91, 16, 427]

# sorted_list = merge_sort(list)        # Out of place solution
# print(sorted_list)

# merge_sort(list)                     # In place solution
# print(list)

# nums = set([1,2,3,4,5,4,3,2,1])

# # nums2 = set('stringy')
# # # print(sum(nums2))
# # print(nums2)

# letters = set({'1234'})
# print(letters)              # {'a', 'r', 'b', 'c', 'd'}

# nums = [1,6,4.3,7,-8,9,2]
# # sorted(nums)
# print(nums.sort())
# print(nums)
# print(sorted(nums)[4:])

# # DO NOT EDIT - Starting with a simple lists of colors and numbers
# colors = ["blue", "Green", "PURPLE", "blue-green", "sky blue"]
# numbers = [2, 34, 8.5, -22.0, 33//4, 2**5]
# print ('COLORS', colors)
# print ('NUMBERS', numbers)

# 1. Print the total number of colors (length of the list)
# print(len(colors))

# # 2. Print the first color
# print(colors[0])

# # 3. Print the second and third colors
# print(colors[1:3])

# # 4. Print the last two colors
# print(colors[-2:])

# 5. Print the smallest number in the numbers list
# print(min(numbers))

# # 6. Print the largest number in the numbers list
# print(max(numbers))

# # 7. Sort the numbers
# print(sorted(numbers))

# # UNCOMMENT WHEN YOU WORK ON #7
# print ('SORTED NUMBERS', numbers)

# 8. Sort the colors alphabetically ignoring case
# print(sorted(colors, key=str.lower))
# colors.sort(key=str.lower)
# print(colors)
# UNCOMMENT WHEN YOU WORK ON #8
# print ('SORTED COLORS', colors)




# def get_first_value(list):
#     return list[0]
# print(get_first_value([1, 2, 3]))        #> 1
# print(get_first_value([80, 5, 100]))     #> 80
# print(get_first_value([-500, 0, 50]))    #> -500


# def get_sum_of_elements(list):
#     return sum(list)

# print(get_sum_of_elements([2, 7, 4]))     #> 13
# print(get_sum_of_elements([45, 3, 0]))    #> 48
# print(get_sum_of_elements([-2, 84, 23]))  #> 105


# def first_last(list):
#     # return [list[0]] + [list[len(list) -1]]
#     return [list[0], list[-1]]

# print(first_last([5, 10, 15, 20, 25]))          #> [5, 25]
# print(first_last([13, None, False, True]))        #> [13, True]
# print(first_last([None, 4, "6", "hello", None]))  #> [None, None]


# def sum_first_last_list(list1, list2):
#     return list1[0] + list2[-1]

# print(sum_first_last_list([1, 2, 3], [5, 8, 9]))     #> 10
# print(sum_first_last_list([53, 26], [5]))            #> 58
# print(sum_first_last_list([9], [5, 8]))              #> 17
# print(sum_first_last_list([64], [5, 6, 2]))          #> 66

# # Write your function, here.
# # def insertion_sort(lst):
# #     for i in range(1, len(lst)):
# #         ele = lst[i]
# #         j = i-1
# #         while lst[j] > ele and j >= 0:
# #             lst[j+1] = lst[j]
# #             j -= 1
# #         lst[j+1] = ele
# #     return lst

# # print(insertion_sort([55, 21, 5, 3, 6, 95])) #> [3, 5, 6, 21, 55, 95]
# # print(insertion_sort([4, 1, 0, 3, 8, 9])) #> [0, 1, 3, 4, 8, 9]
# # print(insertion_sort([1, 4, 3, 0, 3, 0, 2, 8])) #> [0, 0, 1, 2, 3, 3, 4, 8]




# def get_indices(list, item):
#     res = []
#     i = 0
#     for el in list:
#         if el == item:
#             res.append(i)
#         i += 1
#     return res

# #another solution
# def get_indices(lst, val):
#   indices = []
#   for i in range(0, len(lst)):
#     if val == lst[i]:
#       indices.append(i)
#   return indices


# print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
# # Prints [0, 1, 3, 5]

# print(get_indices([1, 5, 5, 2, 7], 7))
# # Prints [4]

# print(get_indices([1, 5, 5, 2, 7], 5))
# # Prints [1, 2]

# print(get_indices([1, 5, 5, 2, 7], 8))
# # Prints []

# def sorted_arr(list, target):
#     res = []
#     sorted_list = sorted(list)
#     for i in range(0, len(sorted_list)):
#         if target == sorted_list[i]:
#             res.append(i)
#     return res

# print(sorted_arr([1,2,5,2,3], 2))
