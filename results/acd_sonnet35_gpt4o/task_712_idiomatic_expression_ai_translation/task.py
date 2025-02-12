import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ai_architectures = [
            "Transformer-based language model",
            "Recurrent Neural Network (RNN)",
            "Neuro-symbolic AI",
            "Generative Adversarial Network (GAN)"
        ]
        language_pairs = [
            ("English", "Mandarin Chinese"),
            ("Spanish", "Japanese"),
            ("Arabic", "Russian"),
            ("Hindi", "Swahili")
        ]
        return {
            "1": {
                "ai_architecture": random.choice(ai_architectures),
                "source_language": language_pairs[0][0],
                "target_language": language_pairs[0][1]
            },
            "2": {
                "ai_architecture": random.choice(ai_architectures),
                "source_language": language_pairs[1][0],
                "target_language": language_pairs[1][1]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze how a {t['ai_architecture']} would process and generate idiomatic expressions when translating from {t['source_language']} to {t['target_language']}. Your response should include:

1. AI Architecture Analysis (150-200 words):
   a) Briefly explain how the {t['ai_architecture']} processes and generates language.
   b) Discuss potential strengths and limitations of this architecture for handling idiomatic expressions.

2. Cross-linguistic Idiom Analysis (200-250 words):
   a) Provide three examples of idiomatic expressions in {t['source_language']} and their literal translations in {t['target_language']}.
   b) Explain the cultural or cognitive factors that might influence the interpretation of these idioms in both languages.

3. AI Translation Process (200-250 words):
   a) Describe how the AI might approach translating the given idioms from {t['source_language']} to {t['target_language']}.
   b) Discuss potential challenges or errors the AI might encounter in this process.

4. Idiom Generation (150-200 words):
   a) Propose two novel idiomatic expressions that the AI might generate in {t['target_language']} based on {t['source_language']} concepts.
   b) Explain the reasoning behind each generated idiom, considering both the AI architecture and cultural influences.

5. Cognitive and Cultural Implications (150-200 words):
   a) Analyze how the AI's processing of idioms might reflect or differ from human cognitive processes.
   b) Discuss potential cultural misunderstandings or insights that could arise from the AI's approach to idiom translation.

6. Comparative Analysis (100-150 words):
   Briefly compare how a different AI architecture might handle the same idiomatic expressions differently.

7. Ethical Considerations (100-150 words):
   Discuss potential ethical implications of using AI for translating culturally-specific idiomatic expressions.

Ensure your response demonstrates a deep understanding of the specified AI architecture, idiomatic expressions, and cultural factors influencing language. Be creative in your analysis while maintaining scientific plausibility. The total word count for your response should be between 1050-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the specified AI architecture and its potential for processing idiomatic expressions.",
            "The analysis of cross-linguistic idioms is thorough and considers relevant cultural and cognitive factors.",
            "The proposed AI translation process and idiom generation are creative and plausible given the AI architecture and cultural context.",
            "The response addresses all seven points in the instructions comprehensively.",
            "The explanation demonstrates interdisciplinary knowledge of AI, linguistics, and cultural studies."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
