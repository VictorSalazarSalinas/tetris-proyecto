Configurar un Entorno Virtual 

En la carpeta del proyecto, haz clic derecho y selecciona Abrir en terminal, o también puedes hacer lo siguiente:

* Abre PowerShell como administrador desde el menú Inicio

* Navega a la carpeta de tu proyecto con el siguiente comando, reemplazando \[ruta\_de\_tu\_proyecto] por la ubicación real:
  cd \[ruta\_de\_tu\_proyecto]

* Una vez dentro de la carpeta del proyecto, crea el entorno virtual con:
  python -m venv venv

Activar el Entorno Virtual

Usa este comando para activarlo:
venv\Scripts\activate

Si tienes problemas al activarlo, ejecuta este comando para permitir scripts temporalmente:
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned

Luego vuelve a ejecutar el comando para activar el entorno:
venv\Scripts\activate

Instalar Dependencias Manualmente

Con el entorno virtual activado, instala pygame manualmente usando el siguiente comando:
pip install pygame

Esto instalará la versión más reciente de pygame disponible.



Ejecutar la Aplicación

Una vez que pygame esté instalado, ejecuta el programa con:
python main.py
