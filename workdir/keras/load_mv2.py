import os
import tensorflow as tf
from keras.applications import MobileNetV2

def main() -> None:

    model = MobileNetV2()
    model.save('/workdir/models/mobilenetv2.h5')


    return

if __name__ == '__main__':
    main()