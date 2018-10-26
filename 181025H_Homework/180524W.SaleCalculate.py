# Name: 180529T.While_Loop_Even.py

import random, pprint

sales = [[random.randint(0,100) for col in range(7)] for row in range (10)]
# 'pip3 install pprint' to get pprint
pprint.pprint(sales)

def salesCalculate(matrix,start_row,start_col,end_row,end_col):
    # get total for week a
    first_week_total = 0
    inbetween_total = 0
    last_week_total = 0
    # fees for weekdays + weekends
    fee = [2,10]
    # get total for the start week
        for col in range(start_col, 7):
            # if weekday
            if col < 5:
                first_week_total = first_week_total + matrix[row][col] * fee[0]
            # if weekend
            else:
                inbetween_total = inbetween_total + matrix[row][col] * fee[1]
        print('total for first week:',first_week_total)

        # get total for all weeks inbetween
        for row in range(start_row + 1, end row): # because of how python works, no -1 is needed
            for col in range(7):
                print(matrix[row][col])
                if col < 5:
                    inbetween_total = inbetween_total + matrix[row][col] * fee[0]
                else:
                    inbetween_total = inbetween_total + matrix[row][col] * fee[1]
        print('total for inbetween', inbetween_total)
