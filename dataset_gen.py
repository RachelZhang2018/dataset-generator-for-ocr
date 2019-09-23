import img_gen
import numpy as np

def digits_generator(len_dig):
	'''
	A function to generate random digits sequence given the length of the sequence.
	Returns a string representing the sequence.
	Parameters
	----------
	len_dig: int
	The length of the sequence.
	'''
	numbers = np.random.randint(10, size = len_dig)
	res = ''.join([str(x) for x in numbers])
	return res

# generate images and save as csv file with corresponding labels
def dataset_generator(len_dig, num_dig, num_img, image_width, min_spacing, max_spacing):
	'''
	A function to generate images with the length of digital sequence given,
	and save images as arrays in a csv file with corresponding labels.
	Parameters
	----------
	len_dig: int
	The length of the sequence.
	num_dig: int
	The number of sequences with the fixed length.
	num_img: int
	The number of images generated for one unique sequence.
	image_width: int
	The image width (in pixel).
	min_spacing: int
	The minimum spacing between digits (in pixel).
	max_spacing: int
	The maximum spacing between digits (in pixel).
	'''
	name = "train_len" + str(len_dig)
	nameLab = "lable_len" + str(len_dig)
	f = open('data/{0}.csv'.format(name), 'wb')
	f_l = open('data/{0}.csv'.format(nameLab), 'w')

	for i in range(num_dig):
		digits = digits_generator(len_dig)
		
		for j in range(num_img):		
			img = img_gen.create_digit_sequence(digits, image_width, min_spacing, max_spacing)
			# show the first 5 generated images
			if i < 5 and j == 0:
				img_gen.show_digits(img)
			img = img.reshape((1,-1))
			np.savetxt(f, img, fmt='%i', delimiter = ",")
			np.savetxt(f_l, [digits], fmt='%s')

	f.close()
	f_l.close()
	print("The task is completed successfully.")
	
	'''
	# test: read labels
	with open('data/{0}.csv'.format(nameLab)) as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			print(row)
	'''