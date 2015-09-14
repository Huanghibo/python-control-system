import ipaddress
import netifaces

def iter_addrs():
    for ifname in netifaces.interfaces():
        for addr_data in netifaces.ifaddresses[netifaces.AF_INET]:
            yield ifname, addr_data
        
def get_local_addresses():
    addrs = []
    nets = []
    for ifname, d in iter_addrs():
        addr = ipaddress.ip_interface(('/'.join([d['addr'], d['netmask']])))
        if addr.network in nets:
            continue
        if addr.ip.is_loopback:
            continue
        if not addr.ip.is_private:
            continue
        addrs.append(addr)
        nets.append(addr.network)
    return addrs
