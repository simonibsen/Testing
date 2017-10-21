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

    print memory,address,namecount,name,box

    if namecount == 1:
        vf = '''Vagrant.configure("2") do |config|
  # create ''' + name +''' node
  config.vm.define :'''+ name +''' do |'''+ name +'''_config||
      '''+name+'''_config.vm.box = "'''+box+'''"
      '''+name+'''_config.vm.hostname = "'''+name+'''"
      '''+name+'''_config.vm.network :private_network, ip: "'''+address+'''"
      '''+name+'''_config.vm.provider = "virtualbox" do |vb|
        vb.memory = "'''+memory+'''"
      end
   end
       '''
    else:


        print vf

def main():

    '''
    print sys.flags
    print sys.path
    '''


    # Let us parse our args 
    parser = argparse.ArgumentParser(description='Utility to speed up creation of Vagrantfiles')

    parser.add_argument("-b", "--box", help='The VM OS you want - note this needs to be available in Vagrantcloud.  The default is centos/6',default='centos/6') 
    parser.add_argument("-n", "--name", help='The name (or prefix) name(s) of the host(s)') 
    parser.add_argument("-c", "--namecount", help='The number of VMs desired prefix named with value of name', default='1') 
    parser.add_argument("-a", "--address", help='The IP address start for this host or list of hosts', default='10.0.100.10') 
    parser.add_argument("-m", "--memory", help='The amount of memory to allocate in MB.  The default is 256MB',default='256') 

    args = parser.parse_args()

    # Check to see if we have any args at all
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    vf_write(args);

if __name__ == "__main__":
  main()
