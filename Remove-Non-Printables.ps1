$file = $args[0]

(Get-Content -Path $file) |
ForEach-Object {$_ -Replace '[\x00-\x08]+', ''} |
ForEach-Object {$_ -Replace '[\x0B-\x0C]+', ''} |
ForEach-Object {$_ -Replace '[\x0E-\x1F]+', ''} |
Set-Content -Path $file
