# language: es
@HU-06
Característica: Ver intentos restantes
  Como jugador
  quiero ver cuántos intentos me quedan
  para saber qué tan cerca estoy de perder

  @CA-1
  Escenario: El jugador ve sus intentos restantes al iniciar la partida
    Dado una partida con la palabra "GATO"
    Entonces se ven 7 intentos restantes
