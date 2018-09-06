The modules in this repository use TensorFlow to predict words. To be specific, they train a neural network with words out of a short story by H.P. Lovecraft. The module in rnn_lovecraft.py uses a general recurrent neural network (RNN), the module in lstm_lovecraft.py uses a Long Short-Term Memory (LSTM) network, and the module in gru_lovecraft.py uses a Gated Recurrent Unit (GRU) network.

## Operation

Each of the three modules starts by reading the content of lovecraft.txt into a string. Then they split the string into words and associate each word with a number determined by the word's frequency. The most common word is associated with 0, the next most common word is associated with 1, and so on.

After obtaining an array of numbers corresponding to the words, each module creates an RNN cell with 600 hidden layers. Then it calls `tf.nn.static_rnn`, which provides the RNN's output values. To determine loss, the module multiplies the RNN's outputs by a matrix of weights and adds biases to the products. Then it creates an `AdagradOptimizer` to minimize the loss.

For each training run, the application assembles a batch containing ten (`batch_size`) sequences of six (`input_size`) values each. As a result, the network can only recognize dependencies between at most six consecutive words. For each six-value sequence, the desired label is the seventh value, which represents the desired word to be produced.

These modules don't perform a fixed number of training runs. Instead, they continue training until the prediction accuracy exceeds 95 percent. For every thousand training runs, the application prints the prediction accuracy.

## Obtaining and Running

You can obtain the source files for this project by cloning the repository:

```git clone https://github.com/mattscar/nlp_lovecraft```

To run the modules, you need to install TensorFlow. If you have pip, you can run the following command:

```pip install tensorflow```

Then you can execute the modules normally:

```
python rnn_lovecraft.py
python lstm_lovecraft.py
python gru_lovecraft.py
```

In my experiments, the GRU network achieves better accuracy than the RNN or LSTM based networks.

