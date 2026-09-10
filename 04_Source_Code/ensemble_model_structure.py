"""
Ensemble Machine Learning Model Structure

Research Title:
Detecting Phishing Websites in Web Browsing Environments
Using Ensemble Machine Learning Algorithms

Purpose:
This script demonstrates the proposed ensemble machine
learning classification structure.
"""


from sklearn.ensemble import (
    RandomForestClassifier,
    VotingClassifier
)

from sklearn.linear_model import LogisticRegression

from sklearn.svm import SVC



def create_ensemble_model():

    """
    Create ensemble classification model.

    Classifiers:
    - Random Forest
    - Logistic Regression
    - Support Vector Machine

    Returns:
        Ensemble model
    """



    random_forest = RandomForestClassifier(
        n_estimators=100
    )


    logistic_regression = LogisticRegression()



    support_vector_machine = SVC(
        probability=True
    )



    ensemble_model = VotingClassifier(

        estimators=[

            (
                "Random Forest",
                random_forest
            ),

            (
                "Logistic Regression",
                logistic_regression
            ),

            (
                "SVM",
                support_vector_machine
            )

        ],

        voting="soft"

    )


    return ensemble_model




# Example usage:
#
# model = create_ensemble_model()
#
# print(model)
