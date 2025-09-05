def decodeString(s):
    stack = []      # To keep track of previous strings and counts
    curr_str = ""   # holds the current substring being built.
    curr_num = 0    # Current number (multiplier)

    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)  
#curr_num * 10 handles multi-digit numbers like "12[ab]".Example: "12" → first 1, then curr_num = 1*10 + 2 = 12.
            
        elif char == "[":
            # Push current state to stack
            stack.append(curr_str, curr_num)
            curr_str = ""
            curr_num = 0
#Example:
#Input "3[a]"
#Stack stores ("", 3) (empty string + repeat count).
#Now curr_str becomes empty to start building "a".

        elif char == "]":
            # Pop from stack and repeat substring
            prev_str, repeat = stack.pop()
            curr_str = prev_str + (curr_str * repeat)

#Pop last stored (prev_str, repeat) from stack.
#Multiply curr_str by repeat.
#Concatenate with prev_str.
#Example:
#Suppose stack = [("", 3)] and curr_str = "a".
#Pop → prev_str = "", repeat = 3.
#Update → curr_str = "" + ("a" * 3) = "aaa".'''

        else:
            curr_str += char

    return curr_str

print(decodeString("3[a]2[bc]"))  
print(decodeString("3[a2[c]]"))   
print(decodeString("2[abc]3[cd]ef"))