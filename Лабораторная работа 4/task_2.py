

import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None: #считывание
    data = []
    with open(INPUT_FILENAME, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')  # разделитель по умолчанию ','
        for row in csv_reader:
            data.append(row)
    #отступ4
    json_output = json.dumps(data, indent=4, ensure_ascii=False)
    #запись
    with open(OUTPUT_FILENAME, mode='w', encoding='utf-8') as json_file:
        json_file.write(json_output)


if __name__ == '__main__':
    task()
    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        for line in output_f:
            print(line, end="")