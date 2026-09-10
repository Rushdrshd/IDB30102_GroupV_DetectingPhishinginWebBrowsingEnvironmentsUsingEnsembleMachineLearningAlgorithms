"""
Website Feature Extraction Module

Research Title:
Detecting Phishing Websites in Web Browsing Environments
Using Ensemble Machine Learning Algorithms

Purpose:
This script demonstrates extraction of website-related
features used for phishing website classification.
"""


def extract_website_features(url):

    features = {}

    # URL length feature
    features["url_length"] = len(url)


    # HTTPS availability
    if "https" in url.lower():
        features["has_https"] = 1
    else:
        features["has_https"] = 0


    # Special character detection
    if "@" in url:
        features["contains_at_symbol"] = 1
    else:
        features["contains_at_symbol"] = 0



    # Suspicious keyword detection

    suspicious_keywords = [
        "login",
        "verify",
        "update",
        "secure",
        "account"
    ]


    keyword_found = False


    for keyword in suspicious_keywords:

        if keyword in url.lower():

            keyword_found = True


    if keyword_found:
        features["suspicious_keyword"] = 1
    else:
        features["suspicious_keyword"] = 0



    return features



# Example usage:
#
# website = "http://secure-login-example.com"
#
# extracted_features = extract_website_features(
#     website
# )
#
# print(extracted_features)
