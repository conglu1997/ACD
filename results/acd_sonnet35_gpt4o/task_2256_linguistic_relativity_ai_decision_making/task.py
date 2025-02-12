import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Hopi', 'Guugu Yimithirr', 'Pirahã', 'Russian', 'Japanese']
        cognitive_domains = ['time perception', 'spatial orientation', 'color discrimination', 'gender associations', 'numerical cognition']
        decision_contexts = ['resource allocation', 'risk assessment', 'ethical dilemmas', 'social interactions', 'environmental planning']
        
        tasks = {
            "1": {
                "language": random.choice(languages),
                "cognitive_domain": random.choice(cognitive_domains),
                "decision_context": random.choice(decision_contexts)
            },
            "2": {
                "language": random.choice(languages),
                "cognitive_domain": random.choice(cognitive_domains),
                "decision_context": random.choice(decision_contexts)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates how the {t['language']} language influences decision-making processes in the context of {t['decision_context']}, focusing on the cognitive domain of {t['cognitive_domain']}. Your system should be based on the linguistic relativity hypothesis, which suggests that the structure of a language affects its speakers' worldview and cognition.

Provide your response in the following format:

1. Linguistic Analysis (250-300 words):
   a) Describe key features of the {t['language']} language relevant to {t['cognitive_domain']}.
   b) Explain how these features might influence thought patterns and decision-making.
   c) Compare these features to English or another widely-spoken language.

2. Cognitive Model (200-250 words):
   a) Propose a cognitive model that represents how language features affect {t['cognitive_domain']}.
   b) Explain how this model integrates linguistic and cognitive processes.
   c) Discuss any assumptions or simplifications in your model.

3. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system.
   b) Explain how your system implements the cognitive model.
   c) Detail how the system simulates decision-making in the context of {t['decision_context']}.
   d) Discuss any novel AI techniques or approaches used in your design.

4. Simulation Scenario (200-250 words):
   a) Present a specific scenario related to {t['decision_context']}.
   b) Describe how your AI system would simulate decision-making in this scenario.
   c) Compare the expected outcomes for speakers of {t['language']} versus English speakers.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy of your AI system's simulations.
   b) Discuss how you would validate your system's predictions against real-world data.
   c) Address potential biases or limitations in your approach.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of simulating language-influenced decision-making.
   b) Address potential misuse or misinterpretation of your system's outputs.
   c) Propose guidelines for responsible development and use of such AI systems.

7. Interdisciplinary Implications (150-200 words):
   a) Discuss how your system could contribute to fields such as linguistics, cognitive science, and AI.
   b) Propose potential applications in areas like cross-cultural communication or AI language model development.
   c) Suggest future research directions based on your system's approach.

Ensure your response demonstrates a deep understanding of linguistic relativity, cognitive science, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistic relativity, cognitive science, and artificial intelligence.",
            "The linguistic analysis accurately describes relevant features of the specified language and their potential influence on cognition.",
            "The cognitive model effectively integrates linguistic and cognitive processes.",
            "The AI system architecture is well-designed and clearly explains how it implements the cognitive model and simulates decision-making.",
            "The simulation scenario is relevant and effectively demonstrates the system's capabilities.",
            "The evaluation and validation methods are appropriate and address potential biases.",
            "Ethical considerations are thoroughly addressed with thoughtful guidelines proposed.",
            "The interdisciplinary implications and future research directions are insightful and well-reasoned.",
            "The response is creative and demonstrates strong interdisciplinary knowledge integration.",
            "The response follows the required format and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
