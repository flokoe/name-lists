#!/usr/bin/env python3

import os, random

random_file_name = random.choice(os.listdir("./lists/"))
path = "lists/" + random_file_name

with open(path, "r") as file:
    lines = file.read().splitlines()
    line =  random.choice(lines)
    print(line)
