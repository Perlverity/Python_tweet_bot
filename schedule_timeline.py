from time import sleep
import schedule
import time
from requests_oauthlib import OAuth1Session

from make_move import make_move
from download_illusts import download
from tweet_timeline import tweet
from compress import compress


def schedule_tweet():
  make_move()
  download()
  compress()
  tweet()

if __name__ == "__main__":
  print('実行中...')
  # schedule_tweet()
  schedule.every(1).minutes.do(schedule_tweet)
  while True:
    schedule.run_pending()
    sleep(1)
  # print('ツイート完了!')