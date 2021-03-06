 # time : 2019/4/8
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tensorflow as tf

state = tf.Variable(0, name='count')
one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))
