from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import db, Student, Grade

main = Blueprint('main', __name__)

# Home
@main.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)

# Add Student
@main.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        classroom = request.form['classroom']

        new_student = Student(first_name=first_name, last_name=last_name, email=email, classroom=classroom)
        db.session.add(new_student)
        db.session.commit()
        flash('Student added successfully!', 'success')
        return redirect(url_for('main.index'))

    return render_template('add_student.html')

# Edit Student
@main.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.first_name = request.form['first_name']
        student.last_name = request.form['last_name']
        student.email = request.form['email']
        student.classroom = request.form['classroom']
        db.session.commit()
        flash('Student updated successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('edit_student.html', student=student)

# Delete Student
@main.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('main.index'))

# Filter by classroom
@main.route('/classroom/<string:classroom>')
def filter_classroom(classroom):
    students = Student.query.filter_by(classroom=classroom).all()
    return render_template('index.html', students=students)
