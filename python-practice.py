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

# print(has_remainder(4, 2))   #>  False
# print(has_remainder(57, 4))  #>  True
# print(has_remainder(6, 3))   #>  False
# print(has_remainder(81, 7))  #>  True


def xor(val1, val2):
    return val1^val2

# print(xor(False, False))   #>  False
# print(xor(True, False))   #>  True
# print(xor(True, True)) #>  False
# print(xor(5, 3))  #> 6
# print(xor(8, 4))  #> 12
# print(xor(2, 2))  #> 0
# print(xor(1, 2))  #> 3
# print(xor(4, 4))  #> 0

# def de_morgans_law (val1, val2):
#     return not val1 or not val2

def de_morgans_law (val1, val2):
    return not (val1 and val2)

# print(de_morgans_law(True, True)) # False
# print(de_morgans_law(True, False)) # True
# print(de_morgans_law(False, False)) # True
# print(de_morgans_law("", [])) # True
# print(de_morgans_law(2, 2)) # False
# print(de_morgans_law(2, 0)) # True


# print('sent message!')

# print('''a comment block
# keep writing typing
# testing testin slekrjselrtjse
# lrjselrjlserjsler
# je
# k''')

def concat_name(first_name, last_name):
    return f'{first_name} {last_name}'

# print(concat_name("First", "Last"))  #> "Last, First"
# print(concat_name("John", "Doe"))    #> "Doe, John"
# print(concat_name("Mary", "Jane"))   #> "Jane, Mary"


# print('''
# this
# is
# a

# multiline
# string
# ''')

# print('''this
# is
# a

# multiline
# string''')

# print("What's up, doc?")

# print('The poet used "day" to mean "life".')

# print('The bunny said, "Let\'s go to the library."')

num = 5
str = "5"
# print('num {0}, str {1}, equal? {2}'.format(num, str, num==str))

# print(f'num {num}, str {str}, equal? {num==str}')

def format_name(first, last):
    return f"Hi, my name is {first} {last}"

# print(format_name("Alex", "Ambrose"))  #> Hi, my name is Alex Ambrose
# print(format_name("Amy", "Mayer"))     #> Hi, my name is Amy Mayer
# print(format_name("Rick", "Morty"))    #> Hi, my name is Rick Morty

def index_string(str):
    return str[3:-1]

# print(index_string("Alchemy"))     #> hem
# print(index_string("Ridiculous"))  #> iculou
# print(index_string("Serendipity")) #> endipit

# string = 'hello'

# string[0] = 'p'

# print(string)

def index_of(string, letter):
    return string.lower().index(letter.lower())

# print(index_of("Arm", "a"))  #> 0
# print(index_of("Pie", "e"))  #> 2
# print(index_of("Lucid", "i"))  #> 3
# print(index_of("Obvious","u"))  #> 5

def is_last_character_n(name):
    return name[-1] == 'n'

# print(is_last_character_n("Aiden"))  #> True
# print(is_last_character_n("Piet"))   #> False
# print(is_last_character_n("Bert"))   #> False
# print(is_last_character_n("Dean"))   #> True

def long_burp(num):
    return 'Bu' + 'r'*num + 'p'

# print(long_burp(3))  #> "Burrrp"
# print(long_burp(5))  #> "Burrrrrp"
# print(long_burp(9))  #> "Burrrrrrrrrp"

def last_three(str, substr):
    return str.lower().endswith(substr.lower())

# print(last_three("Power", "wer"))  #> True
# print(last_three("Application", "App"))   #> False
# print(last_three("Raw", "raw"))   #> True
# print(last_three("Bonjour", "OUR"))   #> True

def is_palindrome(str):
    reverse = ''.join(reversed(str))

    return str == reverse


# print(is_palindrome("kayak")) # True
# print(is_palindrome("app"))  # False
# print(is_palindrome("racecar")) # True
# print(is_palindrome("valid")) # False
