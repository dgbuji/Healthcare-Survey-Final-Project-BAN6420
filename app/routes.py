from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import User
from app import mongo 

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        try:
            User.save_survey(request.form)
            flash('Thank you for completing the survey!', 'success')
            return redirect(url_for('main.survey'))
        except Exception as e:
            flash(f'Error submitting survey: {str(e)}', 'danger')
    
    return render_template('survey.html')

@bp.route('/export')
def export_data():
    try:
        csv_path = User.export_to_csv()
        flash(f'Data exported successfully to {csv_path}', 'success')
    except Exception as e:
        flash(f'Error exporting data: {str(e)}', 'danger')
    return redirect(url_for('main.survey'))

@bp.route('/testdb')
def test_db():
    try:
        # Test connection by counting documents
        count = mongo.db.surveys.count_documents({})
        return f"Database connection successful! Found {count} surveys."
    except Exception as e:
        return f"Database connection failed: {str(e)}", 500
    

