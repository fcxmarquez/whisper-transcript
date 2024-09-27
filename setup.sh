#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Detect GPU
if command_exists nvidia-smi; then
    echo "NVIDIA GPU detected."
    GPU_TYPE="nvidia"
elif command_exists rocm-smi; then
    echo "AMD GPU detected."
    GPU_TYPE="amd"
else
    echo "No GPU detected. Using CPU."
    GPU_TYPE="cpu"
fi

# Make detect_gpu.sh executable and run it
chmod +x ./detect_gpu.sh && ./detect_gpu.sh

# Change to backend directory
cd backend

# Run docker-compose with appropriate configuration
if [ "$GPU_TYPE" = "cpu" ]; then
    echo "Starting containers for CPU environment..."
    docker-compose up --build
else
    echo "Starting containers for GPU environment..."
    docker-compose -f docker-compose.yml -f docker-compose.gpu.yml up --build
fi
