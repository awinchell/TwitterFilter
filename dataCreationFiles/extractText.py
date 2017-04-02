import sys

try:
    import json
except:
    import simplejson as json

tweets_json_filename = sys.argv[1]
tweets_json_file = open(tweets_json_filename, 'r')
output_filename = sys.argv[2]
output_file = open(output_filename, 'w')

uniqueLines = []

for line in tweets_json_file:
    try:
        tweet = json.loads(line.strip())
        if 'text' in tweet:
            if tweet['text'] not in uniqueLines:
                output_file.write(tweet['text'] + '\n')
                output_file.write('%end text%\n')
                uniqueLines.append(tweet['text'])
    except:
        continue

print('Parsed ' + str(len(uniqueLines)) + ' unique lines')
tweets_json_file.close()
output_file.close()
