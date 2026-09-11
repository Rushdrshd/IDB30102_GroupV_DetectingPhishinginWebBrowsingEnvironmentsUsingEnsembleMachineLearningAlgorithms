# 06_Results_or_Expected_Output

## Purpose

This folder provides preliminary evidence that the group's proposed pipeline (data preprocessing → feature extraction → ensemble classification, in `04_Source_Code/`) runs end-to-end, and describes the results and metrics expected once the full PhiUSIIL dataset (Section 05) is used for training and evaluation.

## Files in This Folder

| File | Description |
|---|---|
| `sample_extracted_features.csv` | Output of running `FEATUR_1.py` (`extract_website_features`) on every row of `05_Data_or_Sample_Input/sample_phishing_urls.csv`. Shows the four current features: `url_length`, `has_https`, `contains_at_symbol`, `suspicious_keyword`. |
| `preliminary_classification_results.csv` | Predicted vs. actual label for each URL in the held-out test split, produced by running `ENSEMB_1.py`'s soft-voting ensemble (Random Forest + Logistic Regression + SVM) on the extracted features. |
| `preliminary_evaluation_metrics.md` | Accuracy, precision, recall, F1-score, false positive rate, and confusion matrix from this preliminary run. |

## Important Note on This Preliminary Result

The current run reports **100% accuracy on a 9-row test split**. This is expected and **not representative of final performance** — it reflects three limitations of the current, illustrative stage rather than genuine detection strength:

1. **Sample size.** The sample dataset contains only 24 hand-crafted URLs (12 legitimate, 12 phishing-style), far too small to demonstrate real generalisation.
2. **Feature simplicity.** Only 4 lexical features are currently extracted (`url_length`, `has_https`, `contains_at_symbol`, `suspicious_keyword`). The synthetic phishing examples were deliberately written to contain obvious keywords (e.g., "login", "verify", "secure"), which the current feature set can separate almost perfectly.
3. **No domain/content features yet.** The domain-based (WHOIS age, DNS record) and page-based (favicon, external-link ratio) features described in Chapter 3, Section 3.6.2 of the Research Proposal are planned but not yet implemented in `04_Source_Code/`.

This result should therefore be read only as **evidence that the pipeline works end-to-end**, not as a performance claim.

## Expected Outcome at Full-Scale Evaluation

Once the pipeline is run on the full PhiUSIIL dataset plus the PhishTank/Tranco validation sample (Chapter 3, Section 3.8), the group expects results broadly consistent with the ensemble/Random-Forest-based studies reviewed in Chapter 2 (e.g., Alani & Tawfik, 2022, 97.5% accuracy; Albishri & Dessouky, 2024, 99.93–99.98% accuracy), while specifically checking:

- Whether the ensemble model (Random Forest + Logistic Regression + SVM, soft voting) outperforms each individual base classifier on the same test split (Research Objective 3).
- Whether that performance margin is retained on the separate, more recent validation sample, as the concrete test of the "generalisation" claim in Research Objective 2.

## Evaluation Metrics to Be Used (Full-Scale Evaluation)

| Metric | Purpose |
|---|---|
| Accuracy | Overall proportion of URLs correctly classified. |
| Precision | Proportion of URLs flagged as phishing that are actually phishing. |
| Recall | Proportion of actual phishing URLs successfully detected. |
| F1-score | Harmonic mean of precision and recall; primary comparison metric given possible class imbalance. |
| False Positive Rate | Proportion of legitimate URLs incorrectly flagged; a practical usability measure for a browsing context. |

## Expected System Interface (Description)

At demonstration stage (Phase 4 of the DSRM), the prototype is expected to accept a URL as input, extract its features, and return a classification label (Phishing / Legitimate) together with a confidence score derived from the ensemble's soft-voting probabilities — no interface screenshots exist yet, as the group has not started front-end/browser-extension development.
