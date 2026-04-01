$htmlFile = "d:\examen\modulo_estudio_interactivo.html"
$newItemsFile = "d:\examen\new_questions_interior.txt"

$htmlContent = Get-Content -Raw $htmlFile
$newItemsContent = Get-Content -Raw $newItemsFile
$target = "    ];"
$replacement = "        },`n" + $newItemsContent + "`n    ];"
$htmlContent = $htmlContent.Replace($target, $replacement)

Set-Content -Path $htmlFile -Value $htmlContent -Encoding UTF8
