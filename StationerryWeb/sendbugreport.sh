#!/bin/bash

perl -p -i -e 's/\n/\\n/' $1
truncate -s -2 $1
java Comm $1
