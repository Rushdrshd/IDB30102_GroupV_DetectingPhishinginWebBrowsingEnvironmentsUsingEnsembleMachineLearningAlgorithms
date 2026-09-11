# Research Paper Summary — 01_Research_Papers_1

| Item | Details |
|---|---|
| **Paper Title** | Phishing Attacks Detection Using Ensemble Machine Learning Algorithms |
| **Author(s)** | Nisreen Innab, Ahmed Abdelgader Fadol Osman, Mohammed Awad Mohammed Ataelfadiel, Marwan Abu-Zanona, Bassam Mohammad Elzaghmouri, Farah H. Zawaideh, Mouiad Fadeil Alawneh |
| **Year** | 2024 |
| **Source** | *Computers, Materials & Continua*, Vol. 80, No. 1, pp. 1325–1345. DOI: [10.32604/cmc.2024.051778](https://doi.org/10.32604/cmc.2024.051778) |
| **Research Problem** | Phishing attacks are increasing in frequency and sophistication, making it harder for traditional rule-based methods and manual detection to reliably distinguish phishing websites from legitimate ones. |
| **Method / Technique** | Compared seven machine learning classifiers — Decision Tree, Random Forest, Gradient Boosting, XGBoost, AdaBoost, Multi-Layer Perceptron, and a proposed hard-voting Ensemble (Voting) classifier combining Random Forest, XGBoost, and MLP. Data was preprocessed using Min-Max normalization; models were evaluated with a 90/10 train-test split. |
| **Dataset / Tools** | Two public phishing datasets from Kaggle: (1) 11,055 website instances with 32 URL/website-based features; (2) 10,000 website instances with 50 features. Implemented in Python (scikit-learn, MinMaxScaler) in an Anaconda environment. |
| **Main Findings** | The Voting ensemble classifier achieved the best results on Dataset 1 (accuracy 0.978, precision 0.975, recall 0.987, F1-score 0.981), outperforming all individual classifiers and prior published work on the same dataset. On Dataset 2, nearly all algorithms achieved near-perfect scores (accuracy ≈ 1.0), suggesting the dataset was comparatively easier to classify. |
| **Limitation** | The near-identical, near-perfect results on Dataset 2 raise concerns about potential overfitting or an overly separable dataset, limiting how much can be concluded from it. The study relies only on structured/tabular URL and website features (no deep learning or textual/visual content analysis), applies no feature-selection step, and does not test the model's generalizability across different or evolving phishing datasets — all flagged by the authors as future work. |
| **Relevance to Proposed Research** | Directly supports the group's topic — "Detecting Phishing Websites in Web Browsing Environments Using Ensemble Machine Learning Algorithms." Confirms that ensemble/voting-based approaches (combining RF, XGBoost, and MLP) outperform single classifiers for phishing website detection, and provides a benchmark methodology (preprocessing, evaluation metrics, dataset sources) that can be adapted or extended — e.g., by adding feature selection, testing on updated datasets, or validating within a live browsing environment — as an identified research gap for this proposal. |

---

