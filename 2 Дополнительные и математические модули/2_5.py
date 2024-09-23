import re


# Функция для извлечения значения volume из строки
def extract_volume(line):
    match = re.search(r'volume=(\d+)', line)
    if match:
        return int(match.group(1))  # Конвертируем значение в целое число
    return None


def main():
    f1_path = 'n_log1.txt'
    f2_path = 'n_log2.txt'
    output_path = 'out1.txt'

    volumes = []

    with open(f1_path, 'r', encoding='utf-8') as f1, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in f1:
            if 'KEEP' in line and 'volume=' in line:
                outfile.write(line)  # Записываем строку в выходной файл
                volume = extract_volume(line)
                if volume is not None:
                    volumes.append(volume)

    with open(f2_path, 'r', encoding='utf-8') as f2, open(output_path, 'w', encoding='utf-8') as outfile:
        for line in f2:
            if 'KEEP' in line and 'volume=' in line:
                outfile.write(line)  # Записываем строку в выходной файл
                volume = extract_volume(line)
                if volume is not None:
                    volumes.append(volume)

    if volumes:
        min_volume = min(volumes)
        max_volume = max(volumes)
        avg_volume = sum(volumes) / len(volumes)

        sum_mm = min_volume + max_volume + int(avg_volume)

        print(f'Минимальное volume: {min_volume}')
        print(f'Максимальное volume: {max_volume}')
        print(f'Среднее volume: {avg_volume}')
        print(sum_mm)


if __name__ == '__main__':
    main()