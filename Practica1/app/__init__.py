import sqlite3
import  hashlib

db = sqlite3.connect('C:/Users/lapri/PycharmProjects/Practica1/app/data/prueba.db')
print("Base de datos abierta")

cursor = db.cursor()
tablas = [
		"""
			CREATE TABLE IF NOT EXISTS Libro(
				LSBN INTEGER NOT NULL,
				AUTOR TEXT NOT NULL,
				CANTIDADP INTEGER NOT NULL,
				PUBLICACION INTEGER NOT NULL,
				NOMBRELIBRO TEXT NOT NULL
			);
		"""
	]
for tabla in tablas:
	cursor.execute(tabla);
print("Tablas creadas correctamente")

libros = [
		"""
		INSERT INTO Libro
		(LSBN, AUTOR, CANTIDADP, PUBLICACION, NOMBRELIBRO)
		VALUES
		('001',  'Gabriel Garcia Marquez', '471', '1967', 'Cien años de soledad'),
		('002', ' Jorge Isaacs', '288','1867', 'Maria'),
		('003', ' Miguel de Cervantes Saavedra', '1424', '1605', 'Don Quijote de la Mancha');
		"""
	]
for sentencia in libros:
	cursor.execute(sentencia);
db.commit() #Guardamos los cambios al terminar el ciclo
print("Libros insertados correctamente")

busqueda = input("Introduzca el nombre del libro que desea buscar: ")
if not busqueda:
    print("Búsqueda inválida")
    exit()

sentencia = "SELECT * FROM Libro WHERE NOMBRELIBRO LIKE ?;"

cursor.execute(sentencia, ["%{}%".format(busqueda)])

libros = cursor.fetchall()
print("+{:-<6}+{:-<50}+{:-<20}+{:-<15}+{:-<50}".format("", "", "", "", ""))
print("|{:^6}|{:^50}|{:^20}|{:^15}|{:^50}|".format("LSBN", "Autor", "Cantidad de Paginas", "Publicacion", "Nombre del Libro"))
print("+{:-<6}+{:-<50}+{:-<20}+{:-<15}+{:-<50}+".format("", "", "", "", ""))

for LSBN, AUTOR, CANTIDADP, PUBLICACION, NOMBRELIBRO in libros:
    print("|{:^6}|{:^50}|{:^20}|{:^15}|{:^50}|".format(LSBN, AUTOR, CANTIDADP, PUBLICACION, NOMBRELIBRO))

print("+{:-<6}+{:-<50}+{:-<20}+{:-<15}+{:-<50}+".format("", "", "", "", ""))