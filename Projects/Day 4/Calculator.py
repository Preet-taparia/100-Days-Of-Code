import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        """
        Calculator class for a basic calculator application.

        Args:
            root (tk.Tk): The root window object for the calculator.
        """
        self.answer_variable = ""
        self.expression_label = None
        self.result_label = None
        self.history_label = None
        self.history = []
        self.root = root

    def create_widgets(self):
        """
        Create and layout the calculator widgets.
        """
        self.expression_label = self.create_label(self.root, font=('Arial', 25, 'bold'), height=2, width=20)
        self.expression_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.result_label = self.create_label(self.root, font=('Arial', 25, 'bold'), height=2, width=20, fg='gray')
        self.result_label.grid(row=1, column=0, columnspan=4, sticky="nsew")

        self.history_label = self.create_label(self.root, font=('Arial', 15), height=10, width=20, anchor='center', relief=tk.SOLID, bd=1)
        self.history_label.grid(row=0, column=4, rowspan=8, padx=10, pady=10, sticky="nsew")
        self.history_label.config(text="History")

        buttons = [
            'AC', '√', '%', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.'
        ]

        buttons_list_traversal_counter = 0
        for i in range(2, 7):
            for j in range(4):
                if buttons_list_traversal_counter < len(buttons):
                    button_text = buttons[buttons_list_traversal_counter]
                    if button_text:
                        self.create_button(
                            self.root,
                            font=('Arial', 15, 'bold'),
                            padx=16,
                            pady=16,
                            text=button_text,
                            command=lambda txt=button_text: self.handle_button_click(txt),
                            height=2,
                            width=9
                        ).grid(row=i, column=j, sticky="nsew")
                    buttons_list_traversal_counter += 1

        self.create_button(
            self.root,
            font=('Arial', 15, 'bold'),
            padx=16,
            pady=16,
            text="√",
            command=self.handle_square_root,
            height=2,
            width=9
        ).grid(row=2, column=1, sticky="nsew")

        self.create_button(
            self.root,
            font=('Arial', 15, 'bold'),
            padx=16,
            pady=16,
            text="AC",
            command=self.all_clear,
            height=2,
            width=9
        ).grid(row=2, column=0, sticky="nsew")

        self.create_button(
            self.root,
            font=('Arial', 15, 'bold'),
            padx=16,
            pady=16,
            text="=",
            command=self.evaluate_expression,
            height=2,
            width=9
        ).grid(row=6, column=3, sticky="nsew")

        self.create_button(
            self.root,
            font=('Arial', 15, 'bold'),
            padx=16,
            pady=16,
            text="⌫",
            command=self.backspace,
            height=2,
            width=9
        ).grid(row=6, column=2, sticky="nsew")

        self.create_button(
            self.root,
            font=('Arial', 15, 'bold'),
            padx=16,
            pady=16,
            text=".",
            command=self.handle_decimal_point,
            height=2,
            width=9
        ).grid(row=6, column=1, sticky="nsew")

        # Configure row and column weights for responsive resizing
        for i in range(8):
            self.root.rowconfigure(i, weight=1)
        for j in range(5):
            self.root.columnconfigure(j, weight=1)

    def create_label(self, parent, **kwargs):
        """
        Create a label widget.

        Args:
            parent (tk.Widget): The parent widget.
            **kwargs: Additional keyword arguments for configuring the label.

        Returns:
            tk.Label: The created label widget.
        """
        label = tk.Label(parent, **kwargs)
        return label

    def create_button(self, parent, **kwargs):
        """
        Create a button widget.

        Args:
            parent (tk.Widget): The parent widget.
            **kwargs: Additional keyword arguments for configuring the button.

        Returns:
            tk.Button: The created button widget.
        """
        button = tk.Button(parent, **kwargs)
        return button

    def handle_button_click(self, entry):
        """
        Handle button click event.

        Args:
            entry (str): The button text to be added to the expression.

        """
        self.answer_variable += str(entry)
        self.expression_label['text'] = self.answer_variable
        self.clear_result_label()

    def handle_decimal_point(self):
        """
        Handle decimal point button click event.
        """
        if "." not in self.answer_variable:
            self.answer_variable += "."
            self.expression_label['text'] = self.answer_variable
            self.clear_result_label()

    def backspace(self):
        """
        Handle backspace button click event.
        """
        self.answer_variable = self.answer_variable[:-1]
        self.expression_label['text'] = self.answer_variable
        self.clear_result_label()

    def evaluate_expression(self):
        """
        Evaluate the expression and display the result.
        """
        expression = self.answer_variable
        try:
            result = eval(expression)
            self.answer_variable = str(result)
            self.expression_label['text'] = self.answer_variable
            self.result_label['text'] = str(result)
            self.history.append(expression + " = " + str(result))
            self.update_history_label()
        except ZeroDivisionError:
            self.clear_answer_entry_label()
            self.result_label['text'] = "Division by Zero"
        except (ValueError, SyntaxError, TypeError):
            self.clear_answer_entry_label()
            self.result_label['text'] = "Invalid Expression"

    def update_history_label(self):
        """
        Update the history label with the list of operations performed.
        """
        self.history_label['text'] = "\n".join(self.history)

    def clear_answer_entry_label(self):
        """
        Clear the answer entry label.
        """
        self.answer_variable = ""
        self.expression_label['text'] = ""

    def handle_square_root(self):
        """
        Handle square root button click event.
        """
        try:
            value = eval(str(self.answer_variable))
            if value < 0:
                self.clear_answer_entry_label()
                self.result_label['text'] = "Negative Number Input"
            else:
                sqrt_answer = math.sqrt(value)
                self.answer_variable = str(sqrt_answer)
                self.expression_label['text'] = self.answer_variable
                self.result_label['text'] = str(sqrt_answer)
                self.history.append("√(" + str(value) + ") = " + str(sqrt_answer))
                self.update_history_label()
        except (ValueError, SyntaxError, TypeError):
            self.clear_answer_entry_label()
            self.result_label['text'] = "Invalid Input"

    def all_clear(self):
        """
        Perform an all clear operation, clearing the answer entry, result label, and history.
        """
        self.clear_answer_entry_label()
        self.clear_result_label()
        self.clear_history()

    def clear_result_label(self):
        """
        Clear the result label.
        """
        self.result_label['text'] = ""

    def clear_history(self):
        """
        Clear the history.
        """
        self.history = []
        self.update_history_label()


def main():
    root = tk.Tk()
    root.title('Calculator App')

    calculator = Calculator(root)
    calculator.create_widgets()

    root.mainloop()


if __name__ == "__main__":
    main()
