class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'problem': 'Design a method to efficiently convert carbon dioxide from the atmosphere into a useful product. Consider factors such as energy consumption, scalability, and environmental impact.', 'scientific_principles': 'Chemical reactions, catalysis, energy efficiency, environmental impact, scalability.'},
            '2': {'problem': 'Develop a sustainable method for desalinating seawater to provide fresh drinking water. Take into account energy consumption, cost, and potential environmental effects.', 'scientific_principles': 'Thermodynamics, membrane technology, energy consumption, cost-efficiency, environmental considerations.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: solution generation and scientific explanation.

Part 1: Solution Generation
Read the given scientific problem and generate an innovative and practical solution. Ensure your solution is feasible, efficient, and takes into account all relevant scientific principles. Provide your solution in plain text format.

Problem: {t['problem']}

Part 2: Scientific Explanation
Explain the underlying scientific principles involved in your solution. Describe how these principles apply to your solution and why your approach is effective. Provide your explanation in plain text format.

Relevant Scientific Principles: {t['scientific_principles']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The solution should be innovative and practical.',
            'The solution should be feasible and efficient.',
            'The solution should consider all specified factors (e.g., energy consumption, scalability, environmental impact).',
            'The scientific explanation should correctly describe the underlying principles and their application in the solution.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
