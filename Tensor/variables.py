#Las variables se pueden definir como se muestra a continuación.
a = tf.Variable(tf.zeros([5]), name="a")

#Otra forma de usar variable es

z = tf.Variable(tf.add(x, y), trainable=False)

#Así se crea un placeholder
placeholder(dtype, shape=None, name=None)
