import tensorflow as tf
import numpy as np
import re

text = open('./downloads/sonnets.txt').read()
sonnets = re.split('[0-9]', text)
sonnets = [sonnet.strip() for sonnet in sonnets[1:]]

sonnets_tensor = tf.convert_to_tensor(sonnets)

# i think I need to use a map function here
# first, see the shape of the tensor, I think it's one long stream...
# first may want to divide it into each sonnet, flat tensor of shape 1 with 154 sonnets
# next, apply  amapy to each tensor, or mess with its shape, reshape it to 154 tensors of shape 15


# Below code makes each sonnet a list

# sonnet_list = list()

# for sonnet in sonnets:
#     split = sonnet.split('\n')
#     updated_sonnet = list()
#     for line in split:
#         stripped = line.strip()
#         if stripped:
#             updated_sonnet.append(line.strip())
#     if updated_sonnet:
#         sonnet_list.append(updated_sonnet)

# sonnet_tensor = tf.convert_to_tensor(sonnet_list)
# print(sonnet_tensor)

# max = 0
# for sonnet in sonnet_list:
#     for line in sonnet:
#         if len(line) > max:
#             max = len(line)
# print(max)



# MAX LINE IS 59 characters. Will need to pad lines to 60 characters/

# first, divide sonnet_list into train and test data, I believe...?

# vocab = set()
# for sonnet in sonnet_list:
#     for line in sonnet:
#         words = line.split()
#         for word in words:
#             vocab.add(word)

# vocab = sorted(vocab)

# word2idx = {u:i for i, u in enumerate(vocab)}
# idx2word = np.array(vocab)

# def text_to_int(text):
#     return np.array([word2idx[w] for w in text])

# def int_to_text(ints):
#     try:
#         ints = ints.numpy()
#     except:
#         pass
#     return ''.join(idx2word[ints])








# for sonnet in formatted_sonnets:
#     updated_sonnet = ''
#     for line in sonnet:
#          updated_sonnet += line.strip()
#     sonnet_list.append(sonnet)

# split_sonnet = formatted_sonnets[0].split('\n')
# split_sonnet = [line.strip() for line in split_sonnet]
# print(split_sonnet)
# need to map now and strip each line? 
# for line in text:
#     if line.strip().startswith(NUMBERS):
#         continue
#     count += 1

#     if count >= 15:
#         break

#     print(line.strip())


# vocab = sorted(set(text))

# char2idx = {u: i for i, u in enumerate(vocab)}
# idx2char = np.array(vocab)

# def text_to_int(text):
#     return np.array([char2idx[c] for c in text])

# def int_to_text(ints):
#     try:
#         ints = ints.numpy()
#     except:
#         pass
#     return ''.join(idx2char[ints])

# text_as_int = text_to_int(text)
