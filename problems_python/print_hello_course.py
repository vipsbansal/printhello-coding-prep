"""
Print Hello is a initiative which is led by two coding enthusiasts Naveen and Vipin who want to change the world with their belief that everyone can code and that too beautifully.
"""


def get_all_courses_printhello():


    printhello_course_map = {

    'C,C++' : "This is the first language to learn because it not only helps you to strengthen your programming basics but its logic building techniques help you to excel in coding life.To learn and get more info, visit on www.printhello.in/programming",

    'Python' : "Python No 1 language in the IEEE list which opens the gate for a wide range of projects in ML, AI, computer vison and lot more. Learning this langauge is the best way to keep your first step in world of innovation. To learn and get more info, visit on www.printhello.in/learn-python-in-easier-way.",

    'DS Algo' : "DSA -> Data structures and Algorithm is the most important subject to be prepared for placements. Being good at it will give you an edge in the huge placement competition and make sure that you get the right offer that you seek and deserve. To learn and get more info, visit on www.printhello.in/interview-preparation.",

    'Placement Prep' : "Placement preparation with proper guidance is the key. You need to know which areas to fous into. Gaining understanding in DS and Algo concepts and practising mock interviews are the vital and inevitable building blocks of preparation. Getting guidance from  the right and experienced people will help you come out with flying colors. Want to get prepared for Placements, visit on www.printhello.in/interview-preparation"
    }

    for course,course_description in printhello_course_map:
        print course, course_description