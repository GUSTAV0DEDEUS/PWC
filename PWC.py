# 1
# phrase = input().split()
# newPhrase = ''
# for i in range(len(phrase)):
#   newPhrase += str(phrase[-1]) + " "
#   phrase.pop(-1)
# print(newPhrase)

# # CASO1: Hello, world! openIA is amazing
# # CASO2: Good Morning, How are you?

# #2
# phrase = input().split()
# newPhrase = ""
# for i in range(len(phrase)):
#   noDuplicates = ""
#   for letter in phrase[i]:
#     if letter not in noDuplicates:
#      noDuplicates += letter
#   newPhrase += noDuplicates + " "
# print(newPhrase)

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