from ipaddress import ip_address
import platform
from subprocess import Popen, PIPE
from threading import Thread
import queue
from tabulate import tabulate


def host_ping(user_ip, results):
    # Функция пинга
    param = "-n" if platform.system().lower() == 'windows' else "-c"
    command = ["ping", param, "1", str(user_ip)]
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    code = process.wait()
    if code == 0:
        results.put([str(user_ip), 'Доступен'])
    else:
        results.put([str(user_ip), 'Недоступен'])


def host_range_ping():
    # Ввод данных
    use_ip_str = input("Введите IP-адрес: ")
    use_ip = ip_address(use_ip_str)
    use_ip_str = use_ip_str.split('.')
    range_list_max = 256 - int(use_ip_str[-1])
    range_list = int(input(f"Введите диапазон проверки (max диапазон для данного IP:{range_list_max}): "))

    # Проверка диапазона
    if range_list > range_list_max:
        range_list = range_list_max
        print('Введенный диапазон проверки выше размера одного октета.\nДиапазон изменен на максимальный.')

    output = []
    result = queue.Queue()

    for i in range(range_list):
        index = Thread(target=host_ping, args=(use_ip, result))
        index.start()
        use_ip += 1

    for i in range(range_list):
        output.append(result.get())

    columns = ['IP', 'Статус']
    print(tabulate(output, headers=columns))


host_range_ping()
