#This program just takes text input and stores it nicely in a little
#file with a timestamp.
import time

try:
	file = open("successes.txt")
except:
	file = open("successes.txt","w")

file.close()

def main(input=""):
	if (input):
		file = open("successes.txt","a")
		file.write("On "+time.asctime()+", I "+input)
		file.close()
