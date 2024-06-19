
## Customer Churn Analysis Project

### Overview
This project focuses on predicting customer churn for a telecommunications company using machine learning techniques. Customer churn, which measures the rate at which customers stop doing business with a company, is a critical metric for businesses to understand and mitigate. By predicting churn, companies can proactively take actions to retain customers and optimize business strategies.


### Steps to Execute the Project Locally

**Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/telco-customer-churn.git
   cd telco-customer-churn
   ```

**Setup Environment:**
   - Ensure Python 3.x and necessary libraries (scikit-learn, pandas, numpy, Flask) are installed (Use a virtual environment if needed):
     ```bash
     pip install -r requirements.txt
     ```

#### 1. Data Cleaning and Exploration
- **Jupyter Notebook: `Data_Cleaning_and_Exploration.ipynb`**
  - Use this notebook to explore and clean the dataset.
  - Performed data cleaning tasks such as handling missing values, removing unnecessary columns, and transforming variables.
  - Explored the data distributions and relationships by Univarient and BiVarient analysis between variables through visualizations and statistical summaries.

    **Execute Jupyter Notebook:**
    run `Data_Cleaning_and_Exploration.ipynb` to preprocess and explore the dataset.


#### 2. Modeling and Evaluation
- **Jupyter Notebook: `Modeling_and_Evaluation.ipynb`**
  - Trained and evaluated machine learning models to predict customer churn.
  - Select appropriate models and evaluated them using metrics like accuracy, precision, recall, and F1-score.
  - Implemented SMOTEENN technique to handle class imbalance and optimize model performance.
  - Saved the finalized model using pickle for deployment.
 
     **Execute Jupyter Notebook:**
     run `Modeling_and_Evaluation.ipynb` to train, evaluate, and save the machine learning model.

#### 3. Deployment with Flask
- **Flask Application: `app.py`**
  - Deployed the trained machine learning model using Flask for real-time predictions.
  - Developed a responsive web interface with HTML and CSS allowing users to input customer details.
  - Implemented logic to preprocess user inputs, make predictions using the trained model, and display the results.
 
      **File Structure of Flask Application**

      - **`app.py`**: Main Flask application file containing routes and logic for predicting churn based on user inputs.
      - **`templates`** (directory):
      - **`index.html`**: HTML template for the web interface allowing users to input customer details and receive predictions.
      - **`static`** (directory):
      - **`style.css`**: CSS stylesheet for customizing the appearance of the HTML templates.
 
       **Run Flask Application:** 
     ```bash
     python app.py
     ```
   - Open a web browser and go to `http://localhost:5000` to interact with the application.

### Tableau Dashboards and Stories

- **Tableau: `Telco_Churn_Dashboards.twb`**
  - Explore detailed visualizations and insights regarding customer churn patterns.
  - Utilized Tableau dashboards and stories to present key findings, trends, and actionable insights derived from the data to enhance stakeholder understanding and facilitate data-driven decision-making processes.
