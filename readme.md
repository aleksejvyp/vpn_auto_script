# Auto VPN Script

Скрипт используется для получения возможности включать большинство VPN с помощью одного сочетания клавиш. Работает только для VPN с большой кнопкой посередине окна. Если вам не подходит, вы можете попробовать использовать открытый код моего скрипта; принцип поиска координат простой и не требует высоких знаний.

## Установка

1. **Распакуйте скрипт в отдельную папку**
2. Запустите `auto_vpn_script.exe`.
3. После первого запуска в папке появится файл `config.json`. В нем необходимо заполнить две строки:
   - Имя окна вашего приложения (очень важно, без него скрипт не будет работать).
   - Путь до exe файла используемого вами VPN клиента. Если путь есть, вы можете запускать приложение с помощью скрипта и сразу его включать.
4. В `config.json` можно прописать сочетание клавиш для запуска VPN (по умолчанию `ctrl + alt`) и сочетание для отключения (по умолчанию `alt + m`).
5. Можно закрыть `config.json` и пользоваться скриптом.

> **Важно:** Желательно запускать от имени администратора, так как VPN-клиенты часто требуют того же. А по правилам Windows, если у приложения меньше прав, оно не может взаимодействовать с приложением старше по правам.

## Запуск скрипта из исходного кода

```bash
# Клонируйте репозиторий
git clone https://github.com/aleksejvyp/vpn_auto_script.git
cd vpn_auto_script

# Установите зависимости
pip install -r requirements.txt

# Запустите скрипт
python auto_vpn_script.py
```

Sure, here is the improved English version of your README.md:

---

# Auto VPN Script

This script allows you to enable most VPNs with a single keyboard shortcut. It works only for VPN applications that have a large button in the center of the window. If this doesn't suit your needs, you can try using the open-source code from my script; the coordinate search is simple and does not require advanced knowledge.

## Installation

1. **Unpack the Script into a Separate Folder**
2. Run `auto_vpn_script.exe`.
3. After the first run, a file named `config.json` will appear in the folder. Fill in two lines:
   - Name of your application window (very important; without it, the script won't work).
   - Path to the executable file of your VPN client. If the path is available, you can start the application using the script and immediately enable it.
4. You can set a keyboard shortcut for enabling the VPN in `config.json` (default: `Ctrl + Alt`) and another one for disabling (default: `Alt + M`).
5. You can close `config.json` and use the script.

> **Important:** It is recommended to run the script as an administrator, as many VPN clients require elevated privileges. According to Windows rules, if a program has fewer permissions than another, it cannot interact with that older program.

## Running from Source

```bash
# Clone the repository
git clone https://github.com/aleksejvyp/vpn_auto_script.git
cd vpn_auto_script

# Install dependencies
pip install -r requirements.txt

# Run the script
python auto_vpn_script.py
```
