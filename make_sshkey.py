import os
from pathlib import Path


def generate_new_key(fname) -> None:
    os.system(f"ssh-keygen -t rsa -f ~/.ssh/{fname}")


def copy_key_to_host(hme, nme, hst, prt) -> None:
    os.system(f"ssh-copy-id -i {hme}/.ssh/{hst}  -p {prt} {nme}@{hst}")


def write_keyname_to_config(hme, fname) -> None:
    line: str = ""
    config_file: str = f'{hme}/.ssh/config'

    with open(f"{hme}/.ssh/config", "r") as ssh_conf_file:
        for ln in ssh_conf_file:
            line += f"{ln}\n"

    if os.path.isfile(config_file) is False:
        os.system(f"touch {config_file}")

    with open(f"{hme}/.ssh/config", "w+") as ssh_write:
        line += f"IdentityFile ~/.ssh/{fname}\n"
        ssh_write.write(f"{line} \n")


def run() -> None:
    home_dir: str = str(Path.home())
    uname: str = input("SSH User Name: ")
    host: str = input("SSH Domain/IP: ")
    port: str = input("SSH Port: ")

    generate_new_key(host)
    copy_key_to_host(home_dir, uname, host, port)
    write_keyname_to_config(home_dir, host)
    print("Done!")


if __name__ == "__main__":
    run()
