os.path.isfile('1OLG.pdb')
if os.path.isfile('mastery.txt'):
    raise RuntimeError('File mastery.txt already exists.')

with open('mastery.txt', 'w') as f:
    f.write('This is my file.')
    f.write('There are many like it, but this one is mine.')
    f.write('I must master my file like I must master my life.')
