###############################################################################################################################
#A Pig Latin is an encrypted word in English, which is generated by doing following alterations:
#The first vowel occurring in the input word is placed at the start of the new word along with the remaining alphabets of it.
#The alphabets present before the first vowel are shifted at the end of the new word followed by “ay”.
#The objective is to conceal the words from others not familiar with the rules.
###############################################################################################################################
def pig_latin():

    consonant = (' B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'Y')
    vowel = ('A','E','I','O','U')

    pig_latin_string =''
    user_sentence = input('Type what you would like translated into pig-latin and press ENTER: ')
    user_sentence = str(user_sentence)
    user_sentence = user_sentence
    words = user_sentence.split()

    for user_word in words:
    # getting first letter and making sure its a string and setting it to uppercase
        first_letter = user_word[0]
        first_letter = str(first_letter)
        first_letter = first_letter.upper()
  
        if first_letter in consonant:
            length_of_word = len(user_word)
            remove_first_letter = user_word[1 : length_of_word]
            pig_latin = remove_first_letter + first_letter + 'ay'
            pig_latin_string = pig_latin_string + ' ' + pig_latin
        
        elif first_letter in vowel:
            pig_latin = user_word + 'way'
            pig_latin_string = pig_latin_string + ' ' + pig_latin
        
        else:
            print('Invalid input')



pig_latin()
