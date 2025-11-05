param(
    [string]$path,
    [int]$days = 30
)

Get-ChildItem -Path $path -Recurse |
    Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-$days) } |
    Remove-Item -Force
