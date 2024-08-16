import sqlite3 as sql

def createDB():
    conn = sql.connect ('videojuego.db')
    conn.commit()
    conn.close()

def createTable ():
    conn = sql.connect ('videojuego.db')
    cursor = conn.cursor ()
    cursor.execute(
        """CREATE TABLE usuarios (
            name text,
            wins integer,
            partidas integer
        )"""
    )
    conn.commit()
    conn.close()

def newuser (name, wins, partidas):
    conn = sql.connect ('videojuego.db')
    cursor = conn.cursor ()
    instruccion = f"INSERT INTO usuarios VALUES ('{name}', {wins}, {partidas})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def printusers ():
    conn = sql.connect ('videojuego.db')
    cursor = conn.cursor ()
    instruccion = f"SELECT * FROM usuarios"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print (datos)

def newusers (usersList):
    conn = sql.connect ('videojuego.db')
    cursor = conn.cursor ()
    instruccion = f"INSERT INTO usuarios VALUES (?, ?, ?)"
    cursor.executemany(instruccion, usersList)
    conn.commit()
    conn.close()

def readOrdered (field):
    conn = sql.connect ('videojuego.db')
    cursor = conn.cursor ()
    instruccion = f"SELECT * FROM usuarios ORDER BY {field}" #DESC si se quiere hacer mayor a menor
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conn.commit()
    conn.close()
    print (datos)
    
def search(nombre):
    conn = sql.connect ('videojuego.db')
    cursor = conn.cursor ()
    instruccion = f"SELECT name FROM usuarios WHERE name like '{nombre}'" #también se puede usa > y < para numeros y en el caso de cadenas al final se puede poner % y buscara todo lo que EMPIEZE con lo que escribiste
    cursor.execute(instruccion)                              
    datossearch = cursor.fetchall
    conn.commit()
    conn.close()
    return (datossearch)

def extraer():
    pass



def updatewins (winner):
    conn = sql.connect ('videojuego.db')
    cursor = conn.cursor ()
    instruccion = f"UPDATE usuarios SET wins = wins + 1 WHERE name like '{winner}'" 
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def deletebyname (trash):
    conn = sql.connect ('videojuego.db')
    cursor = conn.cursor ()
    instruccion = f"DELETE FROM usuarios WHERE name = {trash}" 
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def join ():
    name1what = input ('¿Cual es el nombre del usuario?')
    while True:
        names1 = search(name1what)
        if names1 != []:
            nombre1 = name1what
            break
        elif names1 == []:
            print ('Ese usuario no está registrado')

def new_account ():
    name1what = input ('¿Cual es el nombre del nuevo usuario?')
    buscador = search(name1what)
    buscador = []
    print(buscador)
    while True:
        if buscador  == []:
            nombre1 = name1what
            newuser(name1what, 0, 0)
            print ('Registrado correctamente')
            break
        elif buscador != []:
            print ('Ese nombre ya está en uso')
            name1what = input('Escribe otro nombre:')

if __name__ == "__main__":
    #createDB()
    #createTable ()
    #newuser ('Dani', 0, 0)
    #printusers ()
    #users = [
    #    ("Giovanni", 0, 0),
    #    ("Aniely", 0, 0),
    #    ("Rayco", 0, 0)
    #    ...
    #]
    #newusers (users)
    #readOrdered ("name/partidas/wins") 
    #name1what = input('\n')
    search('Dani')
    #uno = 'Giovanni'
    #updatewins (uno)
    #delete ()
    #new_account()