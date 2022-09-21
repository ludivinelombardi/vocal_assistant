import yaml
import numpy as np
import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical


data = yaml.safe_load(open('nlu/train.yml', 'r').read())
#print(data) 

## Lire les data

inputs, outputs = [], []

for command in data['commands']:
    #print(data)
    inputs.append(command['input'].lower()) 
    #print(inputs)
    outputs.append("{}/{}".format(command['entity'], command['action']))
    #print(outputs)


## CREATION DATASET 
#### level de tokenization : words, chars, bytes #####

# creation input data 
max_sent = max([len(x) for x in inputs])
#print(max_sent.shape) = 36

# creation arrays one-hot encoding (shape = nombre d'exemple, length des sequences et la taille du voc)
input_data = np.zeros((len(inputs), max_sent, 256), dtype='float32')

for i, inp in enumerate(inputs):
    for k, ch in enumerate(bytes(inp.encode('utf8'))): 
        input_data[i, k, int(ch)] = 1.0
#print(input_data[0].shape) 

labels = set(outputs)

fwrite = open('nlu/entities.txt', 'w', encoding='utf-8')
for label in labels:
    fwrite.write(label + '\n')
fwrite.close()

labels = open('nlu/entities.txt', 'r', encoding='utf-8').read().split('\n')

label2index = {}
index2label = {}

for k, label in enumerate(labels):
    label2index[label] = k 
    index2label[k] = label 
    
output_data = []

for output in outputs:
    output_data.append(label2index[output])
#print(output_data)

output_data = to_categorical(output_data, len(labels))


## CREATION DU MODEL DEEP LEARNING
model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(labels), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])
model.fit(input_data, output_data, epochs=256)
model.save('nlu/model.h5')