import customtkinter as ctk

from app.ui.components.topbar import TopBar


class OmegaFinanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.configure_window()
        self.create_topbar()

    def configure_window(self):
        self.title("Ômega Finance v0.1.0")
        self.geometry("1400x800")
        self.minsize(1000, 600)

    def create_topbar(self):
        self.topbar = TopBar(
            self,
            on_menu_click=self.toggle_sidebar
        )

        self.topbar.pack(
            side="top",
            fill="x"
        )

    def toggle_sidebar(self):
        print("Botão do menu clicado")