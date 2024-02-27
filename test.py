# count dimensions of each line in bill_embeddings.jsons
import numpy as np
with open('bill_embeddings.jsons', 'r') as f:
    lines = f.readlines()
    for line in lines:
        embedding = eval(line)['embedding']        
        print(np.shape(embedding))