import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_region": "prefrontal cortex",
                "ai_application": "decision-making in autonomous vehicles"
            },
            {
                "brain_region": "hippocampus",
                "ai_application": "privacy-preserving personal assistant"
            },
            {
                "brain_region": "amygdala",
                "ai_application": "emotion recognition in social media analysis"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system architecture inspired by the {t['brain_region']}, then analyze its ethical implications and propose safeguards for its application in {t['ai_application']}. Your response should include:

1. Neuroscientific Basis (200-250 words):
   a) Describe the key functions and characteristics of the {t['brain_region']}.
   b) Explain how these functions relate to the AI application of {t['ai_application']}.
   c) Discuss any limitations or challenges in translating biological neural processes to artificial systems.
   d) Cite at least one relevant scientific paper or study to support your analysis.

2. AI System Architecture (250-300 words):
   a) Propose an AI system architecture inspired by the {t['brain_region']}.
   b) Explain how specific features of your architecture parallel the function of the {t['brain_region']}.
   c) Describe the key components and their interactions within your system.
   d) Include a high-level diagram or pseudocode snippet illustrating a crucial part of your architecture.

3. Ethical Analysis (200-250 words):
   a) Identify potential ethical issues arising from your AI system's application in {t['ai_application']}.
   b) Analyze these issues using at least two different ethical frameworks (e.g., utilitarianism, deontology, virtue ethics).
   c) Discuss any unique ethical considerations that arise from your brain-inspired approach.

4. Safeguards and Governance (200-250 words):
   a) Propose specific technical safeguards to address the ethical issues you identified.
   b) Suggest governance structures or policies for responsible development and deployment of your AI system.
   c) Explain how these safeguards and governance measures relate to the neuroscientific basis of your system.

5. Comparative Analysis (150-200 words):
   a) Compare your brain-inspired approach to a conventional AI approach for {t['ai_application']}.
   b) Discuss potential advantages and disadvantages of your approach in terms of performance, ethics, and societal impact.

6. Reflection and Future Directions (100-150 words):
   a) Discuss potential limitations of your proposed system.
   b) Suggest areas for future research or improvement in your brain-inspired AI approach.

Ensure your response demonstrates a deep understanding of neuroscience, AI principles, and ethical reasoning. Be creative in your approach while maintaining scientific and philosophical rigor. Use appropriate terminology and provide clear explanations for complex concepts.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['brain_region']} and its functions, with at least one relevant scientific citation",
            f"The AI system architecture clearly draws inspiration from the {t['brain_region']} and is well-suited for {t['ai_application']}",
            "The ethical analysis is thorough and applies at least two ethical frameworks correctly",
            "The proposed safeguards and governance measures are specific and relevant to the identified ethical issues",
            "The comparative analysis provides insightful advantages and disadvantages of the brain-inspired approach",
            "The reflection section identifies meaningful limitations and future research directions",
            "The response shows creativity and interdisciplinary knowledge integration throughout"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
