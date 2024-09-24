# HuggingFace Workshop

This workshop is designed for GDSC AI Team & NetAI Lab.

> check [Usage](#Usage) for setting up the environment

## Workshop

This workshop covers the following topics:

- Pipeline API for NLP tasks (`transformers_pipeline.ipynb`)
- Diffuser API for text-to-image generation (`diffuser.ipynb`)
- How to fine-tune a bert-base model on a custom dataset (`transformers_finetune.ipynb`)
- How to use the LLM(Llama) (`llama.ipynb`)

## Usage

create a virtual environment via conda

```shell
conda create -n huggingface-api python=3.12
```

```shell
conda activate huggingface-api
```

```shell
conda install nvidia/label/cuda-12.1.0::cuda-toolkit
```

```shell
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
```

```shell
pip install huggingface_hub transformers datasets
```

## Offical Documents for HuggingFace

- [Transformers](https://huggingface.co/docs/transformers/)
- [Diffusers](https://huggingface.co/docs/diffusers/)
- [Datasets](https://huggingface.co/datasets/)
