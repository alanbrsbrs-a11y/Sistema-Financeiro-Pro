import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(
            master,
            width=220,
            corner_radius=0
        )

        self.expanded_width = 220
        self.collapsed_width = 60
        self.is_expanded = True

        self.pack_propagate(False)

        self.create_widgets()

    def create_widgets(self):
        self.home_button = self.create_menu_button(
            "🏠  Início"
        )

        self.income_button = self.create_menu_button(
            "💰  Receitas"
        )

        self.expense_button = self.create_menu_button(
            "💸  Despesas"
        )

        self.card_button = self.create_menu_button(
            "💳  Cartões"
        )

        self.goals_button = self.create_menu_button(
            "🎯  Metas"
        )

        self.investments_button = self.create_menu_button(
            "📈  Investimentos"
        )

        self.reports_button = self.create_menu_button(
            "📊  Relatórios"
        )

    def create_menu_button(self, text):
        button = ctk.CTkButton(
            self,
            text=text,
            anchor="w",
            height=45
        )

        button.pack(
            fill="x",
            padx=10,
            pady=5
        )

        return button

    def toggle(self):
        if self.is_expanded:
            self.collapse()
        else:
            self.expand()

    def collapse(self):
        self.configure(width=self.collapsed_width)

        buttons = self.winfo_children()

        for button in buttons:
            button.configure(
                text=button.cget("text")[0],
                anchor="center"
            )

        self.is_expanded = False

    def expand(self):
        self.configure(width=self.expanded_width)

        labels = [
            "🏠  Início",
            "💰  Receitas",
            "💸  Despesas",
            "💳  Cartões",
            "🎯  Metas",
            "📈  Investimentos",
            "📊  Relatórios"
        ]

        buttons = self.winfo_children()

        for button, label in zip(buttons, labels):
            button.configure(
                text=label,
                anchor="w"
            )

        self.is_expanded = True