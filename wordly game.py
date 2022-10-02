import random

def isword(user_word,wordly_word):
	for x in user_word:
		print(x,end=" ")
	print()
	for i in range(len(user_word)):
		if user_word[i] == wordly_word[i]:
			print(" green",end =" ")
		elif user_word[i] in wordly_word:
			print(" yellow ",end=" ")
		else:
			print(" red ",end=" ")
	if user_word == wordly_word:
		return 1
	else:
		return 0

words = ('which', 'there', 'their', 'about', 'would')
random_word = random.choice(words)
print(random_word)
num = len(random_word)
print("Let's Play Wordle")
while num > 0:
	user_word=input("\nEnter word: ")
	if (len(user_word)==5 and user_word.isalpha()):
		num = num-1
		if isword(user_word,random_word):
				print("\n","Game Over")
				break
		else:
			continue
	else:
		print("Please enter a valid word")
else:
	print("End of Game, the correct word is:",random_word)
