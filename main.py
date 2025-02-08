# hello world
import os

def create_directory_structure():
    # Base directories
    directories = [
        'data/raw/geospatial',
        'data/raw/weather',
        'data/raw/historical_yields',
        'data/processed',
        'data/external',
        'src/data_processing',
        'src/models',
        'src/messaging',
        'src/visualization',
        'src/utils',
        'notebooks/exploratory',
        'notebooks/analysis',
        'tests/unit',
        'tests/integration',
        'config',
        'logs',
        'models/saved_models'
    ]
    
    # Create directories
    for dir_path in directories:
        os.makedirs(dir_path, exist_ok=True)
        # Create a .gitkeep file in each directory to maintain structure
        with open(os.path.join(dir_path, '.gitkeep'), 'w') as f:
            pass

    # Create essential files
    files = {
        '.gitignore': '''# Data directories
data/
data/*
models/saved_models/

# Environment and credentials
.env
config/credentials.yaml
**/credentials/*

# API keys and secrets
*.pem
*.key

# Large files and datasets
*.csv
*.shp
*.tif
*.geotiff
*.parquet
*.h5

# Python
__pycache__/
*.py[cod]
*$py.class
.Python
env/
venv/
.env/
.venv/

# Jupyter Notebook
.ipynb_checkpoints
*/.ipynb_checkpoints/*

# Logs
logs/
*.log

# OS-specific
.DS_Store
Thumbs.db''',
        
        'requirements.txt': '''# Add your dependencies here
numpy
pandas
scikit-learn
geopandas
rasterio
twilio  # for SMS
python-dotenv''',
        
        'README.md': '''# Farm Yield Predictor

A machine learning model for predicting agricultural yields using geospatial data.

## Setup
1. Clone this repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Configure environment variables in `.env`

## Data
Data is not included in this repository. Contact [Your Name] for access.

## Usage
[Add usage instructions here]''',
        
        '.env': '''# Add your environment variables here
SMS_API_KEY=your_api_key_here
SMS_API_SECRET=your_api_secret_here
'''
    }

    for filename, content in files.items():
        with open(filename, 'w') as f:
            f.write(content)

if __name__ == "__main__":
    create_directory_structure()
    print("Directory structure created successfully!")