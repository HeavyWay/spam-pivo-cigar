import time # модуль часу
import pyautogui # модуль управлінням клавіатурою та мишкою

time.sleep(5) # час перед запуском скрипта

counts = 3 # кількість повторів

for q in range(counts): # цикл
    time.sleep(0)
    with open('text.txt', 'r', encoding='utf-8') as f: # відчитує пиво та дзигар з текстового файлу
        for line in f:
            line = line.strip()  # видалення пробілів
            pyautogui.write(line)  # ввод тексту
            pyautogui.press('enter') # натискання ентер
            time.sleep(0)








