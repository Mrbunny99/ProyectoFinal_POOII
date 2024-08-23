====PROPÓPISTO DEL PROYECTO====

En este proyecto se realizo el Proyecto Final de programacion orientada a objetos
utilizando el lenguaje de programacion python. Aqui se implemento un CRUD y Persistencia ORM
con arquitectura en capas. En mi proyecto realice la creacion de dos tablas en la base de datos
que son "Estudiantes" y "Publicacion", en la cual hago referencia un sistema donde los estudiantes
se apuntan con sus temas de tesis y asi facilitar la administracion de los mismos hasta que
realicen sus respectivas defensas.

====CONFIGURACIÓN Y EJECUCION DEL PROYECTO====

Primero debemos tener en la computadora instalado el "Docker" y tabien " MySQL Workbench".
En el MySQL Workbench hay que crear un servidor donde se va a conectar con el Docker, en el cual
se configura en el Visual Estudio.
Se hace la respectiva copia en el github para poder descargarlo a la computadora, aqui se debe abrir
con la herramienta de "Visual Estudio", se busca la carpeta en el lugar donde se descargo. Una vez
abierto en el Visual Estudio se debe crear un ambiente como el siguiente:

---crear ambiente virtual
python -m venv myenv

Luego se debe activar el ambiente:

---activar ambiente virtual
.\myenv\Scripts\activate

Una vez dentro del ambiente, se debe instalar el conector a mysql:

python -m pip install mysql-connector-python
PARA INSTALAR PYTHON CON MYSQL

Luego se instalamos el sqlalchemy
pip install sqlalchemy

y actualizamos por si acaso:
python.exe -m pip install --upgrade pip

Se ingresa: 
docker-compose -f .\docker-compose-mysql.yml up -d
para poder conectar el MySQL con el Docker. Una vez que este conectado ya se puede ejecutar el programa.

Para ejecutar el programa hay que ir a la ubicacion de la carpeta del proyecto en la terminal e ingresar lo siguiente:

python main.py

Aqui sale el menu donde se pude interactuar dependiendo las necesidad que se requiera.


====EJEMPLO DE USO Y SALIDAS ESPERADAS====

Cuando se ingresa "crear estudiante", el programa te pide diferentes datos que los puedes ingresar por teclado,
ingresas el nombre, apellido, edad, mail, matricula y carrera. Una vez ingresado esto se guarda en la base de datos
y se registra en historial para su uso al exportar.

Cuando se ingresa "mostrar todos los estudiantes", el programa hace una lectura en la base de datos y lo muestra 
para ver los datos que se encuentran ahi.

Cuando se ingresa "editar estudiante" aqui el programa te vuelve a preguntar por el nombre, apellido, edad, mail, matricula y carrera,
entonces aqui los datos que se ingresan se sobreescriben en los datos antiguos y estos se guardan en la base de datos.

Cuando se ingresa"eliminar datos del estudiante" aqui el programa te pide que ingreses el ID del estudiante que deseas eliminar,
una vez que se ingrese el id, este elimina de la base de datos todo lo referente a esta ID.

Cuando se ingresa "Crear publicacion" aqui el programa pide el ID del estudiante, titulo y contenido de la publicacion. Aqui los datos
se colocan en otra tabla de la base de datos llamada 'publicaciones' y se guardan.

Cuando se ingresa "mostrar todas las publicaciones" aqui el programa hace una lectura de los datos que se encuentran en la tabla
de publicaciones y la muestra en la terminal.

Cuando se ingresa "editar publicacion" el programa pide de nuevo el ID del estudiante, el titulo y la descripcion de la publicacion
para que los datos nuevos que se ingresan se sobreescriben y se guardan en la base de datos.

Cuando se ingresa "eliminar publicacion", el programa pide el ID del proyecto, cuando se ingresa el ID este elimina todo lo referente
al ID en la tabla publicaciones de la base de datos.

Cuando se ingresa "Exportar tabla de estudiante o publicacion" hace que los datos que estan guardados en la base de datos se
ingresen en un archivo de texto con el nombre de la tabla y la fecha actual.

Cuando se ingresa "Importar historial" se aprovecha el procesamiento en paralelo para acelerar la insercion de datos desde el archivo
historial.txt a la base de datos, distribuyendo la tarea entre multiples hilos.