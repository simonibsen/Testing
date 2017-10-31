#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys
import argparse

def vf_write(arg_list):

    '''
    Process args and write corresponding Vagrantfile to STDOUT
    '''
    box = arg_list.box
    name = arg_list.name
    namecount = int(arg_list.namecount)
    address = arg_list.address
    memory = arg_list.memory
    primary = arg_list.primary

    localfiles = {}
    remotefiles = {}

    if arg_list.copyfiles:
        for copyfile in arg_list.copyfiles:

            print copyfile
            var = copyfile.split(":")
            print var
            filehostname = var[0]
            localfile =  var[1]
            remotefile = var[2]

            #files[filehostname] = True
            localfiles[filehostname] = localfile
            remotefiles[filehostname] = remotefile

    overs = {}
    override = {}
    obox = {}
    oaddress = {}
    omemory = {}
    oname = {}

    if arg_list.override:
        for ovrde in arg_list.override:

            var = ovrde.split(":")
            overridename = var[0]
            oconfig =  var[1]
            ovalue = var[2]

            #override[overridename] = True
            if oconfig == 'box':
                obox[overridename] = ovalue
            if oconfig == 'address':
                oaddress[overridename] = ovalue
            if oconfig == 'memory':
                omemory[overridename] = ovalue
            if oconfig == 'name':
                oname[overridename] = ovalue
                
    # Begin to write Vagrantfile
    print 'Vagrant.configure("2") do |config|'

    # Create a base config for hosts ([make sure you have the necessary RAM)
    for i in range (0,namecount):

        # Increment the IP
        address = ip_inc(address)
        # Add to the name prefix
        vmname = name + str(i)

        # Test to see if this is a primary box in a multi environment
        if vmname == primary:
            pribox = ", primary: true"
        else:
            pribox = ""

        # These are file values
        if (vmname in localfiles and vmname in remotefiles):
            fileline = '''config.vm.provision "file", source: "%s", destination: "%s" '''%(localfiles[vmname],remotefiles[vmname])
        else:
            fileline = None

        # These are overridden values
        if vmname not in obox:
            obox[vmname] = box
        if vmname not in oname:
            oname[vmname] = vmname
        if vmname not in omemory:
            omemory[vmname] = memory
        if vmname not in oaddress:
            oaddress[vmname] = address

        print '''    config.vm.define :%s%s do |%s_config|
        %s_config.vm.box = "%s"
        %s_config.vm.hostname = "%s"
        %s_config.vm.network :private_network, ip: "%s"
        %s_config.vm.provider "virtualbox" do |vb|
            vb.memory = "%s"
        end
        %s
    end'''%(oname[vmname], 
        pribox, 
        oname[vmname], 
        oname[vmname], 
        obox[vmname], 
        oname[vmname], 
        oname[vmname], 
        oname[vmname], 
        oaddress[vmname], 
        oname[vmname], 
        omemory[vmname],
        fileline)
    print "end"

# Add to the final tuple
def ip_inc(ip):
    tup1,tup2,tup3,tup4 = ip.split(".");
    tup4 = str(int(tup4) + 1); 
    return '.'.join([tup1,tup2,tup3,tup4]) 
    
def main():

    # Let us parse our args 
    parser = argparse.ArgumentParser(description='Utility to speed up creation of Vagrantfiles')

    parser.add_argument("-b", "--box", help='The VM OS you want - note this needs to be available in Vagrantcloud.  The default is centos/7',default='centos/7') 
    parser.add_argument("-n", "--name", help='The name (or prefix) name(s) of the host(s)') 
    parser.add_argument("-c", "--namecount", help='The number of VMs desired prefix named with value of name', default='1') 
    parser.add_argument("-p", "--primary", help='Specify the primary box in a multi box environment') 
    parser.add_argument("-a", "--address", help='The IP address start for this host or list of hosts', default='10.0.100.10') 
    parser.add_argument("-m", "--memory", help='The amount of memory to allocate in MB.  The default is 256MB',default='256') 
    parser.add_argument("-f", "--copyfiles", help='Upload a file or directory to the guest from the host.  Specified in the form of hostname:localfile:remotefile',nargs='*') 
    parser.add_argument("-o", "--override", help='Overrides named host vaules with other values starting with host name, value name, and the value itself, in the form of "hostname:memory:1024" for example.  Currently the following overrides are supported: box, name, memory, address',nargs='*') 

    # Enable auto syncing of files at provision - config.vm.provision "file", https://www.vagrantup.com/docs/provisioning/file.html
    # Enable auto syncing of shell at provision - config.vm.provision "shell", https://www.vagrantup.com/docs/provisioning/shell.html
    # Enable auto syncing of ansible at provision - config.vm.provision "ansible", https://www.vagrantup.com/docs/provisioning/ansible.html
    # Enable port forwarding - https://www.vagrantup.com/docs/networking/forwarded_ports.html
    # Enable synced folders - https://www.vagrantup.com/docs/synced-folders/basic_usage.html
    # Enable docker provider support - https://www.vagrantup.com/docs/docker/basics.html

    args = parser.parse_args()

    # Check to see if we have any args at all
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    vf_write(args);

if __name__ == "__main__":
  main()
