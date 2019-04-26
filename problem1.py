import numpy as np
import time


# Number of combinations using coins in array unob_coins that come to the total. D is the reference array to store answers
def change_combinations(unob_coins, total, D):
    if (len(unob_coins) == 0 and total >= 1) or total < 0:
        return 0
    i = unob_coins.index(unob_coins[-1])
    if D[i, total] != -1:
        return D[i, total]
    if total == 0:
        return 1
    num_combinations = change_combinations(unob_coins[:-1], total, D) + change_combinations(unob_coins, total - unob_coins[-1], D)
    D[i, total] = num_combinations
    return num_combinations


def bootstrap_combinations(unob_coins, total):
    D = np.array(range(len(unob_coins) * (total + 1))).reshape((len(unob_coins), (total + 1)))
    D[:] = -1
    return change_combinations(unob_coins, total, D)


if __name__ == '__main__':
    start_time = time.time()
    answer = bootstrap_combinations([1, 5, 10, 20, 50, 100], 500)
    end_time = time.time()
    print("Combinations: {}, Time: {} seconds".format(answer, end_time-start_time))
