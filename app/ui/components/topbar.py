import customtkinter as ctk


class TopBar(ctk.CTkFrame):
    def __init__(self, master, on_menu_click):
        super().__init__(
            master,
            height=60,
            corner_radius=0
        )

        self.on_menu_click = on_menu_click

        self.create_widgets()

    def create_widgets(self):
        self.menu_button = ctk.CTkButton(
            self,
            text="☰",
            width=45,
            height=40,
            command=self.on_menu_click
        )
        self.menu_button.pack(
            side="left",
            padx=(15, 10),
            pady=10
        )

        self.title_label = ctk.CTkLabel(
            self,
            text="Ômega Finance",
            font=ctk.CTkFont(
                size=20,
                weight="bold"
            )
        )
        self.title_label.pack(
            side="left",
            padx=5
        )