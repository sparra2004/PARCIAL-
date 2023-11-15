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

## ¿COMO CLONAR UNA RAMA EN GIT?

Cuando se trabaja en un proyecto, es probable que tenga características diferentes. Y múltiples colaboradores estarán trabajando en este proyecto y sus características.
Las branches permiten crear un "playground" con los mismos archivos en la master branch. Puedes usar este branch para construir características independientes, probar nuevas características, hacer cambios de últimas hora, crear correcciones, escribir documentos o probar ideas sin romper o afectar el código de producción. Cuando termines, fusiona el branch al master branch de producción.

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

