
class StringReverser(object):
    def __init__(self):
        pass

    def reverse(self, s):
        # The easy Pythonic solution
        #return s[::-1]

        # A more general solution
        reversed = ''
        count = len(s)

        while count > 0:
            reversed += s[count - 1]
            count -= 1
        return reversed

    