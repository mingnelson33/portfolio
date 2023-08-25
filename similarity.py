import numpy as np


# SIMILARITY_THRESHOLD = .5


# code adapted from https://www.analyticsvidhya.com/blog/2021/02/a-simple-guide-to-metrics-for-calculating-string-similarity/
def levenshtein(s1, s2):
    # ensure inputs are strings
    s1 = str(s1)
    s2 = str(s2)
    # initialize matrix
    size1 = len(s1) + 1
    size2 = len(s2) + 1
    matrix = np.zeros((size1, size2))

    for i in range(size1):
        matrix[i, 0] = i
    
    for i in range(size2):
        matrix[0, i] = i
    
    # perform algorithm
    for i in range(1, size1):
        for j in range(1, size2):
            left_diag = matrix [i-1, j-1]
            left_adj = matrix[i-1, j]
            above = matrix[i, j-1]
            if s1[i-1] == s2[j-1]:
                matrix[i, j] = min(left_adj + 1, left_diag, above + 1)
            else:
                matrix[i, j] = min(left_adj + 1, left_diag + 1, above + 1)
    return matrix[size1-1, size2-1]


def str_similarity(s1, s2):
    if s1 == s2: return 1
    lev_score = levenshtein(s1, s2)
    longer_one = max(len(str(s2)), len(str(s2)))
    score = (longer_one - lev_score) / longer_one
    return score if score >= 0 else 0


def num_similarity(n1, n2):
    n1 = float(n1)
    n2 = float(n2)
    if n1 == n2: return 1
    if n1 == 0 or n2 == 0: return 0
    score = float(min(n1, n2)) / float(max(n1, n2))
    return score if score >= 0 else 0


def bool_similarity(b1, b2):
    return 1 if float(b1) == 1.0 and float(b2) == 1.0 else 0


def get_similarity(t1, t2, type='str'):
    if type == 'num': return num_similarity(t1, t2)
    elif type == 'bool': return bool_similarity(t1, t2)
    else: return str_similarity(t1, t2)
    