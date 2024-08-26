str1= "ghee"
freq={char: str1.count(char) for char in set(str1)}
str2=''.join(chr((ord(char)+freq[char]-97)%26+97)for char in str1)
print(str2)
