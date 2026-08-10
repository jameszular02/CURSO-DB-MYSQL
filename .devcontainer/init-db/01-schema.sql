-- Se ejecuta automaticamente la PRIMERA vez que se crea el contenedor db
-- (MariaDB solo corre los scripts de /docker-entrypoint-initdb.d cuando
-- el volumen db-data esta vacio, es decir, en la primera creacion).
--
-- IMPORTANTE: esta estructura es una suposicion basada en las columnas
-- que se usan en insertar_cliente() y consultar_cliente() dentro de
-- mantenimiento_v_1.py. Si ya tienes un archivo .sql exportado desde tu
-- phpMyAdmin local (pestaña Exportar -> formato SQL), borra este archivo
-- y coloca el tuyo en su lugar con el mismo nombre de carpeta
-- (.devcontainer/init-db/) para recrear tu estructura real completa,
-- incluyendo la tabla Ventas u otras que tengas.

USE meat_to_eat;

CREATE TABLE IF NOT EXISTS clientes (
    cliId       INT PRIMARY KEY,
    cliNom      VARCHAR(50)  NOT NULL,
    cliPape     VARCHAR(50)  NOT NULL,
    cliSape     VARCHAR(50),
    cliMovil    VARCHAR(20),
    cliCorreo   VARCHAR(100),
    cliDireccion VARCHAR(150),
    cliFecReg   DATE,
    cliEstado   VARCHAR(10)
);
