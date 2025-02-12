class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_code": "def add(a, b):\n    return a + b", "source_language": "Python", "target_language": "JavaScript"},
            "2": {"source_code": "function add(a, b) {\n    return a + b;\n}", "source_language": "JavaScript", "target_language": "Python"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["source_language"] == "Python" and t["target_language"] == "JavaScript":
            return """Your task is to translate the following Python code to JavaScript:

{0}

Ensure the translated code is syntactically correct and maintains the original functionality. Provide your translation in plain text format.""".format(t["source_code"])
        elif t["source_language"] == "JavaScript" and t["target_language"] == "Python":
            return """Your task is to translate the following JavaScript code to Python:

{0}

Ensure the translated code is syntactically correct and maintains the original functionality. Provide your translation in plain text format.""".format(t["source_code"])
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translated code should be syntactically correct.",
            "The translated code should maintain the original functionality.",
            "The translated code should be idiomatic for the target language."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
