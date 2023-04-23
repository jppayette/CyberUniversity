#!/bin/bash

read -p "Veuillez entrer une adresse IP à scanner : " ip

# Vérifie si l'hôte existe en utilisant la commande ping
if ! ping -c 1 $ip > /dev/null 2>&1 ; then
  echo "Hôte introuvable"
  exit 1
fi

nmap -p- $ip > resultat_scan.txt