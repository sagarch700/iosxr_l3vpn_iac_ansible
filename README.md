# iosxr_l3vpn_iac_ansible
Automated L3VPN Deployment for ios xr using Ansible iac.

**Usage of Makefile**
  - it is to abstract the ansible commands.
  - default goal is run, means it will run all the phony targets mentioned under run target in make file
  - lint: target which will check for any ansible-playbook syntax errors. to run only lint use command "make lint"
  - get_rd_rt: target runs the get_rd_rt_playbook.yml. to run only this target use command "make get_rd_rt"
  - l3vpn_prompt: target runs the get_l3vpn_prompt_playbook.yml. to run only this target use command "make l3vpn_prompt"
  - unit: target runs the iosxr_l3vpn_unittest.yml. to run only this target use command "make unit"
  - iac: target runs the iosxr_l3vpn_iac_playbook.yml. to run only this target use command "make iac"
  - if you use just "make" command it will run all the targets mentioned in run target.

**custom filter: filter.py**
  - in ansible, you can create your own custom filter using filter.py in python. you create methods in filter.py for this purprose.
  - i have created my own custom filter methods for below purposes.
    - rd_max: it will return the max rd value from all the rd values configufed on the router. i used heap DSA.
    - rt_max: it will return the max rt value from the values configured on the router.
    - bgp_password: it will generate a strong bgp password using alphabets, symbols, and numbers. 

**get_rd_rt_playbook.yml playbook**
  - This playbook is to get the last/latest configured rd and rt values from the ref_node, where ref_node ip is the ip of node on which last     l3vpn configuration was done.
  - will use the custom filter to store the necessary values in /vars/rd-rt_vars.yml file

**get_l3vpn_prompt_playbook.yml playbook**
  - This playbook will get the needed data like: vrf name, no of rt values you want to use, and customer AS number from the prompt.
  - i used the customer filter to create a random strong bgp password to be used for establishing bgp password.
  - all the necessary values are stored in /vars/prompt_vars.yml

**iosxr_l3vpn_unittest.yml unnitesting**
  - This is for unitesting.
  - first, for this unittesting to work, i need to get the output of the grep "vrf name" to be deployed and "rd" value to be deployed from       the PE routers. used iosxr.iosxr_command module for this. register the values in respective variables, which will be used later.
  - now write some simple unittests to verify the below.
    - the vrf name to be deployed shouldn't exist.
    - the rd value to be deplyed shouldn't exist.
    - customer AS should be in the private range: 64512 - 65535

**iosxr_l3vpn_iac_playbook.yml playbook**
  - This is the playbook that will push the L3VPN configuration to your PE routers.
  - Task-1: let's say you want to check if your jinja2 templating is correct and it generated the configuration you desire. use this task to     generate a text file from jinja2 template to verify the configuration.
  - Task-2: sends the configuration to the PE devices. i am going to use handlers, so i have used notify.
  - Handlers: to display the configuration that was pushed to the PE routers. to change the ansible host ip of the ref node to the latest PE     node on which the L3VPN configuration is done.

