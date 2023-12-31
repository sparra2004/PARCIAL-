# PARCIAL DE HERRAMIENTAS
### Integrantes: Juan Manuel Ramirez y Santiago Parra 

## OPERACIONES:

**get_byte**: 

![image](https://github.com/sparra2004/PARCIAL-/assets/147517210/9e6b24eb-d7b3-445c-97ce-b4e3bf5221b7)


Esta funcion toma un caracter como entrada y devuelve su representacion en byte como una cadena de ocho bits.

**get_character**: 

![image](https://github.com/sparra2004/PARCIAL-/assets/147517210/620feee9-4eaa-478f-a6cc-7a8c58e6f67f)

Pide al usuario ingresar un carácter y muestra su representación en byte.

**get_word**:

![image](https://github.com/sparra2004/PARCIAL-/assets/147517210/f580b07e-4b6b-4c0b-a2ae-0166627b0f90)

Pide al usuario ingresar una palabra y muestra la representación en byte de cada carácter de la palabra, separados por espacios.

**main**:

![image](https://github.com/sparra2004/PARCIAL-/assets/147517210/4c470f7b-a103-4d1f-81de-381feb6471aa)

Es la función principal que ejecuta un bucle para mostrar un menú interactivo. Dependiendo de la opción seleccionada por el usuario, llama a las funciones correspondientes.


## LIBRERIA SYS

Este módulo provee acceso a algunas variables usadas o mantenidas por el intérprete y a funciones que interactúan fuertemente con el intérprete. 
Existen varios tipos de SYS como:

- sys.abiflags
- sys.addaudithook
- sys.argv
- sys.audit
- sys.exit
- sys.base_exec_prefix
- etc.

Existen muchos mas, pero cada uno cumple con diferente funcionamiento dependiendo de lo que requieras en el programa.

## Introduccion a Git Clon
Git te permite administrar y versionar tu(s) proyecto(s) en un "repositorio". Este repositorio se almacena en un servicio de alojamiento web para el control de versiones, como GitHub.

Luego puedes clonar este repositorio en tu máquina local y tener todos los archivos y branches (ramas) localmente (pronto explicaré más sobre branches).

![imagen](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-23-at-5.47.48-AM.png)

## Como clonar un Git Branches 
Mientras que puedes clonar los repositorios con el comando git clone, ten en cuenta que este clona la branch y el HEAD remoto. Normalmente es la master por defecto e incluye todas las demás ramas del repositorio.

Así que cuando clonas un repositorio, clonas master y todas las demás branches. Esto significa que tendrás que revisar otra rama tú mismo.

Digamos que tu tarea en un proyecto es trabajar en una característica para agregar autenticación sin contraseña a un tablero de usuario. Y esta característica está en la branch passwordless-auth.

Realmente no necesitas la master branch ya que tu "feature branch" se fusionará con master después. ¿Cómo clonas entonces la branch de passwordless-auth sin buscar todas las demás ramas con "un montón de archivos que no necesitas"?

He creado este repositorio de muestra para explicar esto. Este repositorio contiene un simple blog construido con Nextjs y tiene cuatro ramas ficticias:

master
dev
staging
passwordless-auth
En Nextjs, cualquier archivo dentro de la carpeta pages/api es mapeado a la ruta /api/* y será tratado como un endpoint de la API en lugar de un page. En nuestro repositorio, he creado diferentes APIs ficticias en este directorio para que cada branch sea diferente.

La master branch contiene el archivo pages/api/hello.js mientras que passwordless-auth contiene el archivo pages/api/auth.js. Cada archivo devuelve una respuesta de texto ficticio. Ve la respuesta del hello API de master aquí (¿Con un mensaje especial para ti?).

![imagen](https://www.freecodecamp.org/news/content/images/2020/06/Screenshot-2020-06-22-at-2.47.53-AM.png)

## Cómo Clonar una Branch Específica
Ahora vamos a clonar una branch específica de nuestro repositorio de demostración. Hay dos maneras de clonar una branch específica. Puedes hacer cualquiera de ellas:

Clonar el repositorio, obtener todas las branches, y hacer un checkout a una branch específica inmediatamente.
Clonar el repositorio y obtener sólo una branch.

![image](https://github.com/sparra2004/PARCIAL-/assets/147517210/fabfbb65-8b42-48b7-837f-319c645f53a8)

Con esto, se obtienen todas las branches del repositorio, se hace un checkout a la que se ha especificado, y la rama específica se convierte en la branch local configurada para git push y git pull. Pero aún así, obtuviste todos los archivos de cada branch.

![image](https://github.com/sparra2004/PARCIAL-/assets/147517210/9b8d271d-6d5b-45a5-b43a-559c98b99f4b)

Esto realiza la misma acción que la opción uno, excepto que la opción --single-branch fue introducida en la versión 1.7.10 y posteriores de Git. Te permite sólo recuperar archivos de la branch especificada sin recuperar otras ramas.


SI quieres navegar en GIT HUB, a continuacion te dejo el link:	[GIT HUB](https://github.com/)




