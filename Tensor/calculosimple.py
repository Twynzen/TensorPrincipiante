# Import tensorflow library
import tensorflow as tf

# Initialize two constants
a1 = tf.constant([4,3,2,1])
a2 = tf.constant([1,3,4,7])

# Perform Multiplication
res = tf.multiply(a1, a2)

# Intialize the Session
sess = tf.Session()

# Print the result
print(sess.run(res))

# Close the session
