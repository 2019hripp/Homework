def balance(left, right):
    left_weight = 0
    right_weight = 0
    for x in left:
        if (x == '!'):
            left_weight = (left_weight + 2)
        else:
            left_weight = (left_weight + 3)

    for y in right:
        if (y == '!'):
            right_weight = (right_weight + 2)
        else:
            right_weight = (right_weight + 3)

    if (left_weight > right_weight):
        return('left')
    elif (right_weight > left_weight):
        return('right')
    else:
        return('balance')

balance("!!","??")
