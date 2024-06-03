---
license: apache-2.0
library_name: peft
tags:
- generated_from_trainer
base_model: distilbert-base-uncased
metrics:
- accuracy
model-index:
- name: distilbert-base-uncased-lora-text-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-lora-text-classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3417
- Accuracy: {'accuracy': 0.9568965517241379}

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy                         |
|:-------------:|:-----:|:----:|:---------------:|:--------------------------------:|
| No log        | 1.0   | 137  | 0.9158          | {'accuracy': 0.8706896551724138} |
| No log        | 2.0   | 274  | 0.7457          | {'accuracy': 0.8879310344827587} |
| No log        | 3.0   | 411  | 1.2790          | {'accuracy': 0.8879310344827587} |
| 0.2127        | 4.0   | 548  | 0.5679          | {'accuracy': 0.9310344827586207} |
| 0.2127        | 5.0   | 685  | 0.3807          | {'accuracy': 0.9396551724137931} |
| 0.2127        | 6.0   | 822  | 0.3014          | {'accuracy': 0.9568965517241379} |
| 0.2127        | 7.0   | 959  | 0.2646          | {'accuracy': 0.9655172413793104} |
| 0.0956        | 8.0   | 1096 | 0.2935          | {'accuracy': 0.9568965517241379} |
| 0.0956        | 9.0   | 1233 | 0.3156          | {'accuracy': 0.9655172413793104} |
| 0.0956        | 10.0  | 1370 | 0.3417          | {'accuracy': 0.9568965517241379} |


### Framework versions

- PEFT 0.11.1
- Transformers 4.40.2
- Pytorch 2.3.0+cu118
- Datasets 2.19.1
- Tokenizers 0.19.1