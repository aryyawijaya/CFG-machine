# Import Library
import string

# Initialization
alphabetList = list(string.ascii_lowercase)
stateList = [
              'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9',
              'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19',
              'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29',
              'q30', 'q31', 'q32', 'q33', 'q34', 'q35'
              ]

transitionTable = {}

for state in stateList:
  for alphabet in alphabetList:
    transitionTable[(state, alphabet)] = 'error'
  transitionTable[(state, '#')] = 'error'
  transitionTable[(state, ' ')] = 'error'

# print(transitionTable)

transitionTable['q0', ' '] = 'q0'

# siwur
transitionTable[('q0', 's')] = 'q17'
transitionTable[('q17', 'i')] = 'q18'
transitionTable[('q18', 'w')] = 'q19'
transitionTable[('q19', 'u')] = 'q20'
transitionTable[('q20', 'r')] = 'q21'
transitionTable[('q21', ' ')] = 'q35'
transitionTable[('q21', '#')] = 'accept'
transitionTable[('q35', ' ')] = 'q35'
transitionTable[('q35', '#')] = 'accept'

## transition for new token
transitionTable[('q35', 's')] = 'q17'

# jukut - hana
transitionTable[('q0', 'j')] = 'q27'
transitionTable[('q27', 'u')] = 'q28'
transitionTable[('q28', 'k')] = 'q29'
transitionTable[('q29', 'u')] = 'q30'
transitionTable[('q30', 't')] = 'q31'
transitionTable[('q31', ' ')] = 'q35'
transitionTable[('q31', '#')] = 'accept'
transitionTable[('q35', ' ')] = 'q35'
transitionTable[('q35', '#')] = 'accept'

## transition for new token
transitionTable[('q35', 'j')] = 'q27'

# kai - nadia
transitionTable[('q0','k')] = 'q32'
transitionTable[('q32','a')] = 'q33'
transitionTable[('q33','i')] = 'q34'
transitionTable[('q34',' ')] = 'q35'
transitionTable[('q34', '#')] = 'accept'
transitionTable[('q35', ' ')] = 'q35'
transitionTable[('q35', '#')] = 'accept'

## transition for new token
transitionTable[('q35', 'k')] = 'q32'

# cai - aryya
transitionTable[('q0', 'c')] = 'q32'

## transition for new token
transitionTable[('q35', 'c')] = 'q32'

# bumi
transitionTable[('q0', 'b')] = 'q22'
transitionTable[('q22', 'u')] = 'q24'
transitionTable[('q24', 'm')] = 'q25'
transitionTable[('q25', 'i')] = 'q26'
transitionTable[('q26', ' ')] = 'q35'
transitionTable[('q26', '#')] = 'accept'
transitionTable[('q35', ' ')] = 'q35'
transitionTable[('q35', '#')] = 'accept'

## transition for new token
transitionTable[('q35', 'b')] = 'q22'

# maca
transitionTable[('q0', 'm')] = 'q13'
transitionTable[('q13','a')] = 'q14'
transitionTable[('q14','c')] = 'q15'
transitionTable[('q15','a')] = 'q16'
transitionTable[('q16',' ')] = 'q35'
transitionTable[('q16','#')] = 'accept'
transitionTable[('q35',' ')] = 'q35'
transitionTable[('q35','#')] = 'accept'

## transition for new token
transitionTable[('q35', 'm')] = 'q13'

# teuleug
transitionTable[('q0', 't')] = 'q6'
transitionTable[('q6', 'e')] = 'q7'
transitionTable[('q7', 'u')] = 'q8'
transitionTable[('q8', 'l')] = 'q9'
transitionTable[('q9', 'e')] = 'q10'
transitionTable[('q10', 'u')] = 'q11'
transitionTable[('q11', 'g')] = 'q12'
transitionTable[('q12', ' ')] = 'q35'
transitionTable[('q12', '#')] = 'accept'
transitionTable[('q35', ' ')] = 'q35'
transitionTable[('q35', '#')] = 'accept'

## transaction for new token
transitionTable[('q35', 't')] = 'q6'

# mioh
transitionTable[('q13', 'i')] = 'q3'
transitionTable[('q3', 'o')] = 'q4'
transitionTable[('q4', 'h')] = 'q5'
transitionTable[('q5', ' ')] = 'q35'
transitionTable[('q5', '#')] = 'accept'
transitionTable[('q35', ' ')] = 'q35'
transitionTable[('q35', '#')] = 'accept'

# bayur
transitionTable[('q0', 'b')] = 'q22'
transitionTable[('q22', 'a')] = 'q23'
transitionTable[('q23', 'y')] = 'q19'
transitionTable[('q19', 'u')] = 'q20'
transitionTable[('q20', 'r')] = 'q21'
transitionTable[('q21', ' ')] = 'q35'
transitionTable[('q21', '#')] = 'accept'
transitionTable[('q35', ' ')] = 'q35'
transitionTable[('q35', '#')] = 'accept'

# tuang
transitionTable[('q6', 'u')] = 'q1'
transitionTable[('q1', 'a')] = 'q2'
transitionTable[('q2', 'n')] = 'q11'
transitionTable[('q25', 'a')] = 'q19'

# Lexical Analysis
def lexAn(sentence, inputString):
  idxChar = 0
  state = 'q0'
  currentToken = ''
  acceptedState = ['q5', 'q12', 'q16', 'q21', 'q26', 'q31', 'q34']
  while state != 'accept':
    currentChar = inputString[idxChar]
    currentToken += currentChar
    state = transitionTable[(state, currentChar)]
    if state in acceptedState:
      print('current token:', currentToken, 'valid')
      currentToken = ''
    elif state == 'error':
      print('error')
      break;
    idxChar += 1
  if state == 'accept':
    print('semua token diinput:', sentence, 'valid')

# input user
print('Masukkan kalimat Anda:')
sentence = input()
inputString = sentence.lower() + '#'
lexAn(sentence, inputString)