def recursive_reverse_string(s):
    if len(s) == 0:  # Base case: if the string is empty
        return s
    else:
        return s[-1] + recursive_reverse_string(s[:-1])  # Recursive case: last character + reverse of the rest