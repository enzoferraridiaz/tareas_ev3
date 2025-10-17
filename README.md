 1. Stateless (sin sesiones para esta práctica)

Significado:
Una API stateless (sin estado) no guarda información de sesión entre peticiones.
Cada request se procesa de forma independiente: el servidor no recuerda al cliente entre llamadas.

Cómo se aplica en tu API:

Django REST Framework (DRF) está configurado para no usar sesiones si no lo especificas.

Como no tienes autenticación o tokens, cada petición se maneja sola.

Ejemplo: cada curl o petición Postman funciona sin iniciar sesión.

Puedes escribir en tu README:

La API es stateless: no mantiene sesiones entre peticiones.
Cada request incluye toda la información necesaria (sin cookies ni autenticación persistente).

 2. JSON (Content-Type: application/json)

Significado:
La API usa JSON para enviar y recibir datos.

Cómo se aplica:

Los serializers de DRF convierten objetos Python a JSON automáticamente.

El cliente (Postman o curl) debe enviar el header:

Content-Type: application/json


Y el cuerpo en formato JSON:

{"title": "Aprender DRF", "done": false}


Puedes escribir en tu README:

El intercambio de datos entre cliente y servidor se realiza en formato JSON (Content-Type: application/json), garantizando compatibilidad con aplicaciones web y móviles.

 3. Versionado en la ruta: /api/v1/...

Significado:
El versionado permite tener distintas versiones de la API sin romper compatibilidad cuando cambie.

Cómo se aplica:

En tu urls.py, el prefijo /api/v1/ se usa para agrupar endpoints.

path('api/v1/', include(router.urls))


Si en el futuro hay una nueva versión, podrías crear /api/v2/.

Puedes escribir en tu README:

La API utiliza versionado en la ruta (/api/v1/) para permitir la evolución del servicio sin afectar integraciones existentes.

 4. Idempotencia

Significado:
Una operación es idempotente si ejecutarla varias veces produce el mismo resultado.

Aplicado a HTTP:

Verbo	Idempotente	Descripción
GET	✅ Sí	Leer datos no cambia el estado.
POST	❌ No	Cada ejecución crea un nuevo recurso.
PUT	✅ Sí	Reemplaza el recurso, deja mismo estado si se repite.
PATCH	✅ Sí	Actualiza parcialmente, deja mismo estado si se repite.
DELETE	✅ Sí	Elimina el recurso (si se repite, sigue sin existir).

Puedes escribir en tu README:

La API cumple con la idempotencia de los métodos HTTP:

GET nunca modifica el estado.

PATCH y PUT son idempotentes: repetirlos no cambia el resultado final.

POST no es idempotente (crea nuevos recursos).

 5. Diagrama de arquitectura (para el README)

Puedes incluir este diagrama ASCII directamente:

## Diagrama de Arquitectura

[ Cliente (curl / SPA) ]
           |
           | HTTP / JSON
           |
[ API /api/v1 (DRF ViewSets / URLs) ]
           |
[ Lógica / Serializers (Validación) ]
           |
[ Modelo Django (ORM) ]
           |
[ DB SQLite (Local) ]


Explicación breve:

El cliente (como curl o Postman) hace peticiones HTTP.

La API (ViewSets y URLs) recibe la solicitud.

Los serializers validan los datos y los transforman.

El modelo Django usa el ORM para interactuar con la base de datos SQLite.
