# IDB30102_GroupV_DetectingPhishinginWebBrowsingEnvironmentsUsingEnsembleMachineLearningAlgorithms

## Research Project Overview

### Research Title
Detecting Phishing Websites in Web Browsing Environments Using Ensemble Machine Learning Algorithms

### Group Information
- **Group Number:** V
- **Assigned Research Area:** Website Security / Phishing Detection
- **Group Members:**
    - Muhammad Ashmeer Bin Jamil (52215225094)
    - Muhammad Syahmi Afiq Bin Mohd Sohaimin (52215225252)
    - Muhammad Haziq Iskandar Bin Zulzahari (52215225215)
    - Muhammad Rusyaidi Bin Abdul Rashid (52215225041)

### Research Problem
Phishing websites are increasingly sophisticated, and traditional detection methods (blacklists, heuristic filters) are failing to protect users. Single machine learning models often lack the generalization needed to detect diverse phishing techniques effectively. An ensemble approach is proposed to overcome these limitations.

### Research Aim
To design, develop, and evaluate an ensemble machine learning-based system for detecting phishing websites in web browsing environments with high accuracy and low false positives.

### Research Objectives
1.  To identify and analyze key URL and webpage features that distinguish phishing from legitimate websites.
2.  To design and develop an ensemble machine learning model combining multiple classifiers for phishing detection.
3.  To evaluate the proposed ensemble model's performance using accuracy, precision, recall, F1-score, and false positive rate.

### Proposed Solution
A phishing website detection system using ensemble machine learning (e.g., Random Forest, XGBoost, Stacking) that analyzes URL and webpage features to classify sites as phishing or legitimate. The ensemble approach aims to improve generalization and robustness compared to single classifiers.

### Methodology & Development Model
- **Research Methodology:** Design Science Research / Experimental. The research involves building and evaluating an ensemble model artifact and comparing its performance against baselines.
- **Development Model:** Prototyping / Iterative and Incremental. The model and system components will be developed and refined iteratively.

### Proposed Evaluation Plan
- **Baseline:** The ensemble model will be compared against individual base classifiers such as Random Forest, XGBoost, SVM, and Logistic Regression.
- **Dataset:** A standard phishing URL dataset will be used (e.g., UCI Phishing Dataset, PhishTank data, or ISCX URL dataset).
- **Metrics:** 
    - Detection Performance: **Accuracy, Precision, Recall, F1-Score, ROC-AUC**
    - Practical Performance: **False Positive Rate (FPR)**, and **Prediction Latency**.
    - Generalization: **Cross-dataset validation** where applicable.

### Proposed System Architecture
The system follows a typical machine learning pipeline:
1.  Input: URL or webpage content.
2.  Feature Extraction: URL features (length, special characters, domain age), webpage features (HTML content, JavaScript), and lexical features.
3.  Model Prediction: Ensemble of classifiers (e.g., Random Forest, XGBoost, Gradient Boosting) with voting or stacking.
4.  Output: Classification result (Phishing / Legitimate).

### Repository Structure
- `01_Research_Papers/`: Citations, summaries, and analysis of relevant literature on phishing detection and ensemble ML.
- `02_Literature_Review/`: Literature synthesis, research gap analysis, and comparison of existing methods.
- `03_Architecture_and_Flowchart/`: System architecture diagram, model training flow, and detection workflow.
- `04_Source_Code/`: Preliminary Python scripts for data preprocessing, feature extraction, model training, and evaluation.
- `05_Data_or_Sample_Input/`: Dataset descriptions, sample input files, and data source references.
- `06_Results_or_Expected_Output/`: Expected outputs, sample classification results, and performance metrics.
- `07_References/`: Full APA references for all sources used.

### Expected Tools and Technologies
- **Programming Language:** Python 3.x
- **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, XGBoost
- **Tools:** Jupyter Notebook, Git
- **Dataset Source:** Publicly available datasets (UCI, PhishTank, ISCX, Kaggle)
- **Deployment Consideration:** Lightweight enough for browser extension or API integration.
