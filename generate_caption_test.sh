
echo "This script takes all test images and output generated captions in generated_caption.txt."

globalpath="/home/ubuntu/show_and_tell.tensorflow/data/flickr30k-images/test"

pypath="/home/ubuntu/show_and_tell.tensorflow/run.py"

txtpath="/home/ubuntu/show_and_tell.tensorflow/wilson/generated_caption.txt"
length="`ls -l $globalpath | wc -l`"
echo "length$length"

imagenames=`ls $globalpath`
#echo "$imagenames"

for image in $imagenames
do 
	imagepath="$globalpath/$image"
	python $pypath $imagepath 1>> $txtpath
done 


