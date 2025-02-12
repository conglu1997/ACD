import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sorrow', 'anger', 'fear', 'love', 'hope', 'nostalgia', 'serenity']
        languages = ['English', 'Japanese', 'Arabic', 'Russian', 'Swahili', 'Hindi', 'Spanish', 'French']
        poetic_forms = ['sonnet', 'haiku', 'free verse', 'ghazal', 'tanka', 'ode', 'villanelle', 'cinquain']
        
        return {
            "1": {
                "emotion": random.choice(emotions),
                "source_language": random.choice(languages),
                "target_language": random.choice(languages),
                "poetic_form": random.choice(poetic_forms)
            },
            "2": {
                "emotion": random.choice(emotions),
                "source_language": random.choice(languages),
                "target_language": random.choice(languages),
                "poetic_form": random.choice(poetic_forms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and analyzing poetry that conveys specific emotional states across different cultures, then apply it to the following scenario:

Emotion to Express: {t['emotion']}
Source Language: {t['source_language']}
Target Language: {t['target_language']}
Poetic Form: {t['poetic_form']}

Your task has the following parts:

1. Emotion-Language Mapping Framework (200-250 words):
   a) Explain how emotions are expressed differently in {t['source_language']} and {t['target_language']} poetry.
   b) Describe how your AI system would map emotional concepts between these languages.
   c) Discuss challenges in preserving emotional nuances across cultures and languages.

2. AI System Architecture (200-250 words):
   a) Provide a high-level overview of your AI system's architecture for poetry generation and analysis.
   b) Detail the components for emotional state representation, cultural knowledge integration, and poetic form adherence.
   c) Explain how the system handles the interplay between emotion, language, and poetic structure.

3. Poetry Generation (250-300 words):
   a) Generate a poem in the target language that expresses the given emotion using the specified poetic form.
   b) Provide a detailed explanation of the generated poem, including its emotional significance and cultural references.
   c) Describe the system's process for creating this poem, including any challenges encountered.
   d) Explain how the AI ensures adherence to the specified poetic form while maintaining emotional integrity.

4. Cross-Cultural Poetry Analysis (200-250 words):
   a) Describe how your AI system would analyze and interpret poems expressing the given emotion in both source and target languages.
   b) Address potential challenges in identifying emotional content across different cultural contexts.
   c) Provide an example of how the system would compare two poems (one from each language) expressing the same emotion.

5. Evaluation and Refinement (150-200 words):
   a) Propose a method for evaluating the emotional effectiveness and cultural authenticity of the generated poems.
   b) Describe how your AI system would improve its poetry generation based on feedback from native speakers and literary experts.
   c) Suggest specific metrics for measuring the system's performance in cross-cultural emotive poetry generation and analysis.

6. Ethical and Societal Implications (100-150 words):
   a) Discuss potential ethical implications and societal impacts of an AI system capable of generating and analyzing emotionally charged poetry across cultures.
   b) Address the importance of respecting cultural sensitivities and avoiding appropriation.
   c) Consider potential applications of this technology in fields such as mental health, education, or cross-cultural communication.

Ensure your response demonstrates a deep understanding of linguistics, poetry, emotional intelligence, cultural studies, and AI system design. Be creative and innovative while maintaining scientific rigor and cultural sensitivity. Your total response should be between 1100-1400 words.

Format your response with clear headings for each section (e.g., '1. Emotion-Language Mapping Framework:', '2. AI System Architecture:', etc.). Use appropriate subheadings where necessary to organize your thoughts clearly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of how the emotion '{t['emotion']}' is expressed in {t['source_language']} and {t['target_language']} poetry.",
            "The AI system architecture is well-explained and addresses the complexities of emotion, language, and poetic form.",
            f"A poem in {t['target_language']} expressing '{t['emotion']}' in the {t['poetic_form']} form is generated and thoroughly explained.",
            "The cross-cultural poetry analysis approach is comprehensive and culturally sensitive.",
            "The evaluation methods and metrics proposed are specific and relevant to emotive poetry generation and analysis.",
            "Ethical implications and potential applications are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
