# Return the length of the longest word in the provided sentence.
# Your response should be a number.

def findHowLong(text):
    result = 0
    words = text.split()
    for word in words:
        if len(word) > result:
            result = len(word)
    return result