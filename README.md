# Tweet Sampler program

python tweetSampler.py [output-file]

Currently outputs a hard-coded number of tweets to an output file. The tweets are in json format with lots of info about the user and other stuff. Output to a txt file though.

# Extract Text program

python extractText.py [input-file] [output-file]

Takes a text file with tweets in json format, extracts text and writes it to a file. Extracted format looks like this:

[text of tweet, may multiple lines]
%end text%

# Assign Labels program

python assignLabels.py [input-file] [output-file]

Automates the process of manually labeling the text files. 1 for concerning, 0 for not
