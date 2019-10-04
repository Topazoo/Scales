#! /usr/bin/env python

from nmap import PortScanner
import asyncio, netifaces, socket

class Socket_Scanner():
    def find_potential_sockets(self):      
        return self.get_device_ips(self.get_default_gateway())
        
    def get_device_ips(self, default_gateway):
        ips = []

        if not default_gateway:
            default_gateway = self.get_default_gateway()

        for result in PortScanner().scan(hosts=default_gateway+'/24', arguments='-sP')['scan'].values():
            if 'addresses' in result:
                if 'ipv4' in result['addresses'] and \
                result['addresses']['ipv4'] != default_gateway and \
                result['addresses']['ipv4'] not in socket.gethostbyname_ex(socket.gethostname())[-1]:
                    ips.append(result['addresses']['ipv4'])
        
        return ips

    def get_default_gateway(self):
        gateways = netifaces.gateways()
        if 'default' in gateways:
            if 2 in gateways['default']:
                return (gateways['default'][2][0])


if __name__ == '__main__':
    print('Scanning for potential sockets...')
    print('Found: ' + str(Socket_Scanner().find_potential_sockets()))