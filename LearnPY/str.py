# Strings in Python

srting = "Hello, World!"

multiline_string = """Hello, World!
This is a multiline string"""

'''this is a comment'''

print(srting, multiline_string,"main string")

# Indexing in string same as array start form 0
#  N index is not inclusive in sliceing for [2:5] 5 is excluded

print(srting[1], "index") 
print(srting[-1],srting[-2])
print(srting[2:5], "slice") # slice  from 2 to 5
print(srting[-5:-2]) # slice from -5 to -2
print(srting[:5]) # slice from start to 5
print(srting[2:]) # slice from 2 to end

# String length

print(len(srting), "length") # length of string in num

# Join a string (concatenation using +)

print(srting + " " + "concatenation") # concatenation
print(srting + " " + str(5)) # concatenation with num
print(srting + " " + str(5.5)) # concatenation with float
print(srting + " " + str(True)) # concatenation with boolean
print(srting + " " + str(["apple", "banana", "cherry"])) # concatenation with list
print(srting+multiline_string)

# Format strings

print("Hello, {}".format("World!")) # format string

# using format funciton


# Escape characters 

# String methods


print(srting.strip(), "strip") # remove white space from start and end
print(srting.lower(), "lower") # convert to lower case 
print(srting.upper(), "upper") # convert to upper case
print(srting.replace("H", "J"), "replace") # replace H with J
print(srting.split(","), "split") # split string by ,
print(srting.index("W"), "index") # find index of W
            # is digit is numaric is also ther to check returns boolean value
print(srting.isalnum(), "isalnum") # check if all char are numaric



# use \' for year's using ' in string this is know as escape character



# Check string



# swapcase problem 

def swap_case(s):
    result = []
    for char in s:
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
    return ''.join(result)

input_string = "HackerRank.com presents \"Pythonist 2\"."
output_string = swap_case(input_string)
print(output_string)


# string in string find substring
def contains_substring(main_str, sub_str):
    return sub_str in main_str

main_str = "hi my name is hi"
sub_str = "hi"

result = contains_substring(main_str, sub_str)
print(result)



# remove integer(num) from the list of string
my_list = ['Ar3n', 'd23pa4', 'ds4gh6', 'b3l3']
for i in range(len(my_list)):
    # Use list comprehension to remove digits
    my_list[i] = ''.join([char for char in my_list[i] if not char.isdigit()])
print(my_list)

my_list = ['Ar3n', 'd23pa4', 'ds4gh6', 'b3l3']

# Function to remove digits from a string
def remove_digits(s):
    result = ""
    for char in s:
        if not char.isdigit():
            result += char
    return result

# Process each item in the list
for i in range(len(my_list)):
    my_list[i] = remove_digits(my_list[i])

print(my_list)





