import tkinter as tk
from tkinter import messagebox

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

# Функция, которая выполняет вычисления
def calculate():
    try:
        # Берем текст из поля ввода и считаем его функцией eval
        result = eval(entry.get())
        # Очищаем поле и вставляем результат
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Ошибка", "Ты ввел какую-то дичь!")
        entry.delete(0, tk.END)

# Функция для добавления символов в поле при нажатии кнопок
def add_symbol(symbol):
    entry.insert(tk.END, symbol)

def clear():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Python Dark Calc")
root.geometry("384x440") # Немного увеличил высоту для кнопок
root.configure(bg="#1e1e1e")  # Тёмный фон окна
root.resizable(True, True)

# Поле ввода (тёмное с белым текстом)
entry = tk.Entry(root, font=("Consolas", 24), bg="#252526", fg="#ffffff", 
                 borderwidth=0, justify="right", insertbackground="white")
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=25, sticky="nsew")

# Цвета для кнопок
btn_color = "#333333"      # Обычные кнопки
equal_color = "#ff9500"    # Равно (оранжевый)
text_color = "#ffffff"     # Белый текст

# Список кнопок: (текст, строка, колонка, [цвет])
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('**', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('√', 2, 4),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('⌫', 4, 4),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3, equal_color), ('π', 3, 4), 
]

# Создаем кнопки из списка через цикл
for b in buttons:
    text, row, col = b[0], b[1], b[2]
    color = b[3] if len(b) > 3 else btn_color
    
    if text == '=':
        cmd = calculate
        
    elif text == '⌫':
        cmd = backspace
            
    elif text == 'π':
        cmd = lambda: add_symbol('3.14159')


    elif text == '√':
        cmd = lambda: add_symbol('**(0.5)')
    else:
        cmd = lambda t=text: add_symbol(t)
        
    btn = tk.Button(root, text=text, width=4, height=2, font=("Arial", 14, "bold"),
                    bg=color, fg=text_color, borderwidth=0, 
                    activebackground="#4d4d4d", activeforeground="white",
                    command=cmd)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# ОДНА большая красная кнопка очистки в самом низу
btn_clear = tk.Button(root, text="C", height=2, font=("Arial", 14, "bold"), 
                      bg="#ff3b30", fg="white", borderwidth=0, 
                      activebackground="#cc2f26", command=clear)
btn_clear.grid(row=5, column=0, columnspan=5, padx=5, pady=10, sticky="nsew")

root.mainloop()

