import tweepy  # https://github.com/tweepy/tweepy
import csv

from searchtweets import ResultStream, gen_rule_payload, load_credentials
# Twitter API credentials
consumer_key = #REDACTED
consumer_secret = #REDACTED
access_key = #REDACTED
access_secret = #REDACTED


curl -X POST "https://api.twitter.com/1.1/tweets/search/:product/:label.json" -d '{"query":"TwitterDev "search api"","maxResults":"500","fromDate":"<yyyymmddhhmm>","toDate":"<yyyymmddhhmm>"}' -H "Authorization: Bearer TOKEN"
