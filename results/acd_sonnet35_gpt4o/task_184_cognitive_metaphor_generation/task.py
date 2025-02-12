import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_frameworks = [
            {
                "name": "Conceptual Metaphor Theory",
                "key_concepts": ["source domain", "target domain", "cross-domain mapping", "embodied cognition"],
                "metaphor_to_interpret": "Time is money"
            },
            {
                "name": "Conceptual Blending Theory",
                "key_concepts": ["mental spaces", "blended space", "emergent structure", "selective projection"],
                "metaphor_to_interpret": "This surgeon is a butcher"
            }
        ]
        return {
            "1": random.choice(cognitive_frameworks),
            "2": random.choice(cognitive_frameworks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and interprets metaphors based on the {t['name']} framework. Your task:

1. Framework Overview (50-75 words):
   Briefly explain the key principles of {t['name']} and how it relates to metaphor processing.

2. System Architecture (150-200 words):
   Describe the key components and processes of your AI system for metaphor generation and interpretation. Explain how it incorporates the following concepts from {t['name']}: {', '.join(t['key_concepts'])}.

3. Metaphor Generation (100-150 words):
   Explain the step-by-step process your system would use to generate a novel metaphor. Include an example of a generated metaphor and its explanation.

4. Metaphor Interpretation (100-150 words):
   Describe how your system would interpret and analyze an existing metaphor. Provide an analysis of the metaphor: "{t['metaphor_to_interpret']}".

5. Cognitive Implications (100-150 words):
   Discuss how your AI system's approach to metaphor processing might inform our understanding of human cognition and language use.

6. AI Language Model Enhancement (100-150 words):
   Propose how the principles used in your metaphor system could be integrated into general-purpose language models to enhance their understanding and generation of figurative language.

7. Limitations and Ethical Considerations (100-150 words):
   Identify potential limitations of your system and any ethical concerns that might arise from its use or development.

8. Interdisciplinary Connections (50-100 words):
   Suggest how your metaphor generation and interpretation system might be applied in fields outside of cognitive science and AI (e.g., education, therapy, creative writing).

Ensure your response demonstrates a deep understanding of both the specified cognitive framework and AI language processing principles. Be creative in your approach while maintaining scientific plausibility.

Format your response using the following structure:

1. Framework Overview:
   [Your explanation here]

2. System Architecture:
   [Your description here]

3. Metaphor Generation:
   [Your explanation and example here]

4. Metaphor Interpretation:
   [Your analysis of the given metaphor here]

5. Cognitive Implications:
   [Your discussion here]

6. AI Language Model Enhancement:
   [Your proposal here]

7. Limitations and Ethical Considerations:
   [Your analysis here]

8. Interdisciplinary Connections:
   [Your suggestions here]

Your total response should be between 800-1000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a clear explanation of {t['name']} and its relation to metaphor processing",
            f"The system architecture incorporates key concepts from {t['name']}: {', '.join(t['key_concepts'])}",
            "The metaphor generation process is clearly explained with a novel and relevant example",
            f"The metaphor interpretation process is described with a thorough analysis of '{t['metaphor_to_interpret']}'",
            "The response discusses specific cognitive implications of the AI system",
            "The proposal for enhancing general-purpose language models is logical, innovative, and clearly explained",
            "Limitations and ethical considerations are thoughtfully addressed with specific examples",
            "Interdisciplinary applications are suggested with clear relevance to the proposed system",
            "The overall response demonstrates creativity, scientific plausibility, and a deep understanding of cognitive science and AI concepts",
            "The response follows the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
