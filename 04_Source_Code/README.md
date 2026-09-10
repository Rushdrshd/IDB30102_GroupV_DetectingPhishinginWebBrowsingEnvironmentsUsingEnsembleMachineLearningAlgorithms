# Preliminary Source Code

## Research Title

**Detecting Phishing Websites in Web Browsing Environments Using Ensemble Machine Learning Algorithms**

---

## Overview

This folder contains preliminary technical components developed to demonstrate the feasibility and technical direction of the proposed phishing website detection research.

The source code focuses on the early development stages of the proposed framework, including dataset preparation, website feature extraction, and ensemble machine learning model structure.

The implementation provided in this repository represents a proof-of-concept and does not represent the final completed phishing detection system.

---

## Source Code Components

### 1. Data Preprocessing

File:
`data_preprocessing.py`

Purpose:
- Load phishing website datasets
- Remove duplicate records
- Handle missing data
- Prepare datasets before feature extraction and classification


---

### 2. Website Feature Extraction

File:
`feature_extraction.py`

Purpose:

Extract relevant website-based features that may indicate phishing behaviour.

Examples of extracted features:
- URL length
- HTTPS availability
- Special character usage
- Suspicious keyword presence


---

### 3. Ensemble Machine Learning Model Structure

File:
`ensemble_model_structure.py`

Purpose:

Demonstrates the proposed ensemble machine learning classification approach.

The model structure combines multiple machine learning classifiers to improve phishing website classification capability.

Algorithms included:
- Random Forest
- Support Vector Machine (SVM)
- Logistic Regression


---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn


---

## External Source Acknowledgement

An open-source phishing detection project was reviewed as a technical reference.

The source acknowledgement and licence information are provided in:

`external_source_acknowledgement.md`


---

## Research Contribution

The technical components in this folder support the proposed research direction by demonstrating:

1. Dataset preparation approach
2. Website feature extraction concept
3. Ensemble machine learning classification structure

These components will support future implementation and evaluation of the proposed phishing website detection framework.