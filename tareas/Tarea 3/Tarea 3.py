class Playlist:
  def __init__(self,nombre):
    self.nombre = nombre
    self.canciones=[]

  def añadir_cancion(self,titulo):
    if len(self.canciones) >= 10:
      print("Alcanzante el limite maximo de canciones por playlist")
    else:
      if titulo in self.canciones:
        print("La canción ya se encuentra en la playlist")
      else:
        self.canciones.append(titulo)
        print(f"{titulo} añadida a {self.nombre}.")

  def eliminar_cancion(self,titulo):
    if titulo in self.canciones:
      self.canciones.remove(titulo)
      print(f"{titulo} ha sido eliminado de {self.nombre}")
    else:
      print(f"{titulo} no esta en {self.nombre}")

  def total_canciones(self):
    return len(self.canciones)

  def mostrar_playlist(self):
    print(f"========== Playlist: {self.nombre} ==========")
    if len(self.canciones) == 0:
      print("La Playlist esta vacia actualmente")
    else:
      i = 1
      for titulo in self.canciones:
        print(i,titulo)
        i += 1

  def limpiar_playlist(self):
    self.canciones.clear()
    print("La playlist esta vacia")

  def buscador(self,texto):
    resultados = []

    for cancion in self.canciones:
      if texto.lower() in cancion.lower(): #le modifique que busque el texto en minusculas para no tener problemas con las mayusculas de los titulos
        resultados.append(cancion)

    if resultados:
      print(f"Se encontraron las siguientes canciones con '{texto}' en la playlist {self.nombre}")
      for cancion in resultados:
        print(f"* {cancion}")
    else:
      print(f"No se encontraron canciones con '{texto}' en la playlist {self.nombre}")



mix_Pop = Playlist("Mi musica Pop")

mix_Pop.añadir_cancion("Beat it")
mix_Pop.añadir_cancion("Remember the Time")
mix_Pop.añadir_cancion("Bad")
mix_Pop.añadir_cancion("P.Y.T.(Pretty Young Thing)")
mix_Pop.añadir_cancion("Rock with You")
mix_Pop.añadir_cancion("Love Never Feel So Good") 
mix_Pop.añadir_cancion("Human Nature")
mix_Pop.añadir_cancion("Smooth Criminal")

mix_Pop.mostrar_playlist()

mix_Pop.buscador("th")