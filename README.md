# Player Churn Prediction Project

## Description
This project focuses on predicting player churn in online games using machine learning techniques. By analyzing key player metrics and behaviors, the project aims to provide actionable insights for improving player retention. The project includes a complete pipeline from data processing to model training, along with a Power BI dashboard for visual representation.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Project Structure](#project-structure)
4. [Features](#features)
5. [Files in the Repository](#files-in-the-repository)
6. [Data](#data)
7. [Models](#models)
8. [Results](#results)
9. [Visualizations](#visualizations)
10. [Contributing](#contributing)
11. [Acknowledgments](#acknowledgments)
12. [Contact Information](#contact-information)

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

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your proposed changes. Make sure to follow the coding standards and include tests for any new functionality.

## Acknowledgments
- Thanks to the team in building the project - Kalpana Kale, Ruchita Patre
- Special thanks to the contributors of the datasets and tools used in this project.
- Appreciation to the academic and professional communities that provided valuable feedback on the research paper.

## Contact Information
For any questions, feedback, or collaboration opportunities, feel free to reach out to me at[pancham8675@gmail.com.
