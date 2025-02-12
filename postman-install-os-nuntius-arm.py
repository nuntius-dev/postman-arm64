#!/bin/bash

# Definir usuario objetivo
TARGET_USER="nuntius"
TARGET_HOME="/home/$TARGET_USER"

# Descargar Postman
wget "https://dl.pstmn.io/download/latest/linux_arm64" -O postman.tar.gz

# Crear el directorio en /opt si no existe
sudo mkdir -p /opt/postman

# Extraer directamente a /opt/postman
sudo tar -xzf postman.tar.gz -C /opt/postman --strip-components=1

# Crear un enlace simbólico en /usr/bin
sudo ln -sf /opt/postman/Postman /usr/bin/postman

# Crear el archivo .desktop en el escritorio del usuario objetivo
DESKTOP_FILE="$TARGET_HOME/Desktop/postman.desktop"

echo "[Desktop Entry]
Name=Postman
Exec=/opt/postman/Postman
Icon=/opt/postman/app/resources/app/assets/icon.png
Type=Application
Terminal=false
Categories=Development;
Comment=Postman API Platform
Path=
StartupNotify=false" | sudo tee "$DESKTOP_FILE" > /dev/null

# Asegurar permisos adecuados para el usuario objetivo
sudo chown $TARGET_USER:$TARGET_USER "$DESKTOP_FILE"
sudo chmod +x "$DESKTOP_FILE"

echo "Postman se ha instalado y el acceso directo se ha creado en el escritorio de $TARGET_USER."
