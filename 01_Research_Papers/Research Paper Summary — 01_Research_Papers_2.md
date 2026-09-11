# Research Paper Summary — 01_Research_Papers_2

| Item | Details |
|---|---|
| **Paper Title** | Phishing URL Detection System Using Random Forest and Gradient Boosting for Cybercrime Prevention |
| **Author(s)** | Aqilla Khairunnisya, Lindawati, Suzan Zefi |
| **Year** | 2025 |
| **Source** | *CSRID Journal (Computer Science Research and Its Development Journal)*, Vol. 17, No. 3, pp. 296–310. DOI: [10.22303/csrid-.17.3.2025.296-310](https://www.doi.org/10.22303/csrid-.17.3.2025.296-310) |
| **Research Problem** | Traditional phishing detection methods (blacklisting, rule-based heuristics) fail to keep up with evolving and zero-day phishing URLs, creating a need for adaptive, learning-based detection with a practical, accessible tool for end-users. |
| **Method / Technique** | Compared Random Forest and Gradient Boosting classifiers (plus Naive Bayes and Logistic Regression as baselines). Applied Min-Max and Z-score normalization, correlation analysis and Chi-square tests for feature selection, PCA for dimensionality reduction, feature augmentation (e.g., `is_trusted_domain`, `domain_age_adequate`), and GridSearchCV with K-Fold cross-validation for hyperparameter tuning. Used an 80:20 stratified train-test split. |
| **Dataset / Tools** | Kaggle "Web Page Phishing Detection" dataset — 11,430 URLs with 89 features (URL length, subdomain count, HTTPS status, special character count, domain age, Google-indexed status, etc.). Implemented in Python (scikit-learn); best model deployed as a real-time web app using Streamlit. |
| **Main Findings** | Gradient Boosting slightly outperformed all other models: accuracy 0.980, precision 0.981, recall 0.979, F1-score 0.980, ROC-AUC 0.994 (vs. Random Forest accuracy 0.976, ROC-AUC 0.991). Random Forest trained faster and was more computationally efficient, while Gradient Boosting generalized better. Top predictive features were URL length, subdomain count, HTTPS status, and special character count. The best model was deployed as a public real-time phishing-checking Streamlit web app. |
| **Limitation** | The dataset is static and does not reflect continuously evolving phishing tactics, including zero-day attacks not yet captured in any dataset. The model relies solely on structural/lexical URL features and ignores dynamic signals such as webpage content, redirection behaviour, or user interaction. The deployed tool is a standalone web app not yet integrated with broader security infrastructure (e.g., firewalls, antivirus, email filters), and cross-domain generalization (finance, education, government) was not tested. |
| **Relevance to Proposed Research** | Highly relevant to "Detecting Phishing Websites in Web Browsing Environments Using Ensemble Machine Learning Algorithms" — it directly builds on ensemble tree-based methods (RF, Gradient Boosting) similar to the group's proposed approach, and demonstrates a real-world deployment path (a browser-facing real-time detection tool) that closely mirrors the "web browsing environment" focus of the group's research. Its identified gaps — no dynamic/content-based features, no zero-day adaptability, no integration into the browsing environment itself — help justify and scope the group's research objectives and evaluation plan. |

---
*Prepared for IDB30102 Assignment 2 — GitHub Research & Technical Repository (01_Research_Papers/).*
