
def program_instruction(message):
	print(f"Write a program that takes input from the user and display {message}")

questions = str("Please enter your text")

program_instruction("that input back") 

string_to_display = str(input("- Please enter your text: "))
print(string_to_display)

program_instruction("the input in lowercase") 
string_to_lowercase = str(input("-" + questions + " " ":"))

print(string_to_lowercase.lower())

