# Dataset Generator for OCR System
Generate training dataset for OCR system using images of handwritten digits form MNIST database.

## Usage
After cloning this repository to local machine, run the following commands: 

` cd ./training-dataset-for-ocr`

`./venv/bin/activate`

`(venv) $ pip install --upgrade pip`

`(venv) $ pip install --requirement requirements.txt`

`(venv) $ python main.py [-h] [-op OP] [-seq SEQ] [-l LEN] [-nd ND] [-ni NI] [-w W] [-min MIN] [-max MAX]`


There are two options to generate training dataset for OCR system.

### Images Generator
Generate images of a specific digital sequence.

command:

`python main.py [-op OP] [-seq SEQ] [-ni NI] [-w W] [-min MIN] [-max MAX]`

arguments:
~~~
-op, --op 			'images'
-seq, --seq   			provide a sequence of digits (default: 12345)
-ni, --ni       		provide number of images (default: 1000)
-w, --w           		provide width of generated images (default: 150)
-min, --min   			provide minimum spacing between digits (default: 0)
-max, --max   			provide maximum spacing between digits (default: 5)
~~~

The generated images will be saved in a ".csv" file under path "/data" with the specific sequence in the file name. The corresponding labels of each image will be saved in the same folder. Each created image is saved as an 1-d array. When reading it from the csv file, a `numpy.reshape((-1, image_width))` function should be performed to transfer it to a 2-d array. 5 sampled images will be shown for visualization purpose.

### Dataset Generator
Generate `[-nd ND]` digital sequences with length `[-l LEN]`. `[-ni NI]` images are created for each sequence.

command:

`python main.py [-op OP] [-l LEN] [-nd ND] [-ni NI] [-w W] [-min MIN] [-max MAX]`

arguments:
~~~
-op, --op 			'dataset'
-l, -len, --len                 provide length of digital sequence (default: 5)
-nd, --nd   			provide number of digital sequences (default: 5)
-ni, --ni       		provide number of images (default: 1000)
-w, --w           		provide width of generated images (default: 150)
-min, --min   			provide minimum spacing between digits (default: 0)
-max, --max   			provide maximum spacing between digits (default: 5)
~~~

The generated images will be saved in a ".csv" file under path "/data" with the length of digital sequence in the file name. The corresponding labels of each image will be saved in the same folder. 5 sampled images of each unique digital sequence will be shown.


