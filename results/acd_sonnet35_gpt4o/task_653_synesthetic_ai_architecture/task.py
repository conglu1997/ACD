import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        synesthesia_types = [
            {
                "type": "Grapheme-color synesthesia",
                "description": "Letters or numbers are perceived as inherently colored",
                "primary_modality": "Visual (text)",
                "secondary_modality": "Visual (color)"
            },
            {
                "type": "Chromesthesia",
                "description": "Sounds evoke an experience of color",
                "primary_modality": "Auditory",
                "secondary_modality": "Visual (color)"
            },
            {
                "type": "Lexical-gustatory synesthesia",
                "description": "Words or sounds trigger a taste sensation",
                "primary_modality": "Auditory/Visual (text)",
                "secondary_modality": "Gustatory"
            },
            {
                "type": "Spatial-sequence synesthesia",
                "description": "Numerical sequences are perceived as points in space",
                "primary_modality": "Conceptual (numbers)",
                "secondary_modality": "Spatial"
            }
        ]
        
        pattern_recognition_tasks = [
            "Identify patterns in mixed visual-auditory input",
            "Classify emotions from text and speech combinations",
            "Recognize objects from tactile and visual information",
            "Predict sequence continuations using numerical and spatial data"
        ]
        
        return {
            "1": {
                "synesthesia": random.choice(synesthesia_types),
                "task": random.choice(pattern_recognition_tasks)
            },
            "2": {
                "synesthesia": random.choice(synesthesia_types),
                "task": random.choice(pattern_recognition_tasks)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a cognitive architecture for an AI system inspired by {t['synesthesia']['type']}, and use it to solve the following multi-modal pattern recognition problem: {t['task']}. Your response should include:\n\n1. Synesthesia Analysis (150-200 words):\n   a) Explain the given type of synesthesia and its neurological basis.\n   b) Discuss how this form of synesthesia influences human perception and cognition.\n\n2. Cognitive Architecture Design (250-300 words):\n   a) Propose a novel cognitive architecture that incorporates the principles of the given synesthesia type.\n   b) Describe the key components and processes of your architecture.\n   c) Explain how your design enables multi-modal information processing.\n\n3. Implementation for Pattern Recognition (200-250 words):\n   a) Describe how you would implement your cognitive architecture to solve the given pattern recognition task.\n   b) Explain the data preprocessing and representation methods you would use.\n   c) Outline the key algorithms or neural network structures involved in your solution.\n\n4. Advantages and Limitations (150-200 words):\n   a) Discuss the potential advantages of your synesthesia-inspired architecture for AI systems.\n   b) Analyze possible limitations or challenges in implementing and using your architecture.\n   c) Compare your approach to traditional multi-modal AI systems.\n\n5. Ethical Considerations and Future Directions (150-200 words):\n   a) Discuss any ethical implications of developing AI systems inspired by neurological phenomena.\n   b) Propose future research directions to further develop and validate your architecture.\n\nEnsure your response demonstrates a deep understanding of synesthesia, cognitive science, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section and number your paragraphs within each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the given type of synesthesia and its cognitive implications.",
            "The proposed cognitive architecture incorporates principles from the specified synesthesia type in a novel and plausible way.",
            "The implementation for pattern recognition is well-explained and directly addresses the given task.",
            "The response includes a thoughtful analysis of advantages, limitations, and ethical considerations.",
            "The submission demonstrates creativity and interdisciplinary knowledge integration throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
