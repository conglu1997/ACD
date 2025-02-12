import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        texts = [
            "The quick brown fox jumps over the lazy dog.",
            "To be or not to be, that is the question.",
            "I think, therefore I am.",
            "All that glitters is not gold.",
            "In the beginning was the Word, and the Word was with God, and the Word was God."
        ]
        return {
            "1": {"text": random.choice(texts)},
            "2": {"text": random.choice(texts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a neural network model capable of translating between lexical-gustatory and grapheme-color synesthesia, then use it to analyze the following text: '{t['text']}'. Your response should include:\n\n1. Neural Network Architecture (250-300 words):\n   a) Describe the key components of your neural network model.\n   b) Explain how your model represents and processes synesthetic associations.\n   c) Discuss how your architecture allows for translation between different forms of synesthesia.\n\n2. Synesthesia Mapping (200-250 words):\n   a) Explain how your model maps words to tastes (lexical-gustatory synesthesia).\n   b) Describe how your model associates letters or graphemes with colors (grapheme-color synesthesia).\n   c) Discuss any novel approaches in your system for handling the subjective nature of synesthetic experiences.\n\n3. Translation Mechanism (200-250 words):\n   a) Detail how your model translates from lexical-gustatory to grapheme-color synesthesia and vice versa.\n   b) Explain how your model handles words or concepts that might not have direct synesthetic associations.\n   c) Describe how your model maintains consistency in translations while allowing for the variability of synesthetic experiences.\n\n4. Text Analysis (250-300 words):\n   a) Apply your model to analyze the given text, providing both lexical-gustatory and grapheme-color interpretations.\n   b) Describe the synesthetic experience of the text according to your model.\n   c) Discuss any interesting patterns or insights revealed by your analysis.\n\n5. Limitations and Future Directions (150-200 words):\n   a) Discuss potential limitations of your model in capturing the full complexity of synesthetic experiences.\n   b) Propose ideas for expanding your model to include other forms of synesthesia.\n   c) Explore potential applications of your system beyond synesthesia translation (e.g., in creativity support tools, neurological research, or sensory augmentation).\n\nEnsure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your system design while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1050-1300 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of synesthesia and neural network architectures",
            "The model design effectively integrates concepts from neuroscience, linguistics, and artificial intelligence",
            "The synesthesia mapping and translation mechanisms are well-explained and plausible",
            "The analysis of the given text using the model is detailed and insightful",
            "The response shows creativity in system design while maintaining scientific plausibility",
            "Limitations and future directions are thoughtfully considered and discussed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
