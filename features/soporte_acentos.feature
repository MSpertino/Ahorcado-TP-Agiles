# language: es
@HU-11
Característica: Soporte de acentos y caracteres especiales
  Como jugador
  quiero que el sistema reconozca letras con tilde como equivalentes
  para no perder intentos injustamente por diferencias de acentuación

  @CA-1
  Escenario: El jugador ingresa una vocal con tilde y se revela sin perder intentos
    Dado una partida con la palabra "ARBOL"
    Cuando el jugador ingresa la letra "á"
    Entonces se ve la palabra "A _ _ _ _"
    Y se ven 6 intentos restantes