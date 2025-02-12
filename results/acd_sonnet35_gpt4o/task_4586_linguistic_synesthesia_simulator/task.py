import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'linguistic_domain': 'phonology',
                'sensory_domain': 'color perception',
                'application_scenario': 'poetry analysis'
            },
            '2': {
                'linguistic_domain': 'syntax',
                'sensory_domain': 'spatial perception',
                'application_scenario': 'language learning'
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates linguistic synesthesia, focusing on the interaction between {t['linguistic_domain']} and {t['sensory_domain']}. Then, apply your system to the scenario of {t['application_scenario']}. Your response should include:

1. Synesthetic Model (250-300 words):
   a) Describe the key components of your AI system for simulating linguistic synesthesia.
   b) Explain how your model integrates {t['linguistic_domain']} processing with {t['sensory_domain']}.
   c) Discuss any novel approaches or algorithms used in your design.
   d) Include a diagram or pseudocode snippet illustrating a crucial part of your model.

2. Neurocognitive Basis (200-250 words):
   a) Propose a theoretical neurocognitive framework for linguistic synesthesia.
   b) Explain how your AI system models this framework.
   c) Discuss how your model accounts for individual variations in synesthetic experiences.

3. Linguistic-Sensory Mapping (200-250 words):
   a) Describe the specific mappings between {t['linguistic_domain']} features and {t['sensory_domain']} experiences in your model.
   b) Explain how these mappings are established, learned, or evolved in your system.
   c) Provide examples of how different linguistic inputs would be perceived in the sensory domain.

4. Application to {t['application_scenario']} (250-300 words):
   a) Explain how your linguistic synesthesia model could be applied to {t['application_scenario']}.
   b) Describe potential benefits or insights this application might provide.
   c) Discuss any challenges in applying your model to this scenario and how you'd address them.
   d) Provide a specific example of how your system would process a relevant input in this scenario.

5. Evaluation Methodology (150-200 words):
   a) Propose methods to evaluate the accuracy and cognitive plausibility of your synesthesia simulation.
   b) Describe key metrics or experiments that would validate your approach.
   c) Discuss how you would compare your model's output to human synesthetic experiences.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical considerations of simulating altered cognitive experiences like synesthesia.
   b) Explore the philosophical implications of your model for our understanding of perception and language.
   c) Consider potential misuses of this technology and propose safeguards.

7. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or modifications to your linguistic synesthesia model.
   b) Briefly describe how these extensions could further our understanding of language, perception, or cognition.

Ensure your response demonstrates a deep understanding of linguistics, neuroscience, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes a plausible AI system for simulating linguistic synesthesia between {t['linguistic_domain']} and {t['sensory_domain']}.",
            "The neurocognitive framework and its implementation in the AI system are well-explained and scientifically plausible.",
            f"The application to {t['application_scenario']} is thoughtfully explored with specific examples.",
            "The evaluation methodology is well-designed and appropriate for validating the model.",
            "Ethical and philosophical implications are thoroughly considered.",
            "The proposed future research directions are innovative and relevant.",
            "The overall response demonstrates deep understanding and creative integration of linguistics, neuroscience, and AI concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0