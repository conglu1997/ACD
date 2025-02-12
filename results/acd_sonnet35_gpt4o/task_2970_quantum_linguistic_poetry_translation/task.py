import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        poems = [
            ("Sonnet 18", "William Shakespeare", "English", "Italian"),
            ("The Road Not Taken", "Robert Frost", "English", "Japanese"),
            ("Der Panther", "Rainer Maria Rilke", "German", "Spanish"),
            ("Le Lac", "Alphonse de Lamartine", "French", "Russian"),
            ("静夜思", "Li Bai", "Chinese", "Arabic")
        ]
        return {
            "1": {"poem": random.choice(poems)},
            "2": {"poem": random.choice(poems)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum computing system that translates poetry between languages while preserving quantum states of emotional resonance. Then, use your system to translate the poem '{t['poem'][0]}' by {t['poem'][1]} from {t['poem'][2]} to {t['poem'][3]}. Your response should include:\n\n1. Quantum Translation System Design (300-350 words):\n   a) Describe the key components of your quantum poetry translation system.\n   b) Explain how you represent emotional states as quantum states.\n   c) Detail the quantum algorithms used for preserving emotional resonance during translation.\n   d) Discuss how your system handles linguistic ambiguity and cultural nuances.\n   e) Include at least one quantum circuit diagram or mathematical representation of the quantum states involved.\n   f) Describe potential quantum error correction methods relevant to your translation system.\n\n2. Quantum-Linguistic Mapping (250-300 words):\n   a) Explain how you map linguistic features to quantum states.\n   b) Describe how semantic and syntactic structures are preserved in the quantum realm.\n   c) Discuss how you handle language-specific features (e.g., tones in Chinese, cases in Russian).\n\n3. Translation Process (250-300 words):\n   a) Provide a step-by-step explanation of how your system would translate the given poem.\n   b) Describe how emotional resonance is maintained throughout the translation process.\n   c) Explain how you resolve conflicts between linguistic accuracy and emotional preservation.\n\n4. Translated Poem and Analysis (200-250 words):\n   a) Present your quantum-translated version of the poem.\n   b) Analyze how well your translation preserves the original's emotional resonance and poetic devices.\n   c) Discuss any challenges or unexpected outcomes in the translation process.\n\n5. Quantum Advantage and Limitations (250-300 words):\n   a) Compare your quantum approach to state-of-the-art classical natural language processing methods for poetry translation.\n   b) Discuss the potential advantages of your quantum system over classical machine translation methods.\n   c) Analyze the limitations of your approach and propose future improvements.\n   d) Consider the ethical implications of using quantum computing for artistic translation.\n   e) Discuss the potential impact of your system on cross-cultural communication and art.\n\n6. Scalability and Future Applications (150-200 words):\n   a) Discuss the scalability of your quantum translation system for longer texts or multiple languages.\n   b) Propose potential applications of your system beyond poetry translation.\n   c) Speculate on how advances in quantum computing might further enhance your system in the future.\n\nEnsure your response demonstrates a deep understanding of quantum computing, linguistics, and poetic expression. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1400-1700 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum computing principles and their application to linguistic translation",
            "The quantum translation system design is innovative, well-explained, and scientifically plausible, including at least one quantum circuit diagram or mathematical representation and discussion of error correction methods",
            "The quantum-linguistic mapping is clearly described and accounts for complex language features",
            "The translation process is thoroughly explained, addressing both technical and artistic aspects",
            "The translated poem preserves the emotional resonance of the original while adapting to the target language",
            "The analysis of quantum advantages, limitations, and ethical implications shows deep insight into the intersection of quantum computing, linguistics, and art",
            "The discussion on scalability and future applications demonstrates forward-thinking and a broad understanding of the potential impact of the technology"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
