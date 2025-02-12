class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "context": "A fantasy novel set in a mystical land with wizards and dragons.",
                "criteria": [
                    "Name for a wise old wizard.",
                    "Name for a fierce dragon.",
                    "Name for a hidden magical forest."
                ]
            },
            "2": {
                "context": "A futuristic sci-fi world with advanced technology and space travel.",
                "criteria": [
                    "Name for a cutting-edge spaceship.",
                    "Name for a high-tech city on Mars.",
                    "Name for a renegade AI."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate creative and contextually appropriate names based on the given criteria and context.

Context: {t['context']}
Criteria:
1. {t['criteria'][0]}
2. {t['criteria'][1]}
3. {t['criteria'][2]}

Ensure that each name is unique, imaginative, and fits well within the provided context. The names should be original and not derived from existing well-known names in similar genres. Submit your names as a plain text string in the following format:

1. [Name for the first criterion]
2. [Name for the second criterion]
3. [Name for the third criterion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The names should be unique and imaginative.",
            "The names should fit well within the provided context.",
            "The names should be original and not derived from existing well-known names in similar genres.",
            "Each name should correspond correctly to the given criteria."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
