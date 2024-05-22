---
license: apache-2.0
library_name: peft
tags:
- generated_from_trainer
base_model: TheBloke/Mistral-7B-Instruct-v0.2-GPTQ
model-index:
- name: output
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [TheBloke/Mistral-7B-Instruct-v0.2-GPTQ](https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GPTQ) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6997

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

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 4.5908        | 0.92  | 3    | 3.9562          |
| 4.028         | 1.85  | 6    | 3.4157          |
| 3.4351        | 2.77  | 9    | 2.9484          |
| 2.2257        | 4.0   | 13   | 2.5235          |
| 2.6268        | 4.92  | 16   | 2.2715          |
| 2.289         | 5.85  | 19   | 2.0605          |
| 2.0218        | 6.77  | 22   | 1.8764          |
| 1.3978        | 8.0   | 26   | 1.7446          |
| 1.7683        | 8.92  | 29   | 1.7044          |
| 1.2368        | 9.23  | 30   | 1.6997          |


### Framework versions

- PEFT 0.10.0
- Transformers 4.39.3
- Pytorch 2.2.2+cu118
- Datasets 2.19.0
- Tokenizers 0.15.2