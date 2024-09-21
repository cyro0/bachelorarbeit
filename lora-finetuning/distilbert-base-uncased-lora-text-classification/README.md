---
license: apache-2.0
library_name: peft
tags:
- generated_from_trainer
base_model: distilbert-base-uncased
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: distilbert-base-uncased-lora-text-classification
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-lora-text-classification

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7001
- Accuracy: 0.4828
- F1: 0.3144
- Precision: 0.2331
- Recall: 0.4828

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| No log        | 1.0   | 273  | 0.7032          | 0.4828   | 0.3144 | 0.2331    | 0.4828 |
| 0.6723        | 2.0   | 546  | 0.7017          | 0.4828   | 0.3144 | 0.2331    | 0.4828 |
| 0.6723        | 3.0   | 819  | 0.7008          | 0.4828   | 0.3144 | 0.2331    | 0.4828 |
| 0.6716        | 4.0   | 1092 | 0.7002          | 0.4828   | 0.3144 | 0.2331    | 0.4828 |
| 0.6716        | 5.0   | 1365 | 0.7001          | 0.4828   | 0.3144 | 0.2331    | 0.4828 |


### Framework versions

- PEFT 0.11.1
- Transformers 4.40.2
- Pytorch 2.3.0+cu118
- Datasets 2.19.2
- Tokenizers 0.19.1