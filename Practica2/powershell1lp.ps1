function fecha
{
    param([int]$dia, [int]$mes, [int]$año)
    $fecha = Get-Date $dia'.'$mes'.'$año
    Write-Host "El dia es $fecha"
}