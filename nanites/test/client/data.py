# coding: utf-8

'''
Test data
'''

SOURCES = [
    {
        'name': 'test source',
        'description': 'test source description'
    },
    {
        'name': 'test2',
        'description': 'another test'
    }
]

APPLICATIONS = [
    {
        'name': 'CNS Admin Intranet',
        'fields': '__all__',
    },
    {
        'name': 'CNS User Portal',
        'fields': '__all__',
    }

]

ORGANIZATIONS = [
    {
        'name': 'University of Moscow',
        'rank': 'institution',
        'org_tree': 'Research Computing AD',
        'code': 'MSCW',
    },
    {
        'name': 'Derp',
        'rank': 'department',
        'org_tree': 'Research Computing AD',
    },
    {
        'name': 'Slurpiston Lab',
        'rank': 'lab',
        'org_tree': 'Research Computing AD',
        'parents': [
            {
                'parent': 'Derp (a Research Computing AD Department)',
            },
        ]
    },
    {
        'name': 'Center for Advanced Derp',
        'rank': 'center',
        'org_tree': 'Research Computing AD',
    },
    {
        'name': 'Derp Museum',
        'rank': 'museum',
        'org_tree': 'Research Computing AD',
    },
]
PEOPLE = [
    {
        'first_name': 'Derpy',
        'last_name': 'Derpiston',
        'full_name': 'Derpy (Fred) Derpiston, Jr.',
        'primary_email': 'dderpiston@gmail.com',
        'change_comment': 'Initial entry',
        'primary_affiliation': 'Slurpiston Lab (a Research Computing AD Laboratory)',
    },
    {
        'first_name': 'Slurpy',
        'last_name': 'Slurpiston',
        'full_name': 'Slurpy Slurpiston',
        'primary_email': 'sslurpiston@gmail.com',
        'change_comment': 'Initial entry',
        'primary_affiliation': 'Slurpiston Lab (a Research Computing AD Laboratory)',
        'race': 'White',
        'ethnicity': 'Southern',
        'gender': 'Fluid',
        'is_disabled': True,
        'disability': 'Blind',
        'citizenship': 'Switzerland',
        'visa_details': 'Green card',
        'national_origin': 'Louisiana',
        'affiliations': [
            {
                'slug': 'Slurpiston Lab (a Research Computing AD Laboratory)',
                'role': 'pi',
            },
            {
                'slug': 'Center for Advanced Derp (a Research Computing AD Center)',
                'role': 'member',
            }
        ],
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
                'contact': {
                    'type': 'email',
                    'detail': 'slurpy@hotmail.com',
                },
                'role': 'Additional email'
            },
            {
                'contact': {
                    'type': 'phone',
                    'detail': '123-1233'
                },
                'role': 'phone'
            }
        ],
    },
    {
        'first_name': 'Denny',
        'last_name': 'Dennison',
        'full_name': 'Denny J. Dennison',
        'primary_email': 'realDonaldTrump@twitter.com',
        'change_comment': 'Initial entry',
        'primary_affiliation': 'University of Moscow (a Research Computing AD Institution)',
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
    },
    {
        'username': 'ddennison',
        'role': 'user',
        'application': 'CNS User Portal',
        'is_enabled': True,
    },
    {
        'username': 'ddennison2',
        'role': 'user',
        'application': 'CNS User Portal',
        'is_enabled': False
    },
]
