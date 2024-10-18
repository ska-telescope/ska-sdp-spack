-include .make/base.mk
-include .make/oci.mk

set-registry-password:
	@sed -i "s={OCI_PASSWORD}=$(CI_REGISTRY_PASSWORD)=" images/ska-sdp-spack/Dockerfile

oci-pre-lint: set-registry-password

oci-pre-build: set-registry-password
