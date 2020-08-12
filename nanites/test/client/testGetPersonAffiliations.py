# coding: utf-8

'''
Test getPersonAffiliations
'''
from nanites.client import API
from nanites.test.client import data, ApiTest


class TestGetPersonAffiliationsApi(ApiTest):
    '''
    Test for getPersonAffiliations API call
    '''

    def test_get_person_affiliations(self):
        '''
        Ensure that persons are returned with their affiliations
        '''
        # Load the person
        person = API.createPerson(api_client=self.api_client, **data.PEOPLE[1])
        self.assertTrue(person.primary_affiliation == 'Slurpiston Lab (a Research Computing AD Laboratory)', f'Incorrect primary affiliation {person.primary_affiliation}')
        self.assertTrue(len(person.affiliations) == 2, 'Incorrect number of person affiliations %d' % len(person.affiliations))
        person_affiliations = API.getPersonAffiliations()
        self.assertTrue(len(person_affiliations) == 2, 'Incorrect number of person affiliations %s' % str(person_affiliations))
