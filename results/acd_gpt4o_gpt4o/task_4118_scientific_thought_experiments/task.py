class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Imagine a world where the speed of light is only 10 meters per second. Describe the implications for daily life, technology, and physics laws."},
            "2": {"scenario": "Consider a planet with twice the gravitational force of Earth. Explain how this affects the evolution of life forms, architecture, and human activities."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return "Your task is to design and analyze a scientific thought experiment based on the following scenario: " + t["scenario"] + " Provide a detailed description of the potential implications, considering various aspects such as daily life, technology, and underlying scientific principles. Ensure your analysis is thorough, logical, and creative. Format your response as follows:\n\n1. Daily Life: [Your analysis]\n2. Technology: [Your analysis]\n3. Physics Laws (or Evolution, Architecture, Human Activities for Task 2): [Your analysis]\n"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be detailed and cover multiple aspects of the scenario.",
            "The reasoning should be logical and based on scientific principles.",
            "The response should demonstrate creativity in exploring the implications."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
