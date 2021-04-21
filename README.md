# sshbruteforce

This assignment automates the process of brute forcing with a fairly large password list. 

# Required Setup

> Virtual Box - Version 6.1.18 (a newer release should work fine)

Download here: https://www.virtualbox.org/wiki/Downloads. You will need to setup Metasploitable2 VM to carry out SSH brute force. 

> Metasploitable2

The Metasploitable virtual machine is an intentionally vulnerable version of Ubuntu Linux designed for testing security tools and demonstrating common vulnerabilities. Download the file here: https://sourceforge.net/projects/metasploitable/. After downloading and installing the VM, set the network adapter to 'Brigded Adapter' before turning the on the machine.


# Brute Forcing

Before running the program make sure to check the IP address of the Metasploitable VM and use that to SSH to the machine using Paramiko library. Since this brute force attack requires a dataset of passwords, we will be using a file called passwords_list.txt (consisting of 112 insecure passwords) placed in the same directory. To further enhance the speed of brute forcing for this long list of passwords, threading is introduced.

On running the program, we need to input some required parameters:
