#!/bin/bash
ip=$(ip a | grep global | awk '{print $2;}' | sed -n 's/\/.*//p')
echo $ip
