'''

THIS FILE WILL GIVE YOU ANSWER WHAT IS THE MEANING OF SHOTFORM OF PHONE MESSAGES. e.g., LOL,ROFL.. so on
'''

# Function to create the dictionary
def createDictionary():

    '''

        @return output: Dictionary created from the file

    '''

    file_data = open("abbreviations.txt").read()
    key_value = {}
    data_list = file_data.split("\n")
    del data_list[-1]

    for data in data_list:
        key_val = data.split("-")
        key = key_val[0].strip()
        value = key_val[1].strip()
        key_value[key] = value

    return key_value

# Function to translate the abbreviation if present.
def translateAbbreviation(dictionary, abbreviation):

    '''

        @param Input: Dictionary created from the file and a word from the input message
        @return Output: The translated word from the abbreviation if present in dictionary

    '''

    last_char = abbreviation[-1]
    if last_char in ".?!,;:":
        abbreviation = abbreviation.rstrip(last_char)
    else:
        last_char = ""

    # translate abbreviation
    if abbreviation in dictionary:
        word = dictionary[abbreviation]
    else:
        word = abbreviation

    return word + last_char

# Function to translate the message words by word using translateAbbreviation function.
def translateMessage(dictionary, message):

    '''

        @param Input: Dictionary created from the file and the input message
        @return Output: The translated message

    '''

    translation = ""
    for word in message.split():
        translation += translateAbbreviation(dictionary, word) + " "
    return translation

#Main Function
def main():
    print "\033[1;37;40m Note: Whatever you write make sure everything should be in Capital letter."

    message = raw_input("Enter the message to be translated. \n")
    key_value = createDictionary()
    print("The translated text is: ")
    print(translateMessage(key_value, message))

main()
