# Pytest Lab: Creating a Code Challenge Test Suite

## Overview 
### Introduction: Algorithms in Interviews & Testing

#### What is an Algorithm?

An algorithm is a step-by-step procedure or set of rules designed to perform a task or solve a problem. Algorithms are the foundation of computer programming, defining how data is processed, stored, and retrieved efficiently.

#### Algorithms in Tech Interviews

Algorithm challenges are a core part of technical interviews for software engineers, used to evaluate problem-solving skills, coding ability, and efficiency. Companies such as Google, Meta, Amazon, and Microsoft frequently ask candidates to solve coding problems under time constraints.

#### How Leetcode & Codewars Use Testing

Platforms like Leetcode, Codewars, and HackerRank include test suites for each coding challenge. These test suites:

* Provide automated validation of solutions.
* Include edge cases and performance tests.
* Ensure code correctness before submission.

#### Your Task in This Lab

In this lab, you will build your own test suite for a common algorithm problem—the Longest Palindromic Substring—just like platforms like Leetcode would. Instead of solving a challenge with a pre-existing test set, you'll define the test cases yourself, ensuring robust validation before implementing the function (or using a provided solution).

### Scenario:

As a junior software developer, you have been assigned to work on a feature validation team that ensures code reliability before deployment. A senior engineer has provided a function requirement: identifying the longest palindromic substring in a given input string. A palindrome is a word, phrase, or sequence that reads the same backward as forward.
<br>
Before implementing the function, the team follows a Test-Driven Development (TDD) approach, requiring you to first write a test suite that verifies correctness. Your task is to:
* Write test cases using pytest to validate a function for the Longest Palindromic Substring problem.
* Consider normal, edge, and failure cases to ensure test robustness.
* Run your tests and refine them as needed.
* Implement the function yourself OR use the provided working solution if needed.

## Instructions
### Set Up
Before we begin coding, let's complete the initial setup for this lesson: 

1. Fork and Clone
    * Fork the repository to your GitHub account.
    * Clone the forked repository to your local machine.
2. Open and Run File
    * Open the project in VSCode.
    * Run `pipenv install` to install all necessary dependencies.
    * Run `pipenv shell` to enter the virtual environment.

### Instructions
1. Step 1: Understand the Challenge
* You need to write tests for a function that finds the longest palindromic substring in a given string. A palindrome is a word, phrase, or sequence that reads the same backward as forward.
* Function Signature
```python
def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    pass  # Function implementation comes later
```
* Example Inputs/Outputs

|   Input  |  Output | Explanation |
| --- | --- | --- |
| "babad" | "bab" or "aba" | Both are valid palindromes. |
| "cbbd" | "bb" | The longest palindrome is "bb". |
| “a” | “a” | A single character is always a palindrome. |
| “ac” | "a" or "c" | Either character is a valid palindrome. |
| “racecar” | “racecar” | The entire string is a palindrome. |

* Constraints / Assumptions
    * 1 <= s.length <= 1000
    * s consists of only digits and English letters.

2. Step 2: Install Pytest
* Add pytest dependency to the Pipfile and install
```bash
pip install pytest
```
* Create a pytest.ini file in the root directory with the following code:
```
[pytest]
pythonpath = . lib
```
* Create a testing folder inside lib/
```bash
mkdir lib/testing
```
* Create the test_palindrome.py file
```bash
touch lib/testing/test_palindrome.py
```


3. Step 3: Write Your Test Suite
* Your primary task is to create a Pytest test suite for the function in test_palindrome.py.
* Your test cases should cover:
    * Basic Cases – Check common inputs return expected outputs.
    * Edge Cases – Handle single-character strings, empty strings, long strings, and no-palindrome cases.
* ⚠️ Do NOT implement longest_palindromic_substring yet! Follow the Test-Driven Development (TDD) approach.

4. Step 4: Run the Tests
* Once you’ve written your test cases, run them using pytest:
```bash
pytest
```
* You should see failing tests, since the function is not yet implemented. This is expected! 
* If any of the tests pass without a solution implemented, something is wrong with your tests and you’ll need to debug.

5. Step 5: Implement the Function
* Now, solve the algorithm by adding code to the function in palindrome.py until all tests pass.
    * Break Glass Solution
        * 🚨 The purpose of the lab is the test suite implementation, so if you cannot solve the problem on your own that’s okay! You can use this working solution:

```python
def longest_palindromic_substring(s):
    """
    Given a string s, return the longest palindromic substring.
    """
    n = len(s)
    if n < 2:
        return s
    
    start = 0
    max_len = 1

    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(n):
        len1 = expand_around_center(i, i)
        len2 = expand_around_center(i, i + 1)
        max_curr_len = max(len1, len2)
        if max_curr_len > max_len:
            max_len = max_curr_len
            start = i - (max_len - 1) // 2
            
    return s[start:start + max_len]
```


6. Step 6: Handle Additional Edge Cases and Debug (if needed)
* Are there any edge cases your test suite is not handling? If so, add additional tests to ensure edge case coverage.
* Is there any code you need to clean up or debug in the test or solution?

7. Step 7: Verify and Submit
* Confirm your tests pass:
```bash
pytest
```
* Push your final version to GitHub:
```bash
git add .
git commit -m "Completed testing lab"
git push origin main
```
