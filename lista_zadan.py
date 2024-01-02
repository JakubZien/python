class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Zadanie '{task}' dodane.")

    def remove_task(self, task_index):
        if task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Zadanie '{removed_task}' usunięte.")
        else:
            print("Nieprawidłowy numer zadania.")

    def show_tasks(self):
        if self.tasks:
            print("Lista zadań:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1}. {task}")
        else:
            print("Lista zadań jest pusta.")

def main():
    task_manager = TaskManager()
    while True:
        print("\nWybierz opcję:")
        print("1. Dodaj zadanie")
        print("2. Usuń zadanie")
        print("3. Pokaż zadania")
        print("4. Wyjdź")

        choice = input("Wybierz numer opcji: ")

        if choice == "1":
            task = input("Wprowadź nowe zadanie: ")
            task_manager.add_task(task)
        elif choice == "2":
            task_index = int(input("Podaj numer zadania do usunięcia: ")) - 1
            task_manager.remove_task(task_index)
        elif choice == "3":
            task_manager.show_tasks()
        elif choice == "4":
            print("Zamykanie aplikacji.")
            break
        else:
            print("Nieprawidłowy wybór. Wybierz ponownie.")

if __name__ == "__main__":
    main()