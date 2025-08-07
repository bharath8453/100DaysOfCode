def reverse_word_order(text):
    return ' '.join(text.split()[::-1])
# Example
sentence = "I love Python"
print(reverse_word_order(sentence))  # Output: Python love I


def reverse_each_word(text):
    return ' '.join(word[::-1] for word in text.split())
# Example
sentence = "I love Python"
print(reverse_each_word(sentence))  # Output: I evol nohtyP


def reverse_full_string(text):
    return text[::-1]
# Example
sentence = "I love Python"
print(reverse_full_string(sentence)) # Output: nohtyP evol I