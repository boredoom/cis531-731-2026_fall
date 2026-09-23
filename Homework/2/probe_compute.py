import torch

def check_compute():
    if torch.cuda.is_available():
        print("GPU Pool Active - Batch Embedding/Whisper Ready")
    else:
        print("CPU-Only Fallback Active")

if __name__ == "__main__":
    check_compute()