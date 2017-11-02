# vfg - Vagrant File Generator
This is a simple script to more easily spit out Vagrantfiles to support various environments.
```
usage: vfg [-h] [-p PRIMARY] [-b BOX] [-n NAME] [-c NAMECOUNT] [-a ADDRESS] [-m MEMORY]
              [-o [OVERRIDE [OVERRIDE ...]]] -f [COPYFILES [COPYFILES ...]]

Utility to speed up creation of Vagrantfiles

Optional arguments:

  -h, --help            show this help message and exit
  -n NAME, --name NAME  The name (or prefix) name(s) of the host(s).  This is
                        a REQUIRED option
  -b BOX, --box BOX     The VM OS you want - note this needs to be available
                        in Vagrantcloud. The default is centos/7                 
  -c NAMECOUNT, --namecount NAMECOUNT
                        The number of VMs desired prefix named with value of
  -p PRIMARY, --primary PRIMARY
                        Specify the primary box in a multi box environment
  -a ADDRESS, --address ADDRESS
                        The IP address start for this host or list of hosts                        
  -m MEMORY, --memory MEMORY
                        The amount of memory to allocate in MB. The default is
                        256MB                        
  -f [COPYFILES [COPYFILES ...]], --copyfiles [COPYFILES [COPYFILES ...]]
                        Upload a file or directory to the guest from the host.
                        Specified in the form of hostname:localfile:remotefile 
                        where hostname can be ALL
  -s [STRING [STRING ...]], --string [STRING [STRING ...]]
                        Write some arbitrary string (not covered by other
                        option). Specified in the form of hostname:string
                        where hostname can be ALL and string is quoted
  --ports [PORTS [PORTS ...]]
                        Forward ports from host to guest machines. The format
                        is hostname:guestport:hostport
  --shell [SHELL [SHELL ...]]
                        Enable basic shell provisioning [inline type],
                        specified in the form hostname:inline_string where
                        hostname can be ALL and string is quoted
  --ansible [ANSIBLE [ANSIBLE ...]]
                        Enable basic ansible provisioning [inline type],
                        specified in the form hostname:inline_string where
                        hostname can be ALL and string is quoted
  -o [OVERRIDE [OVERRIDE ...]], --override [OVERRIDE [OVERRIDE ...]]
                        Overrides named host vaules with other values starting
                        with host name, value name, and the value itself, in
                        the form of "name:memory:1024" for example. Currently
                        the following overrides are supported: name, memory,
                        address
```
