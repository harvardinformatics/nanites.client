# coding: utf-8

'''
Test data
'''


ORGANIZATIONS = [
    {
        'name': 'Harvard University (CFA)',
        'rank': 'institution',
        'org_tree': 'CNS'
    },
]
PEOPLE = [
    {
        'first_name': 'Derpy',
        'last_name': 'Derpiston',
        'full_name': 'Derpy (Fred) Derpiston, Jr.',
        'primary_email': 'dderpiston@gmail.com',
        'change_comment': 'Initial entry',
        'primary_affiliation': 'Harvard University (CFA) (a CNS Institution)',
    },
]
LOGINS = [
    { # Missing a Person so that it can be set in the test
        'username': 'dderpiston',
        'role': 'admin',
        'application': 'CNS Admin Intranet',
    },
    {
        'username': 'dderpiston',
        'role': 'user',
        'application': 'CNS User Portal',
    }
]
