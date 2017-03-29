import sys

try:
    import json
except:
    import simplejson as json

tweets_json_filename = sys.argv[1]
tweets_json_file = open(tweets_json_filename, 'r')
output_filename = sys.argv[2]
output_file = open(output_filename, 'w')

for line in tweets_json_file:
    try:
        tweet = json.loads(line.strip())
        if 'text' in tweet:
            output_file.write(tweet['text'] + '\n')
    except:
        continue

tweets_json_file.close()
output_file.close()
