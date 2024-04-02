import random
import time
NUM_SHEEP = 9
def main():
    t1 = time.time()
    win_counter = [0] * NUM_SHEEP
    for n in range(100000):
        
        # One round of all sheep dying
        forest = [True] * NUM_SHEEP
        i = 0
        while sum(forest) > 1:
            # One pass of wolf
            forest[i] = False
            direction = random.choice(["L", "R"])
            if direction == "L":
                i -= 1
                if i < 0:
                    i = NUM_SHEEP -1

            else:
                i += 1
                if i >= NUM_SHEEP:
                    i = 0
        
        win_counter[forest.index(True)] += 1
    print("Sheep that lived the longest the most often is: ", win_counter.index(max(win_counter)) )
    t2 = time.time()
    print("Time: ", (t2-t1))
main()