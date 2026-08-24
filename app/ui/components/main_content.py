import customtkinter as ctk

from app.ui.components.finance_card import FinanceCard


class MainContent(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            corner_radius=0
        )

        self.create_widgets()

    def create_widgets(self):
        self.create_header()
        self.create_finance_cards()

    def create_header(self):
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
            pady=(30, 5)
        )

        self.subtitle_label = ctk.CTkLabel(
            self,
            text="Visão geral das suas finanças",
            font=ctk.CTkFont(
                size=14
            )
        )

        self.subtitle_label.pack(
            anchor="w",
            padx=30,
            pady=(0, 20)
        )

    def create_finance_cards(self):
        self.cards_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.cards_frame.pack(
            fill="x",
            padx=30,
            pady=10
        )

        self.create_card(
            title="Saldo",
            value="R$ 8.450,00",
            description="Saldo disponível"
        )

        self.create_card(
            title="Receitas",
            value="R$ 5.200,00",
            description="Total deste mês"
        )

        self.create_card(
            title="Despesas",
            value="R$ 3.100,00",
            description="Total deste mês"
        )

        self.create_card(
            title="Economia",
            value="40,4%",
            description="Taxa de economia"
        )

    def create_card(
        self,
        title,
        value,
        description
    ):
        card = FinanceCard(
            self.cards_frame,
            title=title,
            value=value,
            description=description
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )