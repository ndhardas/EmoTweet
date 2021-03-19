import tweepy
from textblob import TextBlob

# c_key = "5wWngk7LTw5mtZUEWpg5NiDIo"
# s_key = "fhvNQkc1tigJtoDWafvbuh9XfbaXaarW9iv1NYSgws92Z5o0jH"

# a_token = "1240764508878012421-rKiLvJI70dtMwHQToIiJxepmuaP3GX"
# a_secret = "6bt5NvPIMlbD3cFPszkJHnNc8tmzt4OOfQnOW6Q8N3eF2"

c_key = "FB7wq3fg2s4KUFLiHMYRiDvtI"
s_key = "rU8r3L5mAakL5OIeBlZN3wbUzo0f62Xxr4oyeY2NyDXIHSRBQ8"

a_token = "1309394246215118848-JV9PZbViEGUMZRaNybrgfTdMtl5v8N"
a_secret = "uJ94dkQdq1JRbtixX1qT2eFNsyLruOO6tT5YJT9FyRWCD"


def testing(username):
    consumer_key = c_key
    secret_key = s_key

    #api key: xm0yWJEsdsEGVX3CaUU2eNPWG
    # api secret ket: 05vUECrVxoBXlWsEraYdbjgaL8Fu7tmiojjRYttR6J0d08dMDv
    #bearer token:AAAAAAAAAAAAAAAAAAAAAHA4HAEAAAAAuxisE4t0w4HKNqMEBEbf1tcAJ2c%3D4QCg40vYB33w7bhcc5gw0FkjeypAzbQzlUCWzZR8tXlVXct5ce

    access = a_token
    access_secret = a_secret

    auth = tweepy.OAuthHandler(consumer_key, secret_key)
    auth.set_access_token(access, access_secret)
    api = tweepy.API(auth)
    try:
        var = api.get_user(username)
        print(var)
    except:
        print("ye")
        return "no"

def do_calculation(username):
    consumer_key = c_key
    secret_key = s_key

    access = a_token
    access_secret = a_secret

    auth = tweepy.OAuthHandler(consumer_key, secret_key)
    auth.set_access_token(access, access_secret)
    api = tweepy.API(auth)
    try:
        var = api.get_user(username)
        print(var)
    except:
        print("ye")
        return "You didn't enter a valid username. Try again."

    depressing_words = depressing_words = ("ps4", "problem", "miss", "existing", "tired", "hates", "miss her", "hate", "want her", "cry", "alone", "crying", "staring at", "nobody", "pain", "haha")

    tweets = api.user_timeline(screen_name=username, count = 100)
    tot_pol = 0
    tot_sub = 0
    total = 0
    #most_depressing = ""
    for tweet in tweets:
        if (tweet.text[0:2] != "RT") and (tweet.text[0:1] != "@"):
            #print(tweet.text)
            blob = TextBlob(tweet.text)
            temp_pol = blob.sentiment.polarity
            for word in depressing_words:
                if word in tweet.text:
                    temp_pol -= 0.05
            #if temp_pol #find most dperesiing tweet
            tot_pol += temp_pol
            tot_sub += blob.sentiment.subjectivity
            total = total + 1
            #print(blob.sentiment.polarity)

    av_pol = tot_pol/total
    #av_sub = tot_sub/total
    if av_pol < 0.0:
        print("1")
        return username +"'s tweets are generally more sad"
    elif av_pol > 0.25:
        print("2")
        return username +"'s tweets are generally more upbeat"
    else:
        print("3")
        return username +"'s tweets are generally neutral"

def indv_pol(tweet):
    depressing_words = depressing_words = ("she", "her", "ps4", "problem", "miss", "existing", "tired", "hates", "miss her", "hate", "want her", "cry", "alone", "crying", "staring at", "nobody", "pain", "haha")
    blob = TextBlob(tweet)
    pol = blob.sentiment.polarity
    for word in depressing_words:
        if word in tweet:
            pol -= 0.05
    print(pol)
    return pol


def get_sad(username):
    consumer_key = c_key
    secret_key = s_key

    access = a_token
    access_secret = a_secret

    auth = tweepy.OAuthHandler(consumer_key, secret_key)
    auth.set_access_token(access, access_secret)
    api = tweepy.API(auth)

    if do_calculation(username) == "You didn't enter a valid username. Try again.":
        return ""

    tweets = api.user_timeline(screen_name=username, count = 100)
    saddest = ""
    saddest_val = 2

    for tweet in tweets:
        if (tweet.text[0:2] != "RT") and (tweet.text[0:1] != "@"):
            #print("Current tweet " + tweet.text + "\n")
            #print("Current pol " + str(indv_pol(tweet.text)) + "\n")
            if (indv_pol(tweet.text) < saddest_val):
                saddest = tweet.text
                saddest_val = indv_pol(tweet.text)
    #print("Saddest tweet: " + saddest)
    return "Saddest tweet is: \"" + saddest + "\""


def get_happy(username):
    consumer_key = c_key
    secret_key = s_key

    access = a_token
    access_secret = a_secret

    auth = tweepy.OAuthHandler(consumer_key, secret_key)
    auth.set_access_token(access, access_secret)
    api = tweepy.API(auth)

    if do_calculation(username) == "You didn't enter a valid username. Try again.":
        return ""

    tweets = api.user_timeline(screen_name=username, count = 100)
    happy = ""
    happy_val = -2

    for tweet in tweets:
        if (tweet.text[0:2] != "RT") and (tweet.text[0:1] != "@"):
            #print("Current tweet " + tweet.text + "\n")
            #print("Current pol " + str(indv_pol(tweet.text)) + "\n")
            if (indv_pol(tweet.text) > happy_val):
                happy = tweet.text
                happy_val = indv_pol(tweet.text)
    #print("Happy tweet: " + happy)
    return "Happiest tweet is: \"" + happy + "\""


testing("%$#")




