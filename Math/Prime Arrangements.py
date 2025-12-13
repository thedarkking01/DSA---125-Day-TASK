# leetcode 1175: Prime Arrangements
# Difficulty: Easy
# URL: https://leetcode.com/problems/prime-arrangements/
# Problem Statement :

# Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

# (Recall that an integer is prime if and only if it is greater than 1, and cannot be written as a product of two positive integers both smaller than it.)

# Since the answer may be large, return the answer modulo 10^9 +7.


# Examples:
 

# Example 1:

# Input: n = 5
# Output: 12
# Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1] is not because the prime number 5 is at index 1.
 

# Example 2:

# Input: n = 100
# Output: 682289015


# Constraints : 
# 1 <= n <= 100


#    Pseudocode:
        # Define a function numPrimeArrangements that takes an integer nas input and returns an integer.
        # Initialize a variable totalPrime to 0 to count the total number of prime numbers from 1 to n.
        # Iterate from 1 to n:
        # Check if the current number i is prime using the isPrime function:
        # If i is prime, increment totalPrime by 1.
        # Calculate the number of non-prime numbers by subtracting totalPrime from n.
        # Calculate the factorial of totalPrime and nonPrime using the factorial  function.
        # Take the modulo mod of the product of the factorials.
        # Return the result as an integer.

        #    For the factorial  function:
        # Define a function factorial  that takes an integer n as input and returns a long integer.
        # Initialize a variable res to 1.
        # Iterate from 2 to n:
        # Multiply res by the current number i.
        # Take the modulo mod of the result and update res.
        # Return res as the factorial of n.

        #    For the isPrime function:
        # Define a function isPrime that takes an integer n as input and returns a boolean.
        # If n is less than or equal to 1, return false.
        # Iterate from 2 to the square root of n:
        # If n is divisible by i, return false.
        # If the loop completes without finding any divisors, return true

class Solution:
    mod = 10**9 + 7
    
    def numPrimeArrangements(self, n: int) -> int:
        def factorial(num):
            res = 1
            for i in range(2, num + 1):
                res = (res * i) % self.mod
            return res
        
        def is_prime(num):
            if num <= 1:
                return False
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        total_prime = sum(1 for i in range(1, n + 1) if is_prime(i))
        non_prime = n - total_prime
        fact = (factorial(total_prime) * factorial(non_prime)) % self.mod
        return fact