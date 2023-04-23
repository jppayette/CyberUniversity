#!/bin/bash

read -p "Quel est le nom du fichier : " fichier

cat /etc/shadow | awk -F :  '{print $1 " | " $2}' >> $fichier