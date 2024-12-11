from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import random

Base = declarative_base()

student_course_table = Table(
    'student_course', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)


class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    courses = relationship("Course", secondary=student_course_table, back_populates="students")

    def __repr__(self):
        return f"<Student(name='{self.name}')>"


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    students = relationship("Student", secondary=student_course_table, back_populates="courses")

    def __repr__(self):
        return f"<Course(name='{self.name}')>"


engine = create_engine('sqlite:///students_courses.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Create 5 courses
course_names = ["Math", "Physics", "Chemistry", "Biology", "History"]
for name in course_names:
    session.add(Course(name=name))
session.commit()

courses = session.query(Course).all()

for i in range(1, 21):
    student = Student(name=f"Student {i}")
    student.courses = random.sample(courses, k=random.randint(1, 3))
    session.add(student)
session.commit()


def add_student(name, course_name):
    course = session.query(Course).filter_by(name=course_name).first()
    if not course:
        print(f"Course '{course_name}' not found.")
        return

    student = Student(name=name)
    student.courses.append(course)
    session.add(student)
    session.commit()
    print(f"Added {student} to course {course}.")


def get_students_in_course(course_name):
    course = session.query(Course).filter_by(name=course_name).first()
    if not course:
        print(f"Course '{course_name}' not found.")
        return

    return course.students


def get_courses_for_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if not student:
        print(f"Student '{student_name}' not found.")
        return

    return student.courses


def update_student_name(old_name, new_name):
    student = session.query(Student).filter_by(name=old_name).first()
    if not student:
        print(f"Student '{old_name}' not found.")
        return

    student.name = new_name
    session.commit()
    print(f"Updated student name to '{new_name}'.")


def delete_student(student_name):
    student = session.query(Student).filter_by(name=student_name).first()
    if not student:
        print(f"Student '{student_name}' not found.")
        return

    session.delete(student)
    session.commit()
    print(f"Deleted student '{student_name}'.")


add_student("New Student", "Math")
students_in_math = get_students_in_course("Math")
print("Students in Math:", students_in_math)

courses_for_student = get_courses_for_student("Student 1")
print("Courses for Student 1:", courses_for_student)

update_student_name("Student 1", "Updated Student 1")
delete_student("Updated Student 1")
