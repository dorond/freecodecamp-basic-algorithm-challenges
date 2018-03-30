# Return the length of the longest word in the provided sentence.
# Your response should be a number.

def findHowLong(text):     
    return max([len(word) for word in text.split()])