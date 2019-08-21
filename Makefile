#
# Make the swagger client
# Most of it gets generated in nanites/client/swagger, but for some reason, a nanites.client.swagger directory
# is also created.  Contents are copied to the correct location and the dir is removed.
#
PACKAGE_NAME=nanites.client.swagger

client:
	docker run --rm -v `pwd`:/api swaggerapi/swagger-codegen-cli generate -l python -i /api/schema/swagger.json -o /api --additional-properties packageName=$(PACKAGE_NAME)
	cp -r $(PACKAGE_NAME)/* nanites/client/swagger
	rm -rf $(PACKAGE_NAME)
