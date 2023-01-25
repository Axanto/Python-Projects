#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"
f = open("./Input/Names/invited_names.txt", "r")
f2 = open("./Input/Letters/starting_letter.txt" , "r")

name_list = f.readlines()
# if any number is written inside readlines() it means:
# Do not return the next line if the total number of returned bytes are more than xx:
letter = f2.read() # read() returns string

# THIS IS MY CODE AND IT'S HARD TO UNDERSTAND
# who = letter[0]
#
# for names in range(len(name_list)-1):
#     name_list[names] = name_list[names].strip("\n")
#     final = open(f"./Output/ReadyToSend/letter_for_{name_list[names]}.txt", "w")
#     letter[0] = who.replace("[name]",name_list[names])
#     final.write("".join(letter))

# THIS IS INSTRUCTOR'S CODE, OBVIOUSLY BETTER
for name in name_list:
    new_name = name.strip()
    new_letter = letter.replace(PLACEHOLDER, new_name)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", "w") as final:
        final.write(new_letter)

