import tensorflow as tf

def prelu(_x, scope=''):
    """parametric ReLU activation"""
    with tf.variable_scope(name_or_scope=scope, default_name="prelu"+scope):
        _alpha = tf.get_variable("prelu_"+scope, shape=_x.get_shape()[-1],
                                 dtype=_x.dtype, initializer=tf.constant_initializer(0.1))
        return tf.maximum(0.0, _x) + _alpha * tf.minimum(0.0, _x)
def prelu2(_x, scope=''):
    """parametric ReLU activation"""
    with tf.variable_scope(name_or_scope=scope, default_name="prelu"+scope):
        _alpha = tf.get_variable("prelu_"+scope, shape=_x.get_shape()[-1],
                                 dtype=_x.dtype, initializer=tf.constant_initializer(0.1))
        return tf.maximum(0.0, _x) + _alpha * tf.minimum(0.0, _x)
def dice(_x,axis=-1,epsilon=0.000000001,name=""):
    with tf.variable_scope(name,reuse=tf.AUTO_REUSE):
        alphas = tf.get_variable('alpha'+name,_x.get_shape()[-1],initializer=tf.constant_initializer(0.0),dtype=tf.float32)
        input_shape = list(_x.get_shape())

        reduction_axis = list(range(len(input_shape)))
        del reduction_axis[axis]
        broadcast_shape = [1] * len(input_shape)
        broadcast_shape[axis] = input_shape[axis]

    mean = tf.reduce_mean(_x, axis=reduction_axis)
    brodcast_mean = tf.reshape(mean, broadcast_shape)
    std = tf.reduce_mean(tf.square(_x - brodcast_mean) + epsilon, axis=reduction_axis)
    std = tf.sqrt(std)
    brodcast_std = tf.reshape(std, broadcast_shape)
    x_normed = (_x - brodcast_mean) / (brodcast_std + epsilon)
    # x_normed = tf.layers.batch_normalization(_x, center=False, scale=False)
    x_p = tf.sigmoid(x_normed)

    return alphas * (1.0 - x_p) * _x + x_p * _x



def concat_all(a,b,c,d,idx):
    t1 = tf.concat([a,b],axis=idx)
    t2 = tf.concat([c,d],axis=idx)
    return tf.concat([t1,t2],axis=idx)