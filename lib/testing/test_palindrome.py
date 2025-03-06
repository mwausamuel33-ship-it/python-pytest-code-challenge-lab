import pytest
from lib.palindrome import longest_palindromic_substring


class TestLongestPalindromicSubstring:
    """Test suite for the longest_palindromic_substring function"""
    
    def test_basic_palindromes(self):
        """Test basic cases with clear palindromic substrings"""
        # Test case from the problem description
        assert longest_palindromic_substring("babad") in ["bab", "aba"]
        assert longest_palindromic_substring("cbbd") == "bb"
        
    def test_single_character(self):
        """Test single character strings"""
        assert longest_palindromic_substring("a") == "a"
        assert longest_palindromic_substring("z") == "z"
        
    def test_two_characters(self):
        """Test two character strings"""
        assert longest_palindromic_substring("ac") in ["a", "c"]
        assert longest_palindromic_substring("aa") == "aa"
        assert longest_palindromic_substring("ab") in ["a", "b"]
        
    def test_entire_string_is_palindrome(self):
        """Test when the entire string is a palindrome"""
        assert longest_palindromic_substring("racecar") == "racecar"
        assert longest_palindromic_substring("madam") == "madam"
        assert longest_palindromic_substring("aba") == "aba"
        
    def test_no_palindrome_longer_than_one(self):
        """Test strings with no palindromes longer than single characters"""
        assert longest_palindromic_substring("abcdef") in ["a", "b", "c", "d", "e", "f"]
        assert longest_palindromic_substring("xyz") in ["x", "y", "z"]
        
    def test_longer_strings(self):
        """Test longer strings with various palindrome patterns"""
        # Multiple palindromes of different lengths
        assert longest_palindromic_substring("abacabad") == "abacaba"
        # Even length palindrome
        assert longest_palindromic_substring("abccba") == "abccba"
        # Mixed case
        assert longest_palindromic_substring("Aa") in ["A", "a"]
        
    def test_edge_cases(self):
        """Test edge cases and boundary conditions"""
        # Minimum length string (1 character)
        assert longest_palindromic_substring("a") == "a"
        
        # Two identical characters
        assert longest_palindromic_substring("aa") == "aa"
        
        # Three characters with palindrome in middle
        assert longest_palindromic_substring("aba") == "aba"
        
        # Three characters with no palindrome longer than 1
        assert longest_palindromic_substring("abc") in ["a", "b", "c"]
        
    def test_mixed_content(self):
        """Test strings with mixed letters and numbers"""
        assert longest_palindromic_substring("12321") == "12321"
        assert longest_palindromic_substring("abc121cba") == "abc121cba"
        assert longest_palindromic_substring("a1b2c3") in ["a", "1", "b", "2", "c", "3"]
        
    def test_repeated_patterns(self):
        """Test strings with repeated patterns"""
        assert longest_palindromic_substring("aaaa") == "aaaa"
        assert longest_palindromic_substring("abab") in ["aba", "bab"]
        assert longest_palindromic_substring("abcabc") in ["a", "b", "c"]  # No palindrome > 1
        
    def test_constraint_boundary(self):
        """Test strings at the constraint boundaries"""
        # Test maximum length (1000 characters) - simple case
        long_string = "a" * 1000
        assert longest_palindromic_substring(long_string) == long_string
        
        # Test with alternating pattern at max length
        alt_string = "ab" * 500
        result = longest_palindromic_substring(alt_string)
        # The algorithm finds the longest palindrome, which could be longer than 2
        # For "ababab...", the longest palindrome could be "aba" or "bab" (length 3)
        # or even longer palindromes depending on the pattern
        assert len(result) >= 2  # Should be at least 2 characters
        # Check that the result is a valid palindrome
        assert result == result[::-1]
        # Check that it contains only 'a' and 'b' characters
        assert all(c in 'ab' for c in result)
