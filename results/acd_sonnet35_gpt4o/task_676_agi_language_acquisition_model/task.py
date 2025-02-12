import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "language_family": "Indo-European",
                "cognitive_theory": "Connectionism",
                "learning_constraint": "Limited memory capacity"
            },
            {
                "language_family": "Sino-Tibetan",
                "cognitive_theory": "Generative Grammar",
                "learning_constraint": "Absence of negative feedback"
            },
            {
                "language_family": "Austronesian",
                "cognitive_theory": "Usage-Based Theory",
                "learning_constraint": "Multimodal input integration"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language acquisition model for artificial general intelligence (AGI) based on theories of human language development and cognitive science principles. Your model should be tailored to learning languages from the {t['language_family']} family, incorporate principles from the {t['cognitive_theory']} theory of cognition, and address the learning constraint of {t['learning_constraint']}.

Provide your response in the following format:

1. Model Overview (100-150 words):
   Briefly describe your language acquisition model and its key features.

2. Cognitive Theory Integration (100-150 words):
   Explain how your model incorporates principles from {t['cognitive_theory']}.

3. Language Family Adaptation (100-150 words):
   Describe how your model is adapted to learn languages from the {t['language_family']} family.

4. Learning Constraint Solution (100-150 words):
   Explain how your model addresses the constraint of {t['learning_constraint']}.

5. Key Component Representation:
   Provide a simple diagram or pseudocode (5-10 lines) representing a key component of your model.

6. Comparative Analysis (100-150 words):
   Compare your model to one existing language acquisition theory or model.

7. Ethical Considerations (100-150 words):
   Discuss potential ethical implications and proposed safeguards for your model.

Ensure your response demonstrates understanding of linguistics, cognitive science, and AI. Be creative while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations.

Your total response should be between 600-900 words, excluding the diagram or pseudocode."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The model incorporates principles from {t['cognitive_theory']} theory",
            f"The design is adapted to learning languages from the {t['language_family']} family",
            f"The model addresses the learning constraint of {t['learning_constraint']}",
            "The response demonstrates understanding of linguistics, cognitive science, and AI",
            "The proposed model is creative while maintaining scientific plausibility",
            "The response includes a diagram or pseudocode representation of a key component",
            "The comparative analysis contrasts the proposed model with an existing theory or model",
            "Ethical considerations are thoughtfully addressed",
            "The response is well-structured and adheres to the specified format and word limits"
        ]
        scores = [eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria]
        return sum(scores) / len(scores)
