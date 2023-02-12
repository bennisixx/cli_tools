import os
from pathlib import Path


def generate_new_key(fname) -> None:
    # Generate a new RSA key using `ssh-keygen` and the specified file name
    os.system(f"ssh-keygen -t rsa -f ~/.ssh/{fname}")


def copy_key_to_host(hme, nme, hst, prt) -> None:
    # Copy the SSH key to the host using `ssh-copy-id`
    os.system(f"ssh-copy-id -i {hme}/.ssh/{hst}  -p {prt} {nme}@{hst}")


def write_keyname_to_config(hme, fname) -> None:
    # Initialize an empty string to store the contents of the SSH configuration file
    line: str = ""
    # The path to the SSH configuration file
    config_file: str = f'{hme}/.ssh/config'

    # Read the contents of the SSH configuration file
    with open(f"{hme}/.ssh/config", "r") as ssh_conf_file:
        for ln in ssh_conf_file:
            line += f"{ln}\n"

    # Create the SSH configuration file if it does not already exist
    if os.path.isfile(config_file) is False:
        os.system(f"touch {config_file}")

    # Write the key name to the SSH configuration file
    with open(f"{hme}/.ssh/config", "w+") as ssh_write:
        line += f"IdentityFile ~/.ssh/{fname}\n"
        ssh_write.write(f"{line} \n")


def run() -> None:
    # Get home directory
    home_dir: str = str(Path.home())
    # User Input Prompts
    uname: str = input("SSH User Name: ")
    host: str = input("SSH Domain/IP: ")
    port: str = input("SSH Port: ")

    # Generate a new SSH key
    generate_new_key(host)
    # Copy the SSH key to the host
    copy_key_to_host(home_dir, uname, host, port)
    # Write the key name to the SSH configuration file
    write_keyname_to_config(home_dir, host)

    print("Done!")


if __name__ == "__main__":
    run()