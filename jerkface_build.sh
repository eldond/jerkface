#!/bin/bash
# This script is meant to build jerkface

cp jerkface.spec ~/rpmbuild/SPECS/jerkface.spec
rm -rf ~/rpmbuild/SOURCES/jerkface*.tar.gz
tar -zcf ~/rpmbuild/SOURCES/jerkface-0.1.tar.gz --transform s/jerkface_source/jerkface-0.1/ jerkface_source
rpmbuild -ba ~/rpmbuild/SPECS/jerkface.spec
