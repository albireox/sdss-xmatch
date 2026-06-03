#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import annotations

from sdsstools import get_package_version


# pip package name
NAME = "sdss_xmatch"

# package name should be pip package name
__version__ = get_package_version(path=__file__, package_name=NAME)
