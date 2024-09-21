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
- Loss: 0.1017
- Accuracy: 0.9821
- F1: 0.9732
- Precision: 0.9645
- Recall: 0.9821

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

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 0.1169        | 1.0   | 2541  | 0.1062          | 0.9821   | 0.9732 | 0.9645    | 0.9821 |
| 0.0992        | 2.0   | 5082  | 0.0910          | 0.9821   | 0.9732 | 0.9645    | 0.9821 |
| 0.105         | 3.0   | 7623  | 0.0976          | 0.9821   | 0.9732 | 0.9645    | 0.9821 |
| 0.1189        | 4.0   | 10164 | 0.1009          | 0.9821   | 0.9732 | 0.9645    | 0.9821 |
| 0.1048        | 5.0   | 12705 | 0.1017          | 0.9821   | 0.9732 | 0.9645    | 0.9821 |


### Framework versions

- PEFT 0.11.1
- Transformers 4.40.2
- Pytorch 2.3.0+cu118
- Datasets 2.19.2
- Tokenizers 0.19.1