import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_aspect": "Semantic processing",
                "neural_target": "Wernicke's area",
                "application_context": "Cross-cultural communication"
            },
            {
                "linguistic_aspect": "Syntactic processing",
                "neural_target": "Broca's area",
                "application_context": "Language learning and acquisition"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical brain-computer interface (BCI) system for direct neural-linguistic communication, focusing on {t['linguistic_aspect']} and targeting {t['neural_target']}. Then, analyze its potential applications in {t['application_context']} and explore its ethical implications. Your response should include:

1. System Design (250-300 words):
   a) Describe the key components and functionality of your BCI system.
   b) Explain how it interfaces with {t['neural_target']} to facilitate {t['linguistic_aspect']}.
   c) Discuss any novel technologies or approaches used in your design.
   d) Provide a high-level diagram or flowchart of your system (describe it textually).

2. Neurolinguistic Integration (200-250 words):
   a) Explain how your system translates between neural activity and linguistic constructs.
   b) Discuss potential challenges in accurately interpreting and transmitting {t['linguistic_aspect']}.
   c) Propose a method for validating the accuracy and fidelity of the neural-linguistic translation.

3. Application Analysis (200-250 words):
   a) Describe two potential applications of your system in {t['application_context']}.
   b) Analyze the potential benefits and limitations of each application.
   c) Discuss how your system might impact or transform current practices in this context.

4. Ethical Implications (200-250 words):
   a) Identify three major ethical concerns raised by your BCI system.
   b) Analyze these concerns using one ethical framework (e.g., utilitarianism, deontology).
   c) Propose guidelines for the responsible development and use of neural-linguistic BCIs.

5. Future Developments (150-200 words):
   a) Speculate on potential future advancements or extensions of your system.
   b) Discuss how these developments might impact society and human communication.
   c) Propose a related area of research that could enhance neural-linguistic interfaces.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and BCI technology. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate content and length.",
            f"The system design effectively addresses {t['linguistic_aspect']} and targets {t['neural_target']}.",
            "The neurolinguistic integration is well-explained and addresses potential challenges.",
            f"The application analysis provides insightful examples relevant to {t['application_context']}.",
            "Ethical implications are thoroughly explored with appropriate use of ethical frameworks.",
            "The response demonstrates creativity, scientific plausibility, and a deep understanding of neuroscience, linguistics, and BCI technology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
