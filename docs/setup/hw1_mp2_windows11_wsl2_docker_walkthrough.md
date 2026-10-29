# HW 1 & MP 2 Setup Walkthrough: Windows 11 + WSL 2 + Docker Desktop DevContainer Bring-Up

This guide documents the complete end-to-end setup and verification protocol for [**HW 1**](../../assignments/homework/hw1_devcontainer_bringup_architecture.md) and **MP 2** under Windows 11, WSL 2, and Docker Desktop. Follow these steps to verify your container environment, pull the course runtime, and confirm strict manifest compatibility.

---

## 1. Prerequisites Checklist

Ensure your Windows 11 host environment meets or exceeds the following baseline specifications:

* **Operating System:** Windows 11 (Build `26200+` or higher)
* **WSL Kernel:** WSL 2 (Kernel version `6.18+` or higher)
* **IDE & Tooling:** VS Code with the *Dev Containers* extension installed
* **Hardware Virtualization:** Enabled in system BIOS/UEFI

To check your exact WSL configuration, run the following in PowerShell:
```powershell
wsl --status
```

---

## 2. Docker Desktop Configuration Walkthrough

Launch **Docker Desktop** on Windows 11 and configure the following settings based on the updated settings UI.

### Step 2.1: General Settings Verification
1. Open Docker Desktop and click the **Settings (gear icon)** in the top-right header.
2. Select **General** from the right-hand panel.
3. Verify or set the following key fields:
   * **Start Docker Desktop when you sign in to your computer:** `Off` *(or user preference)*
   * **Choose Virtual Machine Manager (VMM):** Set to `WSL 2`
   * **Use containerd for pulling and storing images:** Set to `On`

### Step 2.2: WSL Integration Enablement
1. In the Settings right-hand panel, select **WSL integration**.
2. Toggle **Enable integration with my default WSL distro** to `On`.
3. If you use additional non-default distributions, toggle them under **Enable integration with additional distros**.
4. Click **Apply & Restart Engine** at the bottom right to commit the daemon changes.

---

## 3. Terminal Verification (WSL 2 Client & Daemon Test)

Open your WSL 2 terminal (e.g., `bhsu@Holodoc`) and run the following verification commands.

### Step 3.1: Check Docker CLI Version
```bash
docker --version
```
**Expected Output:**
```text
Docker version 29.9.2, build a82e528
```

### Step 3.2: Verify Docker Daemon Communication
Run the lightweight `hello-world` test container:
```bash
docker run --rm hello-world
```

**Expected Output:**
```text
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
4f55086f7dd0: Pull complete
d5e71e642bf5: Download complete
Digest: sha256:c567b231f65614688711a75f31518a064258a51d442117a3e771a3a8fdba78ef
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.
```

---

## 4. MP 2 Environment Pinning & Digest Verification

To achieve strict manifest compliance for MP 2, deploy the starter `Dockerfile` and run the environment verification routine.

### Step 4.1: The Pinned Dockerfile (`Dockerfile`)
Ensure your repository root contains the exact pinned `Dockerfile`:

```dockerfile
# ==============================================================================
# CIS 531/731: Minimal DevContainer Dockerfile (MP2)
# ==============================================================================
FROM python:3.10-slim-bullseye

# 1. Install System Dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
 build-essential \
 openjdk-11-jre-headless \
 ffmpeg \
 git \
 sudo \
 && rm -rf /var/lib/apt/lists/*

# 2. Configure Environment Variables
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PYSPARK_PYTHON=python3
ENV PIP_NO_CACHE_DIR=1

# 3. Install Python Dependencies (Strict Pinned Versions per MP2 Manifest)
RUN pip install --upgrade pip && \
 pip install \
 pyspark==3.5.1 \
 torch==2.2.1 \
 transformers==4.38.2 \
 openai-whisper==20231117 \
 mlflow==2.11.1 \
 faiss-cpu==1.8.0

# 4. Create Non-Root User
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID
RUN groupadd --gid $USER_GID $USERNAME \
 && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -s /bin/bash \
 && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
 && chmod 0440 /etc/sudoers.d/$USERNAME

USER $USERNAME
WORKDIR /workspace
```

### Step 4.2: DevContainer Configuration (`.devcontainer/devcontainer.json`)
Create or verify `.devcontainer/devcontainer.json`:

```json
{
  "name": "CIS 531/731 MP2 Runtime",
  "build": {
    "dockerfile": "../Dockerfile",
    "context": ".."
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-toolsai.jupyter",
        "redhat.vscode-yaml"
      ]
    }
  },
  "remoteUser": "vscode",
  "updateRemoteUserUID": true
}
```

### Step 4.3: Execute Verification Script (`verify_env.py`)
Create `verify_env.py` in your project root:

```python
import hashlib
import sys

def verify_environment():
    try:
        import torch
        import transformers
        import mlflow
        import faiss
        import whisper
    except ImportError as e:
        print(f"FAILED: Missing module - {e}")
        return

    # Extract version string
    env_str = f"torch-{torch.__version__}_transformers-{transformers.__version__}_mlflow-{mlflow.__version__}_faiss-{faiss.__version__}"
    
    # Generate SHA-256 Digest
    digest = hashlib.sha256(env_str.encode('utf-8')).hexdigest()
    print(f"Environment String: {env_str}")
    print(f"SHA-256 Digest: {digest}")

if __name__ == "__main__":
    verify_environment()
```

### Step 4.4: Build Container & Compute Digest
Build the container and run `verify_env.py` directly:

```bash
# Build the image locally
docker build -t cis531-runtime:mp2 .

# Run the verification script inside the container
docker run --rm cis531-runtime:mp2 python verify_env.py
```

**Expected Verification Output:**
```text
Environment String: torch-2.2.1_transformers-4.38.2_mlflow-2.11.1_faiss-1.8.0
SHA-256 Digest: 6f0648c69f69b1faeb96cfecaa7e2a904ed9210c8c07e0b5dd13d2f9df25ff75
```
*(Note: Submit this exact digest string in your MP 2 report log as required by the autograding system).*

---

## 5. Part 2: Compute Allocation Probing (`probe_compute.py`)

To verify CUDA/GPU availability and compute routing, create and execute `probe_compute.py`:

```python
import torch

def probe_compute():
    if torch.cuda.is_available():
        device_name = torch.cuda.get_device_name(0)
        print(f"GPU Pool Active - Batch Embedding/Whisper Ready ({device_name})")
    else:
        print("CPU-Only Fallback Active")

if __name__ == "__main__":
    probe_compute()
```

Run inside your container environment:
```bash
docker run --rm cis531-runtime:mp2 python probe_compute.py
```

**Expected Output (on CPU-only DevContainer):**
```text
CPU-Only Fallback Active
```
