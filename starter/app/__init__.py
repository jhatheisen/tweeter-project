from flask import Flask, render_template, redirect
from .config import Config
from .tweets import tweets
from .forms.new_tweet import TweetForm
import random
import datetime

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
  randomI = random.randint(0, len(tweets) - 1)
  tweet = tweets[randomI]
  return render_template('index.html', tweet=tweet)

@app.route('/feed')
def feed():
  # tweets = sorted(tweets, key=lambda tweet: print(tweet['date']))
  print()
  return render_template('feed.html', sampleTweets=tweets)

@app.route('/new', methods=['GET', 'POST'])
def newTweet():
  form = TweetForm()
  if form.validate_on_submit():

    new_tweet = {
      "id": len(tweets) + 1,
      "author": form.data["author"],
      "date": datetime.datetime.now().date(),
      "tweet": form.data["tweet"],
      "likes": random.randint(0, 900000)
    }

    print(new_tweet)
    tweets.append(new_tweet)

    return redirect('/feed')

  if form.errors:
    return form.errors
  return render_template('new_tweet.html', form=form)
