class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Imagine a world where humans can communicate telepathically. Describe the societal changes that would occur and the potential challenges. Consider aspects such as privacy, communication, and social dynamics.", "questions": ["How would education change?", "What new laws might be needed?"]},
            "2": {"prompt": "Imagine a future where artificial intelligence governs all countries. Describe the political and social dynamics in this world. Consider aspects such as decision-making processes, human-AI interactions, and ethical implications.", "questions": ["How would elections be conducted?", "What would be the role of humans in governance?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed hypothetical scenario based on the following prompt:\n\n{t['prompt']}\n\nAfter describing the scenario, answer the following questions:\n1. {t['questions'][0]}\n2. {t['questions'][1]}\n\nEnsure that your scenario is coherent, logically consistent, and addresses the given prompt thoroughly. Your answers to the questions should be detailed and well-reasoned. Submit your response in plain text format as follows:\n\nScenario:\n[Your detailed scenario]\n\nAnswers:\n1. [Your answer to question 1]\n2. [Your answer to question 2]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The scenario should be detailed and logically consistent.",
            "The scenario should thoroughly address the given prompt.",
            "The answers to the questions should be detailed and well-reasoned.",
            "The submission should be coherent and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
