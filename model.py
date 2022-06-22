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

for sonnet in split_sonnets:
    if len(sonnet) != 14:
        split_sonnets.remove(sonnet)

# Join individual sonnets on a newline character

joined_sonnets = list()
for sonnet in split_sonnets:
    joined_sonnets.append('\n'.join(sonnet))

# Generate vocab set

vocab = set()
for sonnet in joined_sonnets:
    for c in sonnet:
        vocab.add(c)

# Encode sonnets.

char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

def text_to_int(text):
    return np.array([char2idx[c] for c in text])

encoded_sonnets = list(map(text_to_int, joined_sonnets))

# divide data into train and test groups

