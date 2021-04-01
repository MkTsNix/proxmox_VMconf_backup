from paramiko import SSHClient
from scp import SCPClient
import os

host = 'HOSTNAME_or_IP_ADDRESS'
user = 'You_user_name'
ssh_key = 'PATH_TO_SSH_KEY'
ssh_port = 22
download_path = 'DOWNLOAD_PATH'

ssh = SSHClient()
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
ssh.connect(host, username=user, port=ssh_port, key_filename=ssh_key)
with SCPClient(ssh.get_transport(), sanitize=lambda x: x) as scp:
        scp.get('/etc/pve/qemu-server/*', download_path)


