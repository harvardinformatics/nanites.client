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
    {
        'first_name': 'Slurpy',
        'last_name': 'Slurpiston',
        'full_name': 'Slurpy Slurpiston',
        'primary_email': 'sslurpiston@gmail.com',
        'change_comment': 'Initial entry',
        'primary_affiliation': 'Harvard University (CFA) (a CNS Institution)',
        'race': 'White',
        'ethnicity': 'Southern',
        'gender': 'Fluid',
        'is_disabled': True,
        'disability': 'Blind',
        'citizenship': 'Switzerland',
        'visa_details': 'Green card',
        'national_origin': 'Louisiana',
        'addresses': [
            {
                'type': 'home',
                'street1': '108 Hometown Dr.',
                'city': 'New Orleans',
                'state': 'Louisiana',
                'country': 'Us',
                'postal_code': '4',
            },
            {
                'type': 'work',
                'street1': '109 Hometown Dr.',
                'city': 'New Orleans',
                'state': 'Louisiana',
                'country': 'Us',
                'postal_code': '4',
            },
        ],
        'contacts': [
            {
                'type': 'email',
                'detail': 'slurpy@hotmail.com',
            },
            {
                'type': 'phone',
                'detail': '123-1233'
            }
        ],
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
