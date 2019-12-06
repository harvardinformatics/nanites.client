Client API
==========

The nanites.client API is actually a wrapper around the Swagger client code.  Each Nanites object (e.g. Person) is provided with
a set of 5 method calls for listing objects, paged listing of objects, fetching a single object by id, creating a new object, updating an existing object
and deleting an object.  The methods simply wrap the Swagger client code and provide some convenient conversion.

General usage
-------------
The nanites.client API is typically used in Informatics ifxdjango applications, and so takes advantage of the IFX_APP setting
for authentication.  Query parameters and post data can be specified as regular Python kwargs and plain Python objects
(not dicts) are returned::

    >>> from nanites.client import API
    >>> nice_people = API.listPeople(login='nice')
    >>> nice_people[0].full_name
    'Aaron J Kitzmiller'
    >>>
    >>> person_data = {
    ...     'first_name': 'Derpy',
    ...     'last_name': 'Derpiston',
    ...     'full_name': 'Derpy (Fred) Derpiston, Jr.',
    ...     'primary_email': 'dderpiston@gmail.com',
    ...     'change_comment': 'Initial entry',
    ...     'primary_affiliation': 'Slurpiston Lab (a Research Computing AD Laboratory)',
    ... }
    >>> new_person = API.createPerson(**person_data)


Configuration
-------------
The ``nanites.client.swagger.configuration`` file includes a couple of key modifications that make this client work for Informatics applications.
First the URL base for the REST API is set via ``ifxurls.urls.getIfxUrl`` so that the ``NANITES_API_ROOT`` environment variable is honored.

Second, as mentioned above the authentication token and application username are obtained from ``settings.IFX_APP``.
This ensures that the client is connecting by the appropriate application token.


A custom API Client can be used to change the default configuration
-------------------------------------------------------------------
The Configuration object is created as part of the APIClient setup.  So if a non-standard configuration is needed, a custom APIClient can be
passed to one of the functions::

    >>> from nanites.client.swagger import ApiClient, Configuration
    >>> from nanites.client import API
    >>> configuration = Configuration()
    >>> configuration.debug = True
    >>> api_client = ApiClient(configuration=configuration)
    >>> logins = API.listLogins(api_client=api_client)


404 and 401 Exceptions are translated
-------------------------------------
HTTP responses that include a 404 (Not Found) status code are converted to a plain exception with the text 'Item not found'.  Unauthorized
calls (401) are converted to exceptions including the text 'Not authorized to use'.

Other exceptions are passed on as is.


create<Obj>
-----------
The create method takes keyword arguments corresponding to object field names, creates the object via POST, and returns the object created.
For example, a simple Person object can be created::

    >>> from nanites.client import API
    >>> person_data = {
        'first_name': 'Derpy',
        'last_name': 'Derpiston',
        'full_name': 'Derpy (Fred) Derpiston, Jr.',
        'primary_email': 'dderpiston@gmail.com',
        'change_comment': 'Initial entry',
        'primary_affiliation': 'Slurpiston Lab (a Research Computing AD Laboratory)',
    }
    >>> person = API.createPerson(**person_data)

Whatever nested objects are supported by the REST API can be created as well::

    >>> from nanites.client import API
    >>> person_data = {
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
                'type': 'email',
                'detail': 'slurpy@hotmail.com',
            },
            {
                'type': 'phone',
                'detail': '123-1233'
            }
        ],
    }
    >>> person = API.createPerson(**person_data)


list<Obj>s
-----------
A list of objects can be pulled from Nanites, including either a complete list::

    >>> from nanites.client import API
    >>> logins = API.listLogins()

or using the available query parameters::

    >>> from nanites.client import API
    >>> logins = API.listLogins(primary_email='dderpiston@gmail.com')

The name of the list function uses the plural of the object.  This includes translation so listing Person objects is performed
with the ``listPeople`` function.

If no matching objects are found, an empty list is returned.

Pagination middleware is setup in the Nanites REST Framework settings.  By default the client API sets page size to
a very large number to ensure the full data set is returned.  However, you can set explicit page size and page number::

    >>> from nanites.client import API
    >>> logins = API.listLogins(page_size=100, page=1)

While this will not provide results one page at a time (plist is for that), it will ensure that large data sets do
not time out.

List operations can be passed an "ordering" parameter.  This is based on the
`Django REST Frameowork OrderingFilter <https://www.django-rest-framework.org/api-guide/filtering/#orderingfilter>`
and uses that syntax for ascending, descending, and multiple fields::

    >>> people = API.listPeople(login='nice', ordering='-last_name')
    >>> people[0].last_name
    'Zwicker'
    >>>


plist<Obj>s
-----------
The plist operation will returned paged results.  These are the unaltered output of the pages REST api calls
and so include count, prev, next, and results (the actual data)

    >>> from nanites.client import API
    >>> page_of_people = API.plistPeople(login='nice', page_size=10, page=1)
    >>> page_of_people.count
    1823
    >>> len(page_of_people.results)
    10

plist operations also support ordering::

    >>> page_of_people = API.plistPeople(login='nice', page_size=10, page=1, ordering='-last_name')
    >>> page_of_people.results[0].last_name
    'Zwicker'



update<Obj>
-----------
A single object can be updated.  A PUT operation is used so a complete object must be passed.  An "id" parameter is required.
Somewhat unintuitively, the Swagger object models returned by a create functions cannot be used directly for updates, but must
be converted into a dictionary of data::

    >>> from nanites.client import API
    >>> person = API.createPerson(**person_data)
    >>> person.full_name = 'A new full name'
    >>> person_dict = person.to_dict()
    >>> updatedPerson = API.updatePerson(**person_dict)

