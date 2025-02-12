import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "ecosystem": "coral reef",
                "key_species": "coral polyps",
                "ecological_issue": "coral bleaching"
            },
            {
                "ecosystem": "temperate forest",
                "key_species": "mycorrhizal fungi",
                "ecological_issue": "invasive species"
            }
        ]
        return {
            "1": random.choice(ecosystems),
            "2": random.choice(ecosystems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biosemiotic network model for the {t['ecosystem']} ecosystem, focusing on the role of {t['key_species']} in information flow and communication. Then, apply your model to address the ecological issue of {t['ecological_issue']}. Your response should include:

1. Biosemiotic Network Design (300-350 words):
   a) Describe the key components and relationships in your biosemiotic network model.
   b) Explain how your model incorporates principles from semiotics, information theory, and ecology.
   c) Detail how you represent different types of signs and communication channels in the {t['ecosystem']}.
   d) Discuss how your model captures the role of {t['key_species']} in the ecosystem's semiosphere.

2. Mathematical Formalization (250-300 words):
   a) Provide a mathematical or formal representation of your biosemiotic network model.
   b) Explain the variables, functions, and relationships in your formalization.
   c) Describe how your model quantifies information flow and semiotic processes.
   d) Include at least one equation or algorithm that demonstrates a key aspect of your model.

3. Ecosystem Analysis (200-250 words):
   a) Apply your biosemiotic network model to analyze the {t['ecosystem']}.
   b) Identify key semiotic processes and information flows in this ecosystem.
   c) Explain how {t['key_species']} contribute to these processes.
   d) Discuss any emergent properties or behaviors revealed by your model.

4. Ecological Problem-Solving (250-300 words):
   a) Use your biosemiotic network model to address the issue of {t['ecological_issue']}.
   b) Explain how your model provides insights into the causes or dynamics of this issue.
   c) Propose a solution or intervention based on your model's analysis.
   d) Discuss potential cascading effects of your proposed solution on the ecosystem's semiosphere.

5. Model Evaluation and Limitations (150-200 words):
   a) Discuss the strengths and limitations of your biosemiotic network model.
   b) Compare your approach to traditional ecological modeling techniques.
   c) Propose a method for empirically validating your model's predictions.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your biosemiotic network model could inform or be applied to other fields (e.g., computer science, linguistics, or social sciences).
   b) Propose a novel research question that arises from your model's integration of biosemiotics and ecology.

Ensure your response demonstrates a deep understanding of biosemiotics, ecology, information theory, and systems thinking. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed and scientifically plausible biosemiotic network model for the {t['ecosystem']} ecosystem, with a clear focus on the role of {t['key_species']}.",
            "The mathematical formalization of the model is coherent and demonstrates a strong understanding of both biosemiotics and information theory.",
            f"The ecosystem analysis provides meaningful insights into the semiotic processes and information flows in the {t['ecosystem']}.",
            f"The proposed solution to {t['ecological_issue']} is innovative, well-reasoned, and based on the biosemiotic network model.",
            "The response demonstrates a deep understanding of biosemiotics, ecology, information theory, and systems thinking, with appropriate use of technical terminology.",
            "The interdisciplinary implications and proposed research question show creative thinking and the ability to connect concepts across different fields.",
            "The overall response is well-structured, coherent, and adheres to the specified word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
