# Открываем входной файл для чтения и выходной файл для записи
with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
    # Проходим по каждой строке файла
    for line in infile:
        # Убираем возможные пробелы и символы новой строки
        binary_code = line.strip()
        
        # Конвертируем двоичный код в шестнадцатеричный
        hex_code = hex(int(binary_code, 2))[2:].upper()
        
        # Записываем результат в файл, добавляя перенос строки
        outfile.write(hex_code + '\n')

print("Конвертация завершена. Результаты сохранены в 'output.txt'.")
