class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "source_code": "def greet(name):\n    return f'Hello, {name}!'\n\nprint(greet('Alice'))",
                "source_language": "Python",
                "target_language": "JavaScript"
            },
            "2": {
                "source_code": "function factorial(n) {\n    if (n === 0) {\n        return 1;\n    } else {\n        return n * factorial(n - 1);\n    }\n}\n\nconsole.log(factorial(5));",
                "source_language": "JavaScript",
                "target_language": "Python"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        source_code = t["source_code"]
        source_language = t["source_language"]
        target_language = t["target_language"]
        return f"""Translate the following code from {source_language} to {target_language}. Ensure that the translated code preserves the original functionality and follows the idiomatic style of the target language. The translated code must be executable and produce the same output as the original code. Please provide the translated code as a plain text string.

Source Code ({source_language}):\n{source_code}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The translated code must be executable.", "The translated code must produce the same output as the original code.", "The translated code must follow the idiomatic style of the target language."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0