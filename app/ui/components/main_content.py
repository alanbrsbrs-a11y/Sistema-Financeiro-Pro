import customtkinter as ctk


class MainContent(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            corner_radius=0
        )

        self.create_widgets()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(
            self,
            text="Dashboard",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            )
        )

        self.title_label.pack(
            anchor="w",
            padx=30,
            pady=(30, 10)
        )