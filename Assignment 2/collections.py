def group_anagrams(strings):
    anagram_groups = {}

    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagram_groups:
            anagram_groups[sorted_string].append(string)
        else:
            anagram_groups[sorted_string] = [string]

    return list(anagram_groups.values())

input_strings = ["listen", "silent", "hello", "world", "elbow", "below"]
anagram_groups = group_anagrams(input_strings)
print(anagram_groups)
