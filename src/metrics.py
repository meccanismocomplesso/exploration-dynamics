import numpy as np

def coverage(positions):
    flat = positions.reshape(-1, 2)
    return np.std(flat[:,0]) + np.std(flat[:,1])

def entropy(positions, bins=10):
    flat = positions.reshape(-1, 2)
    hist, _ = np.histogramdd(flat, bins=bins)
    prob = hist / np.sum(hist)
    prob = prob[prob > 0]
    return -np.sum(prob * np.log(prob))
