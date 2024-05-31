---
license: apache-2.0
library_name: peft
tags:
- generated_from_trainer
base_model: TheBloke/TinyLlama-1.1B-Chat-v0.3-GPTQ
model-index:
- name: shawgpt-ft
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# shawgpt-ft

This model is a fine-tuned version of [TheBloke/TinyLlama-1.1B-Chat-v0.3-GPTQ](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v0.3-GPTQ) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.1140

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss |
|:-------------:|:------:|:----:|:---------------:|
| 3.8374        | 0.9231 | 3    | 3.4520          |
| 3.7784        | 1.8462 | 6    | 3.4074          |
| 3.7231        | 2.7692 | 9    | 3.3566          |
| 2.7433        | 4.0    | 13   | 3.2875          |
| 3.601         | 4.9231 | 16   | 3.2389          |
| 3.5324        | 5.8462 | 19   | 3.1956          |
| 3.4831        | 6.7692 | 22   | 3.1602          |
| 2.572         | 8.0    | 26   | 3.1274          |
| 3.4051        | 8.9231 | 29   | 3.1155          |
| 2.3241        | 9.2308 | 30   | 3.1140          |


### Framework versions

- PEFT 0.11.1
- Transformers 4.40.2
- Pytorch 2.3.0+cu118
- Datasets 2.19.1
- Tokenizers 0.19.1