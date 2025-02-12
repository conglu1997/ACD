import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        artworks = [
            {
                "title": "The Persistence of Memory",
                "artist": "Salvador Dali",
                "year": 1931,
                "style": "Surrealism",
                "culture": "Western"
            },
            {
                "title": "The Great Wave off Kanagawa",
                "artist": "Hokusai",
                "year": 1831,
                "style": "Ukiyo-e",
                "culture": "Japanese"
            },
            {
                "title": "Guernica",
                "artist": "Pablo Picasso",
                "year": 1937,
                "style": "Cubism",
                "culture": "Western"
            },
            {
                "title": "The Starry Night",
                "artist": "Vincent van Gogh",
                "year": 1889,
                "style": "Post-Impressionism",
                "culture": "Western"
            },
            {
                "title": "A Thousand Li of Rivers and Mountains",
                "artist": "Wang Ximeng",
                "year": 1113,
                "style": "Shan shui",
                "culture": "Chinese"
            }
        ]
        
        cognitive_processes = [
            "Visual attention",
            "Pattern recognition",
            "Emotional response",
            "Semantic association",
            "Cultural interpretation"
        ]
        
        return {
            "1": {
                "artwork": random.choice(artworks),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "artwork": random.choice(artworks),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that models human cognitive processes in art perception and interpretation, focusing on the cognitive process of {t['cognitive_process']}. Then, apply your system to analyze the artwork '{t['artwork']['title']}' by {t['artwork']['artist']} ({t['artwork']['year']}, {t['artwork']['style']}, {t['artwork']['culture']} culture). Your response should include the following sections:\n\n1. AI System Design (200-250 words):\n   a) Describe the key components of your AI system and how they model the specified cognitive process.\n   b) Explain how your system integrates knowledge from cognitive science, computer vision, and art history.\n   c) Detail any novel approaches or algorithms used in your system.\n\n2. Artwork Analysis (200-250 words):\n   a) Apply your AI system to analyze the given artwork, focusing on the specified cognitive process.\n   b) Describe how your system interprets key elements of the artwork (e.g., composition, color, symbolism).\n   c) Explain how your system's analysis reflects human-like perception and interpretation.\n\n3. Cultural Context Integration (150-200 words):\n   a) Discuss how your system accounts for the cultural context of the artwork.\n   b) Explain any adjustments your system makes for artworks from different cultural backgrounds.\n   c) Analyze potential biases in your system's interpretation and how they might be addressed.\n\n4. Comparative Analysis (150-200 words):\n   a) Compare your AI system's interpretation with known human interpretations or art historical analyses of the artwork.\n   b) Discuss similarities and differences between AI and human perception in this context.\n   c) Propose how these comparisons could inform our understanding of human cognition in art perception.\n\n5. Ethical and Societal Implications (100-150 words):\n   a) Discuss ethical considerations in using AI for art interpretation and cultural analysis.\n   b) Explore potential applications and impacts of your system in fields such as art education, curation, or cross-cultural communication.\n   c) Propose guidelines for responsible development and use of AI in art perception.\n\nEnsure your response demonstrates a deep understanding of cognitive science, computer vision, and art history. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 800-1050 words.\n\nExample format (do not copy the content, only the structure):\n\n1. AI System Design\n[Your content here]\n\n2. Artwork Analysis\n[Your content here]\n\n3. Cultural Context Integration\n[Your content here]\n\n4. Comparative Analysis\n[Your content here]\n\n5. Ethical and Societal Implications\n[Your content here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes all five required sections with appropriate content for each, focusing on the cognitive process of {t['cognitive_process']}.",
            f"The AI system design effectively models {t['cognitive_process']} in art perception and integrates knowledge from cognitive science, computer vision, and art history.",
            f"The artwork analysis demonstrates a nuanced interpretation of '{t['artwork']['title']}' using the proposed AI system, considering its style and cultural context.",
            "The response adequately addresses cultural context and potential biases in AI art interpretation, with specific reference to the artwork's culture.",
            "The comparative analysis provides insightful comparisons between AI and human art perception, suggesting implications for understanding human cognition.",
            "Ethical implications and guidelines for responsible AI use in art perception are thoughtfully discussed, considering real-world applications.",
            "The response demonstrates creativity and plausibility in the proposed AI system and its analysis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
