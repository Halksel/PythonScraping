from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np
from typing import List

categories: List[str] = [
    "chair", "camera", "butterfly", "elephant", "flamingo"
]
nb_classes: int = len(categories)

image_w: int = 64
image_h: int = 64

X_train, X_test, y_train, y_test = np.load("./image/5obj.npy")
X_train = X_train.astype("float") / 256
X_test = X_test.astype("float") / 256

print('X_train shape:', X_train.shape)

model:Sequential = Sequential()
model.add(
    Convolution2D(32, 3, 3, border_mode='same', input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Convolution2D(64, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(
    loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=32, nb_epoch=50)

score = model.evaluate(X_test, y_test)
print(score[0])
print(score[1])
