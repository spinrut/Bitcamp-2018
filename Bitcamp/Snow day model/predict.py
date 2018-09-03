import csv
import json
import numpy as np
import tensorflow as tf
import requests

# These are expired, so get new ones
API_CLIENT_ID = #REDACTED
API_CLIENT_SECRET = #REDACTED

input_size = 3
hidden_size = 5
output_size = 2
mean_stds = np.genfromtxt('stored_weights/mean_stds.csv', dtype = np.float32, delimiter = ',', encoding = None)

def get_weather_data():
    weather = requests.get('https://api.aerisapi.com/forecasts/20850?client_id=' + API_CLIENT_ID + '&client_secret=' + API_CLIENT_SECRET)
    weather_json = weather.json()['response'][0]['periods'][1]
    return np.array([weather_json['maxTempF'], weather_json['minTempF'], weather_json['snowIN']], dtype=np.float32, ndmin = 2)

def normalize(x):
    # Watch out for data destruction
    for i in range(mean_stds.shape[0]):
        x[:, i] = np.divide(np.subtract(x[:, i], mean_stds[i, 0]), mean_stds[i, 1])
        
    return x
model_x = tf.placeholder(tf.float32)
model_y = tf.placeholder(tf.float32)

wh = tf.Variable(tf.zeros([input_size, hidden_size]))
bh = tf.Variable(tf.zeros([hidden_size]))
                 
wo = tf.Variable(tf.zeros([hidden_size, output_size]))
bo = tf.Variable(tf.zeros([output_size]))

out1 = tf.tanh(tf.add(tf.matmul(model_x, wh), bh))
out2 = tf.add(tf.matmul(out1, wo), bo)
out3 = tf.sigmoid(out2)

with tf.Session() as sess:
    saver = tf.train.Saver()
    saver.restore(sess, 'stored_weights/weights')

    thing = get_weather_data()

    pred = sess.run(out3, feed_dict = {model_x: normalize(thing)})

    with open('result.csv', 'w') as out:
        writer = csv.writer(out)
        writer.writerow(pred.ravel())
