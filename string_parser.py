# Created by: Ferdous Sediqi
# Created on: June. 3. 2022
# created by: Ferdous Sediqi
# The program will then call a function that accepts 
# the user's sentence as a string and returns a list of the words in the 
# sentence. The words will then get displayed, one per line without any spaces.

# function to split the words
def parser_string(sentence):
    list_of_words = sentence.split(" ")
    return list_of_words


def main():
    # Ask user for a string
    sentence = input("Enter a string: ")
    
    # call the function 
    display_func = parser_string(sentence)
    print("The word in your sentence one per line are")

    # use for each loop to display one word per line
    for words in display_func:
        print(words,"\n")
        

if __name__ == "__main__":
    main()