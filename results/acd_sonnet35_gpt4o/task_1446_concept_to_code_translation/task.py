import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "name": "Time",
                "description": "The concept of time, including its passage, measurement, and perception."
            },
            {
                "name": "Consciousness",
                "description": "The state of being aware of and able to think and perceive one's surroundings."
            },
            {
                "name": "Causality",
                "description": "The relationship between cause and effect in events or phenomena."
            },
            {
                "name": "Infinity",
                "description": "The concept of endlessness or limitlessness in time, space, or quantity."
            }
        ]
        return {str(i+1): concept for i, concept in enumerate(random.sample(concepts, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system to translate the abstract concept of {t['name']} into functional programming language constructs. {t['description']}

Your task is to:

1. Conceptual Analysis (200-250 words):
   a) Break down the concept of {t['name']} into its core components and characteristics.
   b) Identify key relationships and processes within the concept.
   c) Discuss any paradoxes or complexities inherent in the concept.

2. Programming Language Design (250-300 words):
   a) Create at least three unique data types or structures to represent aspects of {t['name']}.
   b) Design at least two higher-order functions that capture essential operations or transformations related to {t['name']}.
   c) Explain how your language constructs embody the concept's characteristics.

3. Code Implementation (200-250 words):
   a) Provide a code snippet (in a pseudocode or existing functional language of your choice) demonstrating how your data types and functions would be used to model {t['name']}. Clearly indicate the language or notation you are using.
   b) Explain how your implementation captures the nuances and complexities of the concept.

4. Practical Application (150-200 words):
   a) Propose a real-world problem or scenario where your {t['name']} programming constructs could be applied.
   b) Briefly describe how using these constructs could lead to new insights or solutions in this context.

5. Limitations and Extensions (150-200 words):
   a) Discuss any aspects of {t['name']} that are challenging to represent in your system.
   b) Suggest one potential extension or modification to your language design to address these limitations.

Ensure your response demonstrates a deep understanding of both the abstract concept and functional programming principles. Be creative in your approach while maintaining logical consistency and computational feasibility. Use appropriate terminology from philosophy, cognitive science, and computer science throughout your response.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent and insightful analysis of the concept of {t['name']}",
            "The programming language design is creative, logically consistent, and captures key aspects of the concept",
            "The code implementation effectively demonstrates the use of the designed language constructs",
            "The practical application proposed is relevant and demonstrates potential real-world value",
            "The discussion of limitations and extensions shows critical thinking and awareness of the system's constraints",
            "The overall response demonstrates a deep understanding of both the abstract concept and functional programming principles",
            "The response follows the specified format and is within the 950-1200 word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
