import time

def bubble_sort_algo(data, draw_data, sort_speed):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['#22c777' if c == j or c == j + 1 else '#466df0' for c in range(len(data))])
                time.sleep(sort_speed)

    draw_data(data, ['#22c777' for c in range(len(data))])
