# 1
phrase = input().split()
newPhrase = ''
for i in range(len(phrase)):
  newPhrase += str(phrase[-1]) + " "
  phrase.pop(-1)
print(newPhrase)

# CASO1: Hello, world! openIA is amazing.
# CASO2: Good Morning, How are you?

#2
phrase = list(input())
newPhrase = ""
noDuplicates = ""
for letter in phrase:
   if letter not in noDuplicates:
      noDuplicates += letter   
newPhrase = noDuplicates
print(newPhrase)

#CASO1: Hello, world!
#CASO2: Good Morning

#3
word = input()
while True:
  if(len(word) == 0 or word[::-1] in word) :
    print(word)
    break
  else:
    word = word.rstrip(word[-1])   
    
#CASO1: BABAD
#CASO2: OVOWOD

#4
phrase = input().split()
substrings = ['.', ";", "!", "?"]
newPhrase = phrase[0].capitalize()
for i in range(len(phrase) - 1):
  for sub in substrings:
    index = phrase[i].find(sub)
    if (index != -1):
      newPhrase +=  " " + phrase[i + 1].capitalize()
  if(phrase[i + 1].capitalize() not in newPhrase):
    if(len(phrase[i+1]) == 1 and phrase[i+1] == 'i'):
      newPhrase +=  " " + phrase[i + 1].upper()
    else:
      newPhrase +=  " " + phrase[i + 1]
print(newPhrase)
#CASO1: hello. how are you? i'm fine, thank you.
#CASO2: wow. you are doctor, too? yes, i started my job this week! great, congratulations.

#5
word = input()
newWord = ''
for i in range(len(word)):
  newWord += word[-(i+1)]
if newWord == word:
  print('true')
else:
  print('false')
#CASO1: socorrammesubinoonibusemmarrocos
#CASO2: racecar
