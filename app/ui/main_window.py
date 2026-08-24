import customtkinter as ctk

from app.ui.components.topbar import TopBar
from app.ui.components.sidebar import Sidebar
from app.ui.components.main_content import MainContent


class OmegaFinanceApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.configure_window()
        self.create_topbar()
        self.create_content_area()
        self.create_sidebar()

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

    def create_content_area(self):
        self.content_area = ctk.CTkFrame(
            self,
            corner_radius=0
        )

        self.content_area.pack(
            side="top",
            fill="both",
            expand=True
        )

        self.create_main_content()

    def create_main_content(self):
        self.main_content = MainContent(
            self.content_area
        )

        self.main_content.pack(
            side="right",
            fill="both",
            expand=True
        )

    def create_sidebar(self):
        self.sidebar = Sidebar(
            self.content_area
        )

        self.sidebar.pack(
            side="left",
            fill="y",
            before=self.main_content
        )

    def toggle_sidebar(self):
        self.sidebar.toggle()


if __name__ == "__main__":
    app = OmegaFinanceApp()
    app.mainloop()