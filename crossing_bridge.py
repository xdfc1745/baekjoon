
import queue


def solution(bridge_length, weight, truck_weights):
    time = 0
    w = 0
    i = 0 
    d = queue.Queue()

    while True:
        time += 1
        # print(i, d)
        if d.qsize() == bridge_length:
            w -= d.get()

        if w + truck_weights[i] <= weight:
            if i == len(truck_weights)-1:
                time += bridge_length
                break
            d.put(truck_weights[i])
            w += truck_weights[i]
            i += 1
        else:
            d.put(0)
    return time