#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import openstack

# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

# Initialize cloud
cloud = openstack.connect(cloud='engineering')

# Get he list of available flavors
for flavor in cloud.compute.flavors():
    print('{:<32s}{:>6d} MB {:>6d} GB {:>48s}'.format(flavor.name,
                                                      flavor.ram,
                                                      flavor.disk,
                                                      flavor.id))
# Get the list of available images
for image in cloud.compute.images():
    print(image.name)

for network in cloud.network.networks():
        print('{:<18s}{:>16s}'.format(network.name, network.id))
