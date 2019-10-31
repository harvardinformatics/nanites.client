nanites.client
==============

Nanites client is a Python client API for the Nanites REST endpoints.  It is a combination of generated
Swagger API code and a wrapper that should shield applications from changes in Swagger output.

Installation can be done via pip.  Most of the Informatics applications install via pip call in the Dockerfile::

    RUN pip install --upgrade pip && \
        ...
        pip install git+https://github.com/harvardinformatics/nanites.client.git@aa1db152debf3606f04a18d3a8a13f61aafdc5f0

Swagger client code can be rebuilt by updating the swagger.json file in the schema directory and using the Makefile.
A swagger-codegen-cli container does the heavy lifting::

    $ make client
    docker run --rm -v `pwd`:/api swaggerapi/swagger-codegen-cli generate -l python -i /api/schema/swagger.json -o /api --additional-properties packageName=nanites.client.swagger
    [main] INFO io.swagger.parser.Swagger20Parser - reading from /api/schema/swagger.json
    [main] INFO io.swagger.codegen.AbstractGenerator - writing file /api/nanites/client/swagger/models/address.py
    [main] INFO io.swagger.codegen.DefaultGenerator - Skipped generation of /api/test/test_address.py due to rule in .swagger-codegen-ignore

The ``.swagger-codegen-ignore`` file is important for avoiding clobbering some key files including ``nanites.client.swagger.configuration``


.. toctree::
   :maxdepth: 2
   :caption: Contents:

    Client API <client-api>
    Modules <modules>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
