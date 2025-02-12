class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept_pair": ["neuron", "computer"],
                "relationship": "A neuron is to a brain as a computer is to a network."
            },
            "2": {
                "concept_pair": ["root", "tree"],
                "relationship": "A root is to a tree as a foundation is to a building."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a pair of concepts. Your task is to generate a complex analogy that describes the relationship between these concepts and then explain the relationship clearly.

Concept Pair: {t['concept_pair'][0]} and {t['concept_pair'][1]}

Submit your response in the following format:
Analogy: [Your analogy]
Explanation: [Your explanation of the relationship]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analogy should clearly describe the relationship between the given concepts.",
            "The explanation should be coherent and logically justify the analogy.",
            "The response should include both the analogy and the explanation in the correct format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
