import tkinter as tk
from tkinter import ttk, messagebox


class RateWindow:
    """Окно для просмотра информации о клиентах."""

    def __init__(self, parent, bank):
        self.parent = parent
        self.bank = bank
        self.window = tk.Toplevel(parent)
        self.window.title("Информация о клиентах")
        self.window.geometry("400x400")

        # Создаем виджеты для отображения списка клиентов
        self.create_widgets()

    def create_widgets(self):
        """Создаем список клиентов и кнопки управления."""
        # Список клиентов
        self.client_listbox = tk.Listbox(self.window)
        self.client_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Заполняем список именами клиентов
        self.update_client_list()

        # Кнопка для получения информации о выбранном клиенте
        ttk.Button(self.window, text="Показать информацию о клиенте", command=self.show_client_info).pack(fill=tk.X, padx=10, pady=5)

        # Кнопка для сохранения информации о клиентах в файл
        ttk.Button(self.window, text="Сохранить список", command=self.save_clients_to_file).pack(fill=tk.X, padx=10, pady=5)

    def update_client_list(self):
        """Обновляет список клиентов в виджете Listbox."""
        self.client_listbox.delete(0, tk.END)  # Очищаем список перед обновлением
        for client_name in self.bank.clients.keys():
            self.client_listbox.insert(tk.END, client_name)  # Добавляем каждого клиента в Listbox

    def show_client_info(self):
        """Показывает информацию о выбранном клиенте."""
        try:
            selected_client_name = self.client_listbox.get(self.client_listbox.curselection())
            client = self.bank.clients[selected_client_name]

            client_info = (
                f"Имя: {selected_client_name}\n"
                f"Тип депозита: {client['deposit_type'].__class__.__name__}\n"
                f"Количество вкладов: {client['num_of_deposits']}\n"
                f"Размер вклада: {client['deposit_size']} рублей"
            )

            messagebox.showinfo("Информация о клиенте", client_info)

        except IndexError:
            messagebox.showwarning("Предупреждение", "Выберите клиента из списка.")

    def save_clients_to_file(self):
        """Сохраняет информацию о клиентах в файл clients.txt."""
        try:
            file_path = "clients.txt"  # Имя файла для сохранения данных
            with open(file_path, 'w', encoding='utf-8') as file:
                for client in self.bank.clients.values():
                    # Доступ к атрибутам через self.client (уже не нужен словарь!)
                    file.write(f"Имя: {client.name}\n")
                    file.write(f"Тип депозита: {client.deposit_type.__class__.__name__}\n")
                    file.write(f"Количество вкладов: {client.num_of_deposits}\n")
                    file.write(f"Размер вклада: {client.deposit_size} рублей\n")
                    file.write("=" * 40 + "\n")

            messagebox.showinfo("Успех", f"Информация о клиентах успешно сохранена в файл {file_path}.")

        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл.\nОшибка: {str(e)}")
