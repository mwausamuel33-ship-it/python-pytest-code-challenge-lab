def longest_palindromic_substring(s):
    # This function finds the longest palindrome in a string
    # First check if string is too short to have a palindrome
    n = len(s)
    if n < 2:
        return s
    
    # Set up variables to track the longest palindrome found
    start = 0
    max_len = 1

    # Helper function to expand around center
    def expand_around_center(left, right):
        # Keep expanding while characters match
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        # Return length of palindrome
        return right - left - 1

    # Check every position in string
    for i in range(n):
        # Check odd length palindromes (center is one character)
        len1 = expand_around_center(i, i)
        # Check even length palindromes (center is between two characters)
        len2 = expand_around_center(i, i + 1)
        # Get the longer of the two
        max_curr_len = max(len1, len2)
        # If this is longer than what we found before, save it
        if max_curr_len > max_len:
            max_len = max_curr_len
            start = i - (max_len - 1) // 2
            
    # Return the longest palindrome substring
    return s[start:start + max_len]

def is_palindrome(string):
    # Convert to lowercase and remove spaces and special characters
    cleaned = ""
    for char in string.lower():
        if char.isalnum():
            cleaned += char
    
    # Check if cleaned string reads the same forwards and backwards
    return cleaned == cleaned[::-1]
