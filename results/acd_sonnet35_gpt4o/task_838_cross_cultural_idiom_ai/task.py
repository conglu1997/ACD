import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "source_language": "English",
                "target_language": "Mandarin Chinese",
                "cognitive_state": "stress",
                "context": "business negotiation"
            },
            {
                "source_language": "Spanish",
                "target_language": "Japanese",
                "cognitive_state": "curiosity",
                "context": "cultural exchange program"
            },
            {
                "source_language": "Arabic",
                "target_language": "Russian",
                "cognitive_state": "empathy",
                "context": "diplomatic meeting"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating, interpreting, and adapting idiomatic expressions across different languages and cultures based on specific cognitive states. Idiomatic expressions are phrases whose meaning cannot be deduced from the individual words (e.g., "It's raining cats and dogs" in English). Your task focuses on the following scenario:

Source Language: {t['source_language']}
Target Language: {t['target_language']}
Cognitive State: {t['cognitive_state']}
Context: {t['context']}

Provide your response in the following format:

1. AI System Architecture (250-300 words):
   a) Describe at least 3 key components of your AI system for cross-cultural idiom generation and interpretation.
   b) Explain how your system incorporates cultural knowledge, linguistic features, and cognitive modeling.
   c) Detail how the system adapts to the specified cognitive state and context.

2. Idiomatic Expression Generation (200-250 words):
   a) Generate an idiomatic expression in the source language that reflects the given cognitive state and context.
   b) Explain the cultural significance and literal meaning of the generated expression.
   c) Describe how your AI system arrived at this particular expression.

3. Cross-Cultural Adaptation (200-250 words):
   a) Adapt the generated idiomatic expression to the target language and culture.
   b) Provide the adapted expression in the target language, along with its literal translation in English.
   c) Explain the changes made during the adaptation process and why they were necessary.
   d) Discuss any challenges in maintaining the original meaning and cognitive state.

4. Cognitive State Modeling (150-200 words):
   a) Explain how your AI system models and incorporates the specified cognitive state.
   b) Describe how this cognitive modeling affects the idiom generation and adaptation process.

5. Evaluation Metrics (100-150 words):
   a) Propose a method for evaluating the cultural appropriateness and effectiveness of the AI-generated idiomatic expressions.
   b) Describe how you would measure the accuracy of cognitive state representation in the generated expressions.

6. Ethical Considerations (100-150 words):
   Discuss potential ethical issues or biases that could arise from using this AI system for cross-cultural communication and cognitive state representation.

Ensure your response demonstrates a deep understanding of linguistics, cultural nuances, cognitive science, and AI system design. Be creative in your approach while maintaining cultural sensitivity and scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The AI system architecture includes at least 3 key components and effectively incorporates cultural, linguistic, and cognitive elements",
            "The generated idiomatic expression is culturally appropriate and reflects the given cognitive state and context",
            "The cross-cultural adaptation demonstrates a deep understanding of both source and target languages and cultures, with the adapted expression provided in the target language",
            "The cognitive state modeling is well-explained and integrated into the idiom generation and adaptation process",
            "The proposed evaluation metrics and ethical considerations are thoughtful and comprehensive"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
