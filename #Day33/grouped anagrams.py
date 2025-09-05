def groupAnagrams(strs):
    # Dictionary to store groups of anagrams
    anagram_groups = {}

    for word in strs:
        # Sort the word to form the key
        key = ''.join(sorted(word))

        # Add the word to its anagram group
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(word)
#If the key doesn’t exist, initialize an empty list.
#Append the current word to that list.
#Example:
#"eat" → key = "aet", dictionary becomes { "aet": ["eat"] }
#"tea" → same key, dictionary becomes { "aet": ["eat", "tea"] }

    return list(anagram_groups.values())  # returns grouped anagrams

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))