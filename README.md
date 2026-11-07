# FastSpeech 2 – English and Telugu Text-to-Speech

This repository contains my implementation, adaptation, training, inference, and evaluation of **FastSpeech 2 for English and Telugu Text-to-Speech (TTS)** as part of the **LTRC, IIIT Hyderabad Intern/Research Assistant assignment**.

## Project Overview

The objective of this work was to adapt the FastSpeech 2 TTS system for two languages:

- **English** using the Svarah dataset
- **Telugu** using the IndicTTS Telugu dataset

The work includes dataset preparation, text processing, MFA forced alignment, language-specific phoneme handling, model training, speech synthesis, and variance-adaptor analysis.

## Work Completed

The following work was completed:

- Adapted the FastSpeech 2 PyTorch implementation.
- Prepared separate English and Telugu datasets.
- Created training and validation data selections.
- Performed speech and text preprocessing.
- Performed Montreal Forced Aligner (MFA) alignment.
- Added Svarah English phoneme/symbol support.
- Added Telugu phoneme/symbol support.
- Created a custom Telugu MFA pronunciation dictionary.
- Used eSpeak-NG for Telugu pronunciation support.
- Modified text processing for Telugu and non-English text.
- Trained separate FastSpeech 2 models for English and Telugu.
- Generated speech samples for both languages.
- Extracted duration, pitch, and energy predictions from the variance adaptor.
- Generated duration, pitch, and energy plots for the test sentences.
- Compared English and Telugu training and validation losses.
- Analyzed speech quality and variance-adaptor behavior.

## Datasets

### English – Svarah

Approximately 5 hours of training data and 1 hour of validation data were selected.

- Selected training files: **3449**
- Selected validation files: **695**
- Usable aligned training files: **3438**
- Usable aligned validation files: **691**

### Telugu – IndicTTS

Approximately 5 hours of training data and 1 hour of validation data were selected.

- Selected training files: **1167**
- Selected validation files: **201**
- Usable aligned training files: **1160**
- Usable aligned validation files: **198**

Training and validation data were kept separate to avoid overlap.

## Telugu Language Adaptation

Telugu required additional language-specific processing compared with the original FastSpeech2 implementation.

The following adaptations were performed:

- Added Telugu phoneme and symbol support.
- Prepared Telugu text-to-phoneme mappings.
- Created a custom MFA pronunciation dictionary.
- Used eSpeak-NG for Telugu pronunciation support.
- Performed MFA forced alignment for Telugu speech and transcripts.
- Added Telugu-specific preprocessing.
- Updated text processing to handle non-English/non-Mandarin input.
- Extracted Telugu duration, pitch, and energy information.
- Generated Telugu variance-adaptor visualizations.

## Model Configuration

The main FastSpeech2 configuration used for the experiments was:

| Parameter | Value |
|---|---:|
| Sampling rate | 22050 Hz |
| Mel channels | 80 |
| Encoder layers | 4 |
| Decoder layers | 6 |
| Hidden dimension | 256 |
| Attention heads | 2 |
| Variance adaptor filter size | 256 |
| Variance adaptor kernel size | 3 |
| Dropout | 0.5 |
| Batch size | 2 |
| Training steps | 1000 |
| Random seed | 42 |
| Hardware | CPU |

Separate English and Telugu checkpoints were trained.

## Training Results

### English

Final validation losses at step 1000:

- Total loss: **4.9607**
- Mel loss: **1.2817**
- Mel PostNet loss: **1.2940**
- Pitch loss: **1.1246**
- Energy loss: **0.9701**
- Duration loss: **0.2902**

### Telugu

Final validation losses at step 1000:

- Total loss: **6.0723**
- Mel loss: **1.9271**
- Mel PostNet loss: **1.9166**
- Pitch loss: **1.0469**
- Energy loss: **0.8957**
- Duration loss: **0.2859**

The Telugu model has a higher overall validation loss than the English model. The main difference comes from the mel-spectrogram and PostNet losses, while pitch, energy, and duration losses are comparable.

## Generated Speech

Five test speech samples were generated for each language.

### English

- E1
- E2a
- E2b
- E3
- E4

Generated audio files are available under:

`Results/English/test_generated_audios/`

### Telugu

- T1
- T2a
- T2b
- T3
- T4

Generated audio files are available under:

`Results/Telugu/test_generated_audios/`

## Variance Adaptor Analysis

The variance adaptor was analyzed using three predicted features:

### Duration

Duration predictions indicate the number of acoustic frames assigned to phonemes/tokens. The English examples generally show short predicted durations with some longer durations for specific words and sentence endings.

### Pitch

Pitch predictions show the variation of fundamental frequency across the utterance. They provide information about intonation and prosodic variation.

### Energy

Energy predictions show the relative loudness/emphasis pattern across the utterance. Changes in energy can indicate stressed or prominent regions.

The corresponding plots are available in:

```text
Results/English/variance_adaptor_plots/
Results/Telugu/variance_adaptor_plots/
```

with separate directories for:

```text
duration/
pitch/
energy/
```

## Results Directory

```text
Results/
├── English/
│   ├── training_loss.png
│   ├── validation_loss.png
│   ├── test_generated_audios/
│   └── variance_adaptor_plots/
│       ├── duration/
│       ├── pitch/
│       └── energy/
│
└── Telugu/
    ├── training_loss.png
    ├── validation_loss.png
    ├── test_generated_audios/
    └── variance_adaptor_plots/
        ├── duration/
        ├── pitch/
        └── energy/
```

## Trained Checkpoints

The trained FastSpeech2 checkpoints are included using **Git LFS**:

```text
output/ckpt/Svarah/1000.pth.tar
output/ckpt/IndicTTS_Telugu/1000.pth.tar
```

The checkpoints correspond to the English Svarah and Telugu IndicTTS models trained during this assignment.

## Important Modified Files

The main implementation changes are present in:

```text
audio/
preprocessor/
text/
utils/
synthesize.py
```

Additional preprocessing, training, alignment, configuration, and inference files are included in the repository.

## Repository Structure

```text
FastSpeech2/
├── Results/
├── audio/
├── config/
├── demo/
├── hifigan/
├── img/
├── lexicon/
├── model/
├── output/
│   └── ckpt/
│       ├── Svarah/
│       └── IndicTTS_Telugu/
├── preprocessed_data/
├── preprocessor/
├── text/
├── transformer/
├── utils/
├── dataset.py
├── prepare_align.py
├── preprocess.py
├── synthesize.py
├── train.py
├── requirements.txt
├── .gitattributes
├── .gitignore
└── README.md
```

## Technical Report

The technical report documents:

- FastSpeech2 architecture and implementation
- Code modifications
- English and Telugu dataset preparation
- Dataset selection and train/validation split
- Preprocessing
- MFA alignment
- Telugu language adaptation
- Training configuration
- Training and validation loss analysis
- Generated speech observations
- Duration analysis
- Pitch analysis
- Energy analysis
- English versus Telugu comparison
- Limitations
- Possible improvements
- Reproducibility information

## Reproducibility

The experiments were performed in **Ubuntu on WSL2** using a dedicated Conda environment.

Main tools used:

- Python
- PyTorch
- FastSpeech 2
- Montreal Forced Aligner (MFA)
- eSpeak-NG
- HiFi-GAN
- Git
- Git LFS

The required Python dependencies are provided in:

```text
requirements.txt
```

## Acknowledgement

This project is based on the original FastSpeech 2 PyTorch implementation. The original implementation and FastSpeech2 research work are acknowledged as the foundation of this assignment.

The repository contains the modifications, English and Telugu language adaptations, dataset preparation, MFA alignment, model training, inference, generated results, and variance-adaptor analysis performed for this assignment.
