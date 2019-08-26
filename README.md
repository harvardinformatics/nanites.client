# nanites.client
This package is a client API for the Nanites REST endpoints.  In current form, there is Swagger client code
created with the Nanites swagger.json endpoint and the swagger-codegen Docker container.  This is
wrapped in a SwaggerClient class that maps the various swagger bits in a bit of insulation.

## Installation
Probably should be able to just do a python setup.py install, but I haven't tried it yet.

## Testing
The Dockerfile and docker-compose.yml are setup to run tests against a Nanites, Nanites DB combination.
It runs like a Django application (i.e. ./manage.py test)

docker-compose up is a little difficult to read, so I often just run

    $ docker-compose run client

to see only the test output.  Sometimes, the REST API isn't quite ready when the client starts testing and you'll
see a bunch of timeouts.  Just run the client again and it should clear up.

## Rebuilding the Swagger code
If the Nanites REST changes, the Swagger code can be rebuilt using the Makefile that is included.  Just

    $ make

should do it.  This runs the swagger-codegen container on the schema/swagger.json file.  It also cleans up some odd
artifacts left by the process

## The Client
The SwaggerClient class maps the swagger object and function calls to a generic set of API functions.  These
functions represent each of a set of standard operations on each of the "models", namely list, read, create, update, delete.
For example, to work with Nanites Person objects:

```python

from nanites.client import API

personlist = API.listPeople()

person = API.createPerson(
    first_name='Vera',
    last_name='Min',
    full_name='Vera D. Min',
    primary_email='vera@hotmail',
    primary_affiliation='Harvard FAS Informatics',
)

# Yeah this is a bit ugly
person.primary_email = 'vera2@gmail.com'
persondata = person.to_dict()
API.updatePerson(**persondata)

API.deletePerson(id=person.id)