#Problem: Longest Substring with At Most Two Distinct Characters
#Description:
#Given a string s, return the length of the longest substring that contains at most two distinct characters.

"""
e.g.

s = "eceba"
length_of_longest_substring_two_distinct(s)
>>> 3

ece

s = "ccaabbb"
length_of_longest_substring_two_distinct(s)
>>> 5 

aabbb

Constraints:
1 <= s.length <= 10^5
s consists of English letters, digits, symbols, and spaces.
Approach:
To solve this problem, you can use the sliding window technique with a hashmap to store the frequency of characters in the current window. Keep track of the length of the longest valid substring as you move the window.
"""
