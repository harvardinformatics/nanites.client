#
# Make the swagger client
#
PACKAGE_NAME=nanites.client.swagger

client:
	docker run --rm -v `pwd`:/api swaggerapi/swagger-codegen-cli generate -l python -i /api/schema/swagger.json -o /api --additional-properties packageName=$(PACKAGE_NAME)
	cp -r $(PACKAGE_NAME)/* nanites/client/swagger
	rm -rf $(PACKAGE_NAME)