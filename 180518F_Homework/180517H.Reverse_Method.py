#Name: 180517H.Reverse_Method.py

newstray = []

def reversestray(str): #todo dequeue then push
    for outLoop in str:
        for inLoop in str:
            test_arr = []
            if str == test_arr:
                print("stray reversed")
                return newstray
            elif ( str != test_arr ):
                oldItem = str[0]
                minusLast = str.pop[0]
                newstray.extend(oldItem)


reversestray(["5", "8", "4", "2", "9"])
