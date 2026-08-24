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
