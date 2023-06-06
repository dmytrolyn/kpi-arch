class View:
    def display_info(self, message):
        print(f"Info: {message}")

    def display_error(self, message):
        print(f"Error: {message}")

    def get_input(self, prompt, test_input=None):
        if test_input is not None:
            return test_input
        return input(prompt)