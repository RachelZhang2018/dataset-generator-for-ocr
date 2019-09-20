from __future__ import print_function
import tensorflow as tf
from tensorflow import keras
from keras.datasets import mnist
# from keras import backend as K
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

SIZE = 28

num_classes = 10

# input image dimensions
img_rows, img_cols = SIZE, SIZE

# the data, split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Convert class indices to one-hot vectors
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

'''
def dig2img(digit, x_train, y_train):
	# a filter to find the indices of images belonging to class i
	fil = y_train[:, digit] == 1
	indices = fil.nonzero()[0]
	# find a random image from digits belonging to class i
	num_img = indices.size
	rand = np.random.randint(0, num_img)
	rand_img_index = indices[rand]
	rand_img = x_train[rand_img_index].reshape((SIZE, SIZE))
	return rand_img
'''

def create_digit_sequence(number, image_width, min_spacing, max_spacing):
	""" A function that create an image representing the given number,
	with random spacing between the digits.
	Each digit is randomly sampled from the MNIST dataset.
	Returns an NumPy array representing the image.
	Parameters
	----------
	number: str
	A string representing the number, e.g. "14543"
	image_width: int
	The image width (in pixel).
	min_spacing: int
	The minimum spacing between digits (in pixel).
	max_spacing: int
	The maximum spacing between digits (in pixel).
	"""

	length_num = len(number)
	
	# calculate the spacing size
	if(min_spacing == max_spacing):
		spacing_size = min_spacing
	else:
		spacing_size = np.random.randint(min_spacing, max_spacing)

	# calculate the width of each digit
	wsize = (image_width - spacing_size * (length_num - 1)) / length_num
	wsize = int(wsize)
	hsize = wsize

	# image generation
	new_img = Image.new('L', (image_width, hsize), color=0)
	j = 0
	for i in range(length_num):
		class_ind = int(number[i])
		# a filter to find the indices of images belonging to class i
		fil = y_train[:, class_ind] == 1
		indices = fil.nonzero()[0]
		# find a random image from digits belonging to class i
		num_img = indices.size
		rand = np.random.randint(0, num_img)
		rand_img_index = indices[rand]
		rand_img = x_train[rand_img_index].reshape((SIZE, SIZE))
		# convert array to image obejct
		arr2img = Image.fromarray(rand_img, mode='L')
		img = arr2img.resize((wsize, hsize), Image.NEAREST)
		# paste the image to the generated new image
		new_img.paste(img, (j, 0))
		j = j + wsize + spacing_size

	# convert new image to array
	res = np.asarray(new_img)

	return res


def show_digits(arr):
	plt.imshow(arr, cmap = "Greys")
	plt.show()	

for i in range(10):
	dig = create_digit_sequence("19941220", 1000, 3, 10)
	show_digits(dig)


# generate random digits sequence
def digits_generator(num_dig):
	numbers = np.random.randint(10, size = num_dig)
	res = ''.join([str(x) for x in numbers])
	return res

def images_generator(num_dig, num_img, image_width, min_spacing, max_spacing):
	digits = digits_generator(num_dig)
	imgs = []
	for i in range(num_img):
		img = create_digit_sequence(digits, image_width, min_spacing, max_spacing)
		imgs.append(img)

	# imgs is a list of np.array, len(imgs) = num_img, imgs should be saved as x_train
	return imgs