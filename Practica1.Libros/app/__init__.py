import sqlite3

db = sqlite3.connect('C:/Users/lapri/PycharmProjects/Practica1.Libros/app/data/prueba.db')

cursor = db.cursor()
tablas = [
		"""
			CREATE TABLE IF NOT EXISTS Libro(
				LSBN INTEGER PRIMARY KEY,
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

print("1-Inserta libro.")
print("2-Buscar libro.")
print("3-Ver listado de libros")
print("4-Borrar libro.")

a = int(input("Escoja la opcion que desea:"))

if a==1: #insertar
	AUTOR = input("\nAUTOR: ")
	CANTIDADP = input("\nCANTIDADP: ")
	PUBLICACION = input("\nPUBLICACION: ")
	NOMBRELIBRO = input("\nNOMBRELIBRO : ")
	tabla = "INSERT INTO Libro(AUTOR, CANTIDADP, PUBLICACION, NOMBRELIBRO) VALUES (?,?,?,?)"
	cursor.execute(tabla, [AUTOR, CANTIDADP, PUBLICACION, NOMBRELIBRO])
	db.commit()
	print("Guardado correctamente")

elif a==2: #Buscar
	busqueda = input("Introduzca el nombre del libro que desea buscar: ")
	if not busqueda:
		print("Búsqueda inválida")
		exit()

	sentencia = "SELECT * FROM Libro WHERE NOMBRELIBRO LIKE ?;"

	cursor.execute(sentencia, ["%{}%".format(busqueda)])

	libros = cursor.fetchall()
	print("+{:-<6}+{:-<50}+{:-<20}+{:-<15}+{:-<50}".format("", "", "", "", ""))
	print("|{:^6}|{:^50}|{:^20}|{:^15}|{:^50}|".format("LSBN", "Autor", "Cantidad de Paginas", "Publicacion",
													   "Nombre del Libro"))
	print("+{:-<6}+{:-<50}+{:-<20}+{:-<15}+{:-<50}+".format("", "", "", "", ""))

	for LSBN, AUTOR, CANTIDADP, PUBLICACION, NOMBRELIBRO in libros:
		print("|{:^6}|{:^50}|{:^20}|{:^15}|{:^50}|".format(LSBN, AUTOR, CANTIDADP, PUBLICACION, NOMBRELIBRO))

	print("+{:-<6}+{:-<50}+{:-<20}+{:-<15}+{:-<50}+".format("", "", "", "", ""))

elif a==3: #Ver todos
	tabla = "SELECT * FROM Libro;"
	cursor.execute(tabla)
	Libro = cursor.fetchall()
	print("\n", Libro)

elif a==4: #Eliminar

	cursor.execute('''SELECT LSBN, AUTOR, CANTIDADP, PUBLICACION, NOMBRELIBRO FROM Libro''')
	resultado = cursor.fetchall()
	for fila in resultado:
		print("{0} : {1}".format(fila[0], fila[1]))

	LSBN = input("LSBN del libro a eliminar: ")
	for fila in resultado:
		if int(LSBN) == int(fila[0]):
			cursor.execute('''DELETE FROM Libro WHERE LSBN = ?''',
						   (LSBN,))
	db.commit()




