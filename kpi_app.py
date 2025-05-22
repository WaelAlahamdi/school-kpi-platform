from flask import Flask, render_template, request, redirect, session, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'w93m2n1x$8!as92bn!lsk02zqplk@r9a'

# Load users from JSON file
def load_users():
    with open('users.json') as f:
        return json.load(f)

# Save attendance to JSON
def save_attendance(data):
    with open('attendance_data.json', 'w') as f:
        json.dump(data, f, indent=2)

# Load attendance from JSON
def load_attendance():
    if not os.path.exists('attendance_data.json'):
        return {}
    with open('attendance_data.json') as f:
        return json.load(f)

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = load_users()
        if username in users and users[username]['password'] == password:
            session['user'] = username
            session['role'] = users[username]['role']
            if session['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('school_dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/school/dashboard', methods=['GET', 'POST'])
def school_dashboard():
    if 'user' not in session or session.get('role') != 'school':
        return redirect(url_for('login'))
    school_name = session['user']
    if request.method == 'POST':
        total = int(request.form['total_students'])
        absent = int(request.form['absent_students'])
        date = datetime.now().strftime('%Y-%m-%d')
        attendance = load_attendance()
        if school_name not in attendance:
            attendance[school_name] = []
        attendance[school_name].append({"date": date, "total": total, "absent": absent})
        save_attendance(attendance)
        return redirect(url_for('school_report'))
    return render_template('school_dashboard.html', school=school_name)

@app.route('/school/report')
def school_report():
    if 'user' not in session or session.get('role') != 'school':
        return redirect(url_for('login'))
    school_name = session['user']
    data = load_attendance().get(school_name, [])
    return render_template('school_report.html', school=school_name, records=data)

@app.route('/admin/dashboard')
def admin_dashboard():
    if 'user' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))
    attendance = load_attendance()
    summary = []
    for school, records in attendance.items():
        total_days = len(records)
        total_absent = sum(r['absent'] for r in records)
        total_students = sum(r['total'] for r in records)
        avg_absence = round((total_absent / total_students) * 100, 2) if total_students else 0
        summary.append({"school": school, "days": total_days, "avg_absence": avg_absence})
    return render_template('admin_dashboard.html', summary=summary)
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
