import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        temporal_concepts = [
            {
                "culture": "Western",
                "time_concept": "Linear time",
                "key_features": ["past", "present", "future", "sequential ordering"]
            },
            {
                "culture": "East Asian",
                "time_concept": "Cyclic time",
                "key_features": ["recurring patterns", "seasons", "generational cycles"]
            }
        ]
        return {
            "1": random.choice(temporal_concepts),
            "2": random.choice(temporal_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI language model that incorporates principles of temporal cognition based on the {t['culture']} concept of {t['time_concept']}. Your task:

1. Temporal Concept Overview (75-100 words):
   Explain the key principles of {t['time_concept']} in {t['culture']} culture and how it influences language use.

2. Model Architecture (200-250 words):
   Describe the architecture of your AI language model, explaining how it incorporates the following temporal concepts: {', '.join(t['key_features'])}. Include details on data structures, processing mechanisms, and any novel components.

3. Temporal Expression Processing (150-200 words):
   Explain how your model would process and generate temporal expressions. Provide an example of a complex temporal phrase and describe step-by-step how your model would interpret or generate it.

4. Cross-cultural Temporal Translation (150-200 words):
   Describe how your model would approach translating temporal expressions between cultures with different time concepts (e.g., from {t['culture']} to a culture with a different time concept). Provide an example and explain the challenges involved.

5. Cognitive Implications (100-150 words):
   Discuss how your model's approach to temporal cognition might inform our understanding of human cognition and cultural differences in time perception.

6. Ethical Considerations (100-150 words):
   Identify potential ethical concerns or biases that might arise from implementing a culturally-specific temporal cognition model in AI systems.

7. Potential Applications (75-100 words):
   Suggest innovative applications for your temporal cognition language model in fields such as cross-cultural communication, historical analysis, or future prediction.

Ensure your response demonstrates a deep understanding of temporal cognition, cultural linguistics, and AI language model architectures. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using the following structure:

1. Temporal Concept Overview:
   [Your explanation here]

2. Model Architecture:
   [Your description here]

3. Temporal Expression Processing:
   [Your explanation and example here]

4. Cross-cultural Temporal Translation:
   [Your description and example here]

5. Cognitive Implications:
   [Your discussion here]

6. Ethical Considerations:
   [Your analysis here]

7. Potential Applications:
   [Your suggestions here]

Your total response should be between 850-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a clear explanation of {t['time_concept']} in {t['culture']} culture and its influence on language",
            f"The model architecture incorporates the key temporal concepts: {', '.join(t['key_features'])}",
            "The temporal expression processing is explained with a relevant and complex example",
            "The cross-cultural temporal translation approach is described with a specific example and challenges",
            "The response discusses specific cognitive implications of the AI model for understanding human cognition and cultural differences",
            "Ethical considerations are thoughtfully addressed with specific examples",
            "Innovative and relevant potential applications are suggested",
            "The overall response demonstrates creativity, scientific plausibility, and a deep understanding of temporal cognition, cultural linguistics, and AI concepts",
            "The response follows the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
