import os


def run() -> None:
    # User Input Prompts
    user: str = input("SSH User Name: ")
    domain: str = input("Remote Domain/IP: ")
    mountpoint: str = input("Local Mountpoint. Full Path: ")
    port: str = input("SSH Port: ")

    # Construct the SSHFS command
    cmd: str = f"sshfs {user}@{domain}:/ {mountpoint} -p {port} -o reconnect,ServerAliveInterval=15,ServerAliveCountMax=3"
    # Run the SSHFS command
    os.system(cmd)


if __name__ == "__main__":
    run()
