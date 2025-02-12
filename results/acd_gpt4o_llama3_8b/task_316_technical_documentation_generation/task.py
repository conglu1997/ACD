class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "code_snippet": "def add(a, b):\n    '''\n    Adds two numbers together.\n    Arguments:\n    a -- The first number\n    b -- The second number\n    Returns:\n    The sum of the two numbers\n    '''\n    return a + b"
            },
            "2": {
                "software_feature": "A new feature in a note-taking app that allows users to tag notes and search for them based on tags. The feature should include the ability to add, remove, and edit tags, as well as a search functionality that returns all notes associated with a specified tag."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'code_snippet' in t:
            return f"""Generate detailed API documentation for the following code snippet:

{t['code_snippet']}

The documentation should include a description of the function, its arguments, return values, and an example usage. Submit your documentation as a plain text string."""
        elif 'software_feature' in t:
            return f"""Write a user manual for the following software feature:

Feature: {t['software_feature']}

The user manual should include an overview of the feature, step-by-step instructions for using it, and tips for getting the most out of the feature. Submit your user manual as a plain text string."""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The documentation should be clear, accurate, and well-structured.",
            "The documentation should include all necessary details such as descriptions of arguments, return values, and example usage (for API documentation).",
            "The user manual should provide a comprehensive overview, clear step-by-step instructions, and useful tips (for user manual)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
