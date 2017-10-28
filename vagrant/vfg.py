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

    overs = {}
    override = {}
    oaddress = {}
    omemory = {}
    oname = {}

    if arg_list.override:
        for ovrde in arg_list.override:
            #override = arg_list.override
            #var = override[1].split(":")[2]
            #var = override[1].split(":")[2]
            var = ovrde.split(":")
            #print var
            #print var[0]
            overridename = var[0]
            #print var[1]
            oconfig =  var[1]
            #print var[2]
            ovalue = var[2]
            #overs['name'] = oname
            #overs[oname]['config'] = oconfig
            #overs[oname][oconfig] = ovalue
            #overs[oname] = [oconfig, ovalue]
            override[overridename] = True
            if oconfig == 'address':
                oaddress[overridename] = ovalue
            if oconfig == 'memory':
                omemory[overridename] = ovalue
            if oconfig == 'name':
                oname[overridename] = ovalue
                

            '''
            override[name] = True
            memory[name] = new value
            address[name] = new value
            ...
            ''' 


    # Begin to write Vagrantfile
    print 'Vagrant.configure("2") do |config|'

    # Create a base config for hosts ([make sure you have the necessary RAM)
    for i in range (0,namecount):

        # Increment the IP
        address = ip_inc(address)
        # Add to the name prefix
        vmname = name + str(i)

        # These are overridden values
        #if vmname in override: 
        if vmname not in oname:
            oname[vmname] = vmname
        if vmname not in omemory:
            omemory[vmname] = memory
        if vmname not in oaddress:
            oaddress[vmname] = address

        vf = '''    config.vm.define :'''+ oname[vmname] +''' do |'''+ oname[vmname] +'''_config|
      '''+oname[vmname]+'''_config.vm.box = "'''+box+'''"
      '''+oname[vmname]+'''_config.vm.hostname = "'''+oname[vmname]+'''"
      '''+oname[vmname]+'''_config.vm.network :private_network, ip: "'''+oaddress[vmname]+'''"
      '''+oname[vmname]+'''_config.vm.provider "virtualbox" do |vb|
        vb.memory = "'''+omemory[vmname]+'''"
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
    parser.add_argument("-o", "--override", help='Overrides named host vaules with other values starting with host name, value name, and the value itself, in the form of "hostname:memory:1024" for example.  Currently the following overrides are supported: name, memory, address',nargs='*') 

    args = parser.parse_args()

    # Check to see if we have any args at all
    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    vf_write(args);

if __name__ == "__main__":
  main()
