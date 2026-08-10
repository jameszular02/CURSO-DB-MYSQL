'''
Acordarse de instalar el conector en la terminal
pip install mysql-connector-python
(esto ya se instala solo gracias a postCreateCommand en devcontainer.json)

Conector hacia la base de datos MariaDB que corre en el contenedor "db"
definido en .devcontainer/docker-compose.yml. Este contenedor reemplaza
al servidor MySQL/MariaDB que antes daba XAMPP en tu computadora.

OJO: dentro de Codespaces, "db" NO es localhost. Es el nombre del
servicio definido en docker-compose.yml, y Docker lo resuelve como si
fuera una direccion de red dentro del mismo proyecto.
'''

import mysql.connector

try:
    cnn = mysql.connector.connect(
        host='db',         # nombre del servicio en docker-compose.yml (no "localhost")
        user='root',
        password='root',   # debe coincidir con MARIADB_ROOT_PASSWORD en docker-compose.yml
        database='meat_to_eat'
    )
    print("¡La base de datos se ha conectado correctamente!")
except mysql.connector.Error as err:
    print(f"¡La conexión a la base de datos falló!: {err}")
