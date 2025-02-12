import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        source_cultures = [
            "American",
            "Japanese",
            "Nigerian",
            "Indian"
        ]
        target_cultures = [
            "Brazilian",
            "Russian",
            "Egyptian",
            "Australian"
        ]
        communication_contexts = [
            "Business negotiation",
            "Political discourse",
            "Educational setting",
            "Social media interaction"
        ]
        cultural_elements = [
            "Idioms",
            "Metaphors",
            "Historical references",
            "Social norms"
        ]
        return {
            "1": {
                "source_culture": random.choice(source_cultures),
                "target_culture": random.choice(target_cultures),
                "context": random.choice(communication_contexts),
                "focus_element": random.choice(cultural_elements)
            },
            "2": {
                "source_culture": random.choice(source_cultures),
                "target_culture": random.choice(target_cultures),
                "context": random.choice(communication_contexts),
                "focus_element": random.choice(cultural_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of translating not just languages, but entire cultural contexts, focusing on {t['focus_element']}. Then, apply this system to analyze cross-cultural communication between {t['source_culture']} and {t['target_culture']} cultures in the context of a {t['context']}. Your response should include:\n\n1. AI System Design (300-350 words):\n   a) Describe the key components of your AI system for cultural context translation.\n   b) Explain how your system would handle the translation of {t['focus_element']}.\n   c) Discuss any novel AI techniques or algorithms used in your system.\n   d) Address potential challenges in translating cultural contexts and how your system overcomes them.\n   e) Cite relevant research or theories in AI and cultural anthropology to support your design.\n   f) Discuss potential biases in your AI system and propose methods to mitigate them.\n\n2. Cultural Analysis (250-300 words):\n   a) Provide a brief overview of relevant aspects of both {t['source_culture']} and {t['target_culture']} cultures, focusing on {t['focus_element']}.\n   b) Identify potential areas of misunderstanding or conflict in {t['focus_element']} between these cultures.\n   c) Explain how your AI system would analyze these cultural differences.\n   d) Provide specific examples of {t['focus_element']} from both cultures (e.g., if the focus is on idioms, give examples from both cultures).\n\n3. Application to Scenario (300-350 words):\n   a) Describe a specific scenario within the context of {t['context']} where cultural translation is crucial.\n   b) Explain how your AI system would facilitate communication in this scenario.\n   c) Provide a detailed example of how your system would handle a specific cultural translation challenge, including:\n      - Input: A specific {t['focus_element']} from the {t['source_culture']} culture\n      - Processing: Step-by-step explanation of how your AI system would analyze and translate it\n      - Output: The resulting translation or interpretation for the {t['target_culture']} audience\n   d) Compare your AI-driven approach to traditional human-based cultural translation methods in this scenario.\n\n4. Ethical Considerations and Evaluation (200-250 words):\n   a) Discuss potential ethical implications of using AI for cultural translation.\n   b) Address concerns about cultural appropriation, stereotyping, or oversimplification.\n   c) Propose guidelines for responsible use of your AI system in cross-cultural communication.\n   d) Design a method for evaluating the effectiveness of your AI system in real-world scenarios, including metrics and data collection strategies.\n\n5. Future Implications (150-200 words):\n   a) Speculate on how AI-driven cultural translation might impact global communication and understanding.\n   b) Discuss potential applications of your system beyond the given scenario.\n   c) Suggest areas for future research or improvement in AI-driven cultural translation.\n\nEnsure your response demonstrates a deep understanding of AI, linguistics, and cultural anthropology. Use appropriate terminology from each field and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and cultural plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1200-1450 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI, linguistics, and cultural anthropology.",
            "The proposed AI system is innovative, coherent, and technically plausible.",
            "The cultural analysis shows sensitivity and nuanced understanding of both cultures involved.",
            "The application to the scenario is realistic and includes a detailed example of the system's operation.",
            "The response includes relevant citations and comparisons to traditional methods.",
            "Ethical considerations are thoughtfully addressed, including potential biases and mitigation strategies.",
            "A concrete method for evaluating the AI system's effectiveness is proposed.",
            "The response is well-structured, clear, and effectively communicates complex ideas.",
            "All required sections are thoroughly addressed.",
            "The total word count is between 1200-1450 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
