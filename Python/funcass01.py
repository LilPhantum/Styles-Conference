def alphabets_fnc (letters):
    x = []
    for letter in letters:
        if letter == range(1,10):
            x = " {} is not a letter\n".format(letter)
        else:
            x = " {} is a letter\n".format(letter)
    return x
print(alphabets_fnc([1,2,'d',3,'f','g','u','t',]))

def alphabets_fnc (letters):
    x = ""
    for letter in letters:
        if letter.isalpha():
            x = x + letter 
    return x
print(alphabets_fnc("ah28c83hsat3789zngtyi@%"))
#print(alphabets_fnc([1,2,'d',3,'f','g','u','t',]))


def extract_letters(items):
    letters_only = []
    for item in items:
        return letters_only

# Example usage
print(extract_letters([1, 'a', 'b', '%', 'c', 2, '3', 'z']))

#30/
#GPT 
def alphabets_fnc(letters):
    x = ""
    for letter in letters:
        if isinstance(letter, str) and letter.isalpha():
            x += letter
        else:
            x += " {} is not a letter\n".format(letter)
    return x

print(alphabets_fnc([1, 2, 'd', 3, 'f', 'g', 'u', 't']))
