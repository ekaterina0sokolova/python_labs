import matplotlib.pyplot as plt
import re
from datetime import datetime
import datetime as dt


def get_data(path):
    pattern = r'B00000000004 <--->.*?KEEP pressure=(\d+),gard=(\d+\.\d+)'
    results = []

    with open('n_log2.txt', 'r') as file:
        for line in file:
            match = re.search(pattern, line)
            if match:
                results.append({
                    'time_stamp': datetime.strptime(line[:8], '%H:%M:%S'),
                    'pressure': match.group(1),
                    'gard': match.group(2)
                })

    return results


def process_data(data_list):
    first_timestamp_in_split = data_list[0]["time_stamp"]
    pressure_items_count = 1
    pressure_sum = int(data_list[0]["pressure"])
    gard_items_count = 1
    gard_sum = float(data_list[0]["gard"])
    processed_data = []

    for i in range(1, len(data_list)):
        if data_list[i]["time_stamp"] - first_timestamp_in_split < dt.timedelta(minutes=10):
            pressure_items_count += 1
            pressure_sum += int(data_list[i]["pressure"])

            gard_items_count += 1
            gard_sum += float(data_list[i]["gard"])
        else:
            # записываем полученные значения в processed_data
            processed_data.append([first_timestamp_in_split, pressure_sum/pressure_items_count, gard_sum/gard_items_count])
            first_timestamp_in_split = data_list[i]["time_stamp"]
            pressure_items_count = 1
            pressure_sum = int(data_list[i]["pressure"])
            gard_items_count = 1
            gard_sum = float(data_list[i]["gard"])

    return processed_data


def draw_graphics(data):
    timestamps = [i for i in range(len(data))]
    pressure = [point[1] for point in data]
    gard = [point[2] for point in data]

    plt.figure(figsize=(14, 6))

    # график для pressure
    plt.subplot(1, 2, 1)
    plt.plot(timestamps, pressure, marker='o', label='pressure', color='blue')
    plt.xlabel('time')
    plt.ylabel('pressure')
    plt.title('График для параметра pressure')
    plt.legend()
    plt.grid()

    # график для gard
    plt.subplot(1, 2, 2)
    plt.plot(timestamps, gard, marker='o', label='gard', color='orange')
    plt.xlabel('time')
    plt.ylabel('gard')
    plt.title('График для параметра gard')
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.show()


def main():
    result = get_data('n_log2.txt')
    processed_data = process_data(result)
    draw_graphics(processed_data)


if __name__ == '__main__':
    main()
