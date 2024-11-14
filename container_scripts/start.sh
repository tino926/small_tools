#!/bin/bash

apt-get update -y
apt-get upgrade -y

apt-get install openssh-client openssh-server sshfs -y

# enable ssd, may need to give root password first
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
#sed -i 's/#Port 22/Port 10854/' /etc/ssh/sshd_config

sh -c 'echo root:root_password | chpasswd'
/etc/init.d/ssh restart


apt-get install -y curl wget vim

echo 'install mesa \n' > /mount/log.txt
apt-get install -y libpci-dev libgl1-mesa-glx firefox
apt-get install -y fonts-moe-standard-song

sshfs admin@host_ip:/share/homes/admin/fdr1 /mount/fdr1 -o allow_other,default_permissions

echo 'done start \n' >> /mount/log.txt
