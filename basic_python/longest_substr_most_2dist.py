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


## solution 1

def longest_subst(text) -> int:

    assert 1 <= len(text) <= 10^5

    if len(set(text)) <= 2:
        print(text)
        return len(text)
    
    else:
        full_len = len(text)
        for i in range((full_len - 1),0,-1):
            j = 0
    
            while j <= (full_len - i):
                string_piece = text[j:(full_len-(full_len-i)+j)]
                
                if len(set(string_piece)) <= 2
                    return i
                    
                else:
                    j += 1

## optimized solution

def longest_subst(text) -> int:
    left = 0
    max_len = 0
    char_count = {}

    for right in range(len(text)):
        # Expand the window to the right
        char_count[text[right]] = char_count.get(text[right], 0) + 1

        # Shrink the window if we have more than 2 distinct characters
        while len(char_count) > 2:
            char_count[text[left]] -= 1
            if char_count[text[left]] == 0:
                del char_count[text[left]]
            left += 1
        
        # Update the maximum length of the window
        max_len = max(max_len, right - left + 1)

    return max_len
