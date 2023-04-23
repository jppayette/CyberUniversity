function list_file_hash {
    $path = Get-ChildItem -Path "." -Recurse -Filter *.exe | Select-Object -ExpandProperty FullName
    # Write-Host("path : " , $path)

 
    "| Fichier`t`t`t`t | Nombre de ligne `t | Hash `t`t |" | Out-File -Append -FilePath "output_advanced.txt"

    foreach ($file in $path) {
     # Write-Host("file : " , $file)
    
        # Récupération du nombre de lignes
        $lines = Get-Content $file | Measure-Object -Line | Select-Object -ExpandProperty Lines
        # Write-Host("lines : " , $lines)
    
        # Calcul du hash SHA-256
        $hash = Get-FileHash $file -Algorithm SHA256 | Select-Object -ExpandProperty Hash
        # Write-Host("hash : " , $hash)

        # Construction de la chaîne à sauvegarder dans le fichier texte
        $output = "| $file | $lines Hash SHA-256 | $hash |"
        Write-Host("output : " , $output)
    
    
        # Sauvegarde dans un fichier texte
        $output | Out-File -Append -FilePath "output_advanced.txt"
    }

}

list_file_hash
