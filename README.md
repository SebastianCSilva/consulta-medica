Para este proyecto se necesita tener
django 3.1.3
psycopg2
Postgresql 4

En caso de tener posibles problemas con Postgresql se pueden encontrar las configuraciones en 
consulta>>> settings.py
y cambiar posibles configuraciones distintas en DATABASES con los contrasena y puerto que tambien puede tirar error 


Para iniciar toda la base de datos del proyecto
Es necesario estar con enviroment de django activado 

1 python manage.py makemigrations
2 python manage.py migrate

Para correr el servidor local de django
python manage.py runserver

Todas las Rutas pueden ser vistas en tanto dentro del proyecto como en 
consulta>> urls.py
panel_principal>> urls.py

Para ver el como se hizo el Filtrado de datos para el csv esta dentro de 
panel_principal>> views.py
ultima funcion

Para Pedir CSV con filtrado se tiene que hacer con este formato
http://127.0.0.1:8000/exportcsv/2020-11-25/2020-11-26/

http://127.0.0.1:8000/exportcsv/FechaInicio/FechaFinal/

                                2020-11-25

Para ver todas las plantillas html
panel_principal>> templates >>


---Plus 
Procedure para Crear funcion que ve los datos de un doctor/medico
Esto vendria a ser en el panel de Postgresql 4


Create function BuscarMedico(identificador int)
returns setof panel_principal_medico
as
$$
select X.id, X.nombre, X.apellidos, X.rut, X.direccion, X.fecha_nacimiento, X.created_date, Y.id
from public.panel_principal_medico X, public.panel_principal_genero Y where X.id=identificador and X.genero_id=Y.id
$$
Language SQL

------
Asi es como se veria la function

SELECT public.buscarmedico(
	<identificador integer>
)

Y para ingresar datos de busqueda por id en este caso el con id 1
SELECT public.buscarmedico(
	1
)