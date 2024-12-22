#!/bin/bash

# Descargar Postman
wget https://dl.pstmn.io/download/latest/linux_arm64?deviceid=e05842d6-890d-452b-a817-ac70a4271ebf -O postman.tar.gz

# Descomprimir el archivo
tar -xzf postman.tar.gz

# Mover Postman a /opt
sudo mv postman /opt/postman

# Crear un enlace simbólico en /usr/bin
sudo ln -s /opt/postman/postman /usr/bin/postman

# Crear el archivo desktop
USER=$(whoami)
DESKTOP_FILE="/home/$USER/Desktop/postman.desktop"

echo "[Desktop Entry]
Name=Postman
Exec=/opt/postman/postman
Icon=/opt/postman/app/icons/icon_128x128.png
Type=Application
Terminal=false
Categories=Development;
Comment=
Path=
StartupNotify=false" | sudo tee "$DESKTOP_FILE" > /dev/null

# Dar permisos al archivo .desktop
chmod +x "$DESKTOP_FILE"

echo "Postman se ha instalado y creado el acceso directo en el escritorio."
