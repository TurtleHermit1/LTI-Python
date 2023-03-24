wordIs=input("Enter the word :\n")

# n=int(len(wordIs))
vowel=0
wordIs=wordIs.lower() 
for i in wordIs:
    if i=='a' or i=='e' or i=='o'  or i=='u' or i=='i':
        vowel+=1

print(f"Count of vowels in {wordIs} is {vowel}")