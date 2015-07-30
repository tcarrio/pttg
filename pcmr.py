import os
rowS, columnS = os.popen('stty size', 'r').read().split()
row = int(rowS)
col = int(columnS)

pcmr = []
pcmr.append(' ██▓███   ▄████▄   ███▄ ▄███▓ ██▀███  ')
pcmr.append('▓██░  ██▒▒██▀ ▀█  ▓██▒▀█▀ ██▒▓██ ▒ ██▒')
pcmr.append('▓██░ ██▓▒▒▓█    ▄ ▓██    ▓██░▓██ ░▄█ ▒')
pcmr.append('▒██▄█▓▒ ▒▒▓▓▄ ▄██▒▒██    ▒██ ▒██▀▀█▄  ')
pcmr.append('▒██▒ ░  ░▒ ▓███▀ ░▒██▒   ░██▒░██▓ ▒██▒')
pcmr.append('▒▓▒░ ░  ░░ ░▒ ▒  ░░ ▒░   ░  ░░ ▒▓ ░▒▓░')
pcmr.append('░▒ ░       ░  ▒   ░  ░      ░  ░▒ ░ ▒░')
pcmr.append('░░       ░        ░      ░     ░░   ░ ')
pcmr.append('         ░ ░             ░      ░     ')
pcmr.append('         ░                            ')

pcmrW = len(pcmr[0])
pcmrH = len(pcmr)

fillerW = int((col - pcmrW)/2)
fillerH = int((row - pcmrH)/2)

print('\n'*fillerH)
for line in pcmr:
	print(' '*fillerW + line)
print('\n'*fillerH)