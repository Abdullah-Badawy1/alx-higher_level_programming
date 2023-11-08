def weight_average(my_list=[]):
    total_weight = 0
    weighted_sum = 0

    if not my_list:
        return 0

    for item in my_list:
        total_weight += item[1]
        weighted_sum += item[0] * item[1]

    return weighted_sum / total_weight
