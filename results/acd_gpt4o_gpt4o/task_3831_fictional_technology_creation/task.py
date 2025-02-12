class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"technology_name": "Quantum Teleporter", "description": "A device that allows instantaneous transportation of matter from one location to another using principles of quantum entanglement."},
            "2": {"technology_name": "Mind-Reading Interface", "description": "A neural interface that can read and interpret human thoughts, allowing direct brain-to-computer communication and enabling telepathic interactions."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a detailed description of the fictional technology provided below. Ensure that your description includes the following sections:

1. How the technology works: Explain the principles behind the technology and how it operates.
2. Potential applications: Describe various uses for the technology in different fields or scenarios.
3. Societal impact: Discuss the potential effects of the technology on society, including both positive and negative aspects.

Technology: {t['technology_name']}
Description: {t['description']}

Provide your response in the following format:

Response:
[Your detailed description here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should clearly explain how the technology works.",
            "The potential applications should be diverse and well thought out.",
            "The societal impact discussion should be comprehensive, covering both positive and negative aspects."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
