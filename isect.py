from pprint import pprint as pp
from pprint import pformat as pf

from sklearn import metrics

# ours
import isect

# mine
from data_maker import make_random_data



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser("Test isect")
    args = parser.parse_args()

    data, labels = make_random_data()
    #print('data') # debug
    #pp(data) # debug
    #print('labels') # debug
    #pp(labels) # debug
    pred, cluster_info = isect.run(data)
    print('pred') # debug
    pp(pred) # debug
    print('cluster_info') # debug
    pp(cluster_info) # debug
    print("zip style")
    for cluster_idx, score in pred:
        print("  ", cluster_idx, score, cluster_info[cluster_idx]) # debug
    score = metrics.homogeneity_completeness_v_measure(labels, [cluster_idx for cluster_idx, score in pred])
    print("(homogeneity, completeness, v_measure)")
    print(score)


    print('\33[32m' + 'end' + '\033[0m')

