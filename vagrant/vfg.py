#!/usr/bin/env python

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import sys
import argparse

def vf_write(arg_list):

    '''
    Process args and write corresponding Vagrantfile to STDO
    '''
    box = arg_list.box
    name = arg_list.name
    namecount = int(arg_list.namecount)
    address = arg_list.address
    memory = arg_list.memory


    # Begin to write Vagrantfile
    print 'Vagrant.configure("2") do |config|'

    # Create a base config for hosts ([make sure you have the necessary RAM)
    for i in range (0,namecount):

        # Increment the IP
        address = ip_inc(address)
        # Add to the name prefix
        vmname = name + str(i)

        vf = '''    config.vm.define :'''+ vmname +''' do |'''+ vmname +'''_config|
      '''+vmname+'''_config.vm.box = "'''+box+'''"
      '''+vmname+'''_config.vm.hostname = "'''+vmname+'''"
      '''+vmname+'''_config.vm.network :private_network, ip: "'''+address+'''"
      '''+vmname+'''_config.vm.provider "virtualbox" do |vb|
        vb.memory = "'''+memory+'''"
      end
   end'''
        print vf
    print "end"

# Add to the final tuple
def ip_inc(ip):
    tup1,tup2,tup3,tup4 = ip.split(".");
    tup4 = str(int(tup4) + 1); 
    return '.'.join([tup1,tup2,tup3,tup4]) 
    
def main():

    # Let us parse our args 
    parser = argparse.ArgumentParser(description='Utility to speed up creation of Vagrantfiles')

    parser.add_argument("-b", "--box", help='The VM OS you want - note this needs to be available in Vagrantcloud.  The default is centos/6',default='centos/6') 
    parser.add_argument("-n", "--name", help='The name (or prefix) name(s) of the host(s)') 
    parser.add_argument("-c", "--namecount", help='The number of VMs desired prefix named with value of name', default='1') 
    parser.add_argument("-a", "--address", help='The IP address start for this host or list of hosts', default='10.0.100.10') 
    parser.add_argument("-m", "--memory", help='The amount of memory to allocate in MB.  The default is 256MB',default='256') 
    parser.add_argument("-o", "--override", help='Overrides named host vaules with other values starting with host name, value name, and the value itself, in the form of "name:memory:1024" for example.') 

    args = parser.parse_args()

    # Check to see if we have any args at all
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    vf_write(args);

if __name__ == "__main__":
  main()
