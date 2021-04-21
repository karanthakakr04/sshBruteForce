# sshbruteforce

This assignment automates the process of brute forcing with a fairly large password list. 

# Required Setup

> Virtual Box - Version 6.1.18 (a newer release should work fine)

Download here: https://www.virtualbox.org/wiki/Downloads. You will need to setup Metasploitable2 VM to carry out SSH brute force. 

> Metasploitable2

The Metasploitable virtual machine is an intentionally vulnerable version of Ubuntu Linux designed for testing security tools and demonstrating common vulnerabilities. Download the file here: https://sourceforge.net/projects/metasploitable/. After downloading and installing the VM, set the network adapter to 'Brigded Adapter' before turning the on the machine.

![metasploitable_2_adatper](https://user-images.githubusercontent.com/17943347/115628281-6c5e1580-a2ce-11eb-9244-d3cfda90d699.png)


![metasploitable_vm_start](https://user-images.githubusercontent.com/17943347/115628341-80a21280-a2ce-11eb-9651-3f9971dfa15e.png)


# Brute Forcing

Before running the program make sure to check the IP address of the Metasploitable VM and use that to SSH to the machine using Paramiko library. Since this brute force attack requires a dataset of passwords, we will be using a file called passwords_list.txt (consisting of 112 insecure passwords) placed in the same directory. To further enhance the speed of brute forcing for this long list of passwords, threading is introduced.

On running the program, we need to input some required parameters:

![ssh_bruteforce_github_1](https://user-images.githubusercontent.com/17943347/115628421-9c0d1d80-a2ce-11eb-863e-ffb3b114a326.png)

![ssh_bruteforce_github_2](https://user-images.githubusercontent.com/17943347/115628432-a16a6800-a2ce-11eb-96e3-89cc4931283b.png)

The list of passwords can be as long as you want but for testing purposes I chose to stick with a few more than 100 passwords. Below is the snippet:

![passwords_list](https://user-images.githubusercontent.com/17943347/115628583-d5de2400-a2ce-11eb-88f1-77ef9779f7b3.png)
