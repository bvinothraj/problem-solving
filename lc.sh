#!/bin/bash
# script to scaffold a new solution

if [ -n "$1" ] && [ -n "$2" ]; then
    cd leetcode
    mkdir $1_$2
    cd $1_$2
    touch $2.py
fi


