from ipaddress import ip_address
import platform
from subprocess import Popen, PIPE
from threading import Thread


def host_ping(use_ip):
    param = "-n" if platform.system().lower() == 'windows' else "-c"
    command = ["ping", param, "1", str(use_ip)]
    process = Popen(command, stdout=PIPE, stderr=PIPE)
    code = process.wait()
    if code == 0:
        print(str(use_ip) + ' | Доступен')
    else:
        print(str(use_ip) + ' | Недоступен')


def host_range_ping():
    use_ip_str = input("Введите IP-адрес: ")
    use_ip = ip_address(use_ip_str)
    use_ip_str = use_ip_str.split('.')
    # print(use_ip_str)
    range_list_max = 256 - int(use_ip_str[-1])
    range_list = int(input(f"Введите диапазон проверки (max диапазон для данного IP:{range_list_max}): "))

    if range_list > range_list_max:
        range_list = range_list_max
        print('Введенный диапазон проверки выше размера одного октета.\nДиапазон изменен на максимальный.')

    for i in range(range_list):
        flow = Thread(target=host_ping, args=(use_ip,))
        flow.start()
        use_ip += 1


host_range_ping()
