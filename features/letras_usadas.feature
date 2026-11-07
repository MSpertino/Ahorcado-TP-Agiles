# language: es
@HU-15
Característica: Letras usadas
  Como jugador
  quiero ver las letras que ya probé
  para no repetirlas y planear mi próxima jugada

  @CA-1
  Escenario: Se muestran las letras ya usadas
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "E"
    Y el jugador ingresa la letra "A"
    Entonces se ven las letras usadas "A E"
  
  @CA-2
  Escenario: Las letras usadas distinguen aciertos y fallos
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "E"
    Y el jugador ingresa la letra "A"
    Entonces se ven las letras acertadas "A"
    Y se ven las letras falladas "E"