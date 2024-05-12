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



# use \' for year's usign ' in string this is know as escape character



# Check string