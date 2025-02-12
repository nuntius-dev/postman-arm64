# Instalación de Postman en Linux (Genérico)

Este script instala Postman en sistemas Linux, creando un acceso directo en el escritorio del usuario.

## Requisitos
- Tener privilegios de `root` o `sudo`.
- Conexión a Internet.

## Instalación
Ejecute el siguiente comando:

```bash
apt install wget -y ; wget https://raw.githubusercontent.com/nuntius-dev/postman-arm64/refs/heads/main/instalar_postman.sh  ; chmod +x instalar_postman.sh ; ./instalar_postman.sh
```

## Lo que hace el script
1. Descarga la última versión de Postman.
2. Extrae los archivos en `/opt/postman`.
3. Crea un enlace simbólico en `/usr/bin/postman`.
4. Genera un acceso directo en el escritorio del usuario.

## Uso
Para abrir Postman, ejecute:
```bash
postman
```
O haga doble clic en el acceso directo en el escritorio.

---

# Instalación de Postman en `nuntiusdev/nuntius-arm64`

Este script instala Postman en un entorno basado en la imagen `nuntiusdev/nuntius-arm64`.

## Requisitos
- Haber desplegado un contenedor con la imagen `nuntiusdev/nuntius-arm64`.
- Acceder como `root` o usar `sudo`.

## Instalación
Ejecute:

```bash
apt install wget -y ; wget https://raw.githubusercontent.com/nuntius-dev/postman-arm64/refs/heads/main/postman-install-os-nuntius-arm.sh ; chmod +x postman-install-os-nuntius-arm.sh ; ./postman-install-os-nuntius-arm.sh
```

## Especificaciones para `nuntiusdev/nuntius-arm64`
1. El script verifica que el sistema esté basado en `nuntiusdev/nuntius-arm64`.
2. Instala Postman en `/opt/postman` dentro del contenedor.
3. Crea un enlace simbólico en `/usr/bin/postman`.
4. Asegura permisos correctos en el acceso directo del usuario.

## Uso
Para abrir Postman en el contenedor:
```bash
postman
```
Si el contenedor se ejecuta con entorno gráfico, se puede acceder desde el escritorio.


