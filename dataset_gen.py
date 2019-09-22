import img_gen
import numpy as np

# generate random digits sequence and save as csv file
def digits_generator(len_dig):
	numbers = np.random.randint(10, size = len_dig)
	res = ''.join([str(x) for x in numbers])
	return res

def dataset_generator(len_dig, num_dig, num_img, image_width, min_spacing, max_spacing):
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