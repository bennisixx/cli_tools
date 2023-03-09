import os
from pathlib import Path


def generate_new_key(fname, ty, bts, comnt) -> None:
    # Generate a new RSA key using `ssh-keygen` and the specified file name
    os.system(f"ssh-keygen -t {ty} -b {bts} -f ~/.ssh/{fname} {comnt}")


def copy_key_to_host(hme, nme, hst, prt, fname) -> None:
    # Copy the SSH key to the host using `ssh-copy-id`
    os.system(f"ssh-copy-id -i {hme}/.ssh/{fname}  -p {prt} {nme}@{hst}")


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


def check_defaults(d_def) -> dict:
    res = {}
    for k, v in d_def.items():
        if len(v[1]) == 0:
            res[k] = v[0]
        else:
            res[k] = v[1]
    return res


def run() -> None:
    # Get home directory
    home_dir: str = str(Path.home())
    # User Input Prompts
    uname: str = input("SSH User Name: ")
    host: str = input("SSH Domain/IP: ")
    port: str = input("SSH Port (default: 22): ")
    en_type: str = input("Key Type (default: rsa): ")
    bits: str = input("Key Bits (default: 4096): ")
    comment: str = input("Key-Gen Comment (optional): ")
    file_name: str = input("Key Name (Default: Domain/IP)")
    if len(comment) > 0:
        comment: str = f"-C {comment}"
    else:
        comment: str = ""
    d_defaults = {"port": ("22", port), "type": ("rsa", en_type), "bits": ("4096", bits), "name": (f"{host}", file_name)}
    defaults = check_defaults(d_defaults)
    port: str = str(defaults['port'])
    en_type: str = str(defaults['type'])
    bits: str = str(defaults['bits'])
    file_name: str = str(defaults['name'])

    # Generate a new SSH key
    generate_new_key(file_name, en_type, bits, comment)
    # Copy the SSH key to the host
    copy_key = input("Copy key to host? (y,n) ")
    if copy_key.lower() == 'y':
        copy_key_to_host(home_dir, uname, host, port, file_name)

    # Write the key name to the SSH configuration file
    write_keyname_to_config(home_dir, file_name)

    # start key agent
    agent = input("Start ssh key-agent? (git ssh keys etc.) (y,n) ")
    if agent.lower() == 'y':
        os.system(f'eval "${{ssh-agent}}" -s && ssh-add {home_dir}/.ssh/{file_name}')

    print("Done!")


if __name__ == "__main__":
    run()
