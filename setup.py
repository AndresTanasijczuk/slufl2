#!/usr/bin/env python
# -*- coding: utf8 -*-

from distutils.core import setup

setup(name='slufl2',
      version='2.0.0-beta',
      description='Run Ansible playbooks when LDAP entries change.',
      license='BSD',
      author='Damien François',
      author_email='damien.francois@uclouvain.be',
      url='https://github.com/damienfrancois/slufl2',
      scripts=['slufld'],
      data_files=[
                  ('/etc', ['etc/slufld.conf.template']),
                  ('/etc/systemd/system', ['etc/slufld.service']),
                  ('/etc/slufld.conf.d', ['etc/slufld.conf.d/inventory', 'etc/slufld.conf.d/TestCustom.yml'])
                 ],
      long_description="""slufl is a damon that monitors an LDAP server and
                  triggers Ansible playbook upon changes."""
)

# create tar.gz
# python setup.py sdist
# create rpm
# python setup.py bdist_rpm
