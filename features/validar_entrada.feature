# language: es
@HU-04
Característica: Validar entrada
  Como jugador
  quiero que el sistema valide que solo ingreso letras
  para evitar errores que rompan la partida

  @CA-1
  @CA-2
  @CA-3
  Esquema del escenario: El jugador ingresa un carácter que no es letra
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra "<entrada>"
    Entonces se ve el mensaje de error "Solo se permiten letras"
    Y se ven 6 intentos restantes

    Ejemplos:
      | entrada |
      | 3       |
      | #       |

  @CA-1
  @CA-2
  @CA-3
  Escenario: El jugador ingresa un espacio
    Dado una partida con la palabra "GATO"
    Cuando el jugador ingresa la letra " "
    Entonces se ve el mensaje de error "Solo se permiten letras"
    Y se ven 6 intentos restantes