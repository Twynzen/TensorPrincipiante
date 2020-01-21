# Import `tensorflow`
import tensorflow as tf

# Initialize two constants
a1 = tf.constant([4,3,2,1])
a2 = tf.constant([3,1,3,4])

# Perform Multiplication
res = tf.multiply(a1, a2)

# Initialize Session and run `result`
with tf.Session() as sess:
  finalOutput = sess.run(res)
  print(finalOutput)
