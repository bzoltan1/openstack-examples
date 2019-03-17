 Using the Python API of the Openstack SDK

## Used sources:
  Openstack SDK souce - https://github.com/openstack/openstacksdk
  openstack SDK documentation - https://docs.openstack.org/openstacksdk/latest/

## Preparation:
  Install the python3-openstacksdk package

The documentation of the CLI openstack tool covers much more APIs than the Python API documentation
  https://docs.openstack.org/ocata/user-guide/cli.html

The Python APIs are very similar to the CLI APIs. Good practice to find a function in the CLI API documentation and grep the same keyword in the source repository of the Openstack SDK

## Authentication

Either the ~/.config/openstack/clouds.yaml or the /etc/openstack/clouds.yaml

clouds:
  cloudname:
    auth:
      auth_url:
      project_name: 
      username: 
      password:
      user_domain_name: 
      project_domain_name: 
    region_name: 

The credentials can be found in the OpenStack Web UI:
  Project > Compute > Access & Security > Download OpenSatack RC File v3

It is possible to use the CLI openstack commands after sourcing the downloade script in the shell.

TODO: How to use token instead of password authentication

