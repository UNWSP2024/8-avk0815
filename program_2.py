# Program #2: Word Separator
# Write a program that accepts as input a sentence in which all of the words are run together, 
# but the first character of each word is uppercase.  
# Convert the sentence to a string in which the words are separated by spaces, 
# and the first word starts with an uppercase.  
# For example the string "StopAndSmellTheRoses" would be converted to "Stop and smell the roses."

# Start your changes on line 13

def word_separator(sentence):
    if not sentence:
        return ""

    words = []
    current = sentence[0]
    for ch in sentence[1:]:
        if ch.isupper():
            words.append(current)
            current = ch
        else:
            current += ch
    words.append(current)

    formatted = []
    for i, w in enumerate(words):
        if i == 0:
            formatted.append(w[0].upper() + w[1:].lower() if w else "")
        else:
            formatted.append(w.lower())

    return " ".join(formatted) + "."

# Example usage
if __name__=="__main__":
    sentence = "StopAndSmellTheRoses"

    new_sentence = word_separator(sentence)

    print(new_sentence)
