# 06_Results_or_Expected_Output

## Purpose

This folder provides preliminary evidence that the group's proposed pipeline runs end-to-end, and describes the results and metrics expected once the full PhiUSIIL dataset is used for training and evaluation.

## Files in This Folder

| File | Description |
|---|---|
| `sample_extracted_features.csv` | Output of running `FEATUR_1.py` (`extract_website_features`) on every row of `05_Data_or_Sample_Input/sample_phishing_urls.csv`. Shows the four current features: `url_length`, `has_https`, `contains_at_symbol`, `suspicious_keyword`. |
| `preliminary_classification_results.csv` | Predicted vs. actual label for each URL in the held-out test split, produced by running `ENSEMB_1.py`'s soft-voting ensemble (Random Forest + Logistic Regression + SVM) on the extracted features. |
| `preliminary_evaluation_metrics.md` | Accuracy, precision, recall, F1-score, false positive rate, and confusion matrix from this preliminary run. |

## Important Note on This Preliminary Result

The current run reports **100% accuracy on a 9-row test split**. This is expected and **not representative of final performance** — it reflects three limitations of the current, illustrative stage rather than genuine detection strength:

1. **Sample size.** The sample dataset contains only 24 hand-crafted URLs, far too small to demonstrate real generalisation.
2. **Feature simplicity.** Only 4 lexical features are currently extracted (`url_length`, `has_https`, `contains_at_symbol`, `suspicious_keyword`). The synthetic phishing examples were deliberately written to contain obvious keywords, which the current feature set can separate almost perfectly.
3. **No domain/content features yet.** The domain-based and page-based features are planned but not yet implemented in `04_Source_Code/`.

This result should therefore be read only as **evidence that the pipeline works end-to-end**, not as a performance claim.

## Expected Outcome at Full-Scale Evaluation

Once the pipeline is run on the full PhiUSIIL dataset plus the PhishTank/Tranco validation sample, the group expects results broadly consistent with the ensemble/Random-Forest-based studies reviewed while specifically checking:

- Whether the ensemble model outperforms each individual base classifier on the same test split .
- Whether that performance margin is retained on the separate, more recent validation sample, as the concrete test of the "generalisation".

## Evaluation Metrics to Be Used (Full-Scale Evaluation)

| Metric | Purpose |
|---|---|
| Accuracy | Overall proportion of URLs correctly classified. |
| Precision | Proportion of URLs flagged as phishing that are actually phishing. |
| Recall | Proportion of actual phishing URLs successfully detected. |
| F1-score | Harmonic mean of precision and recall; primary comparison metric given possible class imbalance. |
| False Positive Rate | Proportion of legitimate URLs incorrectly flagged; a practical usability measure for a browsing context. |

## Expected System Interface

At demonstration stage, the prototype is expected to accept a URL as input, extract its features and return a classification label (Phishing / Legitimate) together with a confidence score derived from the ensemble's soft-voting probabilities.
