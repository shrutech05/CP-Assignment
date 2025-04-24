# 1. Count vowels in a string
s = input("Enter a string: ")
vowels = 'aeiouAEIOU'
vowel_count = 0
for ch in s:
    if ch in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)

# 2. Convert to lowercase, uppercase, and toggle case without built-in methods
lowercase = ''
uppercase = ''
toggle = ''

for ch in s:
    if 'A' <= ch <= 'Z':
        lowercase += chr(ord(ch) + 32)
        toggle += chr(ord(ch) + 32)
        uppercase += ch
    elif 'a' <= ch <= 'z':
        uppercase += chr(ord(ch) - 32)
        toggle += chr(ord(ch) - 32)
        lowercase += ch
    else:
        lowercase += ch
        uppercase += ch
        toggle += ch

print("Lowercase:", lowercase)
print("Uppercase:", uppercase)
print("Toggle Case:", toggle)

# 3. Check if one string is in another (without using 'in')
main_str = input("Enter main string: ")
sub_str = input("Enter string to search: ")
found = False

for i in range(len(main_str) - len(sub_str) + 1):
    match = True
    for j in range(len(sub_str)):
        if main_str[i + j] != sub_str[j]:
            match = False
            break
    if match:
        found = True
        break

if found:
    print(f"'{sub_str}' is in '{main_str}'")
else:
    print(f"'{sub_str}' is NOT in '{main_str}'")

# 4. Remove one string from another (if present)
source = input("Enter source string: ")
remove = input("Enter string to remove: ")
result = ''
i = 0

while i < len(source):
    match = True
    if i + len(remove) <= len(source):
        for j in range(len(remove)):
            if source[i + j] != remove[j]:
                match = False
                break
    else:
        match = False

    if match:
        i += len(remove)
    else:
        result += source[i]
        i += 1

print("Final string after removal:", result)
