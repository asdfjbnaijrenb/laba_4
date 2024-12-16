from models.client import Client


class Bank:
    def __init__(self):
        """Инициализация банка."""
        self.clients = {}

    def add_new_client(self, name, num_of_deposits, deposit_size, deposit_type):
        """Добавить нового клиента."""
        if name in self.clients:
            raise ValueError(f"Клиент с именем '{name}' уже существует.")

        # Вместо словаря создается объект Client
        self.clients[name] = Client(name, num_of_deposits, deposit_size, deposit_type)
        print(f"Вкладчик {name} добавлен в банк.")

    def get_total_deposits(self):
        """Получить сумму всех вкладов."""
        total = 0
        for client in self.clients.values():
            total += client.num_of_deposits * client.deposit_size
        return total
