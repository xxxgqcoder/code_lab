def DNN(
    name='dnn',
    hidden_units=[8, 8],
    activation='relu',
    norm_type='batch',
    regular=None,
    regular_lambda=1e-3,
    dropout=0.5,
):
    dnn = tf.keras.models.Sequential(name=name)

    # norm
    if norm_type == 'batch':
        dnn.add(tf.keras.layers.BatchNormalization(name=f"{task_names[i]}_BN"))
    elif norm_type == 'layer':
        dnn.add(tf.keras.layers.LayerNormalization(name=f"{task_names[i]}_LN"))
    else:
        pass

    # regular
    if regular == 'l1':
        regularizer = tf.keras.regularizers.L1(l1=regular_lambda)
    elif regular == 'l2':
        regularizer = tf.keras.regularizers.L2(l2=regular_lambda)
    else:
        regularizer = None

    for units in hidden_units:
        dnn.add(tf.keras.layers.Dense(
            units=units,
            activation=activation,
            kernel_initializer=tf.keras.initializers.VarianceScaling(),
            kernel_regularizer=regularizer,
        ))

    return dnn
