import paramiko, time

BUF_SIZE = 20000
TIMEOUT = 1

# Создаем объект — соединение по ssh
ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

host_ip = "10.31.70.209"
login = "restapi"
passwd = "j0sg1280-7@"
# Инициируем соединение по ssh
ssh_connection.connect(host_ip, username=login, password=passwd, look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()

session.send("\n")
session.recv(BUF_SIZE)
session.send("terminal length 0\n")
time.sleep(TIMEOUT)

session.send("\n")
session.recv(BUF_SIZE)
session.send("show run\n")
time.sleep(TIMEOUT*2)
s = session.recv(BUF_SIZE).decode()

print(s)