# training-dataset-for-ocr
Generate training dataset for OCR system using images form MNIST dataset.

There are two options to generate training dataset for OCR system.

## Images Generator
Generate images of a specific digital sequence.

command:
`python main.py -op -seq -ni -w -min -max`

arguments:
~~~
-op, --op 				'images'
-seq, --seq   			provide a sequence of digits (default: 12345)
-ni, --ni       		provide number of images (default: 1000)
-w, --w           		provide width of generated images (default: 150)
-min, --min   			provide minimum spacing between digits (default: 0)
-max, --max   			provide maximum spacing between digits (default: 5)
~~~

The generated images will be saved in a ".csv" file under path "/data" with the specific sequence in the file name. The corresponding labels of each image will be saved in the same folder.

## Dataset Generator
Generate `nd` digital sequences with length `len`. `ni` images are generated for each sequence.

command:
`python main.py -op -l -nd -ni -w -min -max`

arguments:
~~~
-op, --op 				'dataset'
-l, -len, --len         provide length of digital sequence (default: 5)
-nd, --nd   			provide number of digital sequences (default: 5)
-ni, --ni       		provide number of images (default: 1000)
-w, --w           		provide width of generated images (default: 150)
-min, --min   			provide minimum spacing between digits (default: 0)
-max, --max   			provide maximum spacing between digits (default: 5)
~~~

The generated images will be saved in a ".csv" file under path "/data" with the length of digital sequence in the file name. The corresponding labels of each image will be saved in the same folder.