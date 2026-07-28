import customtkinter as ctk


class OmegaFinanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.configure_window()

    def configure_window(self):
        self.title("Ômega Finance v0.1.0")
        self.geometry("1400x800")
        self.minsize(1000, 600)