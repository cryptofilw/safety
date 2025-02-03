from cryptography.fernet import Fernet
import time
from datetime import datetime


def create_file():

    time.sleep(1)
    file_name = input('Введите название файла, который хотите создать (включая ".txt"): ')
    while not file_name.endswith(".txt"):
        file_name = input('Введите название файла (Обязательно включая ".txt"): ')

    file_text = input('Введите текст, который хотите вписать в файл (ту самую приватную информацию): ')

    # Создаём файл
    with open(f'{file_name}', 'w') as file:
        file.write(f"{file_text}")
        print(f'Новый файл "{file_name}" создан')
    time.sleep(1)

    # Зашифровать?
    print(f'Желаете зашифровать файл "{file_name}"? 1. Да 2. Нет')
    choose_2 = int(input('Ваш выбор (1 или 2): '))
    while choose_2 > 3 or choose_2 < 0:
        choose_2 = int(input('Введите цифру 1 или 2: '))

    # Да, зашифровать файл
    if choose_2 == 1:

        with open(f'{file_name}', 'rb') as file:
            file_text_b = file.read()

        # Процесс шифрования
        key = Fernet.generate_key()
        cipher = Fernet(key)
        encrypted_text = cipher.encrypt(file_text_b)

        # Создание зашифрованного файла
        encrypted_file_name = file_name[0:-4]+'_encrypted.txt'
        with open(f'{encrypted_file_name}', 'wb') as file:
            file.write(encrypted_text)
        print(f'Содержимое файла "{file_name}" успешно зашифровано в новый файл "{encrypted_file_name}"')
        time.sleep(1)

        # Создание файла с ключом для расшифровки
        key_file_name = file_name[0:-4]+'_key.txt'
        with open(f'{key_file_name}', 'w') as file:
            file.write(f'Ключ для расшифровки файла "{encrypted_file_name}" сохранён ниже:\n\n{key.decode()}\n\nФайл "{encrypted_file_name}" был зашифрован в это время: {datetime.now().replace(microsecond=0)}')
        print(f'Ключ для расшифровки файла "{encrypted_file_name}" сохранён в файл "{key_file_name}"')
        time.sleep(2)
        print(f'\nОригинальный файл - "{file_name}"\nЗашифрованный файл -"{encrypted_file_name}"\nКлюч - "{key_file_name}"')
        time.sleep(5)
        print('Шифрование завершено')


    # Нет, не шифровать файл
    if choose_2 == 2:
        print('Вы выбрали не шифровать созданный файл')
        time.sleep(1)



def encrypt_file():

    # Выбираем и открываем файл
    time.sleep(1)
    file_name = input('Введите название файла, который хотите зашифровать (включая ".txt"): ')
    while not file_name.endswith(".txt"):
        file_name = input('Введите название файла (Обязательно включая ".txt"): ')

    with open(f'{file_name}', 'rb') as file:
        file_text_b = file.read()
    time.sleep(1)

    # Процесс шифрования
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(file_text_b)

    # Создание зашифрованного файла
    encrypted_file_name = file_name[0:-4] + '_encrypted.txt'
    with open(f'{encrypted_file_name}', 'wb') as file:
        file.write(encrypted_text)
    print(f'Содержимое файла "{file_name}" успешно зашифровано в новый файл "{encrypted_file_name}"')
    time.sleep(1)

    # Создание файла с ключом для расшифровки
    key_file_name = file_name[0:-4] + '_key.txt'
    with open(f'{key_file_name}', 'w') as file:
        file.write(f'Ключ для расшифровки файла "{encrypted_file_name}" сохранён ниже:\n\n{key.decode()}\n\nФайл "{encrypted_file_name}" был зашифрован в это время: {datetime.now().replace(microsecond=0)}')

    print(f'Ключ для расшифровки файла "{encrypted_file_name}" сохранён в файл "{key_file_name}"')
    time.sleep(2)
    print(f'\nОригинальный файл - "{file_name}"\nЗашифрованный файл -"{encrypted_file_name}"\nКлюч - "{key_file_name}"')
    time.sleep(5)
    print('Шифрование завершено')



def decrypt_file():

    # Выбираем и открываем файл
    file_name = input('Введите название файла, который хотите расшифровать (включая ".txt"): ')
    while not file_name.endswith(".txt"):
        file_name = input('Введите название файла (Обязательно включая ".txt"): ')

    with open(f'{file_name}', 'rb') as file:
        encrypted_text = file.read()

    # Начало расшифровки
    key_for_decode = input(f'Введите ключ для расшифровки файла "{file_name}": ')
    cipher = Fernet(key_for_decode)
    decrypted_text = cipher.decrypt(encrypted_text).decode()
    time.sleep(1)

    # Файл расшифрован
    print(f'Содержимое файла:\n{decrypted_text}\n')
    time.sleep(1)

    # Сохранение файла
    print('Желаете сохранить содержимое в отдельный файл? 1. Да 2. Нет')
    new_file = int(input('Ваш выбор (1 или 2): '))
    while new_file < 0 or new_file > 3:
        new_file = int(input('Введите цифру 1 или 2: '))

    # Создание файла
    if new_file == 1:
        name = input('Введите имя нового файла (включая ".txt"): ')
        with open(name, 'w') as file:
            file.write(decrypted_text)
        time.sleep(1)
        print(f'Файл "{name}" сохранён')
        print(f'\nЗашифрованный файл - "{file_name}"\nРасшифрованный файл - "{name}"')



def function():

    try:
        print('Выберите, что хотите сделать:\n1. Создать файл\n2. Зашифровать файл\n3. Расшифровать файл')
        user_choose = int(input('Введите цифру (1, 2, или 3): '))

        while user_choose > 3 or user_choose < 1:
            user_choose = int(input('Введите цифру (1, 2, или 3): '))

        if user_choose == 1:
            create_file()
        elif user_choose == 2:
            encrypt_file()
        elif user_choose == 3:
            decrypt_file()

    # Ошибки
    except FileNotFoundError:
        print(f"Ошибка: такого файла нету в папке safety. Попробуйте снова.")
    except Exception as ex:
        print(f'Ошибка: {ex}')


    finally:
        print('\nПрограмма завершена')