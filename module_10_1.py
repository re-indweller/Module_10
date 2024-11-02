# Задача "Потоковая запись в файлы"

from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write(f"Какое-то слово № {i+1}\n")
        sleep(0.1)
    file.close()
    print(f"Завершилась запись в файл {file_name}")

time_start = datetime.now()

write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")

time_stop = datetime.now()
time_result = time_stop - time_start
print(f'Время работы функций {time_result}')

time_start2 = datetime.now()

thread_first = Thread(target=write_words, args=(10, 'example5.txt'))
thread_second = Thread(target=write_words, args=(30, 'example6.txt'))
thread_third = Thread(target=write_words, args=(200, 'example7.txt'))
thread_fourh = Thread(target=write_words, args=(100, 'example8.txt'))

thread_first.start()
thread_second.start()
thread_third.start()
thread_fourh.start()

thread_first.join()
thread_second.join()
thread_third.join()
thread_fourh.join()

time_stop2 = datetime.now()
time_result2 = time_stop2 - time_start2
print(f'Время работы функций {time_result2}')

print(f'Использование потоков быстрее функций на {time_result-time_result2} секунд')
