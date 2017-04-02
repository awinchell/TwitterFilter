import sys

try:
    import json
except ImportError:
    import simplejson as json

from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

output_filename = sys.argv[1]
output_file = open(output_filename, 'w')

ACCESS_TOKEN = '846935331207294976-47e8rpLBDmEUjN4dqWuaUub84KXznPk'
ACCESS_SECRET = 'TLhILZZUtzlaLR3jeLZOdNQGJdGwCv1cQhXhcaGu28mTW'
CONSUMER_KEY = '5ZlLP8rdIXF1dTF7cr7I4yE1Q'
CONSUMER_SECRET = 'KL4fUTKkG5o9S1UmUrgd8lBJV92DbQMqNVW79778m6AOyKZg9B' 

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter_stream = TwitterStream(auth=oauth)

iterator = twitter_stream.statuses.filter(track='suicide, depressed, kil', language='en')

tweet_count = 300
for tweet in iterator:
    tweet_count -= 1
    output_file.write(json.dumps(tweet) + '\n')
    if tweet_count <= 0:
        break

output_file.close()
