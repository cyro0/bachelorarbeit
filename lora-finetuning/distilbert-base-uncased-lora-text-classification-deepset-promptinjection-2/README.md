---
license: apache-2.0
library_name: peft
tags:
- generated_from_trainer
base_model: distilbert-base-uncased
metrics:
- f1
model-index:
- name: distilbert-base-uncased-lora-text-classification-deepset-promptinjection-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-lora-text-classification-deepset-promptinjection-2

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1816
- F1: 0.9483
- Auprc: 0.9494

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
| No log        | 1.0   | 69   | 0.1696          | 0.9396 | 0.9411 |
| No log        | 2.0   | 138  | 0.3368          | 0.9136 | 0.9161 |
| No log        | 3.0   | 207  | 0.2233          | 0.9483 | 0.9494 |
| No log        | 4.0   | 276  | 0.2551          | 0.9396 | 0.9411 |
| No log        | 5.0   | 345  | 0.1816          | 0.9483 | 0.9494 |


### Framework versions

- PEFT 0.11.1
- Transformers 4.40.2
- Pytorch 2.3.0+cu118
- Datasets 2.19.2
- Tokenizers 0.19.1