class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "biological_process": "photosynthesis",
                "quantum_effect": "quantum coherence"
            },
            "2": {
                "biological_process": "magnetoreception in birds",
                "quantum_effect": "radical pair mechanism"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Quantum biology is an emerging field that explores how quantum mechanical phenomena might play a role in biological processes. Your task is to design a quantum mechanical simulation of {t['biological_process']}, focusing on the role of {t['quantum_effect']}. Your response should include:

1. Quantum Biology Model (300-350 words):
   a) Describe the key components and processes involved in {t['biological_process']}.
   b) Explain how {t['quantum_effect']} is thought to play a role in this process.
   c) Outline a quantum mechanical model that simulates this biological process, including relevant equations or formalism.

2. Simulation Design (250-300 words):
   a) Propose a computational approach to implement your quantum biological model.
   b) Describe the key algorithms or methods you would use in your simulation.
   c) Explain how your simulation would capture both the quantum and biological aspects of the process.

3. Implications Analysis (200-250 words):
   a) Discuss the potential implications of your model for our understanding of {t['biological_process']}.
   b) Analyze how quantum effects might influence the efficiency or functionality of this biological process.
   c) Consider any broader implications for the field of quantum biology or related disciplines.

4. Experimental Validation (200-250 words):
   a) Propose an experimental setup to test predictions made by your quantum biology model.
   b) Describe the key measurements or observations that would be necessary to validate your model.
   c) Discuss potential challenges in experimentally isolating and observing quantum effects in this biological system.

Ensure your response demonstrates a deep understanding of quantum mechanics, biological systems, and computational modeling. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and rigor.

Include at least three citations to recent scientific literature (within the last 5 years) to support your model and analysis. Use a consistent citation format.

Format your response with clear headings for each section. Your total response should be between 950-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and the specified biological process.",
            "The quantum mechanical model is scientifically plausible and clearly explained.",
            "The simulation design effectively integrates quantum and biological aspects.",
            "The implications analysis shows insightful understanding of the potential impact on scientific knowledge.",
            "The proposed experimental validation is feasible and well-designed to test the model's predictions.",
            "The response uses appropriate scientific terminology and provides clear explanations for complex concepts.",
            "The response includes at least three relevant and recent (within 5 years) scientific citations.",
            "The entire response adheres to the 950-1150 word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
