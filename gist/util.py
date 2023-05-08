#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import sys

def list_safe_get(l, i, default):
    if i < len(l):
        return l[i]
    return default

def dict_map(d, func):
    for k in d:
        d[k] = func(d[k])
    return d

