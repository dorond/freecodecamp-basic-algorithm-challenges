def covertTitleCase(text):
    result = ""
    lower_text = text.lower()
    for word in lower_text.split():
        first_letter = word[0].upper()
        new_word = first_letter + word[1:]
        result += new_word + " "
    result = result[0:-1]
    return result