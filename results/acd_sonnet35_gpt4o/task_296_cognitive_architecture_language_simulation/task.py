import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_architectures = [
            {
                "name": "ACT-R (Adaptive Control of Thought-Rational)",
                "key_features": "Modular, production system, declarative and procedural memory"
            },
            {
                "name": "SOAR (State, Operator, and Result)",
                "key_features": "Problem-solving, learning, long-term memory"
            },
            {
                "name": "CLARION (Connectionist Learning with Adaptive Rule Induction ON-line)",
                "key_features": "Dual explicit-implicit processes, bottom-up learning"
            },
            {
                "name": "LIDA (Learning Intelligent Distribution Agent)",
                "key_features": "Global Workspace Theory, consciousness, cognitive cycles"
            }
        ]
        
        language_aspects = [
            "Lexical acquisition",
            "Syntactic rule learning",
            "Pragmatic understanding",
            "Metaphor comprehension"
        ]
        
        return {
            "1": {
                "architecture": random.choice(cognitive_architectures),
                "language_aspect": random.choice(language_aspects)
            },
            "2": {
                "architecture": random.choice(cognitive_architectures),
                "language_aspect": random.choice(language_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a simulation of how the {t['architecture']['name']} cognitive architecture would approach {t['language_aspect']}. Your response should include:\n\n1. Architecture Overview (100-150 words):\n   Briefly explain the key principles and components of {t['architecture']['name']} ({t['architecture']['key_features']}).\n\n2. Language Acquisition/Use Simulation (200-250 words):\n   a) Describe how {t['architecture']['name']} would model the process of {t['language_aspect']}.\n   b) Explain the key mechanisms and processes involved in this simulation.\n   c) Provide a simple pseudocode or flowchart to illustrate the main steps of the simulation.\n\n3. Comparative Analysis (150-200 words):\n   Compare this approach to how current AI language models handle {t['language_aspect']}. Highlight key similarities and differences.\n\n4. Cognitive Implications (150-200 words):\n   Discuss what this simulation suggests about human cognition in relation to {t['language_aspect']}. Address any insights or limitations of the model.\n\n5. AI Development Applications (100-150 words):\n   Propose how insights from this simulation could be applied to improve AI language models or natural language processing systems.\n\nEnsure your response demonstrates a deep understanding of both the cognitive architecture and the specified language aspect. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility. Your total response should be between 700-950 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response accurately describes the key principles and components of the given cognitive architecture.",
            "The simulation of language acquisition/use is logically consistent with the architecture's principles.",
            "The comparative analysis demonstrates a clear understanding of both the cognitive architecture and current AI language models.",
            "The discussion of cognitive implications shows depth of thought and considers both insights and limitations.",
            "The proposed AI development applications are innovative and logically derived from the simulation.",
            "The overall response demonstrates interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
