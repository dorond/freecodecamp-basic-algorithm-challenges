# Return the factorial of the provided integer.
# If the integer is represented with the letter n, a factorial is the product of all positive integers less than or equal to n.
# Factorials are often represented with the shorthand notation n!
# For example: 5! = 1 * 2 * 3 * 4 * 5 = 120

class Factorize(object):
    def __init__(self):
        pass
    def factorize(self, n):
        # Solved using recursion. 
        # Base case: If n == 1, return 1, otherwise recursively call factorise with n-1      
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorize(n - 1)
        

      