class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'task': 'generate_code', 'language': 'Python', 'specification': 'Write a function to calculate the factorial of a given number.'},
            '2': {'task': 'translate_code', 'from_language': 'Python', 'to_language': 'JavaScript', 'code': 'def greet(name):\n    return f"Hello, {name}!"'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task'] == 'generate_code':
            return f"""Generate code in {t['language']} based on the following specification:

Specification: {t['specification']}

Submit your response as a plain text string with the complete code snippet."""
        elif t['task'] == 'translate_code':
            return f"""Translate the following code from {t['from_language']} to {t['to_language']}:

Code: {t['code']}

Submit your response as a plain text string with the translated code snippet."""
        else:
            return ''

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task'] == 'generate_code':
            criteria = ['The generated code should correctly implement the specified functionality and follow the syntax of the specified programming language.']
        elif t['task'] == 'translate_code':
            criteria = ['The translated code should correctly implement the functionality of the original code and follow the syntax of the target programming language.']
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
