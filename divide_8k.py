#this script is to divide training set and test set tockens of flickr8k dataset.

file = open("Flickr8k.token")

train_set = "Flickr_8k.trainImages.txt"
test_set = "Flickr_8k.testImages.txt"

def readfile(fname):
        image_index = []
        with open(fname) as f:
                for line in f:
                        image_index.append(line.split('.')[0])
        return image_index

train_image = readfile(train_set)
test_image = readfile(test_set)

train_file = open("train.token", "w")
test_file = open("test.token", "w")

while 1:
    line = file.readline()
    if not line:
        break
    if(line.split('.')[0] in train_image):
        train_file.write(line)
    elif(line.split('.')[0] in test_image):
        test_file.write(line)

train_file.close()
test_file.close()
