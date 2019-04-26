from scipy.special import comb
import time


# Calculates the roll probability of one number
def calculate_roll_probability(num_dice, max_die_value, desired_roll_sum):
    n = desired_roll_sum - num_dice
    k = num_dice - 1
    t = (max_die_value * num_dice - num_dice) // max_die_value
    valid_combinations = 0
    total_combinations = max_die_value**num_dice
    for i in range(t+1):
        valid_combinations += (-1)**i * comb(num_dice, i) * comb(n - max_die_value*i + k, k)
    return valid_combinations / total_combinations


# Calculates the winning probability for player 1.
def calculate_winning_probability(player1, player2):
    player1_winning_probability = 0
    player2_probability = {}
    for n in range(player2['num_dice'], player2['num_dice']*player2['max_die_value'] + 1):
        player2_probability[n] = calculate_roll_probability(player2['num_dice'], player2['max_die_value'], n)
    for n in range(player1['num_dice'], player1['num_dice']*player1['max_die_value'] + 1):
        player2_filtered = {k: v for (k, v) in player2_probability.items() if k < n}
        player2_probability_sum = sum(player2_filtered.values())
        player1_winning_probability += calculate_roll_probability(player1['num_dice'], player1['max_die_value'], n) \
            * player2_probability_sum
    return player1_winning_probability


if __name__ == '__main__':
    player1_gregor = {'num_dice': 8, 'max_die_value': 5}
    player2_oberyn = {'num_dice': 4, 'max_die_value': 10}
    start_time = time.time()
    answer = calculate_winning_probability(player1_gregor, player2_oberyn)
    end_time = time.time()
    print("Probability of Gregor winning: {}, Time: {} seconds".format(answer, end_time - start_time))
