# AI Personal Finance Manager

An AI-powered personal finance manager that helps users track expenses, predict budgets, categorize transactions, and gain actionable financial insights using machine learning and NLP techniques.

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features
- **Expense Tracking**: Add and track daily transactions with descriptions.
- **Automatic Categorization**: Uses NLP to predict the category of each transaction.
- **Budget Prediction**: Forecast monthly budget based on past spending patterns.
- **Analytics & Insights**: Visualize spending trends with charts, pivot tables, and summary statistics.
- **Offline First**: Core features work offline; optional cloud sync for advanced analytics.
- **User-friendly Interface**: Simple CLI and potential web-based GUI.

## Demo
*(Include screenshots or GIFs of your app in action here)*

## Tech Stack
- **Language**: Python
- **Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn, nltk, transformers
- **Frontend**: CLI (future: web app with Flask/Django)
- **Database**: CSV or SQLite (for local storage)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/AI-Personal-Finance-Manager.git
   cd AI-Personal-Finance-Manager
2.Create and activate a virtual environment:
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
3.Install dependencies:
  pip install -r requirements.txt
## Usage
1. Run the main program:
   python main.py
2. Enter your transaction description:  
   Enter transaction description (or 'exit'): lunch
   Predicted category: Health
3. View analytics and budget insights via generated reports.
##Model Training
1.Data preprocessing with pandas and NLTK
2.Classification model using scikit-learn (RandomForest / XGBoost)
3.Optional fine-tuning with transformer-based models for better accuracy
4.Save and load trained models using joblib or pickle
##Contributing
1. Fork the repository
2. Create a new branch: git checkout -b feature/YourFeature
3. Commit your changes: git commit -m 'Add some feature'
4. Push to the branch: git push origin feature/YourFeature
5. Open a Pull Request

License

This project is licensed under the MIT License. See LICENSE
 for details.

Contact

GitHub: TanishTated
Email: TanishTated2005@gamil.com
