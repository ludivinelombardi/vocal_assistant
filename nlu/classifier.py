from tensorflow.keras.models import load_model
import numpy as np

labels = open('nlu/entities.txt', 'r', encoding='utf-8').read().split('\n')
model = load_model('nlu/model.h5')

label2index = {}
index2label = {}

for k, label in enumerate(labels):
    label2index[label] = k 
    index2label[k] = label 

def classify(text):
    #creation d'un input array
    x = np.zeros((1, 36, 256), dtype='float32')
    
    #remplir l'array x avec les data de input text
    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0 
    
    out = model.predict(x)
    idx = out.argmax()
    print('Text: "{}" est classifié comme "{}"'.format(text, index2label[idx]))
    return index2label[idx]

if __name__ == '__main__':
    while True:
        text = input('Entrer du texte:')
        classify(text)  