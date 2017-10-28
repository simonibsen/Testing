# Little Bits of This and That
Bits and pieces

## vagrant/vfg.py
This is a simple script to more easily spit out Vagrantfiles to support various environments.
```
usage: vfg.py [-h] [-b BOX] [-n NAME] [-c NAMECOUNT] [-a ADDRESS] [-m MEMORY]
              [-o [OVERRIDE [OVERRIDE ...]]]

Utility to speed up creation of Vagrantfiles

Optional arguments:

  -h, --help            show this help message and exit
  
  -b BOX, --box BOX     The VM OS you want - note this needs to be available
                        in Vagrantcloud. The default is centos/6                 
  -n NAME, --name NAME  The name (or prefix) name(s) of the host(s)
  -c NAMECOUNT, --namecount NAMECOUNT
                        The number of VMs desired prefix named with value of
                        name                        
  -a ADDRESS, --address ADDRESS
                        The IP address start for this host or list of hosts                        
  -m MEMORY, --memory MEMORY
                        The amount of memory to allocate in MB. The default is
                        256MB                        
  -o [OVERRIDE [OVERRIDE ...]], --override [OVERRIDE [OVERRIDE ...]]
                        Overrides named host vaules with other values starting
                        with host name, value name, and the value itself, in
                        the form of "name:memory:1024" for example. Currently
                        the following overrides are supported: name, memory,
                        address
```
