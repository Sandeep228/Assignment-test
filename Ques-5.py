# The problem of finding the longest substring without repeating characters is commonly known as the "Longest Substring Without Repeating Characters" problem. There are several approaches to solving this problem, and I'll describe two common ones: the Sliding Window and HashMap approaches.

# Approach 1: Sliding Window
# The idea behind the sliding window approach is to maintain a window of characters in the string without any repetitions.

# Algorithm:

# Use two pointers, start and end, to represent the window.
# Move the end pointer to the right until a repeated character is found.
# Move the start pointer to the right until the repeated character is no longer in the window.
# Repeat steps 2-3 until the end pointer reaches the end of the string.
# Python Implementation:


def longest_substring_without_repeating(s):
    char_index_map = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1

        char_index_map[s[end]] = end
        current_length = end - start + 1
        max_length = max(max_length, current_length)

    return max_length



# Approach 2: HashMap
# The idea behind the HashMap approach is to use a data structure to store the index of the last occurrence of each character.

# Algorithm:

# Use a HashMap to store the index of the last occurrence of each character.
# If a character is repeated, update the starting index to the next index of the last occurrence.
# Update the maximum length during each iteration.
# Python Implementation:



def longest_substring_without_repeating(s):
    char_index_map = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1

        char_index_map[s[end]] = end
        current_length = end - start + 1
        max_length = max(max_length, current_length)

    return max_length



# Both approaches have the same time complexity of O(n), where n is the length of the input string. The sliding window approach is more intuitive and often easier to understand, while the HashMap approach can be useful when you need to track additional information about the substring.