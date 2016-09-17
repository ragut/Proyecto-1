# Grupo08-201610
Este trabajo es realizado para el curso de Desarrollo de Solcuiones Cloud de la Universidad de Los Andes.
El trabajo esta en desarrollo durante el semestre 2016-10.

## Integrantes
Sebastián Sastoque Hernández ([s.sastoque10@uniandes.edu.co](mailto:s.sastoque10@uniandes.edu.co))

Nicolás Cadena ([n.cadena411@uniandes.edu.co](mailto:n.cadena411@uniandes.edu.co))

# Versiones

## Versión 2 (09 de Marzo de 2016)
En esta versión el proyecto puede ser ejecutado desde amazon web services con dos modos de despliegue (Aplicación en una instancia (Despliegue A) y Modelo de despliegue en 3 instancias diferentes (Despliegue B)).
Para desplegar la aplicación desde Amazon Web Services, es necesario en cada máquina virtual configurar las siguientes variables de entorno:
+ MDB_HOST=DNS del servicio de Amazon para bases de datos MySQL. RDS
+ MDB_PORT=Puerto de la base de datos
+ MDB_PASS=Contraseña de la base de datos
+ MDB_USER=Usuario de la base de datos
+ MDB_NAME=Nombre de la Base de datos
+ MDB=Tipo de base de datos en este caso MariaDB
+ FileSystem=Tipo de sistema de archivos propio o NFS
+ smtp_user=Usuario del servicio de correo de amazon
+ smtp_password=Password del servicio de correo de amazon


Se modifica el proyecto para correr en Amazon Web Services, con las siguientes mejoras:
+ Se puede seleccionar que tipo de base de datos utilizar
+ Se crean servicios nuevos para el manejo de archivos y de base de datos
+ Se agrega soporte para base de datos relacional con MariaDB
+ Se modifica el servicio de Mailing para utilizar el de Amazon
+ Parametros configurables para el modo de Despliegue

### Requerimientos
Para poder utilizar el desarrollo se deben tener instalados en la maquina virtual:
+ [Python 2.7](https://www.python.org/download/releases/2.7/)
+ [Tornado 4.3](http://www.tornadoweb.org/en/stable/)
+ [PyMongo 3.2.1](https://api.mongodb.org/python/current/)
+ [MySQL-Python](https://pypi.python.org/pypi/MySQL-python)
+ [Pillow 3.1.1](http://python-pillow.org/)
+ Servicio NDF en una de las máquinas virtuales
+ Base de datos RDS configurada con MariaDB
+ Configuradas las variables de entorno

## Versión 1 (22 de Febrero de 2016)
Esta es la versión inicial del proyecto. Las funcionalidades asociadas a esta versión se listan a continuación:
+ Página principal del sitio Design Match
+ Creación de página y usuario para empresas
+ Creación y gestión de proyectos
+ Visualización de proyectos
+ Envío de propuesta de diseño asociados a un proyecto
+ Visualización de diseños por cada proyecto
+ Visualización de todos los diseños cargados
+ Procesamiento de diseños en batch para unificar tamaños, tipo de archivos y poner leyenda en el diseño subido

### Requerimientos
Para poder utilizar el desarrollo se deben tener instalados en el equipo:
+ [Python 2.7](https://www.python.org/download/releases/2.7/)
+ [Tornado 4.3](http://www.tornadoweb.org/en/stable/)
+ [PyMongo 3.2.1](https://api.mongodb.org/python/current/)
+ [Pillow 3.1.1](http://python-pillow.org/)
+ [MongoDB 3.2](https://www.mongodb.org/)

### Instrucciones
Para poner en línea el servidor se debe ejecutar el archivo [server.py](../master/server.py). 
El servicio se pone en linea en localhost en el puerto 3300.

Para ejecutar el proceso en Batch o Cron que modifica las imagénes y las pone en linea, se debe configurar el CronJob para que se ejecute el archivo [process_images.py](../master/process_images.py)