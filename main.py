#!/usr/bin/env python3
"""Cutest picture entry for make.fun bounty cutest-picture-01.

The program writes one picture to /output/entry.png: it copies the
entry.png beside this file, byte for byte. Python 3.13 standard library
only, no network, no randomness, no wall clock, no environment reads
other than MAKEFUN_OUTPUT_DIR: two runs write identical bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

_HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = os.path.join(_HERE, "entry.png")
_OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(_OUT_DIR, exist_ok=True)
shutil.copyfile(_SRC, os.path.join(_OUT_DIR, "entry.png"))
