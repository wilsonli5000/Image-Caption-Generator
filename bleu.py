from nltk.translate import bleu_score as bleu
import pandas as pd
import os
import numpy as np

capfile = './wilson/generated_caption.txt'
imagefile = './wilson/test_image_index.txt'
annotation_path = './data/results_20130124.token'
flickr_image_path = './data/flickr30k-images/train'

#read lines from a file. with this syntax, the return value in line is string. 
#if use readlines(), return type is list containing only one line.
def readfile(capfile):
	caption = []	
	wc = 0
	with open(capfile) as f:
		for line in f:
			caption.append(line.split())
			wc += 1
	return wc, caption

image_amount, caption = readfile(capfile)
image_amount, image_name = readfile(imagefile)
image_name[0:] = [image[0] for image in image_name[0:]]
image_name = map(lambda x: os.path.join(flickr_image_path, x), image_name)
#here is the trick of modifying list elements. Use list comprehension for in place modification.
#for image in image_name:
#image_name[0:] = [i[0].split('.') for i in image_name[0:]]
#print image_name

annotations = pd.read_table(annotation_path, sep='\t', header=None, names=['image', 'caption'])
annotations['image_num'] = annotations['image'].map(lambda x: x.split('#')[1])
annotations['image'] = annotations['image'].map(lambda x: os.path.join(flickr_image_path,x.split('#')[0]))

#image_index is the list stores the annotations data frame row index for each test image.
#each test image has 5 reference captions, therefore, each element in the list has 5 indexes.
image_index = []
for i in image_name:
	image_index.append(np.where(annotations['image'] == i))
#print image_index

#get the reference captions for each test image.
#references is the list stores the reference captions of each test image, each sublist contains five captions. 235 total sublists.
#print annotations['caption']

references = []
for index in image_index:
	tuple = []	
	for i in index[0]:
		tuple.append(annotations['caption'].iloc[i].split())
	references.append(tuple)
#print references	
 
## params ##
weight = [0.25, 0.25, 0.25, 0.25, 0.25]

#print "captionlen: ", len(caption)
#print "references[0]", references[0]

bleu_score = []
for i in range(len(caption)):
	bleu_score.append(bleu.sentence_bleu(references[i], caption[i], weight, smoothing_function=None))

print np.mean(bleu_score)
