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
- Loss: 0.1199
- Accuracy: {'accuracy': 0.9847328244274809}

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
| No log        | 1.0   | 261  | 0.3227          | {'accuracy': 0.9198473282442748} |
| 0.1636        | 2.0   | 522  | 0.0934          | {'accuracy': 0.9770992366412213} |
| 0.1636        | 3.0   | 783  | 0.1471          | {'accuracy': 0.9732824427480916} |
| 0.0306        | 4.0   | 1044 | 0.1081          | {'accuracy': 0.9847328244274809} |
| 0.0306        | 5.0   | 1305 | 0.1560          | {'accuracy': 0.9770992366412213} |
| 0.0           | 6.0   | 1566 | 0.1596          | {'accuracy': 0.9770992366412213} |
| 0.0           | 7.0   | 1827 | 0.1625          | {'accuracy': 0.9770992366412213} |
| 0.0           | 8.0   | 2088 | 0.1628          | {'accuracy': 0.9770992366412213} |
| 0.0           | 9.0   | 2349 | 0.1380          | {'accuracy': 0.9847328244274809} |
| 0.0           | 10.0  | 2610 | 0.1199          | {'accuracy': 0.9847328244274809} |


### Framework versions

- PEFT 0.11.1
- Transformers 4.40.2
- Pytorch 2.3.0+cu118
- Datasets 2.19.2
- Tokenizers 0.19.1