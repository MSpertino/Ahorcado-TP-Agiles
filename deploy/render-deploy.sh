#!/usr/bin/env bash
# Despliega un commit en Render y espera a que esté en producción. Lo ejecuta el CI.
#   RENDER_DEPLOY_HOOK=... RENDER_URL=... bash deploy/render-deploy.sh <commit-sha>
# Para saber cuándo terminó, consulta /version, que devuelve el commit que está corriendo.
set -euo pipefail

SHA="${1:?Falta el commit a desplegar}"
: "${RENDER_DEPLOY_HOOK:?Falta el secret RENDER_DEPLOY_HOOK}"
: "${RENDER_URL:?Falta la variable RENDER_URL}"

curl -fsS -o /dev/null -X POST "${RENDER_DEPLOY_HOOK}&ref=${SHA}"
echo "Deploy del commit $SHA solicitado a Render"

for _ in $(seq 1 60); do
    ACTUAL=$(curl -fsS --max-time 60 "${RENDER_URL}/version" || true)
    echo "En producción: ${ACTUAL:-(sin respuesta)}"
    if [ "$ACTUAL" = "$SHA" ]; then
        echo "Deploy OK"
        exit 0
    fi
    sleep 15
done
echo "Timeout: producción no llegó al commit $SHA" >&2
exit 1
