#!/bin/bash

. /opt/spack/share/spack/setup-env.sh

if [ $# -eq 0 ]
then
 /bin/bash
else
 exec "${@}"
fi
