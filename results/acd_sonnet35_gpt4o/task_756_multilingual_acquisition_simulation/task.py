import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "languages": ["Mandarin", "English", "Spanish"],
                "environmental_factors": ["bilingual parents", "international school", "frequent travel"],
                "neurolinguistic_focus": "neural plasticity and critical periods"
            },
            {
                "languages": ["Arabic", "French", "Swahili"],
                "environmental_factors": ["multilingual community", "exposure to media in multiple languages", "language classes"],
                "neurolinguistic_focus": "cognitive control and attention switching"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a computational model simulating multilingual language acquisition in children, focusing on the following languages: {', '.join(t['languages'])}. Your model should incorporate the following environmental factors: {', '.join(t['environmental_factors'])}, and address the neurolinguistic aspect of {t['neurolinguistic_focus']}. Your response should include:

1. Model Architecture (250-300 words):
   a) Describe the key components of your computational model.
   b) Explain how your model simulates the process of language acquisition for multiple languages simultaneously.
   c) Detail how the model incorporates the given environmental factors.
   d) Discuss how the model addresses the specified neurolinguistic focus.

2. Neurolinguistic Principles (200-250 words):
   a) Explain the key neurolinguistic principles underlying your model.
   b) Describe how these principles are implemented in the computational framework.
   c) Discuss any assumptions or simplifications made in translating neurolinguistic theories to a computational model.

3. Simulation Process (200-250 words):
   a) Outline the steps your model would take to simulate language acquisition over time.
   b) Provide an example of how the model might represent the acquisition of a specific linguistic feature across the given languages.
   c) Explain how the model accounts for interactions between the languages being acquired.

4. Predictive Analysis (150-200 words):
   a) Describe a specific prediction your model would make about multilingual language acquisition.
   b) Explain the reasoning behind this prediction based on your model's architecture and underlying principles.
   c) Propose a method to test this prediction in real-world scenarios.

5. Model Evaluation (150-200 words):
   a) Discuss potential methods for validating your model against empirical data on multilingual language acquisition.
   b) Identify possible limitations of your model and suggest ways to address them.
   c) Explain how your model could be extended or improved in future iterations.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using such a model in research or educational settings.
   b) Consider issues such as language policy, educational practices, and cultural preservation.
   c) Propose guidelines for the responsible use and interpretation of your model's results.

Ensure your response demonstrates a deep understanding of language acquisition, neurolinguistics, and computational modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and coherence across all sections of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of language acquisition, neurolinguistics, and computational modeling.",
            "The model architecture is clearly described and incorporates all specified languages, environmental factors, and neurolinguistic focus.",
            "The simulation process and predictive analysis are logically explained and grounded in the model's design.",
            "The response addresses model evaluation, limitations, and potential improvements thoughtfully.",
            "Ethical considerations are thoroughly discussed with relevant guidelines proposed.",
            "The overall response is well-structured, coherent, and demonstrates creative problem-solving within the constraints of scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
