# Git Best Practices for ML Projects

## ✅ What Was Done

Your repository has been cleaned up to follow ML/AI best practices:

### 1. **Updated .gitignore**
The `.gitignore` file now properly excludes:
- Large model files (`.pth`, `.pkl`, `.h5`, etc.)
- Database files (`.db`, `.sqlite`)
- Data files (`.csv`, `.xlsx`, large datasets)
- Secret files (`.env`, credentials, API keys)
- Python cache (`__pycache__`, `.pyc`)
- Jupyter checkpoints (`.ipynb_checkpoints`)
- Virtual environments (`venv/`, `ml-env/`)
- IDE files (`.vscode/`, `.idea/`, `.DS_Store`)

### 2. **Removed from Git Tracking**
These files were removed from Git but **kept on your computer**:
- `.env` files (contain secrets)
- `mlflow.db` (database files)
- `.pkl` model files
- Large CSV/Excel data files
- `__pycache__` directories
- `.ipynb_checkpoints`

---

## 🚫 What Should NEVER Be Committed

### Secrets & Credentials
- ❌ `.env` files
- ❌ API keys, tokens, passwords
- ❌ AWS/GCP credentials
- ❌ Private keys (`.pem`, `.key`)
- ❌ Database connection strings

### Large Files
- ❌ Model weights (`.pth`, `.pkl`, `.h5`) - use Git LFS or cloud storage
- ❌ Datasets (`.csv`, `.xlsx`) - use DVC or cloud storage
- ❌ Database dumps (`.db`, `.sql`)
- ❌ Large binary files (> 50MB)

### Generated/Temporary Files
- ❌ `__pycache__/` directories
- ❌ `.ipynb_checkpoints/`
- ❌ Virtual environments (`venv/`, `env/`)
- ❌ Log files (`.log`)
- ❌ Temporary files (`.tmp`, `.temp`)

---

## ✅ What SHOULD Be Committed

### Code
- ✅ Python scripts (`.py`)
- ✅ Jupyter notebooks (`.ipynb`) - with output cleared
- ✅ Configuration files (`config.yaml`, `requirements.txt`)
- ✅ Documentation (`.md` files)

### Project Structure
- ✅ README files
- ✅ `.gitignore`
- ✅ `requirements.txt` or `environment.yml`
- ✅ Setup scripts
- ✅ Docker files

### Small Reference Data
- ✅ Small sample datasets (< 1MB) for testing
- ✅ Example configuration files
- ✅ Test fixtures

---

## 📝 Recommended Workflow

### Before Each Commit

1. **Clear Jupyter notebook outputs** (optional but recommended)
   ```bash
   jupyter nbconvert --clear-output --inplace *.ipynb
   ```

2. **Check what you're about to commit**
   ```bash
   git status
   git diff
   ```

3. **Verify no secrets are included**
   ```bash
   git diff | grep -i "api_key\|password\|secret\|token"
   ```

4. **Check file sizes**
   ```bash
   git ls-files | xargs ls -lh | awk '{if ($5 > 1000000) print $5, $9}'
   ```

### Commit Messages
Use clear, descriptive commit messages:
```bash
# Good examples
git commit -m "feat: add decision tree classifier implementation"
git commit -m "fix: correct data normalization in preprocessing"
git commit -m "docs: add explanation for model architecture"
git commit -m "chore: update dependencies in requirements.txt"

# Bad examples
git commit -m "update"
git commit -m "fix stuff"
git commit -m "asdfgh"
```

---

## 🔧 Handling Large Files

### Option 1: Git LFS (Large File Storage)
For model files you want to version:
```bash
# Install Git LFS
git lfs install

# Track specific file types
git lfs track "*.pth"
git lfs track "*.pkl"
git lfs track "*.h5"

# Now you can commit these files
git add .gitattributes
git commit -m "chore: configure Git LFS for model files"
```

### Option 2: DVC (Data Version Control)
For datasets and large files:
```bash
# Install DVC
pip install dvc

# Track a dataset
dvc add datasets/large_dataset.csv

# Commit the .dvc file (not the actual data)
git add datasets/large_dataset.csv.dvc .gitignore
git commit -m "data: add large dataset tracking with DVC"
```

### Option 3: Cloud Storage
Store large files externally:
- **Model Hub**: Hugging Face, ModelDB
- **Cloud Storage**: AWS S3, Google Cloud Storage, Azure Blob
- **ML Platforms**: Weights & Biases, MLflow (with artifact storage)

---

## 🔐 Managing Secrets

### Use Environment Variables
Never hardcode secrets:
```python
# ❌ Bad - hardcoded
api_key = "sk-1234567890abcdef"

# ✅ Good - from environment
import os
api_key = os.getenv("OPENAI_API_KEY")
```

### Use .env Files (with .gitignore)
Create `.env` for local development:
```bash
# .env (this file is in .gitignore)
OPENAI_API_KEY=sk-1234567890abcdef
DATABASE_URL=postgresql://user:pass@localhost/db
```

### Provide a Template
Create `.env.example` (this CAN be committed):
```bash
# .env.example
OPENAI_API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:password@localhost/dbname
```

---

## 🚀 Next Steps

1. **Review the changes**
   ```bash
   git status
   ```

2. **Add all restructured files**
   ```bash
   git add .
   ```

3. **Commit the changes**
   ```bash
   git commit -m "refactor: restructure project for teaching curriculum

   - Reorganize into numbered modules (01-07)
   - Update .gitignore for ML projects
   - Remove large files and secrets from tracking
   - Add comprehensive README files for each module
   - Move working files to archive"
   ```

4. **Push to remote** (if you have one set up)
   ```bash
   git push
   ```

---

## 📚 Additional Resources

- [Git LFS Documentation](https://git-lfs.github.com/)
- [DVC Documentation](https://dvc.org/doc)
- [GitHub: Managing Large Files](https://docs.github.com/en/repositories/working-with-files/managing-large-files)
- [Gitignore.io](https://www.toptal.com/developers/gitignore) - Generate .gitignore files

---

## ⚠️ Important Notes

- The `archive/` folder is in `.gitignore` - it won't be tracked
- Your original structure was backed up before reorganization
- All large files and secrets have been removed from Git tracking
- Files still exist on your computer, just not in version control

---

**Remember**: Git is for code, not for data or secrets! 🔐
