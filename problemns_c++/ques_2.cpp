#include <iostream>
using namespace std;
char** available_courses(int no_of_courses){
    char** courses = (char**)malloc(no_of_courses * sizeof(char*));
    for (int i =0 ; i < no_of_courses; ++i)
        courses[i] = (char*)malloc(20 * sizeof(char));
    courses[0] = "C/C++";
    courses[1] = "python";
    courses[2] = "DSA";
    courses[3] = "PlacementPreparation";
    return courses;
}
int no_of_course(){
    return 4;
}
void course_details(char* course){
    if(course == "C/C++"){
        printf("C/C++\nThis is the first language to learn because it not only helps you to strengthen"
        " your programming basics but its logic building techniques help you to excel in coding life."
        "\n\nTo learn and get more info, visit on \nwww.printhello.in/programming\n\n");
    }
    else if(course == "python"){
        printf("Python\nNo 1 language in the IEEE list which opens the gate for a wide range of projects in ML, AI, computer vison and lot more. Learning this langauge is the best way"
        " to keep your first step in world of innovation\n\nTo learn and get more info, visit on \nwww.printhello.in/learn-python-in-easier-way\n\n");
    }
    else if(course == "DSA"){
        printf("DSA\nData structures and Algorithm is the most important subject to be prepared for placements. Being good at it will give you an edge in the huge placement competition and make sure that you get the right offer that you seek and deserve."
        "\n\nTo learn and get more info, visit on \nwww.printhello.in/interview-preparation\n\n");
    }
    else(course == "PlacementPreparation"){
        printf("Placement preparation with proper guidance is the key. You need to know which areas to fous into. Gaining understanding in DS and Algo concepts and practising mock interviews are the vital and inevitable building blocks of preparation. Getting guidance from  the right and experienced people will help you come out with flying colors. "
        "\n\nWant to get prepared for Placements, visit on \nwww.printhello.in/interview-preparation\n\n");
    }
}
int main() {
    int no_of_courses = no_of_course();
    printf("-----------------------PrintHello-------------------------------\n");
    char *courses = available_courses(no_of_courses);
    for(int i=0;i<no_of_courses;i++){
        course_details(courses[i]);
    }
    printf("Register Now. New Batches are starting from 8th October\nwww.printhello.in");
    return 0;
}