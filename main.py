import os

os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"

import keras
import numpy as np
from tqdm import tqdm
from keras.models import Model
from keras.layers import Dense, Dropout, Input
from keras.optimizers import Adam, RMSprop
from keras.callbacks import ModelCheckpoint
import keras.backend as K
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from random import shuffle

x_data = np.load('x_data.npy')
y_data = np.load('y_data.npy')

print(x_data.shape, y_data.shape)

def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

def odds_loss(x_data):


    def loss(y_true, y_pred):
        if x_data == None:
            return K.zeros_like(y_true)

        odds_a = x_data[:, 0:1]
        odds_x = x_data[:, 1:2]
        odds_b = x_data[:, 2:3]
        print(odds_a)
        win_home_team = y_true[:, 0:1]
        win_home_or_draw = y_true[:, 1:2]
        draw = y_true[:, 2:3]
        win_away = y_true[:, 3:4]
        win_away_or_draw = y_true[:, 4:5]
        no_bet = y_true[:, 5:6]

        gain_loss_vector = K.concatenate([win_home_team * (odds_a - 1) + (1 - win_home_team) * -1,
          win_home_or_draw * (1/(1 -1/odds_b) - 1) + (1 - win_home_or_draw) * -1,
          win_away * (odds_b - 1) + (1 - win_away) * -1,
          win_away_or_draw * (1/(1 -1/odds_a) - 1) + (1 - win_away_or_draw) * -1,
          draw * (odds_x - 1) + (1 - draw) * -1,
          K.zeros_like(odds_a)], axis=1)
        return -1 * K.mean(K.sum(gain_loss_vector * y_pred, axis=1))

    return loss

def create_model():


    inputs = Input(shape  = (x_data.shape[1],))
    layer1 = Dense(15, activation='relu')(inputs)
    drop1 = Dropout(0.1)(layer1)
    layer2 = Dense(10, activation='relu')(drop1)
    drop2 = Dropout(0.1)(layer2)
    predictions = Dense(y_data.shape[1], activation='softmax')(drop2)
    model = Model(inputs=inputs, outputs=predictions)

    return model

def main_train():
    global x_data, y_data
    x_data, y_data = unison_shuffled_copies(x_data, y_data)
    print(x_data.shape, y_data.shape)
    model = create_model()
    print(model.summary())

    filepath="model_saves/weights-improvement-{epoch:02d}-{val_loss:.2f}.hdf5"
    checkpoint = ModelCheckpoint(filepath, monitor='val_loss', verbose=0, save_best_only=True, mode='min')

    optimizer = Adam(lr = 0.0005)
    model.compile(loss = odds_loss(model.layers[0].output), optimizer = optimizer)

    val_history = model.fit(x_data, y_data, batch_size=16, epochs=70, validation_split=0.15 ,verbose=1, callbacks = [checkpoint])

    plt.subplot(1,2, 1)
    plt.grid(color='r',alpha = 0.2, linestyle='-', linewidth=1)
    plt.plot(val_history.history['loss'])
    plt.title('train loss')
    plt.ylabel('loss')
    plt.xlabel('epochs')

    plt.subplot(1, 2, 2)
    plt.grid(color='r',alpha = 0.2, linestyle='-', linewidth=1)
    plt.plot(val_history.history['val_loss'])
    plt.title('val loss')
    plt.ylabel('loss')
    plt.xlabel('epochs')

    plt.show()

def main_val():
    global x_data, y_data
    x_data, y_data = unison_shuffled_copies(x_data, y_data)
    print(x_data.shape, y_data.shape)
    model = create_model()
    print(model.summary())

    model.load_weights('model_saves/0.18_save.hdf5')

    optimizer = Adam(lr = 0.0005)
    model.compile(loss = odds_loss(model.layers[0].output), optimizer = optimizer)

    history = model.evaluate(x_data, y_data, verbose = 1)

    print(history)


if __name__ == "__main__":
    main_val()
