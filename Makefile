#
# Make the swagger client
# Most of it gets generated in nanites/client/swagger, but for some reason, a nanites.client.swagger directory
# is also created.  Contents are copied to the correct location and the dir is removed.
#
PACKAGE_NAME=nanites.client.swagger
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXAPIDOC  = sphinx-apidoc
SOURCEDIR     = docs/src
BUILDDIR      = docs/build

client:
	docker run --rm -v `pwd`:/api swaggerapi/swagger-codegen-cli generate -l python -i /api/schema/swagger.json -o /api --additional-properties packageName=$(PACKAGE_NAME)
	cp -r $(PACKAGE_NAME)/* nanites/client/swagger
	rm -rf $(PACKAGE_NAME)
	echo 'Reverting PersonChange due to incorrect author and comment rules' && git checkout nanites/client/swagger/models/person_change.py


help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help test Makefile docs clean

test: clean
	docker build -t nanites-client .
	docker-compose run client; docker-compose down

docs:
	docker-compose run client make html; docker-compose down
clean:
	find . -name "*.pyc" -print0 | xargs -0 rm -f

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXAPIDOC) -e -M --force -o "$(SOURCEDIR)" nanites
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
