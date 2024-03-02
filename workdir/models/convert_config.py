import os
import json

import tensorflow as tf
from keras.models import Model
import keras


def main() -> None:

    model = keras.models.load_model('/workdir/models/mobilenetv2.h5')
    model.summary()

    config = model.get_config()

    with open('/workdir/mobilenetv2.json', 'w') as f:
        json.dump(config, f, indent=2)


    return


if __name__ == '__main__':
    main()