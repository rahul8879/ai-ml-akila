#!/bin/bash
# Git Cleanup Script - Remove large files and secrets from Git tracking
# This script removes files from Git index but keeps them on your local filesystem

echo "🧹 Starting Git cleanup..."
echo ""

# Remove .env files (secrets)
echo "📌 Removing secret files from Git tracking..."
git rm --cached GenAI/.env 2>/dev/null || true

# Remove database files
echo "📌 Removing database files from Git tracking..."
git rm --cached mlflow.db 2>/dev/null || true
git rm --cached MLOps/mlflow.db 2>/dev/null || true
git rm --cached MLOps/mlruns/mlflow.db 2>/dev/null || true

# Remove model files (.pkl, .pth)
echo "📌 Removing model files from Git tracking..."
git rm --cached machine_learning/encoder.pkl 2>/dev/null || true
git rm --cached MLOps/random_forest_model.pkl 2>/dev/null || true
git rm --cached translator_rnn_model.pth 2>/dev/null || true

# Remove all CSV files
echo "📌 Removing CSV data files from Git tracking..."
git rm --cached Python/car_price_dataset_medium.csv 2>/dev/null || true
git rm --cached Python/Reviews.csv 2>/dev/null || true
git rm --cached 'Python/pandas/1_getting_started/nyc_weather.csv' 2>/dev/null || true
git rm --cached 'Python/pandas/2_dataframe_basics/weather_data.csv' 2>/dev/null || true
git rm --cached 'Python/pandas/3_Key operations on Dataframes/*.csv' 2>/dev/null || true
git rm --cached Python/simple_data.csv 2>/dev/null || true

# Remove Excel files
echo "📌 Removing Excel files from Git tracking..."
git rm --cached Python/simple_data.xlsx 2>/dev/null || true
git rm --cached 'Python/pandas/3_Key operations on Dataframes/*.xlsx' 2>/dev/null || true
git rm --cached data/'Online Retail Data Set.xlsx' 2>/dev/null || true

# Remove __pycache__ directories
echo "📌 Removing __pycache__ directories from Git tracking..."
git rm -r --cached MLOps/__pycache__/ 2>/dev/null || true
find . -type d -name __pycache__ -exec git rm -r --cached {} \; 2>/dev/null || true

# Remove .ipynb_checkpoints
echo "📌 Removing Jupyter checkpoint files from Git tracking..."
find . -type d -name .ipynb_checkpoints -exec git rm -r --cached {} \; 2>/dev/null || true

echo ""
echo "✅ Git cleanup complete!"
echo ""
echo "⚠️  IMPORTANT: Files have been removed from Git tracking but still exist on your computer."
echo "   They are now listed in .gitignore and won't be committed in the future."
echo ""
echo "Next steps:"
echo "  1. Review changes: git status"
echo "  2. Commit the cleanup: git commit -m 'chore: remove large files and secrets from Git tracking'"
echo "  3. Push to remote: git push"
echo ""
