---
# Football Players Transfer Fees Predictions
---
This project predicts football players' transfer fees and analyzes player data using various machine-learning algorithms and web frameworks.

## Data

The data for this project is sourced from a CSV file named `final_data.csv`, containing information on football players such as:
- Team
- Height
- Age
- Goals
- Assists
- Yellow cards
- Red cards
- and more.

## Data Preprocessing

### Libraries Used
- `pandas`, `numpy` for data manipulation
- `matplotlib`, `seaborn` for data visualization
- `dtale` for interactive data exploration
- `sklearn` for model building
- `streamlit`, `fastAPI` for deployment

### Steps
1. **Data Loading**: Load the data using `pandas.read_csv()`.
2. **Data Exploration**: Check for uniqueness, completeness, and accuracy.
3. **Handling Missing Values**: No missing values were found.
4. **Categorical Features**: 
   - The "position" feature is pre-encoded.
   - "Team" is converted to one-hot encoded features using `OneHotEncoding`.
5. **Numerical Features**:
   - Identify outliers using boxplots and histograms.
   - Perform feature scaling using `StandardScaler`.
6. **Feature Selection**: Use all features for initial model building.

## Model Building

The core objective is to predict transfer fees and analyze player data using several machine-learning algorithms:
- **K-Means Clustering**: Segments data points into clusters.
- **DBSCAN**: Groups data points based on density.
- **Decision Trees**: Classifies data points through decision-making processes.
- **K-Nearest Neighbors (KNN)**: Classifies data points based on nearest neighbors.
- **Linear Regression**: Models a linear relationship between transfer fees and player attributes.
- **Logistic Regression**: Predicts the probability of binary outcomes.
- **Support Vector Machine (SVM)**: Creates a hyperplane to separate classes.

## Evaluation

Model performance is evaluated using:
- **Clustering Algorithms**: Silhouette score
- **Classification Algorithms**: Accuracy, F1-score
- **Regression Models**: R-squared for predicting transfer fees

## Deployment

- **Streamlit**: Creates an interactive web application for visualizing model outputs and player analysis, including transfer fee predictions.
- **FastAPI**: Provides a scalable API for model deployment, enabling integration with other applications.

## Next Steps

1. Analyze model performance and identify the best technique for predicting transfer fees and specific player analysis tasks.
2. Fine-tune models by adjusting hyperparameters and performing feature engineering.
3. Enhance the web application with more interactive features and visualizations.

## Further Exploration

- Analyze the impact of different feature sets on model performance.
- Explore advanced models like Random Forest or Gradient Boosting.
- Integrate with external data sources for enriched analysis.
