-include .make/base.mk
-include .make/oci.mk

set-registry-password:
	@if [ -z "$(CI)" ]; then \
		echo 'oci-* targets currently only work on CI'; \
		exit 1; \
	fi
	@sed -i "s={OCI_PASSWORD}=$(CI_REGISTRY_PASSWORD)=" images/ska-sdp-spack/Dockerfile

oci-pre-lint: set-registry-password

oci-pre-build: set-registry-password
