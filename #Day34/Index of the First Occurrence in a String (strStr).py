def strStr(haystack, needle):
    # Edge case: empty needle
    if needle == "":
        return 0

    n, m = len(haystack), len(needle)

    # Slide over haystack
    for i in range(n - m + 1):
        # Check substring of length m
        if haystack[i:i+m] == needle:
            return i

    return -1

print(strStr("hello", "ll"))
print(strStr("aaaaa", "bba"))
print(strStr("", "")) 