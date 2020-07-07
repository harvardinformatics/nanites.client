# -*- coding: utf-8 -*-

'''
nanites client init

Initializes data for a new system.  To be used in both prod and dev.

Uses get_or_create so that it can be run when partial data exists

Created on  2019-12-23

@author: Aaron Kitzmiller <aaron_kitzmiller@harvard.edu>
@copyright: 2019 The Presidents and Fellows of Harvard College.
All rights reserved.
@license: GPL v2.0
'''

from collections import OrderedDict


def migrate(apps, schema_editor):
    '''
    Set data via migration
    '''
    initUsers(apps.get_model('auth', 'User'))


def main():
    '''
    If called directly, rather than as a migration
    '''
    from django.contrib.auth.models import User

    modelsForFixture = OrderedDict()
    modelsForFixture['auth.User'] = initUsers(User)

    return modelsForFixture



def initUsers(cls):
    '''
    Initialize application users.  Do NOT set tokens here.
    '''
    pks = []
    users = [
        {
            'username': 'nice',
            'first_name': 'NICE',
            'last_name': 'Application',
            'is_active': True,
            'is_superuser': True,
        },
        {
            'username': 'p3',
            'first_name': 'p3',
            'last_name': 'Application',
            'is_active': True,
            'is_superuser': True,
        },
        {
            'username': 'p3approve',
            'first_name': 'p3approve',
            'last_name': 'Application',
            'is_active': True,
            'is_superuser': True,
        },
        {
            'username': 'cns',
            'first_name': 'CNS',
            'last_name': 'Application',
            'is_active': True,
            'is_superuser': True,
        },
        {
            'username': 'cas',
            'first_name': 'CAS',
            'last_name': 'Application',
            'is_active': True,
            'is_superuser': True,
        },
        {
            'username': 'pubs',
            'first_name': 'PUBS',
            'last_name': 'Application',
            'is_active': True,
            'is_superuser': True,
        },
        {
            'username': 'ifxonboard',
            'first_name': 'IfxOnboard',
            'last_name': 'Application',
            'is_active': True,
            'is_superuser': True,
        },
        {
            'username': 'portal',
            'first_name': 'Portal',
            'last_name': 'Application',
            'is_active': True,
            'is_superuser': True,
        },
        {
            'username': 'hers',
            'first_name': 'HeRS',
            'last_name': 'Application',
            'is_active': True,
            'is_superuser': True,
        },
    ]

    for userdata in users:
        (obj, created) = cls.objects.get_or_create(**userdata)
        pks.append(obj.pk)

    return pks


if __name__ == '__main__':
    main()
