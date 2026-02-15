# Module 7: MLOps (Machine Learning Operations)

## Overview
This module teaches how to deploy, monitor, and maintain machine learning models in production.

## Prerequisites
- Module 4: Machine Learning (required)
- Module 5: Deep Learning (recommended)
- Understanding of software engineering practices
- Familiarity with version control (Git)

## Learning Objectives
By the end of this module, you will be able to:
- Track experiments and model versions using MLflow
- Deploy ML models to production environments
- Monitor model performance and detect drift
- Implement CI/CD pipelines for ML projects
- Manage model lifecycle from development to retirement
- Version datasets and models effectively

## Study Order
1. **mlflow.ipynb** - Introduction to MLflow for experiment tracking
2. **model_dev.ipynb** - Model development best practices
3. **main.py** - Production model serving example

## Key Concepts to Master
- Experiment tracking and reproducibility
- Model versioning and registry
- Feature stores and data pipelines
- Model serving (batch vs real-time)
- A/B testing and canary deployments
- Model monitoring and performance tracking
- Data drift and model degradation detection

## Tools & Frameworks
- **MLflow** - Experiment tracking and model management
- **Docker** - Containerization for deployment
- **Git** - Version control for code and experiments
- Model serving: Flask, FastAPI, or cloud solutions

## Project Structure Best Practices
- Separate data, models, and code
- Use configuration files for hyperparameters
- Implement logging and error handling
- Write tests for model validation
- Document model cards and performance metrics

## MLflow Artifacts
The `mlruns/` directory contains experiment tracking data and saved models. Use MLflow UI to visualize experiments:
```bash
mlflow ui
```

## Career Path
With MLOps skills, you're ready to work as a production ML engineer or move into specialized roles like ML infrastructure engineer or ML platform developer.
