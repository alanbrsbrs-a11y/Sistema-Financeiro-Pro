import customtkinter as ctk


class FinanceCard(ctk.CTkFrame):
    def __init__(
        self,
        master,
        title,
        value,
        description=""
    ):
        super().__init__(
            master,
            height=130,
            corner_radius=12
        )

        self.title = title
        self.value = value
        self.description = description

        self.create_widgets()

    def create_widgets(self):
        self.title_label = ctk.CTkLabel(
            self,
            text=self.title,
            font=ctk.CTkFont(
                size=14
            )
        )

        self.title_label.pack(
            anchor="w",
            padx=20,
            pady=(18, 2)
        )

        self.value_label = ctk.CTkLabel(
            self,
            text=self.value,
            font=ctk.CTkFont(
                size=24,
                weight="bold"
            )
        )

        self.value_label.pack(
            anchor="w",
            padx=20,
            pady=2
        )

        if self.description:
            self.description_label = ctk.CTkLabel(
                self,
                text=self.description,
                font=ctk.CTkFont(
                    size=12
                )
            )

            self.description_label.pack(
                anchor="w",
                padx=20,
                pady=(2, 15)
            )