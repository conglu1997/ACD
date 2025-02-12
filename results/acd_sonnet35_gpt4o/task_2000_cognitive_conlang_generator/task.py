import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_models = [
            {
                "model": "Embodied Cognition",
                "focus": "spatial relations",
                "cultural_context": "nomadic society"
            },
            {
                "model": "Distributed Cognition",
                "focus": "collective decision-making",
                "cultural_context": "highly interconnected digital society"
            }
        ]
        return {
            "1": random.choice(cognitive_models),
            "2": random.choice(cognitive_models)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f'''Design a constructed language (conlang) - an artificially created language - based on the cognitive model of {t['model']}, focusing on {t['focus']}, and situated in the cultural context of a {t['cultural_context']}. Your task includes:

1. Language Design (300-350 words):
   a) Describe the key features of your conlang, including its phonology, morphology, and syntax.
   b) Explain how these features reflect the specified cognitive model and cultural context.
   c) Provide three example sentences in your conlang, with translations and explanations of how they embody the cognitive model.
   Note: Ensure your language design is original and not based on existing conlangs or natural languages.

2. Cognitive Analysis (200-250 words):
   a) Analyze how your conlang might influence thought patterns and perception, particularly in relation to {t['focus']}.
   b) Discuss potential cognitive advantages or challenges for speakers of your language.
   c) Compare your conlang's cognitive implications to those of natural languages.

3. Cultural Integration (200-250 words):
   a) Explain how your conlang reflects and reinforces the values and practices of the {t['cultural_context']}.
   b) Describe how the language might evolve as the culture changes over time.
   c) Discuss potential challenges in adopting this language in different cultural contexts.

4. AI Language Processing (150-200 words):
   a) Propose an AI system designed to learn and process your conlang.
   b) Explain how this system would differ from those designed for natural languages.
   c) Discuss potential applications of this AI system in cognitive science or cultural studies.

5. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues in designing languages based on cognitive models.
   b) Discuss the implications of using such languages for intercultural communication.
   c) Propose guidelines for responsible development and use of cognitive-model-based conlangs.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and original in your language design while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 950-1200 words.'''

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang design is original and clearly reflects the cognitive model of {t['model']} and the cultural context of a {t['cultural_context']}.",
            f"The language features and example sentences demonstrate a specific focus on {t['focus']}.",
            "The cognitive analysis provides insightful and plausible connections between language features and thought patterns.",
            "The cultural integration section offers a well-reasoned explanation of how the language reflects and reinforces cultural values.",
            "The AI language processing proposal is innovative and addresses unique challenges specific to the designed conlang.",
            "Ethical considerations are thoughtfully discussed with relevant and practical guidelines proposed.",
            "The response demonstrates creativity, originality, and a deep understanding of linguistics, cognitive science, and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
