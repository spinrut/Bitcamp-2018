# Snow Day Predictor
import csv
import numpy as np
import tensorflow as tf

mean_stds = []

def normalize_col(col):
    global mean_stds
    mean_std = [np.mean(col), np.std(col)]
    col = col - mean_std[0]
    col = np.divide(col, mean_std[1])
    mean_stds.append(mean_std)
    return col

def get_train_in_out():
    cols = np.genfromtxt('data/processed.csv', dtype = np.float32, delimiter = ',', encoding = None)
    train_in1 = np.delete(cols, -1, axis = 1)
    train_in = np.delete(train_in1, -1, axis = 1)
    train_in = np.apply_along_axis(normalize_col, 0, train_in)
    train_out = np.reshape(cols[:,-2:], [-1, 2])

    with open('stored_weights/mean_stds.csv', 'w') as f:
        csv.writer(f).writerows(mean_stds)
        
    return train_in, train_out

# Hyperparameters and other stuff
input_size = 3
hidden_size = 5
output_size = 2
alpha = 3e-1
times = 100000

model_x = tf.placeholder(tf.float32)
model_y = tf.placeholder(tf.float32)

train_in, train_out = get_train_in_out()

#Parameters

# Neural Network
# Seems to work fine
wh = tf.Variable(tf.random_normal([input_size, hidden_size]))
bh = tf.Variable(tf.zeros([hidden_size]))
                 
wo = tf.Variable(tf.random_normal([hidden_size, output_size]))
bo = tf.Variable(tf.zeros([output_size]))

out1 = tf.tanh(tf.add(tf.matmul(model_x, wh), bh))
out2 = tf.add(tf.matmul(out1, wo), bo)

# Logistic Regression
# Underfits; can't represent enough complexity
##wo = tf.Variable(tf.random_normal([input_size, output_size]))
##bo = tf.Variable(tf.zeros([output_size]))
##
##out2 = tf.add(tf.matmul(model_x, wo), bo)

out3 = tf.sigmoid(out2)
error = tf.reduce_mean(tf.losses.sigmoid_cross_entropy(model_y, out2))
residuals = tf.subtract(model_y, out3)
mse = tf.reduce_mean(tf.square(residuals), axis=0)
_, variance = tf.nn.moments(model_y, axes = 0)
r_squared = tf.subtract(1.0, tf.divide(mse, variance))

train = tf.train.GradientDescentOptimizer(alpha).minimize(error)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    saver = tf.train.Saver()
    saver.restore(sess, 'stored_weights/weights')
    
    for i in range(times):
        err, _ = sess.run([error, train], feed_dict = {model_x: train_in, model_y: train_out})
        if i % 1000 == 0:
            print('Epoch: ', i, ' Cost: ', err)
            
    saver.save(sess, 'stored_weights/weights')
