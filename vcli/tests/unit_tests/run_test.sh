#!/bin/bash
#
#
# (c) Copyright 2021 Micro Focus or one of its affiliates.
#
#

dir=$(pwd)
project_root=$dir/../../


# install requirements.txt
pip3 install -r requirements.txt

# start execute unit test
pytest --cov=$project_root . $@


# start generate coverage report
# pytest --cov=$project_root --cov-report=html . $@
