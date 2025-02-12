import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_nlp_tasks = [
            {
                "focus_area": "Semantic Entanglement",
                "application": "Sentiment Analysis"
            },
            {
                "focus_area": "Quantum Superposition",
                "application": "Machine Translation"
            },
            {
                "focus_area": "Quantum Interference",
                "application": "Text Summarization"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(quantum_nlp_tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired natural language processing system that leverages the principle of {t['focus_area']} to enhance {t['application']}. Your response should include the following sections:

1. Quantum NLP Framework (250-300 words):
   a) Explain how the principle of {t['focus_area']} can be applied to natural language processing.
   b) Describe the core components of your quantum-inspired NLP system.
   c) Discuss how your system differs from classical NLP approaches.

2. Mathematical Formulation (200-250 words):
   a) Provide a mathematical representation of your quantum NLP model.
   b) Explain how this formulation incorporates the principle of {t['focus_area']}.
   c) Describe how your model processes and represents linguistic information.

3. Application to {t['application']} (200-250 words):
   a) Detail how your quantum-inspired system would approach the task of {t['application']}.
   b) Explain the potential advantages of your approach over classical methods.
   c) Discuss any challenges or limitations specific to this application.

4. Implementation Strategy (150-200 words):
   a) Propose a method for implementing your system using current or near-future technology.
   b) Discuss any hardware or software requirements for your implementation.
   c) Suggest potential optimizations or approximations necessary for practical use.

5. Evaluation Metrics (150-200 words):
   a) Propose specific metrics to evaluate the performance of your quantum-inspired NLP system.
   b) Describe an experimental setup to compare your system against classical NLP approaches.
   c) Discuss how you would validate the quantum nature of your system's processing.

6. Ethical and Societal Implications (150-200 words):
   a) Analyze potential ethical concerns related to using quantum-inspired NLP for {t['application']}.
   b) Discuss societal implications of advanced quantum NLP systems.
   c) Propose guidelines for responsible development and use of such technologies.

Ensure your response demonstrates a deep understanding of both quantum computing principles and natural language processing. Be innovative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology from both fields and provide clear explanations for complex concepts.

Your total response should be between 1100-1400 words. Use clear headings for each section in your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['focus_area']} and how it can be applied to {t['application']}.",
            "The quantum NLP framework should be innovative, logically consistent, and well-explained.",
            "The mathematical formulation should accurately incorporate quantum principles and be relevant to the NLP task.",
            "The application to the specific NLP task should be detailed and demonstrate potential advantages over classical methods.",
            "The implementation strategy should be plausible given current or near-future technology.",
            "The evaluation metrics and experimental setup should be appropriate for assessing the system's performance.",
            "The response must thoughtfully address ethical and societal implications of the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
