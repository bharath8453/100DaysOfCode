def remove_duplicates_inplace(chars):
    if not chars:
        return 0
    
    write = 0  # slow pointer
    
    for read in range(len(chars)):
        # Check if this char has already appeared before write pointer
        duplicate_found = False
        for i in range(write):
            if chars[i] == chars[read]:
                duplicate_found = True
                break
        
        if not duplicate_found:
            chars[write] = chars[read]
            write += 1
    
    # Optionally trim the list
    while len(chars) > write:
        chars.pop()
    
    return chars

# Test
chars = list("banana")
print(remove_duplicates_inplace(chars))  # ['b', 'a', 'n']