# ⚙️ Setup 

## 🚀 One Command Setup

*(Assuming you have a script for this)*

## 🧰 Fine-Grained Setup

### Backend Setup

> ⚠️ Before running the GPU detection script, make sure `nvidia-smi` or `rocm-smi` is installed to correctly detect the GPU.

1. **Run the GPU detection script from the root directory**:

   - On Linux and macOS:

     ```bash
     chmod +x ./detect_gpu.sh && ./detect_gpu.sh
     ```

   - On Windows:

     ```powershell
     .\detect_gpu.ps1
     ```

2. **Build and run the Docker containers from the `backend` directory**:

   - **For GPU environments**:

     ```bash
     cd backend
     docker-compose -f docker-compose.yml -f docker-compose.gpu.yml up --build
     ```

   - **For CPU environments**:

     ```bash
     cd backend
     docker-compose up --build
     ```

> ⚠️ Warning: The AMD Dockerfile is not tested yet.
### Frontend setup

1. Go to the frontend directory:
```bash
cd frontend
```

2. Setup the frontend by running npm install:

```bash
npm install
```

3. Run the frontend:

In development mode:
```bash
npm run dev
```

In production mode:
```bash
npm run build && npm run preview
```
