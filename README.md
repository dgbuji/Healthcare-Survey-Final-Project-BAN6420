# Healthcare Spending Survey Tool

A Flask-based web application for collecting and analyzing income and spending data, with a focus on healthcare expenditures.

## Features

- Web form for data collection
- MongoDB backend for data storage
- Data export to CSV
- Jupyter Notebook for analysis and visualization
- Ready for AWS deployment

## Setup

### Prerequisites

Before deploying, ensure you have:
AWS Account (with Elastic Beanstalk access)
AWS CLI installed and configured (aws configure)
Python 3.8+ (recommended)
Elastic Beanstalk CLI (pip install awsebcli)
MongoDB Atlas URI (or a self-hosted MongoDB instance)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dgbuji/healthcare-survey-final-project.git
   cd healthcare-survey
   ```
2. Create and activate virtual environment:
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
3. Install dependencies:
   pip install -r requirements.txt

4. Set up environment variables:
   Create a .env file: Not pushed to git repo

Running the Application
bash
python run.py
The application is available at http://127.0.0.1:5000

Data Analysis
Run the Flask app and collect some data

Export data to CSV using the admin link

Open analysis/survey_analysis.ipynb in Jupyter Notebook

Run all cells to generate visualizations

Deployment to AWS
http://healthcare-survey-env.eba-v89mzpyp.us-east-1.elasticbeanstalk.com/

Project Structure
app/: Flask application code

static/: CSS and JavaScript files

templates/: HTML templates

**init**.py: Application factory

models.py: Database models

routes.py: Application routes

analysis/: Jupyter Notebook for data analysis

config.py: Configuration settings

run.py: Application entry point

requirements.txt: Python dependencies

Deployment Steps
1️⃣ Clone the Project & Set Up Virtual Environment
bash
git clone <your-repo-url>
cd <project-folder>
python -m venv venv
source venv/bin/activate # Linux/Mac

# OR

venv\Scripts\activate # Windows
2️⃣ Install Dependencies
bash
pip install -r requirements.txt
Example requirements.txt:

Flask==2.3.2
flask_pymongo==2.3.0
gunicorn==21.2.0
python-dotenv==1.0.0
3️⃣ Configure Environment Variables
Create a .env file (for local testing) and set:

env
MONGO_URI=mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority
SECRET_KEY=XXXXX
⚠️ Do NOT commit .env to Git!

4️⃣ Test Locally
Run Flask locally:python run.py

☁️ Deploying to AWS Elastic Beanstalk
1️⃣ Initialize EB CLI
bash
eb init -p python-3.8 <healthcare-survey> --region us-east-1
(Replace us-east-1 with your preferred AWS region.)

2️⃣ Create an EB Environment
bash
eb create <env-name> --single --instance-types t3.micro
This sets up a single-instance environment with a t3.micro instance.

3️⃣ Configure .ebextensions for Gunicorn
Create .ebextensions/01_python.config:

yaml
option_settings:
aws:elasticbeanstalk:container:python:
WSGIPath: run:app # Replace with your app's entry point (e.g., run:app)

files:
"/etc/nginx/conf.d/proxy.conf":
mode: "000644"
owner: root
group: root
content: |
client_max_body_size 20M;
4️⃣ Set Environment Variables in EB
bash
eb setenv MONGO_URI="mongodb+srv://<username>:<password>@cluster0.mongodb.net/<dbname>?retryWrites=true&w=majority" SECRET_KEY="your-secret-key"
5️⃣ Deploy!
bash
eb deploy
🔍 Troubleshooting
Common Errors & Fixes
Error Solution
502 Bad Gateway Check Gunicorn logs (/var/log/web.stdout.log). Ensure Gunicorn is running.
ModuleNotFoundError Ensure all dependencies are in requirements.txt.
MongoDB Connection Failed Verify MONGO_URI is correct and IP is whitelisted in MongoDB Atlas.
Gunicorn Crashes Manually test with gunicorn --bind 0.0.0.0:8000 run:app.
Checking Logs
bash
eb logs
Or SSH into the instance:

bash
eb ssh
sudo tail -f /var/log/nginx/error.log
sudo tail -f /var/log/web.stdout.log
📜 Project Structure (Example)
your-flask-app/
├── .ebextensions/
│ └── python.config # EB config for Gunicorn
├── .env # Local environment variables (DO NOT COMMIT)
├── requirements.txt # Python dependencies
├── run.py # Flask entry point (or app.py)
└── app/
├── **init**.py # Flask app initialization
├── routes.py # API routes
└── models.py # MongoDB models
🔗 Useful Commands
Command Description
eb deploy Deploy changes to AWS EB
eb open Open the deployed app in browser
eb ssh SSH into the EB instance
eb logs View deployment logs
