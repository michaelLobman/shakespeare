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

# MAX LINE IS 59 characters. Will need to pad lines to 60 characters.

# create vocab set.

# divide data into train and test groups
