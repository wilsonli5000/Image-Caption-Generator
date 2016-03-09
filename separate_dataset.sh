echo "This script is to separate training set and test set. Input: train.txt, test.txt"
echo "author: Jingyuan Li"

#path parameters
traintxt="./Flickr_8k.trainImages.txt"
testtxt="./Flickr_8k.testImages.txt"

train_list="`cat $traintxt`"
test_list="`cat $testtxt`"

for list in $train_list
do
        mv ./Flickr8k_Dataset/$list ./Flickr8k_Dataset/train/
        echo "Moved $list to train."
done

for listt in $test_list
do
        mv ./Flickr8k_Dataset/$listt ./Flickr8k_Dataset/test/
        echo "Moved $listt to test."
done

