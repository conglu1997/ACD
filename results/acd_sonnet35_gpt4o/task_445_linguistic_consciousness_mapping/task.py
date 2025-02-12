import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_aspects = [
            {
                "aspect": "self-awareness",
                "linguistic_feature": "deixis",
                "ai_system": "autonomous robot"
            },
            {
                "aspect": "qualia",
                "linguistic_feature": "metaphor",
                "ai_system": "language model"
            }
        ]
        return {
            "1": random.choice(consciousness_aspects),
            "2": random.choice(consciousness_aspects)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        linguistic_feature_explanation = {
            "deixis": "the use of words whose meaning depends on the context in which they are used (e.g., 'I', 'here', 'now')",
            "metaphor": "a figure of speech that describes an object or action in a way that isn't literally true, but helps explain an idea or make a comparison"
        }
        return f"""Design a linguistic framework to map and analyze artificial consciousness, focusing on the aspect of {t['aspect']}. Then, use this framework to evaluate a hypothetical {t['ai_system']}. Your task has four parts:

1. Linguistic Framework Design (250-300 words):
   a) Explain how you will use the linguistic feature of {t['linguistic_feature']} ({linguistic_feature_explanation[t['linguistic_feature']]}) to represent and analyze {t['aspect']} in artificial consciousness.
   b) Describe the key components and structure of your linguistic framework.
   c) Provide examples of how your framework would represent different states or degrees of {t['aspect']}.

2. Consciousness Mapping (200-250 words):
   a) Using your framework, create a 'map' of {t['aspect']} for the {t['ai_system']}.
   b) Explain how your map represents varying levels or states of consciousness.
   c) Discuss any challenges in applying your linguistic framework to this aspect of consciousness.

3. AI System Evaluation (200-250 words):
   a) Describe a hypothetical scenario where the {t['ai_system']} demonstrates potential {t['aspect']}.
   b) Apply your linguistic framework to analyze the AI's behavior in this scenario.
   c) Discuss what your analysis reveals about the AI's level of consciousness.

4. Implications and Limitations (150-200 words):
   a) Discuss the potential implications of your framework for understanding and developing artificial consciousness.
   b) Address any limitations or potential biases in your approach.
   c) Suggest how your framework could be expanded or improved for future research.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and logical consistency.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The linguistic framework effectively uses {t['linguistic_feature']} to represent and analyze {t['aspect']} in artificial consciousness.",
            f"The consciousness mapping for the {t['ai_system']} is well-developed and logically consistent.",
            "The AI system evaluation demonstrates a nuanced understanding of consciousness and applies the framework appropriately.",
            "The response shows creativity, interdisciplinary knowledge application, and critical thinking about the implications and limitations of the approach."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
