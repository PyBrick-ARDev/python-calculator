import tkinter as tk
from tkinter import messagebox

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
root.geometry("385x500")
root.configure(bg="#1e1e1e")  # Тёмный фон окна
root.resizable(True, True)

# Поле ввода (тёмное с белым текстом)
entry = tk.Entry(root, font=("Consolas", 24), bg="#252526", fg="#ffffff", 
                 borderwidth=0, justify="right", insertbackground="white")
entry.grid(row=0, column=0, columnspan=8, padx=10, pady=25, sticky="nsew")

# Цвета для кнопок
btn_color = "#333333"      # Обычные кнопки
op_color = "#505050"       # Знаки (+, -, *, /)
equal_color = "#ff9500"    # Равно (оранжевый)
text_color = "#ffffff"     # Белый текст

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('**', 1, 4),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('C', 2, 4), # Добавил C сюда
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), 
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3, equal_color), 
]

# Создаем кнопки
for b in buttons:
    text, row, col = b[0], b[1], b[2]
    # Если в кортеже есть 4-й элемент (цвет), берем его, иначе стандартный
    color = b[3] if len(b) > 3 else btn_color
    
    if text == '=':
        cmd = calculate
    elif text == 'C':
        cmd = clear
        color = "#ff3b30" # Красный для сброса
    else:
        cmd = lambda t=text: add_symbol(t)
        
    btn = tk.Button(root, text=text, width=4, height=2, font=("Arial", 14, "bold"),
                    bg=color, fg=text_color, borderwidth=0, 
                    activebackground="#4d4d4d", activeforeground="white",
                    command=cmd)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

# Кнопка очистки (отдельно)
tk.Button(root, text="C", width=23, height=2, font=("Arial", 14), bg="red", fg="white", command=clear).grid(row=5, column=0, columnspan=4, pady=10)

root.mainloop()
