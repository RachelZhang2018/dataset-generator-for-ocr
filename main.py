import argparse
import img_gen
import dataset_gen

parser = argparse.ArgumentParser(description='Generate training dataset.')

parser.add_argument('-op', '--op', default='images', type=str,
                    help='choose type of generator (default: images; options: dataset)')
parser.add_argument('-seq', '--seq', default='12345', type=str,
                    help='provide a sequence of digits (default: 12345)')
parser.add_argument('-l', '-len', '--len', default=5, type=int,
                    help='provide length of digital sequence (default: 5)')
parser.add_argument('-nd', '--nd', default=5, type=int,
                    help='provide number of digital sequences (default: 5)')
parser.add_argument('-ni', '--ni', default=1000, type=int,
                    help='provide number of images (default: 1000)')
parser.add_argument('-w', '--w', default=150, type=int,
                    help='provide width of generated images (default: 150)')
parser.add_argument('-min', '--min', default=0, type=int,
                    help='provide minimum spacing between digits (default: 0)')
parser.add_argument('-max', '--max', default=5, type=int,
                    help='provide maximum spacing between digits (default: 5)')

args = parser.parse_args()

if(args.op == 'images'):
	digits = args.seq
	num_img = args.ni
	image_width = args.w
	min_spacing = args.min
	max_spacing = args.max
	img_gen.images_generator(digits = digits,
							num_img = num_img,
							image_width = image_width,
							min_spacing = min_spacing,
							max_spacing = max_spacing)

elif(args.op == 'dataset'):
	len_dig = args.len
	num_dig = args.nd
	num_img = args.ni
	image_width = args.w
	min_spacing = args.min
	max_spacing = args.max

	dataset_gen.dataset_generator(len_dig = len_dig, 
								num_dig = num_dig,
								num_img = num_img, 
								image_width = image_width, 
								min_spacing = min_spacing, 
								max_spacing = max_spacing)

else:
	parser.print_help()
