"""
Programmer: Stefanie Streger
Assignment: Module 6 - Alternate Programming Assignment
Date Completed: 10/1/21
Course: CITC 2391 - CO2
Instructor: Martin Bell
"""


def main():
    while True:
        user_course = str(input('Enter a course number: '))
        matched_choice = match_course(user_course)
        if user_course != matched_choice:
            print('Please enter a valid course number')
            # user_course = str(input('Enter a course number: '))
            continue
        else:
            location = get_location(user_course)
            instructor = get_instructor(user_course)
            time = get_time(user_course)
            print('The details for course', user_course, 'are: ')
            print('Room: ', location)
            print('Instructor: ', instructor)
            print('Time: ', time)
            break


def match_course(course):
    course_list = {'CS101', 'CS102', 'CS103', 'NT110', 'CM241'}
    course_match = ''
    for value in course_list:
        if course == value:
            course_match += course
    return course_match


def get_location(course):
    location = {
        'CS101': '3004',
        'CS102': '4501',
        'CS103': '6755',
        'NT110': '1244',
        'CM241': '1411'
    }
    selected_location = location.get(course)
    return selected_location


def get_instructor(course):
    instructor = {
        'CS101': 'Haynes',
        'CS102': 'Alvarado',
        'CS103': 'Rich',
        'NT110': 'Burke',
        'CM241': 'Lee'
    }
    selected_instructor = instructor.get(course)
    return selected_instructor


def get_time(course):
    time = {
        'CS101': '8:00 am',
        'CS102': '9:00 am',
        'CS103': '10:00 am',
        'NT110': '11:00 am',
        'CM241': '1:00 pm'
    }
    selected_time = time.get(course)
    return selected_time


main()
