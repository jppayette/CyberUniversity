#!/bin/bash

read -p "Veuillez entrer une adresse IP à scanner : " ip


# Effectue un scan de port sur l'adresse IP avec nmap
nmap -p- $ip > resultat_scan.txt
