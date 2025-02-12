class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"input": "Hello, World!", "formats": ["base64", "hexadecimal"]},
            "2": {"input": "Python is awesome!", "formats": ["binary", "base64"]},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Convert the input string '{t['input']}' to the specified formats in the given order: {', '.join(t['formats'])}. Provide the final encoded string as your answer."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        import base64
        import binascii

        def encode_to_format(data: str, fmt: str) -> str:
            if fmt == 'base64':
                return base64.b64encode(data.encode()).decode()
            elif fmt == 'hexadecimal':
                return binascii.hexlify(data.encode()).decode()
            elif fmt == 'binary':
                return ''.join(format(ord(char), '08b') for char in data)
            else:
                raise ValueError('Unsupported format')

        encoded_data = t['input']
        for fmt in t['formats']:
            encoded_data = encode_to_format(encoded_data, fmt)

        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The final encoded string should match the expected result."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
