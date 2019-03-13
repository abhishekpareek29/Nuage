https://travis-ci.com/abhishekpareek29/Nuage.svg?token=tTiVGqyKDszVyzMomxYq&branch=master

# Instructions

RUN: python3 nuage.py ./dir1/dir2/dir3/dir4/input.yaml

# Requirements

import sys
import os
import yaml

# Test Case
RUN: python3 test.py

# Dummy directory structure
dir1
|__input.yaml
|__dir2
    |___dir3
          |____input.yaml
          |____dir4
                 |___input.yaml
