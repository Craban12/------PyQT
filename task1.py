import platform
from subprocess import Popen, PIPE


def host_ping(ip_list):
    for url in ip_list:
        param = "-n" if platform.system().lower() == 'windows' else "-c"
        command = ["ping", param, "2", url]
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        code = process.wait()
        if code == 0:
            print(url + ' || ' + 'Узел доступен')
            print(50 * '=')
        else:
            print(url + ' || ' + 'Узел недоступен')
            print(50 * '=')


testing_list = ['ya.ru', 'google.com', 'a', '192.168.1.1', '127.0.0.1', '8.8.8.8']
host_ping(testing_list)
