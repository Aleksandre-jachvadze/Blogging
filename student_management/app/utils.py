import matplotlib.pyplot as plt
from io import BytesIO
import base64

def plot_grades(student):
    subjects = [grade.subject for grade in student.grades]
    scores = [grade.score for grade in student.grades]

    plt.figure(figsize=(6,4))
    plt.bar(subjects, scores)
    plt.title(f'Grades for {student.first_name}')
    plt.xlabel('Subjects')
    plt.ylabel('Score')

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close()
    return img_base64
