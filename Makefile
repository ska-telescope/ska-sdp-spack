PYTHON_LINT_TARGET = packages/wsclean/package.py
PYTHON_SWITCHES_FOR_PYLINT = --disable=import-error,missing-module-docstring,missing-function-docstring

-include .make/base.mk
-include .make/oci.mk
-include .make/python.mk

set-registry-password:
	@if [ -z "$(CI)" ]; then \
		echo 'oci-* targets currently only work on CI'; \
		exit 1; \
	fi
	@sed -i "s={OCI_PASSWORD}=$(CI_REGISTRY_PASSWORD)=" images/ska-sdp-spack/Dockerfile

oci-pre-lint: set-registry-password

oci-pre-build: set-registry-password

oci-post-build:
# These Smoke tests run DP3 and wsclean using the created image.
# Use the same tag as ociImageBuild
	@if [[ "$(CAR_OCI_REGISTRY_HOST)" == registry.gitlab.com* ]] || [[ -z "$(CAR_OCI_REGISTRY_HOST)" ]]; then \
		OCI_TAG=$(VERSION)-dev.c$(CI_COMMIT_SHORT_SHA); \
	else \
		OCI_TAG=$(VERSION); \
	fi; \
	$(OCI_BUILDER) run --rm -t $(OCI_IMAGE):$${OCI_TAG} DP3 -v && \
	$(OCI_BUILDER) run --rm -t $(OCI_IMAGE):$${OCI_TAG} wsclean -version
