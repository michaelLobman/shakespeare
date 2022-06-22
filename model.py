from ntpath import join
import tensorflow as tf
import numpy as np
import re

# Open plain text file, split the file into "sonnets" on their delineating number.

text = open('./downloads/sonnets.txt').read()
sonnets = re.split('[0-9]', text)
sonnets = [sonnet.strip() for sonnet in sonnets[1:]]

# Split each sonnet into a 1D list of its respective lines. Strip whitespace, remove 

split_sonnets = list()

for sonnet in sonnets:
    split = sonnet.split('\n')
    updated_sonnet = list()
    for line in split:
        stripped = line.strip()
        if stripped:
            updated_sonnet.append(line.strip())
    if updated_sonnet:
        split_sonnets.append(updated_sonnet)

# Remove sonnets from data that do not conform to standard 14-line pattern.
# Generate vocab

vocab = set()
for sonnet in split_sonnets:
    if len(sonnet) != 14:
        split_sonnets.remove(sonnet)
    else:
        for line in sonnet:
            for c in line:
                vocab.add(c)

# Join individual sonnets on a newline character

joined_sonnets = list()

for sonnet in split_sonnets:
    joined_sonnets.append('\n'.join(sonnet))
print(joined_sonnets[10])

# Convert sonnets to tensor (shape=152, 14)

# might not want this as a tensor

# sonnets_tensor = tf.convert_to_tensor(split_sonnets)
# flattened_tensor = tf.reshape(split_sonnets, [-1])

# MAX LINE IS 59 characters. Will need to pad lines to 60 characters?

# Encode text.
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

# Below does not work. Need a way to encode the text.
# May have to allow the line breaks? 
# can join the split sonnets on them! yes, join with a '\n'

# def text_to_int(sonnet_list):
#     for sonnet in sonnet_list:
#         for line in sonnet:
#             return np.array([char2idx[c] for c in line])

# text_as_int = text_to_int(split_sonnets)

# print(text_as_int)
# # Create function to decode text.



# divide data into train and test groups
