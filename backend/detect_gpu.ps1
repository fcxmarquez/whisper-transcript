$envFile = "./backend/.env"  # Path to the .env file in the backend directory

# Function to set or replace a variable in the .env file
function Set-EnvVar {
    param(
        [string]$VarName,
        [string]$VarValue
    )
    if (Select-String -Path $envFile -Pattern "^$VarName=") {
        (Get-Content $envFile) -replace "^$VarName=.*", "$VarName=$VarValue" | Set-Content $envFile
    }
    else {
        Add-Content -Path $envFile -Value "$VarName=$VarValue"
    }
}

# Ensure the .env file exists
if (-not (Test-Path $envFile)) {
    New-Item -ItemType File -Path $envFile | Out-Null
}

"" | Add-Content -Path $envFile  # Add a newline

if (Get-Command "nvidia-smi" -ErrorAction SilentlyContinue) {
    Write-Output "NVIDIA GPU detected"
    Set-EnvVar -VarName "GPU_DOCKERFILE" -VarValue "Dockerfile.nvidia"
    Set-EnvVar -VarName "GPU_DRIVER" -VarValue "nvidia"
    Set-EnvVar -VarName "GPU_GROUP" -VarValue "video"
}
elseif (Get-Command "rocm-smi" -ErrorAction SilentlyContinue) {
    Write-Output "AMD GPU detected"
    Set-EnvVar -VarName "GPU_DOCKERFILE" -VarValue "Dockerfile.amd"
    Set-EnvVar -VarName "GPU_DRIVER" -VarValue "amd"
    Set-EnvVar -VarName "GPU_GROUP" -VarValue "video"
}
else {
    Write-Output "No supported GPU detected, defaulting to CPU"
    Set-EnvVar -VarName "GPU_DOCKERFILE" -VarValue "Dockerfile.cpu"
    Set-EnvVar -VarName "GPU_DRIVER" -VarValue "none"
    Set-EnvVar -VarName "GPU_GROUP" -VarValue "video"
}
