# Research Paper Summary — 01_Research_Papers3

| Item | Details |
|---|---|
| **Paper Title** | Browser Extension for Phishing Website Detection Using Machine Learning |
| **Author(s)** | Shyni Shajahan, Teena George, Jithi P V, Snehamol K M, Sanjana Krishna, Sanjaly Krishna, Nagul Jagadish |
| **Year** | 2025 |
| **Source** | *AIJR Proceedings* (Proceedings of ICIMRBE 2025), Vol. 7, No. 5, pp. 30–37. DOI: [10.21467/proceedings.7.5.5](https://doi.org/10.21467/proceedings.7.5.5) |
| **Research Problem** | Traditional phishing defences (blacklists, rule-based systems) cannot keep pace with rapidly evolving phishing tactics and fail to detect newly created phishing sites, leaving users exposed while actively browsing the web. |
| **Method / Technique** | Built a lightweight browser extension (JavaScript/HTML/CSS front-end, Flask/Python back-end API) powered by an XGBoost classifier (ensemble gradient-boosted trees). The extension automatically extracts URL and page features when a user navigates to a new page and sends them to the model for real-time prediction; a confidence-based auto-blocking mechanism halts page loading when phishing confidence reaches 100%. |
| **Dataset / Tools** | A labeled dataset of phishing and legitimate URLs (features from URL structure, suspicious characters, HTTPS usage, subdomain count, domain age via WHOIS, and embedded JavaScript/form behaviour). Built with JavaScript, HTML, CSS, Python (Flask), and XGBoost; JSON used for extension–API communication. |
| **Main Findings** | The XGBoost-based extension achieved ~95% accuracy, 92% precision, 90% recall, and an F1-score of 0.91 on real browsing traffic. Feature extraction and classification completed in about 500 milliseconds, with negligible impact on page-load time, demonstrating the model's suitability for real-time, in-browser deployment. |
| **Limitation** | The system can miss newly emerging phishing sites that don't resemble patterns in the training data (false negatives), and occasionally misflags legitimate sites with unusual features such as very long URLs (false positives). Detection quality depends heavily on the size/quality of the training dataset and requires periodic retraining; the study also does not yet incorporate deep learning or visual-similarity detection, and support is limited to a single browser. |
| **Relevance to Proposed Research** | This paper is one of the closest matches to the group's exact topic — an ensemble ML model (XGBoost) deployed specifically **within a web browsing environment** for real-time phishing detection. It provides a concrete architecture (extension + API + ensemble classifier + confidence-based blocking) that the group can reference for its own proposed system design, and its stated limitations (no deep learning, single-browser support, static training data) directly highlight gaps the group's proposed ensemble-based research can address. |

---

