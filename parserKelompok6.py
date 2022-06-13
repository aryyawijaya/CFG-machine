# add EOS on the last sentence
sentence = 'siwur maca jukut'
tokens = sentence.lower().split()
tokens.append('EOS')

# symbol definition
non_terminals = ['S', 'NN', 'VB']
terminals = ['siwur', 'jukut', 'kai', 'cai', 'bumi', 'maca', 'teuleug', 'mioh', 'bayur', 'tuang']

# parse table definition
parse_table = {}

# aryya
parse_table[('S', 'siwur')] = ['NN', 'VB', 'NN']
parse_table[('S', 'jukut')] = ['NN', 'VB', 'NN']
parse_table[('S', 'kai')] = ['NN', 'VB', 'NN']
parse_table[('S', 'cai')] = ['NN', 'VB', 'NN']
parse_table[('S', 'bumi')] = ['NN', 'VB', 'NN']
parse_table[('S', 'maca')] = ['error']
parse_table[('S', 'teuleug')] = ['error']
parse_table[('S', 'mioh')] = ['error']
parse_table[('S', 'bayur')] = ['error']
parse_table[('S', 'tuang')] = ['error']

# hana
parse_table[('NN', 'siwur')] = ['siwur']
parse_table[('NN', 'jukut')] = ['jukut']
parse_table[('NN', 'kai')] = ['kai']
parse_table[('NN', 'cai')] = ['cai']
parse_table[('NN', 'bumi')] = ['bumi']
parse_table[('NN', 'maca')] = ['error']
parse_table[('NN', 'teuleug')] = ['error']
parse_table[('NN', 'mioh')] = ['error']
parse_table[('NN', 'bayur')] = ['error']
parse_table[('NN', 'tuang')] = ['error']

# nadia

parse_table[('VB', 'siwur')] = ['error']
parse_table[('VB', 'jukut')] = ['error']
parse_table[('VB', 'kai')] = ['error']
parse_table[('VB', 'cai')] = ['error']
parse_table[('VB', 'bumi')] = ['error']
parse_table[('VB', 'maca')] = ['maca']
parse_table[('VB', 'teuleug')] = ['teuleug']
parse_table[('VB', 'mioh')] = ['mioh']
parse_table[('VB', 'bayur')] = ['bayur']
parse_table[('VB', 'tuang')] = ['tuang']

# stack initialization
stack = []
stack.append('#')
stack.append('S')

# input reading initialization
idxToken = 0
symbol = tokens[idxToken]

# parsing process
while (len(stack) > 0):
  top = stack[len(stack) - 1]
  # print('top =', top)
  # print('symbol =', symbol)
  if top in terminals:
    # print('top adalah symbol terminal')
    if top == symbol:
      stack.pop()
      idxToken += 1
      symbol = tokens[idxToken]
      if symbol == 'EOS':
        # print('isi stack:', stack)
        stack.pop()
    else:
      # print('error')
      break
  elif top in non_terminals:
    # print('top adalah symbol non-terminal')
    if parse_table[(top, symbol)][0] != 'error':
      stack.pop()
      symbolsToBePushed = parse_table[(top, symbol)]
      for i in range(len(symbolsToBePushed) - 1, -1, -1):
        stack.append(symbolsToBePushed[i])
    else:
      # print('error')
      break
  else:
    # print('error')
    break
  # print('isi stack:', stack)
  # print()

# conclusion
if symbol == 'EOS' and len(stack) == 0:
  print(sentence, 'diterima')
else:
  print(sentence, 'tidak diterima')