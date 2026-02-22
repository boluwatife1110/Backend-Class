# Strings- simple text data in quotes

' hgdvghvdghvdghvd'
'' #single quote line
"" # double quote
''' ''' #triple single quote
""" """ #triple double quote

sentence = "Andi is a boy"
print(
    sentence[-1]
)

# membership
obs = "d" in "you"

# repitition
repeat = "Hi" * 3
print(repeat)

# concatenation
string_a = "st"
string_b = "ring"

concat = string_a + string_b

print(concat)

# Slicing

message = " Your email is Andikanudom123@gmail. Click the link below to proceed"

sliced_method = message[7:16]
sliced_method_2 = message[-17:-1]
sliced_method_3 = message[-15:]

print(sliced_method_2)

str_1 = "This is a string"

to_lower = str_1.lower()
to_upper = str_1.upper()
to_capitalize = str_1.capitalize()
to_title = str_1.title

searched_value = " king "
stored_value = "king"

compared_spaces = searched_value.strip() == stored_value

take_out_spaces = "The main book".replace(" ", "")

# print(
#     take_out_spaces
# )

check_length = len("weryusfd")
print(check_length)

for char in "string":
    print(char)

#Escape characters - special charcters used in a string
'''
newline - \n
tab - \t
double quote- \"
backlash \\
'''

sentence_two = "\tOnce Jhon kicked the ball, he scored,\n Everyone rejoiced "

print(sentence_two)