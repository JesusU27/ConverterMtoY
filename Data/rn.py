import os

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
import numpy as np

meters = np.array([20.0,65.0,100.0,250.0,320.0,410.0,560.0,600.0,890], dtype=float)
yards = np.array([21.872,71.084,109.361,273.403,349.956,448.381,612.423,656.168,973.316], dtype=float)

layer = tf.keras.layers.Dense(units=1, input_shape=[1])
#Capas densas son capas con neuronas conectadas a todas las neuronas siguientes
#"units=1" -> neuronas de salida (1) || "input_shape=[1]" ->neuronas de entrada

model = tf.keras.Sequential([layer])
#modelo secuencial, generalmente para redes neuronales simples


model.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    #Algoritmo Adam para entrenar
    #se da de parametro 0.1 (tasa de aprendizaje), dice que tanto ajustar los pesos y sesgos de cada neurona

    loss='mean_squared_error'
    #funcion de perdida, una poca cantidad de errores grandes es peor que una gran cantidad de errores pequeños
)

print("Proccessing...")


historial = model.fit(meters,yards, epochs=3000, verbose = False)
#(datos de entrada, datos de salida, epocas)


print("Successfully processed")

a = input("Enter a number to convert meters to yards: ")

print("Convert " + a + " to yards:\n\n")
a = float(a)

print(model.predict(x=np.array([a])))

#model.save('meters_to_yards.h5')
#model.save('meters_to_yards.json')
#model.save('meters_to_yards.bin')

