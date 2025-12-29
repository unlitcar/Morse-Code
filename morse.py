"""
This script takes user input from the terminal and convert it to morse and 
if pygame is installed it opens a window that flashes according to the morse code.
"""


# Check if pygame is availble, if not the visual part is skipped
visual_mode = True
try:
	try:
		import os
		os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = ''
	except ModuleNotFoundError:
		pass
	import pygame
except ModuleNotFoundError:
	print("This Python file uses the Pygame module for visuals; it seems that it isn't installed so the file will run but with no graghics")
	visual_mode = False


# Dictionary of all characters to morse
morse = {
	" ":     "       ",
	"A":         "· −",
	"B":     "− · · ·",
	"C":     "− · − ·",
	"D":       "− · ·",
	"E":           "·",
	"F":     "· · − ·",
	"G":       "− − ·",
	"H":     "· · · ·",
	"I":         "· ·",
	"J":         "· −",
	"K":       "− · −",
	"L":     "· − · ·",
	"M":         "− −",
	"N":         "− ·",
	"O":       "− − −",
	"P":     "· − − ·",
	"Q":     "− − · −",
	"R":       "· − ·",
	"S":       "· · ·",
	"T":           "−",
	"U":       "· · −",
	"V":     "· · · −",
	"W":       "· − −",
	"X":     "− · · −",
	"Y":     "− · − −",
	"Z":     "− − · ·",
	"a":         "· −",
	"b":     "− · · ·",
	"c":     "− · − ·",
	"d":       "− · ·",
	"e":           "·",
	"f":     "· · − ·",
	"g":       "− − ·",
	"h":     "· · · ·",
	"i":         "· ·",
	"j":     "· − − −",
	"k":       "− · −",
	"l":     "· − · ·",
	"m":         "− −",
	"n":         "− ·",
	"o":       "− − −",
	"p":     "· − − ·",
	"q":     "− − · −",
	"r":       "· − ·",
	"s":       "· · ·",
	"t":           "−",
	"u":       "· · −",
	"v":     "· · · −",
	"w":       "· − −",
	"x":     "− · · −",
	"y":     "− · − −",
	"z":     "− − · ·",
	"0":   "− − − − −",
	"1":   "· − − − −",
	"2":   "· · − − −",
	"3":   "· · · − −",
	"4":   "· · · · −",
	"5":   "· · · · ·",
	"6":   "− · · · ·",
	"7":   "− − · · ·",
	"8":   "− − − · ·",
	"9":   "− − − − ·",
	".": "· − · − · −",
	",": "− − · · − −",
	"?": "· · − − · ·",
	"'": "· − − − − ·",
	"!": "− · − · − −",
	"/":   "− · · − ·",
	"(":   "− · − − ·",
	")": "− · − − · −",
	"&":     "· − · ·",
	":": "− − − · · ·",
	";": "− · − · − ·",
	"=":   "− · · · −"}

# List of inputted plain text and its conversions
codes_list = []


"""
Codes class manages and stores converting plain text to morse and 
converting morse to a visual encoding representing length of the morse
(i.e. not just a dit or dash character, rather a 1 or 0 to represent on for 
dit or dash or off for spacing, with dash being on for longer so more 1's)
this class also have methods to printing output minimally or verbosely
"""
class Codes:
	def convert_to_morse(self, text):
		code1 = ""
		for char in text:
			if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,?'!/()&:;= ":
				code1 += morse[char]
				if char == " ":
					code1 += ""
				else:
					code1 += "   "
		return code1

	def convert_to_visual(self, morse_code):
		code2 = ""
		for char2 in morse_code:
			if char2 == "−":
				code2 += "111"
			elif char2 == "·":
				code2 += "1"
			elif char2 == " ":
				code2 += "0"
		return code2

	def __init__(self, plain_text):
		self.plain_text = plain_text
		self.morse_encoding = self.convert_to_morse(self.plain_text)
		self.visual_encoding = self.convert_to_visual(self.morse_encoding)

	def print_minimal(self):
		print(self.morse_encoding)
		print(self.visual_encoding)
		print()

	def print_verbose(self):
		print()
		print("You inputted: " + self.plain_text)
		print("\tIn morse it is: " + self.morse_encoding)
		print("\tThe timing is: " + self.visual_encoding)
		print()



"""
Visual class manages the visual element of program such that it turns white on a
1 in visual encoding (dit or dash in morse), and black for 0 (space)
Visual class also set size, name, and icon (if found) of the window
"""
class Visual:
	def __init__(self, v):
		if visual_mode == True:
			self.v = v
			self.screen = None
			self.window()

	def window(self):
		pygame.init()
		self.screen = pygame.display.set_mode((201, 201))
		pygame.display.set_caption("Morse")
		try:
			icon = pygame.image.load("morse_logo.png")
			pygame.display.set_icon(icon)
		except:
			pass
		self.main_loop()

	def main_loop(self):
		for c in self.v:
			if c == "1":
				self.screen.fill((255, 255, 255))
			elif c == "0":
				self.screen.fill((0, 0, 0))

			pygame.display.update()
			pygame.time.delay(250)

		pygame.quit()


"""
query0 checks if there will be any new text input to convert
if not, it shows a history of the inputs, with all relavent data
by calling print_verbose() for each Codes class object in codes_list
"""
def query0():
	print("Morse?")
	start = input()
	if start == "0":
		for i in codes_list:
			i.print_verbose()
		return False
	elif start == "1":
		return True
	else:
		print("Input 1 or 0!")
		return query0()


"""
query1 is a function that takes input and makes Codes class for said input
"""
def query1():
	print("Enter plain text.")
	codes_list.append(Codes(input()))
	codes_list[-1].print_minimal()
	return codes_list[-1]

"""
main has a loop 
"""
def main():
	while True:
		if query0() == True:
			query1()
			Visual(codes_list[-1].visual_encoding)
		else:
			break


if __name__ == '__main__':
	main()
