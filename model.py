import tensorflow as tf
import numpy as np
import re

# Open plain text file, split the file into "Sonnets" on their delineating number.

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

for sonnet in split_sonnets:
    if len(sonnet) != 14:
        split_sonnets.remove(sonnet)

# Convert sonnets to tensor (shape=152, 14)

sonnets_tensor = tf.convert_to_tensor(split_sonnets)

# MAX LINE IS 59 characters. Will need to pad lines to 60 characters.

# create vocab set.

# divide data into train and test groups
