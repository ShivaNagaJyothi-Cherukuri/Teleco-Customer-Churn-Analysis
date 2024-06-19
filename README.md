## Customer-Churn-Analysis

![TCC](https://github.com/ShivaNagaJyothi-Cherukuri/Teleco-Customer-Churn-Analysis/assets/125705831/05488a65-037b-4e3f-986e-7e989e5e3955)
--
### Overview
This project focuses on predicting customer churn for a telecommunications company using machine learning techniques. Customer churn, which measures the rate at which customers stop doing business with a company, is a critical metric for businesses to understand and mitigate. By predicting churn, companies can proactively take actions to retain customers and optimize business strategies.

### Steps and Methodology

1. **Data Collection and Initial Exploration**
   - Gathered a comprehensive dataset containing customer information such as demographics, services subscribed, contract details, and churn status.
   - Explored the dataset to understand its structure, features, and distribution using statistical summaries and visualizations.

2. **Data Preprocessing**
   - Conducted thorough data cleaning to handle missing values, outliers, and inconsistencies.
   - Engineered features, including transforming categorical variables into numerical representations suitable for machine learning models.
   - Binned continuous variables like tenure into categorical groups to capture meaningful patterns.

3. **Exploratory Data Analysis (EDA)**
   - Utilized univariate and bivariate analysis to uncover relationships between variables and their impact on churn.
   - Visualized key insights using plots such as histograms, bar charts, and correlation matrices.
   - Created Tableau dashboards to visually explore churn patterns, customer segments, and the impact of different service subscriptions.

4. **Model Selection and Evaluation**
   - Selected multiple machine learning models including Decision Trees, Random Forests, and Gradient Boosting Machines (GBM).
   - Evaluated models using metrics such as accuracy, precision, recall, and F1-score to understand their performance in predicting churn.
   - Identified Random Forest as the optimal model due to its robust performance in handling both categorical and numerical features.

5. **Handling Class Imbalance**
   - Addressed class imbalance in the dataset (where churned customers were a minority) using Synthetic Minority Over-sampling Technique (SMOTE) combined with Edited Nearest Neighbors (ENN).
   - Applied SMOTEENN to generate synthetic samples for the minority class, enhancing the model's ability to generalize to unseen data.

6. **Model Training and Optimization**
   - Trained the Random Forest model on the resampled dataset to predict customer churn.
   - Fine-tuned model hyperparameters using techniques like grid search to optimize model performance.

7. **Model Evaluation**
   - Evaluated the final model using cross-validation and held-out validation sets to ensure its reliability and generalizability.
   - Achieved an accuracy of 93%, indicating strong predictive capability in identifying potential churners.

8. **Deployment with Flask**
   - Serialized the trained model using pickle for deployment in a Flask web application.
   - Developed a responsive web interface allowing users to input customer details and receive real-time predictions on customer churn likelihood.
   - Enhanced user experience with CSS for styling and interactive elements, ensuring accessibility and usability.

9. **Tableau Dashboards and Stories**
   - Created detailed Tableau dashboards and stories to complement the predictive analytics findings.
   - Visualized churn trends, customer behavior, and key insights derived from the dataset.
   - Provided stakeholders with interactive visualizations to facilitate data-driven decision-making processes and actionable insights.

### Conclusion
This project showcases proficiency in data analysis, machine learning modeling, and data visualization using Python, Tableau, and web development with Flask. By leveraging advanced analytics techniques, the project delivers actionable insights to reduce customer churn and improve business outcomes for telecommunications companies.

For further details or questions regarding the process, feel free to reach out.

---
