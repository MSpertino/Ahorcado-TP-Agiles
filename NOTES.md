# NOTES — Trazabilidad Historia → Criterio → AT → UT

Story Map: https://miro.com/app/board/uXjVHwePskk=/?share_link_id=83546637908

Mecanismo elegido: una `Característica` por historia con etiqueta `@HU-xx`, etiqueta `@CA-x` por escenario,
prefijo `HU-xx` en los commits y esta matriz para el tramo AT → UT.

Correr los AT de una historia: `pytest -m HU-03 features/` · un criterio: `pytest -m "HU-03 and CA-2" features/`

## Matriz

| Historia                  | Criterio                                             | Escenario (AT)                                                                               | Unit Tests (Ahorcado) | Estado                                |
| ------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------- | ------------------------------------- |
| HU-02 Iniciar partida     | CA-1 palabra oculta con guiones                      | `iniciar_partida.feature` — El jugador inicia una partida con una palabra / … más larga |                       | AT verde                              |
| HU-03 Ingresar letra      | CA-1 ingresa un solo carácter                       | `ingresar_letra.feature` — El jugador ingresa un solo carácter válido                   |                       | AT verde, a reescribir (ver feedback) |
| HU-03 Ingresar letra      | CA-2 / CA-3 rechaza más de un carácter con mensaje | `ingresar_letra.feature` — El jugador intenta ingresar más de un carácter               | `test_arriesgar_mas_de_una_letra_se_rechaza` | AT verde                              |
| HU-04 Validar solo letras | CA-1 rechaza números, símbolos y espacios          | `validar_entrada.feature` — El jugador ingresa un carácter que no es letra (3, #) / … un espacio | `test_arriesgar_algo_que_no_es_letra_se_rechaza[numero, simbolo, espacio]`, `test_arriesgar_una_letra_no_se_rechaza` | AT rojo                               |
| HU-04 Validar solo letras | CA-2 no descuenta intento                            |                                                                                              |                       |                                       |
| HU-04 Validar solo letras | CA-3 mensaje de error visible                        | (mismos escenarios que CA-1: verifican el mensaje exacto "Solo se permiten letras")          |                       | AT rojo                               |

## Decisiones

- **La UI habla con Ahorcado vía form → Flask.** El dominio es Python (pytest). El input vive en un `<form>`;
  la ruta de Flask solo lee la request, le pregunta a `Ahorcado` y renderiza. Sin lógica de juego en la ruta ni en JS.
- **HU-02 no verifica vidas.** Ningún criterio de HU-02 habla de vidas; el paso se sacó del `.feature` y el span del HTML.
  Vuelve con la historia de vidas.
-
