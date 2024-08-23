import logging
from sqlalchemy.orm import Session
from accessData.conexion import SessionLocal
from accessData.entities.models import Estudiante, Publicacion
from services.Estudiante_Service import EstudianteService
from services.Publicacion_Service import PublicacionService
from services.Export_Service import export_table
from services.ImportService import import_historial
from services.logger_Service import log_action

logging.basicConfig(filename='logs/app.log', level=logging.INFO)

def main():
    db: Session = SessionLocal()
    estudiante_service = EstudianteService()
    publicacion_service = PublicacionService()

    while True:
        print("\n-----MENU------")
        print("1. Crear Estudiante")
        print("2. Mostrar todos los Estudiantes")
        print("3. Editar Estudiante")
        print("4. Eliminar datos del Estudiante")
        print("5. Crear Publicación")
        print("6. Mostrar todas las Publicaciones")
        print("7. Editar Publicacion")
        print("8. Eliminar Publicación")
        print("9. Exportar Tabla de estudiante o publicacion")
        print("10. Importar Historial")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            edad = int(input("Ingrese la edad: "))
            mail = input("Ingrese el correo electrónico: ")
            matricula = input("Ingrese la matrícula: ")
            carrera = input("Ingrese la carrera: ")
            logging.info(f'Intentando crear estudiante con nombre: {nombre}, apellido: {apellido}, edad: {edad}, mail: {mail}, matricula {matricula}, carrera: {carrera}')
            nuevo_estudiante = Estudiante(nombre=nombre, apellido=apellido, edad=edad, mail=mail, matricula=matricula, carrera=carrera)
            estudiante_service.create(db, nuevo_estudiante)
            log_action('C: Estudiante creado')
            with open('registro.txt', 'a') as file:
                file.write(f'Estudiante creado: {nombre}, {apellido}, Edad: {edad} Email: {mail}, edad: {edad}, mail: {mail}, matricula {matricula}, carrera: {carrera}\n')

        elif opcion == '2':
            print("--Esta es la lista solicitada de estudiantes--")
            estudiantes = estudiante_service.select_all(db)
            for estudiante in estudiantes:
                print(f"ID: {estudiante.id}, Nombre: {estudiante.nombre}, Apellido: {estudiante.apellido}")
            log_action('R: Estudiantes leídos')
            with open('registro.txt', 'a') as file:
                file.write('Estudiantes leídos\n')

        elif opcion == '3':
            entity_id = int(input("Ingrese el ID del estudiante: "))
            nuevo_nombre = input("Ingrese el nuevo nombre del estudiante: ")
            nuevo_apellido = input("Ingrese el nuevo apellido del estudiante: ")
            nueva_edad = input("Ingrese la nueva edad: ")
            nuevo_mail = input("Ingrese el nuevo mail: ")
            nueva_matricula = input("Ingrese la nueva matricula: ")
            nueva_carrera = input("Ingrese la nueva carrera: ")
            nuevo_data = {
            'nombre': nuevo_nombre,
            'apellido': nuevo_apellido,
            'edad': nueva_edad,
            'mail': nuevo_mail,
            'matricula': nueva_matricula,
            'carrera': nueva_carrera
            }
            estudiante_service.update(db, entity_id, nuevo_data)
            print("Estudiante actualizado con exito")
            log_action('U: Usuario actualizado')
            with open('registro.txt', 'a') as file:
                file.write(f'Usuario actualizado: {entity_id} a {nuevo_nombre}, {nuevo_apellido}, {nueva_edad}, {nuevo_mail}, {nueva_matricula}, {nueva_carrera} \n')


        elif opcion == '4':
            entity_id = int(input("Ingrese el ID del estudiante a eliminar: "))
            estudiante_service.delete(db, entity_id)
            print ("--Estudiante eliminado de la lista--")
            log_action('D: Estudiante eliminado')
            with open('registro.txt', 'a') as file:
                file.write(f'Estudiante eliminado: {entity_id}\n')

        elif opcion == '5':
            estudiante_id = int(input("Ingrese el ID del usuario: "))
            titulo = input("Ingrese el título de la publicación: ")
            contenido = input("Ingrese el contenido de la publicación: ")
            nueva_publicacion = Publicacion(titulo=titulo, contenido=contenido, estudiante_id=estudiante_id)
            publicacion_service.create(db, nueva_publicacion)
            print("Publicacion creada")
            log_action('C: Publicación creada')
            with open('registro.txt', 'a') as file:
                file.write(f'Publicación creada: {titulo}\n')

        elif opcion == '6':
            publicaciones = publicacion_service.select_all(db)
            for publicacion in publicaciones:
                print(f'-Título: {publicacion.titulo}, Contenido: {publicacion.contenido}')
            log_action('R: Publicaciones leídas')
            with open('registro.txt', 'a') as file:
                file.write('Publicaciones leídas\n')

        elif opcion == '7':
            entity_id = int(input("Ingrese el ID de la publicación: "))
            nuevo_titulo = input("Ingrese el nuevo título de la publicación: ")
            nuevo_contenido = input("Ingrese el nuevo contenido de la publicación: ")
            publicacion_service.update(db, entity_id, {'titulo': nuevo_titulo, 'contenido': nuevo_contenido})
            print("Se realizo la actualizacion de la Publicacion")
            log_action('U: Publicación actualizada')
            with open('registro.txt', 'a') as file:
                file.write(f'Publicación actualizada: {entity_id} a {nuevo_titulo}\n')

        elif opcion == '8':
            entity_id = int(input("Ingrese el ID de la publicación a eliminar: "))
            publicacion_service.delete(db, entity_id)
            print("Publicacion eliminada de la lista")
            log_action('D: Publicación eliminada')
            with open('registro.txt', 'a') as file:
                file.write(f'Publicación eliminada: {entity_id}\n')

        elif opcion == '9':
            table_name = input("Ingrese el nombre de la tabla a exportar ('estudiante' o 'publicacion'): ")
            export_table(db, table_name)
            log_action(f'Exportación de tabla: {table_name}')

        elif opcion == '10':
            print("Importación de historial iniciada...")
            log_action('Importación de historial iniciada')
            import_historial(db)
            print("Importación de historial completada.")
            log_action('Importación de historial completada')

        elif opcion == '0':
            print("Hasta la proximaaa")
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
