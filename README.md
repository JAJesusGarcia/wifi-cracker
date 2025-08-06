# Descrifrador WiFi Educativo en Python

Este proyecto es un descifrador de contraseñas WiFi desarrollado en Python con fines educativos y demostrativos. Su objetivo es comprender los mecanismos de seguridad WPA/WPA2 y las vulnerabilidades que pueden existir. **Es crucial que esta herramienta sea utilizada únicamente para pruebas en redes propias o con permiso explícito, nunca para actividades ilegales.**

## ⚠️ Consideraciones Éticas y Legales (IMPORTANTE)

Antes de comenzar:

- Solo puedes realizar pruebas en redes que te pertenezcan o donde tengas permiso explícito del propietario.
- El uso no autorizado de estas técnicas está penalizado por ley en la mayoría de los países.
- Esta herramienta debe ser usada exclusivamente con fines educativos, de pruebas de penetración autorizadas o en entornos controlados de laboratorio.

## 🚀 Objetivos del Proyecto

- Desarrollar un programa en Python que pueda escanear redes WiFi, capturar handshakes (simulado), y realizar un ataque de diccionario para descifrar contraseñas WPA/WPA2.
- Comprender los principios de seguridad de redes WiFi y las técnicas de ataque.
- Crear un entorno de desarrollo reproducible utilizando Docker.

## 🛠️ Herramientas Usadas

- **Python 3:** Lenguaje de programación principal.
- **Visual Studio Code (VSC):** Editor de código recomendado.
- **Docker:** Plataforma para crear y ejecutar contenedores, asegurando un entorno de desarrollo consistente.
- **Librerías de Python:**
  - `subprocess`: Para ejecutar comandos del sistema operativo.
  - `plistlib`: Para parsear la salida XML del comando `airport` en macOS.
  - `hashlib`: Para implementar funciones de hashing y derivación de claves (PBKDF2).
- **Kali Linux:** Distribución de Linux especializada en seguridad informática (usada dentro del contenedor Docker).
- **aircrack-ng:** Suite de herramientas para auditoría de seguridad WiFi (incluida en Kali Linux).

## ⚙️ Requisitos

- **macOS:** Este proyecto está diseñado para ejecutarse en macOS.
- **Python 3:** Asegúrate de tener Python 3 instalado. Puedes instalarlo con Homebrew: `brew install python3`
- **Visual Studio Code (VSC):** Editor de código recomendado.
- **Docker Desktop:** Necesario para crear y ejecutar contenedores Docker. Descarga e instala desde [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).

## 📦 Instalación

1.  **Clona el repositorio:**

    ```bash
    git clone [URL del repositorio]
    cd [nombre del repositorio]
    ```

    Reemplaza `[URL del repositorio]` con la URL de tu repositorio de GitHub y `[nombre del repositorio]` con el nombre de la carpeta creada al clonar el repositorio.

2.  **Descarga o genera una wordlist:**

    Como el archivo `rockyou.txt` (u otra wordlist grande) suele ser demasiado grande para incluir en un repositorio de GitHub, debes descargarlo por separado o usar una wordlist más pequeña para pruebas.

    - **Descargar `rockyou.txt` (si tienes permiso para usarlo):**
      (No podemos proporcionar enlaces directos a wordlists por razones de seguridad, pero puedes buscar en internet fuentes confiables)

    - **Crear una wordlist de prueba:** Si no tienes acceso a una wordlist grande, puedes crear un archivo de texto simple con algunas contraseñas de prueba (una contraseña por línea).

3.  **Coloca la wordlist en la carpeta `wordlist`:**

    Mueve o copia el archivo de la wordlist (por ejemplo, `rockyou.txt` o `mi_wordlist.txt`) a la carpeta `wordlist` en la raíz del proyecto.

## 🛠️ Configuración

1.  **Configura el ESSID en `dictionary_attack.py`:**

    Abre el archivo `src/dictionary_attack.py` con VSC u otro editor de código.

    Busca la sección:

    ```python
    if __name__ == "__main__":
        wordlist_path = "wordlist/rockyou.txt"  # Reemplaza con la ruta a tu wordlist
        ssid = "NombreDeMiRed"  # Reemplaza con el ESSID de la red
        handshake_mic = "mic_del_handshake"  # Simulamos el MIC del handshake
        run_dictionary_attack(wordlist_path, ssid, handshake_mic)
    ```

    Reemplaza `"NombreDeMiRed"` con el ESSID (nombre) de la red WiFi que estás probando. **Asegúrate de tener permiso para probar esta red.**

2.  **Verifica la ruta a la wordlist:**

    Asegúrate de que la variable `wordlist_path` refleje la ruta correcta a tu wordlist dentro del contenedor Docker (por defecto, debería ser `wordlist/rockyou.txt` si colocaste el archivo en la carpeta `wordlist` en la raíz del proyecto).

## 🚀 Uso

1.  **Construye la imagen Docker:**

    Navega hasta la raíz del proyecto en tu Terminal y ejecuta:

    ```bash
    docker build -t wifi-cracker -f docker/Dockerfile .
    ```

    Este comando construirá la imagen Docker a partir del `Dockerfile`.

2.  **Ejecuta el contenedor Docker:**

    ```bash
    docker run -it wifi-cracker bash
    ```

    Este comando creará y ejecutará un contenedor interactivo de Kali Linux a partir de la imagen `wifi-cracker`.

3.  **Ejecuta el script de ataque de diccionario:**

    Dentro del contenedor, ejecuta el script `dictionary_attack.py` con el siguiente comando:

    ```bash
    python3 /app/src/dictionary_attack.py
    ```

    Este comando leerá la wordlist y comenzará a probar las contraseñas contra el ESSID especificado, calculando el PMK para cada contraseña.

    **Nota:** Actualmente, el script solo calcula el PMK. Los siguientes pasos (cálculo del PTK y comparación del MIC) aún no están implementados.

## 🧪 Próximos Pasos

- **Implementar la lógica para capturar handshakes:**
  - (Este paso requiere un adaptador WiFi USB compatible con el modo monitor y no es posible en macOS sin hardware adicional).
  - Investigar cómo usar `airodump-ng` y otras herramientas dentro del contenedor Docker para capturar handshakes.
- **Implementar el análisis del handshake:**
  - Investigar cómo parsear archivos `.cap` o `.pcap` capturados para extraer la información necesaria (BSSID, ESSID, nonces, MIC).
  - Considerar el uso de librerías como Scapy o PyShark para el parsing de paquetes.
- **Implementar el cálculo del PTK y la comparación del MIC:**
  - Añadir la lógica para calcular el PTK a partir del PMK y otra información del handshake.
  - Implementar la comparación del MIC calculado con el MIC del handshake capturado para verificar la validez de la contraseña.
- **Añadir soporte para diferentes tipos de seguridad:**
  - Expandir el script para manejar otros tipos de seguridad WiFi, como WEP.
- **Optimizar el rendimiento:**
  - Investigar técnicas para paralelizar el ataque de diccionario (por ejemplo, usando `multiprocessing` o `asyncio`).
  - Considerar la integración con `hashcat` para un descifrado acelerado por GPU.

## 🤝 Contribución

Las contribuciones son bienvenidas. Si encuentras errores, tienes ideas para mejoras o quieres añadir nuevas características, ¡no dudes en crear un "issue" o enviar una "pull request"!

## 📜 Licencia
