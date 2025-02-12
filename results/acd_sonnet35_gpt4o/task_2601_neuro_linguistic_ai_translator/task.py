import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_aspects = [
            "Syntax",
            "Semantics",
            "Pragmatics",
            "Phonology"
        ]
        neural_network_types = [
            "Convolutional Neural Network (CNN)",
            "Recurrent Neural Network (RNN)",
            "Transformer",
            "Graph Neural Network (GNN)"
        ]
        linguistic_formalisms = [
            "Chomsky's Generative Grammar",
            "Systemic Functional Grammar",
            "Construction Grammar",
            "Cognitive Grammar"
        ]
        
        return {
            "1": {
                "language_aspect": random.choice(language_aspects),
                "neural_network": random.choice(neural_network_types),
                "linguistic_formalism": random.choice(linguistic_formalisms)
            },
            "2": {
                "language_aspect": random.choice(language_aspects),
                "neural_network": random.choice(neural_network_types),
                "linguistic_formalism": random.choice(linguistic_formalisms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that can translate between human natural language, artificial neural network representations, and formal linguistic structures. Focus on the language aspect of {t['language_aspect']}, using a {t['neural_network']} architecture and {t['linguistic_formalism']} as the linguistic formalism. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the overall structure of your translation system.\n   b) Explain how it integrates principles from linguistics, neuroscience, and AI.\n   c) Detail the key components and their roles in the translation process.\n   d) Include a diagram or pseudocode snippet illustrating a crucial part of your architecture.\n\n2. Natural Language Representation (200-250 words):\n   a) Explain how human natural language, focusing on {t['language_aspect']}, is represented in your system.\n   b) Describe how your system captures the complexities and nuances of natural language.\n\n3. Neural Network Representation (200-250 words):\n   a) Describe how you use the {t['neural_network']} architecture to represent language.\n   b) Explain how this neural representation captures the relevant aspects of {t['language_aspect']}.\n   c) Discuss any novel approaches you've developed for this neural representation.\n\n4. Linguistic Formalism Representation (200-250 words):\n   a) Explain how you represent language using {t['linguistic_formalism']}.\n   b) Describe how this formalism captures the relevant aspects of {t['language_aspect']}.\n   c) Discuss any adaptations or extensions you've made to the formalism for your system.\n\n5. Translation Process (250-300 words):\n   a) Provide a step-by-step explanation of the translation process between all three representations.\n   b) Describe any intermediate representations or transformations used in the process.\n   c) Explain how your system ensures the translation preserves meaning across representations.\n   d) Discuss how your system handles ambiguity or multiple possible interpretations.\n\n6. Evaluation and Validation (150-200 words):\n   a) Propose methods to evaluate the accuracy and quality of your system's translations.\n   b) Describe key metrics or experiments that would validate your approach.\n\n7. Implications and Applications (150-200 words):\n   a) Discuss the potential impact of your system on linguistics, neuroscience, and AI research.\n   b) Explore possible applications in natural language processing, brain-computer interfaces, or cognitive modeling.\n\n8. Limitations and Future Directions (100-150 words):\n   a) Identify potential limitations of your proposed system.\n   b) Suggest improvements or extensions to address these limitations.\n\nEnsure your response demonstrates a deep understanding of linguistics, neuroscience, and artificial intelligence. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1500-1900 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, neuroscience, and artificial intelligence.",
            "The proposed system effectively integrates principles from all three fields.",
            "The translation process between the three representations is clearly explained and logically sound.",
            "The response shows creativity and innovation while maintaining scientific plausibility.",
            "The implications, applications, and limitations of the system are thoughtfully discussed.",
            "The response adheres to the specified structure and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
