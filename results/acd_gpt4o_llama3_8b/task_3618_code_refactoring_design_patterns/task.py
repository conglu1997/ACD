class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code": "class DataLoader:\n    def __init__(self, source):\n        self.source = source\n\n    def load_data(self):\n        if self.source == 'file':\n            return self.load_from_file()\n        elif self.source == 'database':\n            return self.load_from_database()\n\n    def load_from_file(self):\n        return 'Data from file'\n\n    def load_from_database(self):\n        return 'Data from database'\n\n# Usage example:\ndata_loader = DataLoader('file')\ndata = data_loader.load_data()",
                "pattern": "Factory Method"
            },
            "2": {
                "code": "class NotificationSender:\n    def __init__(self, type):\n        self.type = type\n\n    def send(self, message):\n        if this.type == 'email':\n            this.send_email(message)\n        elif this.type == 'sms':\n            this.send_sms(message)\n\n    def send_email(self, message):\n        print('Sending email:', message)\n\n    def send_sms(self, message):\n        print('Sending SMS:', message)\n\n# Usage example:\nnotifier = NotificationSender('email')\nnotifier.send('Hello World')",
                "pattern": "Strategy"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are provided with a piece of code and a design pattern. Your task is to refactor the given code to follow the specified design pattern while maintaining its functionality.

Original Code:\n{t['code']}

Design Pattern: {t['pattern']}

Refactor the code to adhere to the specified design pattern. Ensure that the functionality of the refactored code remains the same as the original. Submit your refactored code as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The refactored code should follow the specified design pattern.",
            "The functionality of the refactored code should remain the same as the original code.",
            "The refactored code should be syntactically correct and executable.",
            "The refactored code should not contain any hints or answers from the original code's structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
