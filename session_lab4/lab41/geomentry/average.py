def aveg_list (list):
    global sum
    sum = 0
    for num in list:
        sum = sum + num
    average = (sum / len (list))
    return average
