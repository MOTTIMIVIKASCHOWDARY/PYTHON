sentence = input("Enter a sentence: ")
vowels = 0
consonants = 0

for letter in sentence:
  letter = letter.lower()
  if letter in "aeiou":
    vowels += 1
  elif letter.isalpha():
    consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
