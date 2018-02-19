import random
import string
import pyperclip

def generateQuestion():
	problemText = '''\paragraph{\\arabic{qnumber}.} \\hspace{-4mm} Given $i$ is the imaginary unit, $\\displaystyle (NUMBER1NUMBER2LETTER1i)^2$ in simplest form is:
	\\\\
	{
		\\renewcommand{\\arraystretch}{2.0}\\begin{tabular}{p{2in} p{2in}}
		\\circled{1} CHOICE1 
		& \\circled{3} CHOICE3 \\\\
		\\circled{2} CHOICE2 
		& \\circled{4} CHOICE4 \\\\
		\\end{tabular}
	}

	% Source: Source
	\\stepcounter{qnumber}'''

	slots = ['NUMBER1', 'SIGN', 'NUMBER2', 'LETTER1', 'CHOICE1', 'CHOICE2', 'CHOICE3', 'CHOICE4',]
	letters = list(string.ascii_lowercase)
	letters.remove('i')

	number1 = random.choice([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10])
	number2 = random.choice([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10])
	letter1 = random.choice(letters)

	# number1 = -2
	# number2 = 1
	# letter1 = 'y'
	if number2 < 0:
		sign = '-'
	else:
		sign = '+'

	# choices
	if abs(number2 ** 2) == 1:
		firstPlaceHolder = ''
	else:
		firstPlaceHolder = number2 ** 2

	# choice1
	if number1 * number2 < 0:
		choiceSign = '-'
	else:
		choiceSign = '+'
	choiceA = '${}{}^2{}{}{}i+{}$'.format(firstPlaceHolder,letter1, sign, abs(2 * number1 * number2), letter1, number1 ** 2)
	
	#choice2
	if number1 * number2 < 0:
		choiceSign = '-'
	else:
		choiceSign = '+'
	choiceB = '$-{}{}^2{}{}{}i+{}$'.format(firstPlaceHolder,letter1, sign, abs(2 * number1 * number2), letter1, number1 ** 2)
	

	choiceC = '$-{}{}^2+{}$'.format(firstPlaceHolder, letter1, number1 ** 2)
	choiceD = '${}{}^2+{}$'.format(firstPlaceHolder, letter1, number1 ** 2)

	# shufflechoices
	choices = [choiceA, choiceB, choiceC, choiceD]
	random.shuffle(choices)
	choice1 = choices[0]
	choice2 = choices[1]
	choice3 = choices[2]
	choice4 = choices[3]

	for slot in slots:
		replacementText = str(eval(slot.lower()))
		if slot == 'NUMBER2' and int(replacementText) > 0:
			replacementText = '+' + replacementText
		if slot == 'NUMBER2' and int(replacementText) == 1:
			replacementText = '+'
		elif slot == 'NUMBER2' and int(replacementText) == -1:
			replacementText = '-'
		problemText = problemText.replace(slot, replacementText)
	return problemText

if __name__ == '__main__':
	questionText = generateQuestion()
	pyperclip.copy(questionText)
	print(questionText)