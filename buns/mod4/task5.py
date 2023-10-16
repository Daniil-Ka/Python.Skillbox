def calculate_letter_frequency(filename):
    letter_counts = dict()

    try:
        with open(filename, 'r') as file:
            for line in file:
                for char in line:
                    if char.isalpha():
                        letter_counts[char] = letter_counts.get(char, 0) + 1
    except FileNotFoundError:
        print(f'Файл не найден: {filename}')
        return None

    # Сортируем результаты по частоте встречаемости букв
    sorted_counts = sorted(letter_counts.items(), key=lambda x: (x[1], x[0]))
    return sorted_counts


def write_statistics_to_file(statistics, output_filename):
    try:
        with open(output_filename, 'w') as output_file:
            for item in statistics:
                output_file.write(f'{item[0]}: {item[1]}\n')
    except Exception as e:
        print('Ошибка при записи в файл.')
        raise e


input_filename = input('Имя файла: ') or 'input.txt'
output_filename = 'output.txt'

letter_statistics = calculate_letter_frequency(input_filename)

if letter_statistics:
    write_statistics_to_file(letter_statistics, output_filename)