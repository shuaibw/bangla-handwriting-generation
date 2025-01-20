# Bangla Handwriting Synthesis
Base paper: [Handwriting Transformer](https://arxiv.org/abs/2104.03964)

Base repository: [Handwriting Transformer](https://github.com/ankanbhunia/Handwriting-Transformers)

## Environment Setup
This repository contains the code for Bangla handwriting synthesis using Handwriting Transformer. Run the following command to install the required environment:
```bash
conda env create --name hwt-env -f environment.yml
conda activate hwt-env
```

## Dataset Preparation
Run the following commands to download and prepare the dataset:
```bash
gdown 18Q55Y79O_ESm8sWFZx4RTlBbUykZ3Gwi # BN-EN-WORDS.txt
gdown 1JwztzCtnhQ0NuJDw5j4QeBbq-knzoX5G # BN-EN-IAM-MULTI.pickle
mkdir files
python prepare_data.py
mv BN-EN-WORDS.txt files/BN-EN-WORDS.txt
```

## WandB Login
Provide your WandB API key to log in and track the training process in real-time. When you start the training, it will ask for the API key. Copy and paste the key to the terminal.

## Training
```bash
python train.py
```

