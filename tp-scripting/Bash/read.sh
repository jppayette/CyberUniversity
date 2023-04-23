#!/bin/bash

read -p "Quelle est ta couleur favorite : " couleur

if [ "$couleur" = "bleu" ]; then
  echo "Chouette ! C'est aussi ma couleur favorite"
else
  echo "Zut ! T'as pas de gouts."
fi