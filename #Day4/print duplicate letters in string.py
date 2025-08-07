text = input("Enter") 
duplicates = [] 
for char in text: 
    if text.count(char) > 1 and char not in duplicates: 
        duplicates.append(char) 
# Print duplicate letters 
for char in duplicates: 
    print(char)