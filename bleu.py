from nltk.translate import bleu_score as bleu
import pandas as pd
import os

capfile = './wilson/generated_caption.txt'
annotation_path = './data/results_20130124.token'
flickr_image_path = './data/flickr30k-images/train'

with open(capfile) as f:
    caption = f.readlines()[0].split(' ')

annotations = pd.read_table(annotation_path, sep='\t', header=None, names=['image', 'caption'])
annotations['image_num'] = annotations['image'].map(lambda x: x.split('#')[1])
annotations['image'] = annotations['image'].map(lambda x: os.path.join(flickr_image_path,x.split('#')[0]))
## params ##
weight = [0.25, 0.25, 0.25, 0.25, 0.25]
#print caption
#for i in range(5):
#	print annotations['caption'][i]
reference = []
for i in range(5):
	reference.append(annotations['caption'][i].split(' '))
#print reference
bleu_score = bleu.sentence_bleu(reference, caption, weight, smoothing_function=None)

print bleu_score
