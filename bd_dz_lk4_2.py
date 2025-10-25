import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Приветствие")
        self.root.geometry("450x500")
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        # Текст приветствия
        hello_label = tk.Label(self.root, text="привет", font=("Arial", 12))
        hello_label.pack(pady=15)

        # Изображение
        image_path = r"c:\Users\dmitry\Downloads\эээ.jfif"
        if os.path.exists(image_path):
            try:
                image = Image.open(image_path)
                # Масштабируем изображение если нужно
                image = image.resize((200, 150), Image.Resampling.LANCZOS)
                self.photo = ImageTk.PhotoImage(image)
                image_label = tk.Label(self.root, image=self.photo)
                image_label.pack(pady=10)
            except Exception as error:
                print(f"Ошибка загрузки изображения: {error}")
                error_label = tk.Label(self.root, text="Ошибка загрузки изображения")
                error_label.pack(pady=10)
        else:
            print(f"Файл {image_path} не найден")
            error_label = tk.Label(self.root, text="Изображение не найдено")
            error_label.pack(pady=10)

    def show(self):
        self.root.mainloop()

class ProfileWindow:
    def __init__(self):
        self.window = tk.Toplevel()
        self.window.title("Профиль пользователя")
        self.window.geometry("400x700+550+100")
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс для второго окна."""
        # Основной фрейм с прокруткой
        main_frame = ttk.Frame(self.window)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Canvas для прокрутки
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.setUpMainWindow(scrollable_frame)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def createImageLabels(self, parent):
        """Создаёт метки изображений."""
        images = [
            r"c:\Users\dmitry\Downloads\лега230.jfif"
        ]

        image_frame = ttk.Frame(parent)
        image_frame.pack(pady=10)

        for image_path in images:
            if os.path.exists(image_path):
                try:
                    image = Image.open(image_path)
                    # Масштабируем изображение
                    image = image.resize((100, 120), Image.Resampling.LANCZOS)
                    self.photo_profile = ImageTk.PhotoImage(image)
                    image_label = tk.Label(image_frame, image=self.photo_profile)
                    image_label.pack(side=tk.LEFT, padx=5)
                except Exception as e:
                    print(f"Ошибка при загрузке изображения {image_path}: {e}")
                    error_label = tk.Label(image_frame, text="Ошибка изображения")
                    error_label.pack(side=tk.LEFT, padx=5)
            else:
                print(f"Файл {image_path} не найден")
                error_label = tk.Label(image_frame, text="Изобр. не найдено")
                error_label.pack(side=tk.LEFT, padx=5)

    def setUpMainWindow(self, parent):
        """Создайте метки, которые будут отображаться в окне."""
        # Изображения
        self.createImageLabels(parent)

        # Имя пользователя
        user_label = tk.Label(parent, text="Киров Дима", font=("Arial", 20))
        user_label.pack(pady=20)

        # Биография
        bio_label = tk.Label(parent, text="Информация", font=("Arial", 17))
        bio_label.pack(anchor="w", padx=15, pady=(15, 0))

        about_label = tk.Label(parent, text="Я студент 2 курса", wraplength=350, justify=tk.LEFT)
        about_label.pack(anchor="w", padx=15, pady=5)

        # Навыки
        skills_label = tk.Label(parent, text="Mellstroy.game", font=("Arial", 17))
        skills_label.pack(anchor="w", padx=15, pady=(15, 0))

        languages_label = tk.Label(parent, text="open the door", wraplength=350, justify=tk.LEFT)
        languages_label.pack(anchor="w", padx=15, pady=5)

class App:
    def __init__(self):
        self.main_window = MainWindow()
        self.profile_window = ProfileWindow()

    def run(self):
        self.main_window.show()

# Запуск приложения
if __name__ == "__main__":
    app = App()
    app.run()