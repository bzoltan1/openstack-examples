#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import openstack

# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

# Initialize cloud
# The URL and credentials for the 'engineering' name should be defined in the
# ~/.config/openstack/clouds.yaml or /etc/openstack/clouds.yaml.
cloud = openstack.connect(cloud='engineering')

# Create new instance
# The image and flavor is specific to the OpenStack service.
# See the flavors_and_images.py example on how to list the available 
# images and flavors
cloud_server = cloud.create_server('bzoltan-jeos',
                                   image='SLE15-SP1-JeOS-root',
                                   flavor=dict(id='22'),
                                   wait=True,
                                   auto_ip=True)

# Find a server by name
cloud_server = cloud.get_server('bzoltan-jeos')

cloud.pprint(cloud_server)
