---
license: apache-2.0
library_name: peft
tags:
- generated_from_trainer
base_model: distilbert-base-uncased
metrics:
- f1
model-index:
- name: distilbert-base-uncased-lora-text-classification-toxicchat-jailbreak
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-lora-text-classification-toxicchat-jailbreak

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0311
- F1: 0.9936
- Auprc: 0.8224

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
| 0.088         | 1.0   | 636  | 0.0273          | 0.9934 | 0.8172 |
| 0.0436        | 2.0   | 1272 | 0.0372          | 0.9933 | 0.8174 |
| 0.0288        | 3.0   | 1908 | 0.0290          | 0.9920 | 0.7779 |
| 0.0154        | 4.0   | 2544 | 0.0324          | 0.9920 | 0.7978 |
| 0.0108        | 5.0   | 3180 | 0.0311          | 0.9936 | 0.8224 |


### Framework versions

- PEFT 0.11.1
- Transformers 4.40.2
- Pytorch 2.3.0+cu118
- Datasets 2.19.2
- Tokenizers 0.19.1