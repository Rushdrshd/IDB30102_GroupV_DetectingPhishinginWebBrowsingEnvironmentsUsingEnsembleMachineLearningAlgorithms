# CHAPTER 2: LITERATURE REVIEW

**Research Title:** Detecting Phishing Websites in Web Browsing Environments Using Ensemble Machine Learning Algorithms

---

## 2.1 Introduction

This chapter reviews prior research relevant to detecting phishing websites, narrowed from the broader literature search conducted in Assignment 1 to focus specifically on studies that apply machine learning (ML), ensemble learning, deep learning (DL), and real-time browser-based detection. The review is organised into three sub-topics that trace how the field has progressed: (2.2) traditional and ensemble machine learning approaches, (2.3) deep learning and transformer-based approaches, and (2.4) real-time and browser-integrated detection systems. This structure is used to identify the specific research gap this proposal addresses.

## 2.2 Machine Learning and Ensemble Learning Approaches for Phishing Website Detection

A substantial body of work has applied classical supervised machine learning algorithms — particularly Random Forest (RF), Decision Tree (DT), Gradient Boosting (GB), and XGBoost — to phishing URL and website classification, frequently combining several of these classifiers into an ensemble to improve accuracy and robustness.

Alani and Tawfik (2022) proposed PhishNot, a cloud-based Random Forest classifier trained on 88,646 URLs using only 14 selected characteristics, achieving 97.5% detection accuracy while maintaining fast processing suitable for near real-time use; however, the model's reliance on externally observable URL characteristics limits it when phishing sites deliberately mimic legitimate URL structures. Building on the strength of Random Forest, Albishri and Dessouky (2024) evaluated ensemble classifiers across multiple daily test periods and reported consistently high accuracy of 99.93–99.98%, outperforming traditional ML methods, though the eight-day evaluation window may not capture longer-term concept drift as phishing tactics evolve. Similarly, a 2025 Cluster Computing study combined multi-objective evolutionary feature selection with XGBoost, achieving a favourable balance between model complexity and predictive accuracy, though at a high computational cost.

Two studies obtained through additional research directly compare multiple ensemble classifiers side-by-side. Innab et al. (2024) evaluated seven algorithms — Decision Tree, Random Forest, Gradient Boosting, XGBoost, AdaBoost, Multi-Layer Perceptron (MLP), and a hard-voting ensemble — across two Kaggle phishing datasets, finding that the Voting classifier (combining RF, XGBoost, and MLP) achieved the best results (accuracy 0.978, F1-score 0.981), consistently outperforming any single classifier. Khairunnisya et al. (2025) similarly compared Random Forest and Gradient Boosting (alongside Naive Bayes and Logistic Regression baselines) on an 11,430-URL dataset with extensive feature engineering (correlation analysis, Chi-square testing, PCA), finding Gradient Boosting marginally superior (accuracy 0.980, ROC-AUC 0.994) and deploying the model as a real-time Streamlit web tool. Together, these studies confirm that ensemble methods reliably outperform individual classifiers for phishing website detection, which directly supports the ensemble-based methodology proposed in this research.

A systematic literature review by Safi and Singh (2023), which compared datasets and algorithms across 80 academic studies, found that ML-based approaches were used in 57 of the 80 studies reviewed, with certain CNN-based approaches exceeding 99.98% accuracy — but noted that inconsistent datasets across studies make direct comparison of reported results difficult, a methodological consideration this proposal accounts for when selecting a benchmark dataset.

## 2.3 Deep Learning and Transformer-Based Approaches

Beyond conventional ML, several recent studies apply deep learning and transformer architectures to extract richer structural and semantic features from URLs. Elsadig et al. (2022) combined BERT-based textual feature extraction with a convolutional neural network (CNN) on a large dataset of 549,346 URLs, achieving 96.66% accuracy and 93.63% F1-score, though performance was noted to depend heavily on the specific dataset and extracted features used. Do, Selamat, Fujita, and Krejcar (2024) proposed an integrated model (ResNet-TCN-MPNet) fusing character- and word-level URL features using ResNet, temporal convolution, and a pre-trained transformer, reporting up to 99.71% detection on a 1-million-URL dataset, while acknowledging that URL data's unstructured nature can limit cross-dataset generalisation. Said, Alsheikhy, Lahza, and Shawly (2024) enhanced a CNN with a multi-head self-attention mechanism, improving precision by roughly 2.74% over a standard CNN, though the study relied partly on synthetically generated phishing URLs that may not fully reflect real-world attacker behaviour.

Lightweight and explainable variants have also emerged. Roy et al. (2024) introduced PhishLang, a quantized small language model designed for low-latency, on-device URL classification (97.1% accuracy, under 5ms inference), directly demonstrating that transformer-style models can be compressed for practical deployment, though it showed more false positives on non-English domains. Tawfik, Alani, and Al-Daraiseh (2025) proposed XF-PhishBERT, an explainable few-shot learning framework combining ModernBERT with Random Forest-based feature selection (SHAP, RFECV), reporting 99.9% accuracy with only 10 labelled examples per class and a browser-extension inference latency of just 42 milliseconds — a result of particular relevance because it demonstrates that high accuracy and real-time browser-level responsiveness are simultaneously achievable.

## 2.4 Real-Time and Browser-Based Phishing Detection Systems

Since this proposal is specifically concerned with detection within web browsing environments, particular attention is given to studies that move beyond offline dataset evaluation toward live, in-browser deployment. Asiri, Xiao, Alzahrani, and Li (2024) developed PhishingRTDS, a real-time detection system combining a browser extension with a deep learning back-end; the extension captures URLs as the user browses, uses a sandboxed Docker environment to safely open suspicious pages, and extracts HTML/JavaScript features for classification, successfully detecting TinyURL redirects and Browser-in-the-Browser attacks. Its main limitation is the added processing overhead from dynamically opening and analysing suspicious pages, which can affect browsing responsiveness.

Shajahan et al. (2025), obtained through additional research for this proposal, built a lightweight browser extension around an XGBoost classifier, achieving 95% accuracy with feature extraction and classification completing in roughly 500 milliseconds — small enough to avoid any perceptible delay to the user. The system further included a confidence-based auto-blocking feature, automatically preventing page load when the model reached 100% phishing confidence. Its authors noted that newly emerging phishing patterns absent from the training data could still evade detection, and that performance depends on periodic dataset updates. Tawfik et al.'s (2025) XF-PhishBERT (Section 2.3) also reported browser-extension-level latency figures, reinforcing these findings.

These browser-based studies illustrate a clear and growing trend: moving ML models out of the laboratory and into the browser itself, where detection must occur within milliseconds without disrupting the user's browsing experience. However, none of the reviewed studies combine a multi-classifier ensemble (shown to be most accurate in Section 2.2) directly within a live browser extension (shown to be practical in this section) — most browser-based systems in the literature rely on a single classifier rather than an ensemble/voting approach. This is the specific direction pursued in this proposal, discussed further in Chapter 3.

## 2.5 Summary of Literature Review

| No. | Author(s) & Year | Method / Approach | Dataset | Key Findings | Limitation |
|---|---|---|---|---|---|
| 1 | Alani & Tawfik (2022) | Random Forest, cloud API | 88,646 URLs | 97.5% accuracy, 14 features | Relies on external URL characteristics |
| 2 | Safi & Singh (2023) | Systematic review of ML/DL/RF/CNN | 80 studies | CNN up to 99.98% accuracy | Inconsistent datasets across studies |
| 3 | Albishri & Dessouky (2024) | Ensemble RF evaluation | Labelled URL dataset | 99.93–99.98% accuracy | 8-day evaluation window only |
| 4 | Cluster Computing Study (2025) | XGBoost + evolutionary feature selection | Benchmark phishing dataset | Balanced accuracy/complexity | High computational cost |
| 5 | Innab et al. (2024) | Voting Ensemble (RF+XGB+MLP) vs. 6 classifiers | 2 Kaggle datasets | Voting: 0.978 accuracy, 0.981 F1 | Near-perfect results on 2nd dataset (overfitting risk) |
| 6 | Khairunnisya et al. (2025) | RF vs. Gradient Boosting + feature engineering | 11,430 URLs | GB: 0.980 accuracy, 0.994 ROC-AUC | Static dataset; no dynamic features |
| 7 | Elsadig et al. (2022) | BERT + CNN | 549,346 URLs | 96.66% accuracy | Depends on dataset/feature choice |
| 8 | Do et al. (2024) | ResNet + TCN + MPNet transformer | Ebbu2017, 1M-PD, etc. | 99.71% detection rate | Cross-dataset generalisation limited |
| 9 | Said et al. (2024) | CNN + multi-head self-attention | Real + generated URLs | 99.7% precision | Synthetic URLs may not reflect real attacks |
| 10 | Roy et al. (2024) | PhishLang – quantized small LM | PhishTank + UNB ISCX | 97.1% accuracy, <5ms latency | More false positives on non-English domains |
| 11 | Tawfik et al. (2025) | XF-PhishBERT few-shot + SHAP/RFECV | Phishing website dataset | 99.9% accuracy, 42ms latency | Few-shot performance needs broader validation |
| 12 | Asiri et al. (2024) | Browser extension + Docker + DL | TinyURL, Browser-in-Browser URLs | Detects advanced redirect attacks | Sandbox analysis adds processing overhead |
| 13 | Shajahan et al. (2025) | XGBoost browser extension | Labelled URL dataset | 95% accuracy, ~500ms latency | Misses novel/unseen phishing patterns |

---
*Prepared for IDB30102 Assignment 2 — Research Proposal, Chapter 2. Content is consistent with, and narrows the scope of, the broader literature search conducted in Assignment 1 to focus specifically on the group's proposed research topic.*
