"""
Ejercicio 1:
    a) Diferencia en porcentaje entre el curso actual en comparación con:
    el más rapido de otros cursos
    el más lento de otros cursos
    el promedio de los cursos
    
    b)porcentaje de material inservible (crudo menos duración del curso)
    que se reduce en:
    el promedio de los cursos
    el curso actual
    
    c) ver 10 horas de este curso a cuántas horas equivale de otros cursos
"""

this_course = 1.5
min_course = 2.5
average_course = 4
max_course = 7

this_course_crude = 3.5
other_course_crude_average = 5

#clause a

this_vs_min = ((min_course - this_course) / min_course) * 100
this_vs_max = ((max_course - this_course) / max_course) * 100
this_vs_av =  ((average_course - this_course) / average_course) *100

print(f"this course has a duration of {this_vs_min}% less than the shortest course")
print(f"this course has a duration of {this_vs_max}% less than the longest course")
print(f"this course has a duration of {this_vs_av}% less than the average course")

#clause b
time_eliminated_this = ((this_course_crude-this_course)/this_course_crude)*100

time_eliminated_average = ((other_course_crude_average - average_course)/other_course_crude_average)*100

print(f"The percentage of elimitated time for this course is: {time_eliminated_this}")
print(f"The percentage of elimitated time for average courses is: {time_eliminated_average}")

#clause c
time_10_this = (average_course/this_course)*10
time_10_others = (this_course/average_course)*10
print(f"watching teen hours of this course, is equivalent to watch {time_10_this} hours of the average courses")
print(f"watching teen hours of average courses, is equivalent to watch {time_10_others} hours of this courses")


"""
ejercicio 2
solicirar una frase al usuario y regresar cuánto tiempo se tardaría en decir la frase
teniendo en cuenta que el promedio es de 2 palabras por segundo

y cuanto tardaría una persona que habla un 205 más lento y una que habla un 20% más rapido
"""
string = input("give me a sentence: ")
string_split = string.split(" ")
number_words = len(string_split)
if number_words < 120:
    print(f"The estimated time to speak this sentence is {number_words/2} seconds." )
    print(f"someone who speaks 20 percent faster would take {number_words/2/1.2} seconds.")
    print(f"someone who speaks 20 percent slower would take {number_words/2*1.2} seconds.")
