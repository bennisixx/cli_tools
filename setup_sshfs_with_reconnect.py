import os

user = input("SSH User Name: ")
domain = input("Remote Domain/IP: ")
mountpoint = input("Local Mountpoint. Full Path: ")
port = input("SSH Port: ")
cmd = f"sshfs {user}@{domain}:/ {mountpoint} -p {port} -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3"
os.system(cmd)
