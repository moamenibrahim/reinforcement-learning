from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPool2D, Activation, Flatten
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.optimizers import Adam
from collections import deque
from custom_tensorboard import ModifiedTensorBoard


REPLAY_MEMORY_SIZE = 50_000


class DQNAgent:
    def __init__(self):
        #   Main model, gets trained every step
        self.model = self.create_model()

        #   Target model
        self.target_model = self.create_model()
        self.target_model.set_weights(self.model.get_weights())

        # An array with last n steps for training
        self.reply_memory = deque(maxlen=REPLAY_MEMORY_SIZE)

        # Custom tensorboard object
        self.tensorboard = ModifiedTensorBoard()

    def create_model(self):
        model = Sequential()
        # OBSERVATION_SPACE_VALUES = (10, 10, 3) a 10x10 RGB image.
        model.add(Conv2D(256, (3, 3), input_shape=env.OBSERVATION_SPACE_VALUES))
        model.add(Activation('relu'))
        model.add(MaxPool2D(pool_size=(2, 2)))
        model.add(Dropout(0, 2))

        model.add(Conv2D(256, (3, 3)))
        model.add(Activation('relu'))

        model.add(Flatten())
        model.add(Dense(64))

        # ACTION_SPACE_SIZE = how many choices (9)
        model.add(Dense(env.ACTION_SPACE_SIZE, activation='linear'))
        model.compile(loss="mse", optimizer=Adam(
            learning_rate=0.001), metrics=['accuracy'])
        return model
