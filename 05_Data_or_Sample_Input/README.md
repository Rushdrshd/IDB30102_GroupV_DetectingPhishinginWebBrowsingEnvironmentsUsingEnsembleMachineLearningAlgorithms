# 05_Data_or_Sample_Input

## Purpose

This folder provides supporting evidence of the data that will be used to develop and evaluate the proposed phishing website detection prototype. At the Research Proposal stage, only a small, illustrative sample is included here. The full dataset described below will be assembled during the Design and Development phase (Phase 3 of the DSRM, see Chapter 3 of the Research Proposal).

## Primary Dataset (to be used for full model training/evaluation)

- **Name:** PhiUSIIL Phishing URL Dataset
- **Authors:** Prasad, A., & Chandra, S. (2024)
- **Source:** UCI Machine Learning Repository
- **Link:** https://archive.ics.uci.edu/dataset/967/phiusiil+phishing+url+dataset
- **Description:** A large, recent benchmark dataset containing labelled legitimate and phishing URLs with pre-extracted lexical, host-based and content-based attributes.
- **Intended use:** Primary training and test source for the ensemble classification model.

## Supplementary Live Sources (for a recency/generalisation check)

- **PhishTank** — community-verified, continuously updated phishing URL feed. Link: https://phishtank.org
- **Tranco List** — research-oriented ranked list of popular, active legitimate domains. Link: https://tranco-list.eu

These two sources will be used only to draw a small, more recent validation sample (see Chapter 3, Section 3.8.3 of the Research Proposal), to check whether the model's performance generalises beyond the original PhiUSIIL distribution. Because their content is time-sensitive and third-party licensed, only the dataset names, sources and official links are provided here rather than bulk-downloaded copies, in line with the assignment's data-sharing guidance.

## Files in This Folder

| File | Description |
|---|---|
| `sample_phishing_urls.csv` | A small, synthetic/illustrative sample of 24 URLs (12 legitimate, 12 phishing-style) used only to demonstrate the data format and preprocessing/feature-extraction pipeline in `04_Source_Code/`. **These phishing-style entries are fabricated for demonstration purposes and are not real, live phishing URLs.** No genuine malicious infrastructure is referenced or linked. |

## Dataset Format

Each row contains:
- `url` — the website URL (string)
- `label` — `1` if phishing, `0` if legitimate

This format matches the input expected by `04_Source_Code/DATA_P_1.py` (`load_dataset`, `clean_dataset`) and `04_Source_Code/FEATUR_1.py` (`extract_website_features`).

## Note on Data Handling

No confidential, private, or restricted data is included in this folder. No live phishing website is accessed, scraped in real time, or interacted with as part of data collection — consistent with Section 3.7 (Ethical and Legal Considerations) of the Research Proposal.
