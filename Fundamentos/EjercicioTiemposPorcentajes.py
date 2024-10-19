#Practice Excercices
#Ejercicio_1.1

#Promedio de duración
otros_cursos_min = 2.5 
otros_cursos_max = 7
otros_cursos_prom = 4
dalto_curso = 1.5

#Duración de crudos (contenido sin editar)
crudo_dalto = 3.5
crudo_promedio = 5



#Diferencias de duración
diferencia_min = round(100 - (dalto_curso / otros_cursos_min * 100), 2)
diferencia_max = round(100 - (dalto_curso / otros_cursos_max * 100), 2)
diferencia_prom = round(100 - (dalto_curso / otros_cursos_prom * 100), 2)
print(f"El curso de Dalto dura un: {diferencia_min}% menos que el más rápido.")
print(f"El curso de Dalto dura un: {diferencia_max}% menos que el más lento.")
print(f"El curso de Dalto dura un: {diferencia_prom}% menos que el promedio.")

#Diferencias de contenido crudo
diferencia_crudo = round(100 - (crudo_dalto/crudo_promedio * 100), 2)
tiempo_eliminado_promedio = round(100 - (otros_cursos_prom/crudo_promedio * 100), 2)
tiempo_eliminado_dalto = round(100 - (dalto_curso /crudo_dalto * 100), 2)

print(f"Un curso promedio elimina un {tiempo_eliminado_promedio}% de tiempo vacío")
print(f"Este curso eliminó un {tiempo_eliminado_dalto}% de tiempo vacío")
diez_este = round(otros_cursos_prom/dalto_curso *10 , 2)
diez_otro = round(dalto_curso/otros_cursos_prom *10 , 2)
#Mostrando diferencias si los cursos duraran 10 hrs
print(f"Ver 10 horas de este curso equivale a ver {diez_este} horas de otros curso")
print(f"Ver 10 horas otro curso equivale a ver {diez_otro} horas de este curso")
