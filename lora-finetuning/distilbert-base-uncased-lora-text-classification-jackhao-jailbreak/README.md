---
license: apache-2.0
library_name: peft
tags:
- generated_from_trainer
base_model: distilbert-base-uncased
metrics:
- f1
model-index:
- name: distilbert-base-uncased-lora-text-classification-jackhao-jailbreak
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-lora-text-classification-jackhao-jailbreak

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0744
- F1: 0.9809
- Auprc: 0.9877

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | Auprc  |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| No log        | 1.0   | 131  | 0.1594          | 0.9313 | 0.9696 |
| No log        | 2.0   | 262  | 0.0829          | 0.9847 | 0.9894 |
| No log        | 3.0   | 393  | 0.0571          | 0.9809 | 0.9877 |
| 0.0806        | 4.0   | 524  | 0.0699          | 0.9847 | 0.9894 |
| 0.0806        | 5.0   | 655  | 0.0744          | 0.9809 | 0.9877 |


### Framework versions

- PEFT 0.11.1
- Transformers 4.40.2
- Pytorch 2.3.0+cu118
- Datasets 2.19.2
- Tokenizers 0.19.1