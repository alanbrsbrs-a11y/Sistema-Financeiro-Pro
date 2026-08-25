import customtkinter as ctk


class FinanceCard(ctk.CTkFrame):
    def __init__(
        self,
        master,
        title,
        value,
        description="",
        variation="",
        variation_type="neutral"
    ):
        super().__init__(
            master,
            height=130,
            corner_radius=12
        )

        self.title = title
        self.value = value
        self.description = description
        self.variation = variation
        self.variation_type = variation_type

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
                pady=(2, 5)
            )

        self.create_variation()

    def create_variation(self):
        if not self.variation:
            return

        if self.variation_type == "positive":
            symbol = "↑"
        elif self.variation_type == "negative":
            symbol = "↓"
        else:
            symbol = "→"

        variation_color = self.get_variation_color()

        self.variation_label = ctk.CTkLabel(
            self,
            text=f"{symbol} {self.variation}",
            text_color=variation_color,
            font=ctk.CTkFont(
                size=12,
                weight="bold"
            )
        )

        self.variation_label.pack(
            anchor="w",
            padx=20,
            pady=(0, 15)
        )

    def get_variation_color(self):
        if self.variation_type == "positive":
            return "#2ECC71"

        if self.variation_type == "negative":
            return "#E74C3C"

        return "#A0A0A0"