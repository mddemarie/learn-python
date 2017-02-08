from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords('Python') # let's define all words we would like to have a look for
    tso.set_language(['de', 'en']) # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'aaabbb',
        consumer_secret = 'cccddd',
        access_token = '111222',
        access_token_secret = '333444'
     )

     # this is where the fun actually starts :)
    num_tweets = []
    for tweet in ts.search_tweets_iterable(tso):
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        num_tweets.append()
    print "Number of tweets with the word "Python" is:", num_tweets.count()


except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)