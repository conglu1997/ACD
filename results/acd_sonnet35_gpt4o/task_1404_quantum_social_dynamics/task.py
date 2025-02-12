import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        societal_issues = [
            {
                "issue": "Political polarization",
                "quantum_concept": "Superposition",
                "social_aspect": "Opinion formation"
            },
            {
                "issue": "Economic inequality",
                "quantum_concept": "Entanglement",
                "social_aspect": "Resource distribution"
            }
        ]
        return {
            "1": random.choice(societal_issues),
            "2": random.choice(societal_issues)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model of social interactions based on quantum mechanics principles, then apply it to address the societal issue of {t['issue']}. Your model should incorporate the quantum concept of {t['quantum_concept']} and focus on the social aspect of {t['social_aspect']}. Provide your response in the following format:

1. Quantum Social Model (250-300 words):
   a) Describe your theoretical model that applies quantum principles to social interactions.
   b) Explain how you incorporate the specified quantum concept into your model.
   c) Discuss how your model represents and analyzes the given social aspect.

2. Mathematical Framework (200-250 words):
   a) Provide a basic mathematical representation of your model (you can use pseudo-equations or descriptive math).
   b) Explain the key variables and their relationships in your model.
   c) Describe how your model quantifies or measures social phenomena.

3. Application to Societal Issue (250-300 words):
   a) Apply your quantum social model to analyze the given societal issue.
   b) Explain how your model provides new insights into the problem.
   c) Propose a potential solution or intervention based on your model's predictions.

4. Experimental Design (200-250 words):
   a) Propose an experiment or study to test a key aspect of your quantum social model.
   b) Describe the methodology, including data collection and analysis methods.
   c) Discuss potential challenges in empirically validating your model.

5. Ethical Implications (150-200 words):
   a) Discuss ethical considerations of applying quantum principles to social systems.
   b) Address potential misuse or unintended consequences of your model.
   c) Propose guidelines for the responsible development and use of quantum social models.

Ensure your response demonstrates a deep understanding of both quantum mechanics and social sciences. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified quantum concept and its creative application to social systems.",
            "The mathematical framework is logically consistent and effectively represents the proposed model.",
            "The application to the societal issue is insightful and presents a novel perspective or solution.",
            "The experimental design is well-thought-out and addresses key aspects of the model.",
            "Ethical implications are thoroughly considered and addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
