import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_language": "Japanese",
                "target_language": "English",
                "poetic_form": "Haiku",
                "cultural_theme": "Wabi-sabi (imperfection and transience)",
                "example_poem": "古池や蛙飛び込む水の音 (Furu ike ya / kawazu tobikomu / mizu no oto)"
            },
            {
                "source_language": "Spanish",
                "target_language": "Mandarin Chinese",
                "poetic_form": "Sonnet",
                "cultural_theme": "Duende (emotional darkness and authenticity)",
                "example_poem": "Yo sé que mi perfil será tranquilo / en el metal de un daguerrotipo viejo"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for translating poetry from {t['source_language']} to {t['target_language']}, focusing on the {t['poetic_form']} form and the cultural theme of {t['cultural_theme']}. Your system should preserve not only the meaning but also the cultural nuances, rhythm, and poetic devices of the original poem.

Here's an example poem in the source language to consider:
{t['example_poem']}

Your response should be structured as follows:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI poetry translation system.
   b) Explain how it handles the specific challenges of translating {t['poetic_form']} and preserving {t['cultural_theme']}.
   c) Detail the main components and their interactions.

2. Cultural and Linguistic Analysis (200-250 words):
   a) Discuss how your system analyzes and preserves cultural nuances specific to {t['source_language']} and {t['target_language']}.
   b) Explain how it handles idiomatic expressions and culturally-specific metaphors.
   c) Describe methods for maintaining the poem's emotional resonance across cultures.

3. Poetic Device Preservation (200-250 words):
   a) Explain how your system identifies and preserves poetic devices (e.g., rhyme, meter, alliteration) in {t['poetic_form']}.
   b) Describe techniques for adapting these devices to {t['target_language']} when direct translation is not possible.
   c) Discuss how the system balances preserving poetic structure with maintaining meaning.

4. Example Translation (150-200 words):
   a) Provide a translation of the example poem into {t['target_language']} using your system.
   b) Explain the decisions made in the translation process, especially regarding {t['cultural_theme']}.
   c) Highlight how your system preserved specific poetic devices and cultural nuances.

5. Evaluation Metrics (150-200 words):
   a) Propose quantitative and qualitative metrics to evaluate the quality of the poetry translations.
   b) Explain how you would measure preservation of cultural nuances and poetic devices.
   c) Discuss potential challenges in evaluating poetry translations across cultures.

6. Ethical and Cultural Implications (100-150 words):
   a) Discuss potential ethical concerns related to AI-driven poetry translation.
   b) Address issues of cultural appropriation or misrepresentation.
   c) Propose guidelines for responsible use of your system.

Ensure your response demonstrates a deep understanding of computational linguistics, poetry, and cross-cultural communication. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive system architecture for translating {t['poetic_form']} from {t['source_language']} to {t['target_language']}.",
            f"The system adequately addresses the preservation of the cultural theme {t['cultural_theme']}.",
            "The response demonstrates a deep understanding of computational linguistics, poetry, and cross-cultural communication.",
            "The proposed system includes innovative approaches to preserving poetic devices and cultural nuances in translation.",
            f"The example translation of '{t['example_poem']}' effectively illustrates the system's capabilities and preserves cultural nuances.",
            "The response proposes specific, measurable evaluation metrics for assessing translation quality.",
            "The response addresses ethical implications and proposes concrete guidelines for responsible use.",
            "The total response length is between 1050-1350 words and follows the specified structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
