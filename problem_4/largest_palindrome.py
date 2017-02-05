#!/usr/bin/python3

def largest_palindrome():
    max_palindrome = 0
    for i in range(999):
        for j in range(999):
            palindrome = str(i * j)
            if is_palindrome(palindrome):
                if int(palindrome) > max_palindrome:
                    max_palindrome = int(palindrome)
    return max


def is_palindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i -= 1
        j -= 1
    return True

print(largest_palindrome())
