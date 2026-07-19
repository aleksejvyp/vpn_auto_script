import time
import ctypes
import json
import keyboard
import subprocess
import os

# Подключаем функции Windows API
user32 = ctypes.windll.user32

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    "app_name": "uBoost",
    "app_path": "C:\\Path\\To\\my_vpn.exe",
    "hotkey_click": "ctrl+alt",
    "hotkey_exit": "alt+m"
}

def load_config():
    # Если файла настроек нет — создаем его с дефолтными данными
    try:
        with open(CONFIG_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
        
    except:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_CONFIG, f, indent=4, ensure_ascii=False)
        ctypes.windll.user32.MessageBoxW(
            0, 
            "Файл настроек config.json создан рядом с программой. Отредактируйте его и запустите утилиту снова.", 
            "Первый запуск", 
            0x40 # Иконка информации
            )
        
        os._exit(0) # Закрываем скрипт
        
    # Если файл есть — просто читаем его
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_window_rect(hwnd):
    user32.ShowWindow(hwnd, 1)
    user32.SetForegroundWindow(hwnd)
    time.sleep(1)
    """Получает координаты углов окна"""
    rect = ctypes.wintypes.RECT()
    if user32.GetWindowRect(hwnd, ctypes.byref(rect)):
        return rect.left, rect.top, rect.right, rect.bottom
    return None

def click(x, y):                     
    """Перемещает мышь и делает клик"""
    user32.SetCursorPos(x, y)
    user32.mouse_event(2, 0, 0, 0, 0) # Левая кнопка вниз (DOWN)
    time.sleep(0.05)
    user32.mouse_event(4, 0, 0, 0, 0) # Левая кнопка вверх (UP)

def start_uboost(app_path):
    try:
        subprocess.Popen(app_path)
        time.sleep(2)   # Ждем, пока окно появится
    except:
        os._exit(0) # Если не удалось запустить приложение, завершаем работу


def find_and_click_windows_way():
    config = load_config()
    print("Ищу окно в системе...")
    
    # Ищем дескриптор (ID) окна по его точному заголовку
    # Важно: название должно совпадать идеально
    hwnd = user32.FindWindowW(None, config["app_name"])

    
    if not hwnd:
        start_uboost(config["app_path"])
        time.sleep(5)
        hwnd = user32.FindWindowW(None, config["app_name"])

        
        
    if hwnd:

        print(f"Окно найдено! ID: {hwnd}")
        time.sleep(1)
        # Получаем координаты окна на экране
        coords = get_window_rect(hwnd)
        if coords:
            left, top, right, bottom = coords
            width = right - left
            height = bottom - top
            print(f"Позиция окна: Лево={left}, Топ={top}, Ширина={width}, Высота={height}")
            
            # Вычисляем центр окна (обычно кнопка "Старт/Подключить" по центру)
            center_x = left + (width // 2)
            center_y = top + (height // 2)
            
            # Если кнопка смещена, можно скорректировать, например: center_y = top + 150
            print(f"Кликаю в центр окна: X={center_x}, Y={center_y}")
            click(center_x, center_y)
            #click(right-55,top+40) #Сокрытие окна(невозможно подсчитать для всех, поэтому подключают те, кто сам может настроить эту команду)
            return True

if __name__ == "__main__":
    HOTKEY = 'ctrl+alt'
    keyboard.add_hotkey(HOTKEY, find_and_click_windows_way)
    print(f"Караулю нажатие [{HOTKEY}]...")
    print(f"Чтобы выйти нажмите alt + m")
    keyboard.wait("alt+m")