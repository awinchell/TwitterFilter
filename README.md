# Run the main program in the root directory

python linsvm.py

# Repository structure

## Root directory

linsvm.py is the main program and contains a couple function definitions specific to linear SVMs.
setup.py reads in the data files and creates the cache. 
gradientdescent.py handles most the gradient descent code. 

## data directory

Contains the final labels files and the files with the extracted text from the tweets.

## cache directory 

Contains pickle objects of the matrices for the labels and feature/sample matrices, as well as pickle objects for the training unigram and bigram list. setup.py in the root directory will create and load these files automatically.

## dataCreationFiles directory

This directory contains python scripts used to create the data files and some of the old data files before neccesary processing. Explanation of a couple of the scripts:

### Tweet Sampler program

python tweetSampler.py [output-file]

Currently outputs a hard-coded number of tweets to an output file. The tweets are in json format with lots of info about the user and other stuff. Output to a txt file though.

### Extract Text program

python extractText.py [input-file] [output-file]

Takes a text file with tweets in json format, extracts text and writes it to a file. Extracted format looks like this:

[text of tweet, may multiple lines]
%end text%

### Assign Labels program

python assignLabels.py [input-file] [output-file]

Automates the process of manually labeling the text files. 1 for concerning, 0 for not
