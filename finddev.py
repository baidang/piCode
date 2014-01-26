from bluetooth import *
from pprint import pprint

print "Performing inquiry..."

find_dev = discover_devices(lookup_names = True)

print "Found %d devices" % len(find_dev)

for name, addr in find_dev:
	print "%s - %s" % (addr, name)
	service = find_service(address=addr)
	pprint(service)
