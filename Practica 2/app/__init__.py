import sqlite3

db = sqlite3.connect('C:/Users/lapri/PycharmProjects/Practica2.3/app/data/Usuario.db')
print("Base de datos abierta")

cursor = db.cursor()

tabla1 = [
		"""
			CREATE TABLE IF NOT EXISTS Persona(
				ID INTEGER PRIMARY KEY,
				ID_Persona INTEGER NOT NULL,
				NOMBRE TEXT NOT NULL,
				P_APELLIDO TEXT NOT NULL,
				S_APELLIDO TEXT NOT NULL,
				LUGAR TEXT NOT NULL,
				FOREIGN KEY (ID_Persona)
                REFERENCES Familia(ID_Persona)
			)ENGINE=InnoDB;
		"""
    ]
# for tabla11 in tabla1:
# 	cursor.execute(tabla11);
print("Tablas creadas correctamente")

tabla4 = [
		"""
			CREATE TABLE IF NOT EXISTS Familia(
				ID_Padre INTEGER PRIMARY KEY,
				ID_Madre INTEGER PRIMARY KEY,
				ID_Hijo INTEGER PRIMARY KEY,
				ID_Persona INTEGER PRIMARY KEY
			)ENGINE=InnoDB;
		"""
    ]
# for tabla44 in tabla4:
# 	cursor.execute(tabla44);
print("Tablas creadas correctamente")


print("1-Insertar Persona.")
print("2-Ver Persona.")
print("3-Borrar Persona.")
print("4-Salir")

a = int(input("Escoja la opcion que desea:"))

if a==1: #insertar

        NOMBRE = input("\nNOMBRE: ")
        P_APELLIDO = input("\nP_APELLIDO: ")
        S_APELLIDO = input("\nS_APELLIDO: ")
        LUGAR = input("\nLUGAR : ")
        tabla55 = "INSERT INTO Persona(NOMBRE, P_APELLIDO, S_APELLIDO, LUGAR) VALUES (?,?,?,?)"
        cursor.execute(tabla55, [NOMBRE, P_APELLIDO, S_APELLIDO, LUGAR])
        db.commit()
        print("Guardado correctamente")


elif a==2: #ver

    print("1-Ver todo.")
    print("2-Ver por familia")

    b = int(input("Escoja la opcion que desea:"))
    if b==1:
        tabla55 = "SELECT * FROM Persona;"
        cursor.execute(tabla55)
        Persona = cursor.fetchall()
        print("\n", Persona)

    elif b==2:
        relacion = "SELECT * FROM Familia"
        cursor.execute(relacion)
        Familia = cursor.fetchall()  # muestra la fila
        for row in Familia:
            print("\n",Familia)

        # "SELECT Padre. *, Familia. *"
        # "SELECT Madre. *, Familia. *"
        # "SELECT Hijo. *, Familia. *"

        tabla44 = "SELECT * FROM Familia;"
        cursor.execute(tabla44)
        Familia = cursor.fetchall()
        print("\n", Familia)


elif a==3: #eliminar

        cursor.execute('''SELECT ID, NOMBRE, P_APELLIDO, S_APELLIDO, LUGAR FROM Persona''')
        resultado = cursor.fetchall()
        for fila in resultado:
            print("{0} : {1}".format(fila[0], fila[1]))

        ID = input("ID de usuario a eliminar: ")
        for fila in resultado:
            if int(ID) == int(fila[0]):
                 cursor.execute('''DELETE FROM Persona WHERE id = ?''',
                                (ID,))
        db.commit()



else:
	print("Hasta luego")
