---
license: apache-2.0
library_name: peft
tags:
- generated_from_trainer
base_model: distilbert-base-uncased
metrics:
- f1
model-index:
- name: distilbert-base-uncased-lora-text-classification-safeguard-promptinjection
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased-lora-text-classification-safeguard-promptinjection

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0200
- F1: 0.9971
- Auprc: 0.9966

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
| 0.0598        | 1.0   | 1030 | 0.0220          | 0.9961 | 0.9946 |
| 0.0273        | 2.0   | 2060 | 0.0199          | 0.9961 | 0.9946 |
| 0.0321        | 3.0   | 3090 | 0.0334          | 0.9951 | 0.9945 |
| 0.0099        | 4.0   | 4120 | 0.0345          | 0.9937 | 0.9929 |
| 0.0059        | 5.0   | 5150 | 0.0200          | 0.9971 | 0.9966 |


### Framework versions

- PEFT 0.11.1
- Transformers 4.40.2
- Pytorch 2.3.0+cu118
- Datasets 2.19.2
- Tokenizers 0.19.1