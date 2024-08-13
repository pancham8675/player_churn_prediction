# Player Churn Prediction Project

## Description
This project focuses on predicting player churn in online games using machine learning techniques. By analyzing key player metrics and behaviors, the project aims to provide actionable insights for improving player retention. The project includes a complete pipeline from data processing to model training, along with a Power BI dashboard for visual representation.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Project Workflow](#project-workflow)
5. [Features](#features)
6. [Files in the Repository](#files-in-the-repository)
7. [Data](#data)
8. [Models](#models)
9. [Results](#results)
10. [Visualizations](#visualizations)
11. [Contributors](#contributors)
12. [Acknowledgments](#acknowledgments)
13. [Contact Information](#contact-information)

## Installation
1. Clone the repository to your local machine.
2. Ensure you have Python installed (preferably version 3.7 or above).
3. Install the required Python packages using the `requirements.txt` file.
4. Open the Jupyter Notebook `PlayerChurnForecasting.ipynb` to run the code.
5. To view the Power BI dashboard, download and open the `player_churn_powerbi_dashboard.pbix` file using Power BI Desktop.

## Usage
- Run the Jupyter Notebook to process the data and build predictive models.
- Open the Power BI dashboard to visualize player churn metrics and insights.
- Utilize the findings from the research paper for further analysis or academic purposes.

## Project Structure
- **`dataset.csv`**: Raw dataset containing player metrics.
- **`final_dataset.csv`**: Processed dataset after feature engineering and cleaning.
- **`PlayerChurnForecasting.ipynb`**: Jupyter Notebook containing the entire workflow from data processing to model building.
- **`player_churn_powerbi_dashboard.pbix`**: Power BI file with visualizations of player churn metrics.
- **`Research Paper.pdf`**: Published research paper detailing the methodologies and findings of the project.

## Project Workflow

The workflow of the Player Churn Prediction project is as follows:

1. **Data Collection:**
   - The initial raw data was collected from various gaming platforms, capturing key player metrics and behaviors.

2. **Data Preprocessing:**
   - **Loading Data:**
     ```python
     import pandas as pd
     raw_data = pd.read_csv('dataset.csv')
     ```
   - **Data Cleaning:**
     - Handle missing values, remove duplicates, and normalize data types.
     ```python
     cleaned_data = raw_data.dropna().drop_duplicates()
     ```
   - **Feature Engineering:**
     - Create new features that enhance the predictive power of the dataset.
     ```python
     cleaned_data['session_duration_log'] = np.log(cleaned_data['session_duration'] + 1)
     ```
   - **Splitting Data:**
     - Split the data into training and testing datasets.
     ```python
     from sklearn.model_selection import train_test_split
     X = cleaned_data.drop('churn', axis=1)
     y = cleaned_data['churn']
     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
     ```

3. **Model Building:**
   - **Model Selection:**
     - Choose appropriate machine learning models for prediction.
     - Here, Random Forest and Logistic Regression were selected.
   - **Model Training:**
     ```python
     from sklearn.ensemble import RandomForestClassifier
     rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
     rf_model.fit(X_train, y_train)
     ```
   - **Model Evaluation:**
     - Evaluate the model performance using accuracy, precision, recall, and F1-score.
     ```python
     from sklearn.metrics import accuracy_score, classification_report
     y_pred = rf_model.predict(X_test)
     print("Accuracy:", accuracy_score(y_test, y_pred))
     print("Classification Report:\n", classification_report(y_test, y_pred))
     ```

4. **Data Visualization:**
   - **Power BI Dashboard:**
     - Use Power BI to visualize key metrics and player churn insights.
     - Load the `final_dataset.csv` into Power BI and create visuals.
   - **Dashboard Integration:**
     - The dashboard integrates insights from the predictive model and highlights areas for improving player retention.

5. **Documentation:**
     - The findings, methodology, and results were documented in a research paper, which was published and added to the repository.
     - The paper provides detailed analysis and insights derived from the project, offering valuable contributions to the field.

## Features
- **Predictive Modeling**: Utilizing machine learning algorithms like Random Forest and Logistic Regression to predict player churn.
- **Data Processing**: Feature engineering and data cleaning techniques to enhance prediction accuracy.
- **Visualization**: Power BI dashboard providing a clear visual representation of churn metrics and insights.

## Files in the Repository
- **`dataset.csv`**: The raw data used for the project.
- **`final_dataset.csv`**: Cleaned and processed data ready for modeling.
- **`PlayerChurnForecasting.ipynb`**: The main code file containing the data analysis, modeling, and prediction steps.
- **`player_churn_powerbi_dashboard.pbix`**: The Power BI dashboard file to visualize and analyze the results.
- **`Research Paper.pdf`**: A detailed document discussing the project’s findings and contributions.

## Data
- The **`dataset.csv`** contains raw player data, including metrics such as session duration, in-game purchases, and player demographics.
- The **`final_dataset.csv`** includes the processed data with engineered features ready for model training.

## Models
- **Random Forest**: Used for predicting player churn with high accuracy.
- **Logistic Regression**: Applied as a baseline model for churn prediction.
- **Evaluation Metrics**: Models were evaluated using accuracy, precision, recall, and F1-score.

## Results
- The models provided strong predictive performance, with Random Forest achieving the highest accuracy.
- Key findings from the analysis revealed that certain player behaviors and demographics significantly impact churn likelihood.

## Visualizations
- **Power BI Dashboard**: The dashboard visualizes player churn metrics, allowing for easy interpretation of the data.

  ![PowerBI Dashboard (Person not to churn out)](https://github.com/pancham8675/player_churn_prediction/blob/main/powerbi_dashboard/not_to_churn.jpg)

  ![PowerBI Dashboard (Person to churn out)](https://github.com/pancham8675/player_churn_prediction/blob/main/powerbi_dashboard/to_churn.jpg)

## Contributors
- Kalpana Kale
- Ruchita Patre
- Prof. Rahesha Mulla

## Acknowledgments
- Thanks to the team in building the project - Kalpana Kale, Ruchita Patre
- Special thanks to the contributors of the datasets and tools used in this project.
- Appreciation to the academic and professional communities that provided valuable feedback on the research paper.

## Contact Information
For any questions, feedback, or collaboration opportunities, feel free to reach out to me at pancham8675@gmail.com.
