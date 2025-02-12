import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            'Ancient Egyptian',
            'Renaissance Italian',
            'Edo period Japanese',
            'Mayan',
            'Aboriginal Australian',
            'West African Yoruba'
        ]
        art_forms = [
            'visual art',
            'poetry',
            'music',
            'dance',
            'architecture',
            'storytelling'
        ]
        themes = [
            'creation myth',
            'harvest ritual',
            'coming of age ceremony',
            'funeral rites',
            'royal coronation',
            'spiritual enlightenment'
        ]
        
        return {
            "1": {
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "art_form": random.choice(art_forms),
                "theme": random.choice(themes)
            },
            "2": {
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures),
                "art_form": random.choice(art_forms),
                "theme": random.choice(themes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to create and analyze an art piece that fuses elements from {t['culture1']} and {t['culture2']} cultures, expressed through the medium of {t['art_form']}, centered around the theme of {t['theme']}. Follow these steps:\n\n1. Cultural Context (100-150 words):\n   Briefly explain the significance of the chosen theme in both cultures, highlighting similarities and differences.\n\n2. Artistic Creation (250-300 words):\n   a) Describe your proposed art piece in detail, explaining how it incorporates elements from both cultures.\n   b) Discuss the specific techniques, symbols, or motifs you've borrowed from each culture.\n   c) Explain how the chosen art form is used to express the theme.\n\n3. Analysis and Interpretation (200-250 words):\n   a) Analyze the symbolic meaning of key elements in your art piece.\n   b) Discuss how your creation reflects the worldviews or values of both cultures.\n   c) Explain how the fusion of cultures in your piece creates new meanings or perspectives.\n\n4. Cultural Sensitivity and Authenticity (150-200 words):\n   a) Discuss potential concerns about cultural appropriation in your art piece.\n   b) Explain how you've maintained respect and authenticity for both cultures.\n   c) Propose how artists from the involved cultures might react to your creation.\n\n5. Comparative Analysis (150-200 words):\n   Compare your fusion piece to traditional art from each of the source cultures, discussing:\n   a) How it adheres to or deviates from traditional forms\n   b) What new insights or expressions it might offer\n   c) How it might be received in each cultural context\n\n6. Reflection on AI and Creativity (100-150 words):\n   Reflect on the implications of AI systems creating culturally-inspired art:\n   a) Discuss potential benefits and challenges\n   b) Consider how this might impact human artists and cultural preservation\n   c) Propose ethical guidelines for AI in cross-cultural art creation\n\nEnsure your response demonstrates deep understanding of the cultures involved, artistic principles, and the complexities of cross-cultural creation. Be creative while maintaining cultural sensitivity and academic rigor.\n\nFormat your response with clear headings for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately represents elements from both {t['culture1']} and {t['culture2']} cultures.",
            f"The art piece effectively uses {t['art_form']} to express the theme of {t['theme']}.",
            "The creation demonstrates creativity and originality in fusing cultural elements.",
            "The analysis shows deep understanding of cultural symbolism and artistic principles.",
            "The response addresses cultural sensitivity and authenticity concerns thoughtfully.",
            "The comparative analysis offers insightful observations about traditional and fusion art.",
            "The reflection on AI and creativity demonstrates critical thinking about ethical implications.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
