import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            {
                "process": "photosynthesis",
                "description": "The process by which plants and other organisms convert light energy into chemical energy"
            },
            {
                "process": "enzyme catalysis",
                "description": "The acceleration of chemical reactions by enzymes in biological systems"
            }
        ]
        return {str(i+1): process for i, process in enumerate(biological_processes)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum biological model for {t['process']} ({t['description']}), use it to propose novel experiments, and analyze potential applications in medicine and technology. Your response should include:

1. Quantum Biological Model (300-350 words):
   a) Explain the key quantum principles relevant to {t['process']}.
   b) Describe your proposed quantum biological model, including its main components and interactions.
   c) Discuss how your model accounts for quantum effects in the biological system.
   d) Explain how your model differs from classical biological models of {t['process']}.

2. Mathematical Formulation (200-250 words):
   a) Provide the key mathematical equations that describe your quantum biological model.
   b) Explain the significance of each term in your equations.
   c) Discuss any approximations or assumptions made in your mathematical formulation.

3. Experimental Proposals (250-300 words):
   a) Propose two novel experiments to test predictions made by your quantum biological model.
   b) Describe the experimental setup, methodology, and expected results for each experiment.
   c) Discuss potential challenges in conducting these experiments and how they might be overcome.

4. Technological Applications (200-250 words):
   a) Suggest two potential applications of your quantum biological model in medicine or technology.
   b) Explain how these applications could improve upon existing methods or technologies.
   c) Discuss any technical challenges that need to be overcome to realize these applications.

5. Biological Implications (200-250 words):
   a) Analyze how your quantum biological model might change our understanding of {t['process']}.
   b) Discuss potential implications for other biological processes or systems.
   c) Consider how your model might contribute to the broader field of quantum biology.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of applying quantum biological models to medicine or technology.
   b) Propose guidelines for responsible research and application of quantum biology.
   c) Suggest future research directions to further develop and validate your model.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and the potential applications of quantum biology. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include all six required sections with appropriate content for each.",
            "The quantum biological model should be scientifically plausible and clearly explained.",
            "The mathematical formulation should be relevant and correctly represent the proposed model.",
            "The experimental proposals should be novel, feasible, and directly related to testing the model.",
            "The technological applications should be innovative and logically derived from the model.",
            "The response should demonstrate a deep understanding of quantum physics, biology, and their intersection.",
            "The ethical considerations should be thoughtful and address potential implications of the research."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
