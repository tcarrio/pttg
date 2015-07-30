# encoding=utf8
import os
rowS, columnS = os.popen('stty size', 'r').read().split()
row = int(rowS)
col = int(columnS)

feral = []
feral.add("   █████▒▓█████  ██▀███   ▄▄▄       ██▓      ")
feral.add(" ▓██   ▒ ▓█   ▀ ▓██ ▒ ██▒▒████▄    ▓██▒      ")
feral.add(" ▒████ ░ ▒███   ▓██ ░▄█ ▒▒██  ▀█▄  ▒██░      ")
feral.add(" ░▓█▒  ░ ▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██ ▒██░      ")
feral.add(" ░▒█░    ░▒████▒░██▓ ▒██▒ ▓█   ▓██▒░██████▒  ")
feral.add("  ▒ ░    ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░▓  ░  ")
feral.add("  ░       ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░ ▒  ░  ")
feral.add("  ░ ░       ░     ░░   ░   ░   ▒     ░ ░     ")
feral.add("            ░  ░   ░           ░  ░    ░  ░  ")
feral.add("                                             ")
feral.add("  ▄████  ▄▄▄       ███▄ ▄███▓▓█████   ██████ ")
feral.add(" ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀ ▒██    ▒ ")
feral.add("▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███   ░ ▓██▄   ")
feral.add("░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄   ▒   ██▒")
feral.add("░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒▒██████▒▒")
feral.add(" ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░")
feral.add("  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░░ ░▒  ░ ░")
feral.add("░ ░   ░   ░   ▒   ░      ░      ░   ░  ░  ░  ")
feral.add("      ░       ░  ░       ░      ░  ░      ░  ")

feralW = len(feral[0])
feralH = len(feral)

fillerW = int((col - feralW)/2)
fillerH = int((row - feralH)/2)

print('\n'*fillerH)
for line in feral:
	print(' '*fillerW + line)
print('\n'*fillerH)