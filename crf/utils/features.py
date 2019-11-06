import numpy as np

def get_sign(x):
    if x > 0:
        return '+'
    elif x < 0:
        return '-'
    else:
        return ''

def word2features(word, features_dict, prefix=''):
    features = []
    for name, func in features_dict.items():
        name = prefix+name
        if not func:
            features.append(name)
        else:
            features.append(name + '=' + str(func(word)))
    return features

def generate_features(sentence, features, n_surrounding=1, surrounding_features={}):
    sentence_features = []
    for idx, word in enumerate(sentence):
        word_features = word2features(word, features)
        
        if idx == 0:
            word_features.append('BOS')
        elif idx == len(sentence) - 1:
            word_features.append('EOS')
        for offset in range(-n_surrounding, n_surrounding+1):
            if offset == 0 or idx+offset < 0 or idx+offset > len(sentence) - 1:
                continue
            word_features.extend(word2features(sentence[idx+offset],
                                               surrounding_features,
                                               prefix=f'{get_sign(offset)}{np.abs(offset)}:'))
        sentence_features.append(word_features)
    return sentence_features