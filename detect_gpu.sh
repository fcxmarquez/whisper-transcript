#!/bin/bash

ENV_FILE="./backend/.env"  # Path to the .env file in the backend directory

# Function to set or replace a variable in the .env file
set_env_var() {
    local var_name="$1"
    local var_value="$2"
    if grep -q "^${var_name}=" "$ENV_FILE"; then
        sed -i "s|^${var_name}=.*|${var_name}=${var_value}|" "$ENV_FILE"
    else
        echo "${var_name}=${var_value}" >> "$ENV_FILE"
    fi
}

# Ensure the .env file exists
touch "$ENV_FILE"

echo "" >> "$ENV_FILE"  # Add a newline

if command -v nvidia-smi &> /dev/null
then
    echo "NVIDIA GPU detected"
    set_env_var "GPU_DOCKERFILE" "Dockerfile.nvidia"
    set_env_var "GPU_DRIVER" "nvidia"
    set_env_var "GPU_GROUP" "video"
elif command -v rocm-smi &> /dev/null
then
    echo "AMD GPU detected"
    set_env_var "GPU_DOCKERFILE" "Dockerfile.amd"
    set_env_var "GPU_DRIVER" "amd"
    set_env_var "GPU_GROUP" "video"
else
    echo "No supported GPU detected, defaulting to CPU"
    set_env_var "GPU_DOCKERFILE" "Dockerfile.cpu"
    set_env_var "GPU_DRIVER" "none"
    set_env_var "GPU_GROUP" "video"
fi
