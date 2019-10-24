import os
import tensorflow as tf

from kubeflow import fairing
# Setting up google container repositories (GCR) for storing output containers
# You can use any docker container registry istead of GCR
DOCKER_REGISTRY = 'index.docker.io/brightfly/fairing'
fairing.config.set_builder(
    'append',
    base_image='tensorflow/tensorflow:1.13.1-py3',
    registry=DOCKER_REGISTRY,
    push=True)
fairing.config.set_deployer('job')


def train():
    hostname = tf.constant(os.environ['PATH'])
    sess = tf.Session()
    print(sess.run(hostname))

if __name__ == '__main__':
    print('local train()')
    train()
    print('remote train()')
    remote_train = fairing.config.fn(train)
    remote_train()