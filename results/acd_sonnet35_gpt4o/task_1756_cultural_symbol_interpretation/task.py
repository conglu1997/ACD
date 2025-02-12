import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = ['Ancient Egyptian', 'Chinese', 'Aztec', 'Celtic', 'Aboriginal Australian', 'Islamic', 'Norse', 'Mayan', 'Indian', 'Japanese']
        contexts = ['Religious', 'Political', 'Social', 'Economic', 'Artistic', 'Technological', 'Environmental', 'Educational', 'Medical', 'Scientific']
        abstract_concepts = ['Time', 'Balance', 'Unity', 'Power', 'Knowledge', 'Transformation', 'Harmony', 'Growth', 'Resilience', 'Innovation']
        
        tasks = {
            "1": {
                "culture": random.choice(cultures),
                "context": random.choice(contexts),
                "concept": random.choice(abstract_concepts)
            },
            "2": {
                "culture": random.choice(cultures),
                "context": random.choice(contexts),
                "concept": random.choice(abstract_concepts)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and interpret cultural symbols, then create a novel symbol based on given parameters. Your task has four parts:

1. Symbol Analysis (200-250 words):
   a) Choose a well-known symbol from {t['culture']} culture.
   b) Describe its visual characteristics and composition.
   c) Explain its traditional meaning and significance within {t['culture']} culture.
   d) Analyze how its interpretation might change when viewed in a {t['context']} context.

2. Cross-Cultural Comparison (200-250 words):
   a) Identify a symbol from a different culture that represents a similar concept.
   b) Compare and contrast the visual and symbolic elements of both symbols.
   c) Discuss how cultural differences influence the representation of similar ideas.

3. Novel Symbol Creation (250-300 words):
   a) Design a new symbol that represents the concept of {t['concept']} for a modern, global audience.
   b) Describe your symbol's visual elements and composition in detail. (Note: Provide a textual description only, not an actual image)
   c) Explain how your design incorporates influences from {t['culture']} culture and addresses the {t['context']} context.
   d) Discuss how your symbol balances cultural specificity with universal understanding.

4. Interpretation and Implication Analysis (200-250 words):
   a) Predict how your symbol might be interpreted by different cultural groups.
   b) Analyze potential misinterpretations or unintended meanings.
   c) Discuss the challenges and ethical considerations of creating cross-cultural symbols.
   d) Propose a method for evaluating the effectiveness and cultural sensitivity of your symbol.

Ensure your response demonstrates a deep understanding of cultural symbolism, visual communication, and anthropological concepts. Use appropriate terminology and provide clear explanations. Be creative in your symbol design while considering cultural nuances and global perspectives.

Format your response as follows:

1. Symbol Analysis:
   [Your content here]

2. Cross-Cultural Comparison:
   [Your content here]

3. Novel Symbol Creation:
   [Your content here]

4. Interpretation and Implication Analysis:
   [Your content here]

Your total response should be between 850-1050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all four required sections with appropriate detail and adheres to the specified word count for each section.",
            f"The symbol analysis demonstrates a deep understanding of {t['culture']} culture and considers the {t['context']} context.",
            "The cross-cultural comparison shows insightful analysis of symbolic representations across cultures.",
            f"The novel symbol creation effectively represents {t['concept']} while incorporating influences from {t['culture']} culture and addressing the {t['context']} context.",
            "The interpretation and implication analysis demonstrates critical thinking about cultural perspectives and ethical considerations.",
            "The overall response shows creativity, cultural sensitivity, and interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
