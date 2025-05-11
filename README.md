# Football Players Transfer Fees Prediction

![Transfer Market](https://img.shields.io/badge/Football-Transfer%20Market-green?style=for-the-badge)
![ML Project](https://img.shields.io/badge/Machine%20Learning-Prediction-blue?style=for-the-badge)

## ⚽ Project Overview
A machine learning project that predicts football players' transfer fees based on performance metrics, player attributes, market conditions, and historical transfer data. This model helps clubs, agents, and football analysts estimate player valuations in the dynamic transfer market.

## 🎯 Objectives
- Develop accurate prediction models for football player transfer fees
- Identify key factors that influence player valuations
- Analyze market trends and valuation patterns across different leagues and positions
- Create an interpretable model that provides insights into the transfer market mechanics

## 📊 Data & Features
The model utilizes comprehensive player data including:

- **Player Information**
  - Age, nationality, position, contract duration
  - Current club, league level, international status

- **Performance Statistics**
  - Goals, assists, minutes played
  - Pass completion, chances created
  - Defensive actions, aerial duels
  - Advanced metrics (xG, xA, VAEP, etc.)

- **Market Factors**
  - Previous transfer history
  - Club financial status
  - Market inflation
  - League commercial value

## 🧠 Models & Methodology

### Data Processing Pipeline
- Feature engineering to create relevant metrics
- Handling of missing values and outliers
- Normalization and scaling
- Feature selection and dimensionality reduction

### Machine Learning Models
Multiple models were evaluated to find the optimal solution:
- Linear Regression as baseline
- Random Forest Regression
- Gradient Boosting (XGBoost, LightGBM)
- Neural Networks
- Ensemble approach combining multiple models

### Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
- Custom football-specific evaluation metrics

## 📈 Key Findings
- Age and contract length show non-linear relationships with transfer fees
- Goal contribution statistics carry different weights for different positions
- Market inflation has a significant year-over-year impact on valuations
- League commercial value strongly influences player valuation beyond performance
- Player nationality and marketability contribute measurably to transfer value

## 🛠️ Technologies Used
- **Python**: Core programming language
- **Pandas & NumPy**: Data manipulation and numerical analysis
- **Scikit-learn**: Machine learning implementation
- **XGBoost/LightGBM**: Gradient boosting frameworks
- **TensorFlow/PyTorch**: Neural network implementation
- **Matplotlib & Seaborn**: Data visualization
- **Jupyter Notebooks**: Interactive development and analysis
- **MLflow**: Model tracking and experiment management

## 📁 Repository Structure
```
Football-Players-Transfer-Fees-Predictions/
├── data/
│   ├── raw/                      # Original datasets
│   ├── processed/                # Cleaned and transformed data
│   └── external/                 # External data sources
├── notebooks/
│   ├── 01_data_exploration.ipynb # Initial data exploration
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_development.ipynb
│   └── 04_model_evaluation.ipynb
├── src/
│   ├── data/                     # Data processing scripts
│   ├── features/                 # Feature engineering
│   ├── models/                   # Model implementation
│   └── visualization/            # Visualization utilities
├── models/                       # Saved model files
├── reports/                      # Analysis reports and figures
├── requirements.txt              # Project dependencies
└── README.md                     # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip package manager

### Installation
1. Clone the repository
   ```bash
   git clone https://github.com/Tw-0l/Football-Players-Transfer-Fees-Predictions.git
   cd Football-Players-Transfer-Fees-Predictions
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. Install required dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run Jupyter to explore notebooks
   ```bash
   jupyter notebook
   ```

## 💻 Usage Examples

```python
# Example code for making predictions with the trained model
from src.models.predictor import TransferPredictor

# Initialize the predictor with the trained model
predictor = TransferPredictor(model_path='models/best_model.pkl')

# Player data dictionary with features
player_data = {
    'age': 23,
    'position': 'Forward',
    'goals': 15,
    'assists': 7,
    'minutes_played': 2340,
    'contract_years_left': 2,
    # Additional features...
}

# Get prediction
predicted_fee = predictor.predict(player_data)
print(f"Predicted transfer fee: €{predicted_fee:,.2f}")
```

## 📌 Applications
- **Club Recruitment Teams**: Objective player valuation for potential targets
- **Football Agents**: Negotiation benchmarks for client contracts
- **Sports Analytics Firms**: Market analysis and player portfolio management
- **Fantasy Football**: Player value assessment for fantasy leagues

## 🔮 Future Enhancements
- Integration of video analysis metrics using computer vision
- Real-time valuation updates based on match performances
- Web interface for instant predictions
- Inclusion of social media presence and commercial value metrics
- Position-specific models for more targeted predictions

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an Issue to discuss potential improvements.

## 📊 Data Sources
- Historical transfer data from major football databases
- Performance statistics from leading sports analytics providers
- Market valuation estimates from football scouting platforms
- *(Note: Specific data sources and their usage rights are detailed in the data documentation)*
  

## 📞 Contact
- GitHub: [@Tw-0l](https://github.com/Tw-0l)

---

*This project aims to bring data-driven insights to the often opaque world of football transfers, helping stakeholders make more informed decisions in the transfer market.*
