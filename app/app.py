"""
Student Feedback System - Flask Application
"""
from flask import Flask, render_template, request, redirect, url_for, flash
from database import init_db, insert_feedback, get_all_feedback

app = Flask(__name__)
app.secret_key = 'student-feedback-secret-key-2026'


@app.route('/')
def index():
    """Render the feedback form along with all existing feedback."""
    feedbacks = get_all_feedback()
    return render_template('index.html', feedbacks=feedbacks)


@app.route('/submit', methods=['POST'])
def submit():
    """Handle feedback form submission."""
    name = request.form.get('name', '').strip()
    feedback = request.form.get('feedback', '').strip()

    if not name or not feedback:
        flash('Both Name and Feedback fields are required!', 'error')
        return redirect(url_for('index'))

    insert_feedback(name, feedback)
    flash('Feedback submitted successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
