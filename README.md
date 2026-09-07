# TP Integrador - Juego del Ahorcado

**Cátedra:** Metodologías Ágiles — UTN FRRO
**Grupo:** 12
**Integrantes:** Esteban Karlen Aguirre; Gabriel Perlin; Tomas Sanchez Machado; Mateo Spertino

## Descripción del producto

Desarrollo de una versión web del **Juego del Ahorcado**, construida aplicando prácticas ágiles de ingeniería que permitan evolucionar, probar e integrar el producto de manera continua.

El objetivo no es solo hacer que el juego funcione, sino experimentar cómo las prácticas de producto e ingeniería trabajan juntas: aprendizaje, feedback rápido, automatización, calidad y entrega continua.

### Visión del producto

- **Simple:** experiencia sencilla, fácil de comprender y utilizar.
- **Claro:** cada acción produce feedback visible y comprensible para el usuario.
- **Evolutivo:** la solución comienza con un alcance reducido y permite incorporar nuevos comportamientos apoyándose en buenas prácticas de diseño e ingeniería.

### Usuario objetivo

**Jugador casual:** persona que busca entretenimiento rápido y una interacción sencilla, sin necesidad de comprometerse con partidas largas. Puede tener distinta experiencia digital, por lo que el juego debe poder ser comprendido por personas con distinto nivel de manejo de tecnología.

### Objetivo

Crear una experiencia de juego simple, dinámica y confiable, con partidas cortas, reglas comprensibles y feedback inmediato. El producto debe permitir aprender del uso y evolucionar sin perder calidad.

## Story Mapping y MVP

El Story Map completo (User Journey, Features/Stories y cortes de Release) se encuentra documentado en:

https://miro.com/app/board/uXjVHwePskk=/?share_link_id=83546637908

### Alcance del MVP (Release 1)

El MVP se centra exclusivamente en poder **jugar una partida completa de punta a punta**, sin login, sin configuración y sin ranking:

- Entrar directo al juego sin necesidad de registrarme.
- Ver la palabra oculta representada con guiones.
- Ingresar una letra por vez.
- Validar que solo se ingresen letras.
- Descontar un intento ante letra incorrecta.
- Ver cantidad de intentos restantes.
- Validar letra repetida.
- Ver mensaje de resultado (Ganó/Perdió).
- Revelar la palabra completa si se pierde.
- Botón para jugar de nuevo.

Quedan fuera del MVP (Release 2 y 3): configuración de dificultad/idioma/categoría, pistas, dibujo progresivo del ahorcado, modo multijugador, sistema de puntaje, ranking, historial y login/registro real.

## Consignas técnicas del TP

- [ ] **Story Mapping del producto** — primera versión + corte de MVP.
- [ ] **Unit Tests con TDD** — lógica central desarrollada test-first.
- [ ] **Single Repository** — todo el código en este repositorio.
- [ ] **CI: compilación automática**
- [ ] **CI: ejecución de Unit Tests**
- [ ] **CI: Code Coverage**
- [ ] **UI Web + Acceptance Tests** — al menos 4 escenarios automatizados (Cucumber/Gherkin + Selenium/Playwright o equivalente).
- [ ] **CI/CD: deploy a producción** — repetible y trazable.
- [ ] **CI: ejecución de Acceptance Tests** contra el ambiente desplegado.
- [ ] **Análisis Estático de Código** (SonarQube/SonarCloud o equivalente).

## Stack tecnológico

- **Lenguaje:** Python
- **Testing (Unit Tests):** pytest

## Licencia

Trabajo práctico académico — UTN FRRO.
