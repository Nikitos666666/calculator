import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Получаем числа и оператор из пользовательского ввода
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "":
            # Проверяем, выбран ли оператор
            messagebox.showerror("Ошибка", "Пожалуйста, выберите оператор")
            return

        # Выполняем выбранную операцию
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        # Выводим результат на метку
        result_label.config(text="Результат: " + str(result))
    except ValueError:
        # Обрабатываем ошибку неверного ввода
        messagebox.showerror("Ошибка", "Неверный ввод чисел")

# Создаем главное окно с заданными размерами
window = tk.Tk()
window.title("Калькулятор")
window.geometry("300x200")

# Создаем и размещаем элементы интерфейса

# Подпись для первого операнда
label1 = tk.Label(window, text="Первый операнд")
label1.pack()

# Поле ввода для первого операнда
entry1 = tk.Entry(window)
entry1.pack()

# Подпись для второго операнда
label2 = tk.Label(window, text="Второй операнд")
label2.pack()

# Поле ввода для второго операнда
entry2 = tk.Entry(window)
entry2.pack()

# Переменная для хранения выбранного оператора
operator_var = tk.StringVar(window)
label3 = tk.Label(window, text="Оператор")
label3.pack()

# Выпадающее меню для выбора оператора
operator_choices = ["+", "-", "*", "/"]
operator_dropdown = tk.OptionMenu(window, operator_var, *operator_choices)
operator_dropdown.pack()

# Кнопка "Рассчитать" для выполнения операции
calculate_button = tk.Button(window, text="Рассчитать", command=calculate)
calculate_button.pack()

# Метка для вывода результата
result_label = tk.Label(window, text="Результат: ")
result_label.pack()

# Запуск основного цикла обработки событий
window.mainloop()
