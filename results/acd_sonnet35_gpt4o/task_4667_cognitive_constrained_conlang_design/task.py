import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_constraints = [
            "Limited short-term memory (only 3 items)",
            "No concept of time",
            "Binary logic system",
            "Synesthesia-based lexicon",
            "Emotional state-dependent grammar"
        ]
        
        linguistic_features = [
            "Phonology",
            "Morphology",
            "Syntax",
            "Semantics",
            "Pragmatics"
        ]
        
        complex_concepts = [
            "Democracy",
            "Climate change",
            "Artificial intelligence",
            "Quantum entanglement",
            "Emotional intelligence"
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "cognitive_constraint": random.choice(cognitive_constraints),
                "linguistic_feature": random.choice(linguistic_features),
                "complex_concept": random.choice(complex_concepts)
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a constructed language (conlang) that incorporates the cognitive constraint of {t['cognitive_constraint']}, with a focus on the linguistic feature of {t['linguistic_feature']}. Then, use your conlang to express and analyze the complex concept of {t['complex_concept']}. Your response should include:\n\n" \
               f"1. Conlang Design (250-300 words):\n" \
               f"   a) Explain how your conlang incorporates the given cognitive constraint.\n" \
               f"   b) Describe the key features of your conlang, focusing on {t['linguistic_feature']}.\n" \
               f"   c) Provide examples of basic sentences or expressions in your conlang, with translations.\n\n" \
               f"2. Cognitive Analysis (200-250 words):\n" \
               f"   a) Analyze how the cognitive constraint influences the structure and use of your conlang.\n" \
               f"   b) Discuss potential cognitive implications for speakers of this language.\n\n" \
               f"3. Complex Concept Translation (200-250 words):\n" \
               f"   a) Translate the concept of {t['complex_concept']} into your conlang.\n" \
               f"   b) Explain how your conlang expresses this concept, given its cognitive and linguistic constraints.\n" \
               f"   c) Discuss any challenges or unique insights that arise from this translation.\n\n" \
               f"4. Interdisciplinary Implications (150-200 words):\n" \
               f"   a) Explore how your conlang might influence or be applied in fields such as cognitive science, AI, or intercultural communication.\n" \
               f"   b) Propose an experiment to test the cognitive effects of using your conlang.\n\n" \
               f"Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and the chosen complex concept. Use appropriate terminology and provide clear explanations for your design choices. Be creative while maintaining scientific plausibility throughout your response."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang design clearly incorporates the cognitive constraint of {t['cognitive_constraint']}.",
            f"The linguistic feature of {t['linguistic_feature']} is well-developed and explained in the conlang.",
            f"The translation and analysis of the complex concept {t['complex_concept']} is thorough and considers the language's constraints.",
            "The response demonstrates a deep understanding of linguistics and cognitive science principles.",
            "The interdisciplinary implications and proposed experiment are insightful and well-reasoned.",
            "The response is creative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
