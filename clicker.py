import keyboard
import mouse
import time

is_clicking = False
click_count = 0
max_clicks = 10000  # Максимальное количество кликов перед завершением

def set_clicker():
    global is_clicking
    is_clicking = not is_clicking
    state = "включен" if is_clicking else "выключен"
    print(f"Кликер {state}")

# Привязка горячих клавиш
keyboard.add_hotkey('Alt+Z', set_clicker)
print("Горячая клавиша Alt+Z для включения/выключения кликера установлена.")

def exit_program():
    print("Выход из программы")
    keyboard.unhook_all_hotkeys()
    exit(0)

keyboard.add_hotkey('Alt+X', exit_program)
print("Горячая клавиша Alt+X для выхода из программы установлена.")

try:
    print("Программа запущена. Ожидание действий...")
    while True:
        if is_clicking:
            click_count += 1
            print(f"Кликер активен, выполняется {click_count}-й двойной клик...")
            
            mouse.double_click(button='left')
            time.sleep(0.01)
            
            # Проверка, достигли ли мы максимального количества кликов
            if click_count >= max_clicks:
                print("Достигнуто максимальное количество кликов. Остановка.")
                is_clicking = False
                click_count = 0  # Сброс счетчика после достижения лимита
        else:
            # Добавим задержку, чтобы не нагружать процессор
            time.sleep(0.01)
except KeyboardInterrupt:
    print("Программа завершена пользователем.")
