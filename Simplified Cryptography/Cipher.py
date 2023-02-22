#  File: Cipher.py

#  Description: This program takes in two strings from a text file and applies a rotation cipher to encrypt
#  				the first line in the file while decrypting the second line in the file

#  Student Name: Julian Wearden

#  Student UT EID: jfw864

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 313E

#  Unique Number: 52604

#  Date Created: 09/11/2021

#  Date Last Modified: 09/13/2021

# Import Libraries
import math
import sys


# Input: None
# Output: The text that needs to be encrypted as
#         encrypt_text and the text to be decrypted
#         as decrypt_text
def read_file():
	file = sys.stdin.read()								# Read the file
	a = file.split("\n")								# Create list split up by end lines
	encrypt_text = a[0]									# First line is message to be encrypted
	decrypt_text = a[1]									# Second line is message to be decrypted

	return encrypt_text, decrypt_text


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def encrypt(strng):

	matrix = create_encrypt_array(strng)					# Create array with strng
	matrix = rotate90(rotate90(rotate90(matrix))) 			# Rotate matrix 90 degrees clockwise (3 times counter clockwise)
	encrypted_text = read_array(matrix) 					# Read array as a string

	return encrypted_text


# Input: strng is a string of 100 or less of upper case, lower case, 
#        and digits
# Output: function returns an encrypted string 
def decrypt(strng):
	matrix = create_decrypt_array(strng)  					# Create array with strng
	matrix = rotate90(matrix)  								# Rotate matrix 90 degrees counter-clockwise
	decrypted_text = read_array(matrix)  					# Read array as a string

	return decrypted_text

# Input: strng is text to populate into a 2d array
# Output: matrix a 2d array with strng text and *
def create_decrypt_array(strng):
	# Find next square number
	l = len(strng)
	if l % math.sqrt(l) != 0:
		sqrt_m = int(math.floor(math.sqrt(l)) + 1)
		m = sqrt_m ** 2
	else:
		sqrt_m = int(math.sqrt(l))
		m = sqrt_m ** 2

	# Create 2d matrix
	matrix = [['0' for x in range(sqrt_m)] for y in range(sqrt_m)]

	# Calculate number of stars (*) needed
	n_stars = m - len(strng)

	# Iterate through array from bottom to top and left to right while filling in the stars
	i = sqrt_m - 1
	j = 0
	for n in range(n_stars):
		if n_stars > 0:
			matrix[i][j] = '*'
		if i == 0:
			i = sqrt_m - 1
			if j == sqrt_m - 1:
				j = 0
			else:
				j += 1
		else:
			i -= 1

	# Fill in the remaining string from left to right and top to bottom
	x = 0
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if matrix[i][j] != '*':
				matrix[i][j] = strng[x]
				x += 1

	return matrix


# Input: strng is text to populate into a 2d array
# Output: matrix a 2d array with strng text and *
def create_encrypt_array(strng):
	# Find next square number (m) and its square root (sqrt_m)
	l = len(strng)
	if l % math.sqrt(l) != 0:
		sqrt_m = int(math.floor(math.sqrt(l)) + 1)
		m = sqrt_m ** 2
	else:
		sqrt_m = int(math.sqrt(l))
		m = sqrt_m ** 2

	# Create 2d matrix filled with *
	matrix = [['*' for x in range(sqrt_m)] for y in range(sqrt_m)]

	# Populate 2d array with string
	i, j = 0, 0
	for character in strng:
		matrix[i][j] = character
		if sqrt_m != 1:
			if j % (sqrt_m - 1) == 0 and j != 0:
				j = 0
				if i % (sqrt_m - 1) == 0 and i != 0:
					i = 0
				else:
					i += 1
			else:
				j += 1

	return matrix


# Input: matrix is a 2d array
# Output: function returns a string of the characters in matrix
def read_array(matrix):
	strng = ""
	# Iterate through array and append all non * characters to strng
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if matrix[i][j] != '*':
				strng += matrix[i][j]

	return strng


# Input: matrix a 2d array
# Output: matrix by 90 degrees counter-clockwise
def rotate90(matrix):
	# Create 2d matrix
	# Used outside info for this line of code.
	# Source: stackoverflow.com/questions/53250821/in-python-how-do-i-rotate-a-matrix-90-degrees-counterclockwise
	matrix2 = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0])-1, -1, -1)]
	return matrix2


def main():
	# read the strings P and Q from standard input
	P, Q = read_file()
	# encrypt the string P
	encrypted_P = encrypt(P)
	# decrypt the string Q
	decrypted_Q = decrypt(Q)
	# print the encrypted string of P
	print(encrypted_P)
	# and the decrypted string of Q
	print(decrypted_Q)


if __name__ == "__main__":
	main()


