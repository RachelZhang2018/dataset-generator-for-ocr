import argparse
import training_gen

parser = argparse.ArgumentParser(description='Generate training dataset.')

parser.add_argument('-l', '-len', '--len', default=10, type=int,
                    help='provide length of digital sequence (default: 10)')
parser.add_argument('-n', '--n', default=1000, type=int,
                    help='provide number of images (default: 1000)')
parser.add_argument('-w', '--w', default=300, type=int,
                    help='provide number of images (default: 300)')
parser.add_argument('-min', '--min', default=0, type=int,
                    help='provide minimum spacing between digits (default: 0)')
parser.add_argument('-max', '--max', default=5, type=int,
                    help='provide maximum spacing between digits (default: 5)')

args = parser.parse_args()

len_dig = args.len
num_img = args.n
image_width = args.w
min_spacing = args.min
max_spacing = args.max

training_gen.images_generator(len_dig = len_dig, 
							num_img = num_img, 
							image_width = image_width, 
							min_spacing = min_spacing, 
							max_spacing = max_spacing)

