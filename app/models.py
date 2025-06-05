from datetime import datetime, timezone
from app import mongo
import os

class User:
    @staticmethod
    def save_survey(data):
        """Save survey data to MongoDB"""
        survey_data = {
            'age': int(data['age']),
            'gender': data['gender'],
            'total_income': float(data['total_income']),
            'expenses': {
                'utilities': float(data.get('utilities', 0)),
                'entertainment': float(data.get('entertainment', 0)),
                'school_fees': float(data.get('school_fees', 0)),
                'shopping': float(data.get('shopping', 0)),
                'healthcare': float(data.get('healthcare', 0))
            },
            'timestamp': datetime.now(timezone.utc) 
        }
        return mongo.db.surveys.insert_one(survey_data)
    
    @staticmethod
    def export_to_csv():
        """Export all survey data to CSV"""
        import pandas as pd
        from config import Config
        
        surveys = list(mongo.db.surveys.find({}, {'_id': 0, 'timestamp': 0}))
        
        # Flatten the expenses dictionary
        for survey in surveys:
            survey.update(survey.pop('expenses'))
        
        df = pd.DataFrame(surveys)
        csv_path = os.path.join(Config.EXPORT_FOLDER, 'survey_data.csv')
        df.to_csv(csv_path, index=False)
        return csv_path