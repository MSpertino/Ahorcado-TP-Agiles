# NOTES — Trazabilidad Historia → Criterio → AT → UT

Story Map: https://miro.com/app/board/uXjVHwePskk=/?share_link_id=83546637908

Mecanismo elegido: una `Característica` por historia con etiqueta `@HU-xx`, etiqueta `@CA-x` por escenario,
prefijo `HU-xx` en los commits y esta matriz para el tramo AT → UT.

Correr los AT de una historia: `pytest -m HU-03 features/` · un criterio: `pytest -m "HU-03 and CA-2" features/`

## Matriz

| Historia | Criterio | Escenario (AT) | Unit Tests (Ahorcado) | Estado |
| --- | --- | --- | --- | --- |
| HU-02 Iniciar partida | CA-1 palabra oculta con guiones | `iniciar_partida.feature` — El jugador inicia una partida con una palabra / … más larga | | AT verde |
| HU-02 Iniciar partida | CA-2 sin palabra indicada, se usa una por defecto | `iniciar_partida.feature` — Sin palabra indicada se usa una por defecto | (No lleva UT, es ruta Flask) | AT verde |
| HU-03 Ingresar letra | CA-1 revelar letra acertada | `ingresar_letra.feature` — El jugador ingresa una letra y se revela en la palabra | `test_arriesgar_letra_acertada_revela_letra`, `test_arriesgar_letra_revela_multiples_ocurrencias`, `test_arriesgar_letra_no_presente_no_revela_nada` | AT verde, UT verde |
| HU-03 Ingresar letra | CA-2 / CA-3 rechaza más de un carácter con mensaje | `ingresar_letra.feature` — El jugador intenta ingresar más de un carácter | `test_arriesgar_mas_de_una_letra_se_rechaza` | AT verde, UT verde |
| HU-04 Validar solo letras | CA-1 rechaza números, símbolos y espacios | `validar_entrada.feature` — El jugador ingresa un carácter que no es letra (3, #) / … un espacio | `test_arriesgar_algo_que_no_es_letra_se_rechaza[numero, simbolo, espacio]`, `test_arriesgar_una_letra_no_se_rechaza` | AT verde, UT verde |
| HU-04 Validar solo letras | CA-2 no descuenta intento | | | |
| HU-04 Validar solo letras | CA-3 mensaje de error visible | (mismos escenarios que CA-1: verifican el mensaje exacto "Solo se permiten letras") | | AT verde, UT verde |
| HU-05 Descontar intento | CA-1 disminuye ante letra incorrecta | `fallar_letra.feature` — El jugador falla una letra | `test_fallar_letra_descuenta_intento` | AT verde, UT verde |
| HU-05 Descontar intento | CA-2 sin cambios ante letra correcta | | `test_acertar_letra_no_descuenta_intento` | UT verde |
| HU-06 Ver intentos | CA-1 al iniciar se ven 6 intentos | `ver_intentos.feature` — El jugador ve sus intentos restantes al iniciar la partida | `test_una_partida_nueva_tiene_6_intentos_restantes` | AT verde, UT verde |

## Decisiones

- **La UI habla con Ahorcado vía form → Flask.** El dominio es Python (pytest). El input vive en un `<form>`;
  la ruta de Flask solo lee la request, le pregunta a `Ahorcado` y renderiza. Sin lógica de juego en la ruta ni en JS.
- **HU-02 no verifica vidas.** Ningún criterio de HU-02 habla de vidas; el paso se sacó del `.feature` y el span del HTML.
  Vuelve con la historia de vidas.
- **HU-06 CA-1 no hizo falta refactor de producción.** El `goto` pasó del `Cuando` al `Dado` (commit `REFACTOR`) para que
  cualquier `Entonces` lea la página sin navegar; solo se movió código de los steps, no cambió ningún valor esperado.