constant(value, dtype=None, shape=None, name='Const', verify_shape=False)
#value - Puede tomar cualquier valor asignado
#shape - esto es opcional, toma las dimensiones
#name - puede asignar cualquier nombre a la constante
#verify_shape - otro parámetro opcional que verifica la dimensión de la constante.
x = tf.constant(42, name="a", dtype=tf.float32)
