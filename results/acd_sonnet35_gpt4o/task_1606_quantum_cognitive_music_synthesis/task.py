import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_styles = [
            "Baroque",
            "Romantic",
            "Jazz",
            "Minimalist",
            "Electronic",
            "World Fusion"
        ]
        cognitive_processes = [
            "Working Memory",
            "Auditory Processing",
            "Pattern Recognition",
            "Emotional Processing",
            "Divergent Thinking",
            "Attention and Focus"
        ]
        return {
            "1": {"style": random.choice(musical_styles), "process": random.choice(cognitive_processes)},
            "2": {"style": random.choice(musical_styles), "process": random.choice(cognitive_processes)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a quantum computing algorithm that simulates the cognitive process of {t['process']} involved in musical creativity, and use it to compose a piece of music in the {t['style']} style. Your response should include:\n\n1. Quantum Algorithm Design (250-300 words):\n   a) Describe the key components of your quantum algorithm and how they model the specified cognitive process.\n   b) Explain how quantum principles (e.g., superposition, entanglement) are utilized in your algorithm.\n   c) Discuss how your algorithm interfaces with classical computing elements for music generation.\n\n2. Cognitive Process Simulation (200-250 words):\n   a) Analyze how the {t['process']} contributes to musical creativity.\n   b) Explain how your quantum algorithm simulates this cognitive process.\n   c) Discuss any limitations or approximations in your simulation.\n\n3. Musical Style Implementation (200-250 words):\n   a) Describe how your algorithm incorporates the key characteristics of the {t['style']} style.\n   b) Explain any challenges in representing this musical style in a quantum system.\n   c) Discuss how your algorithm balances style constraints with creative freedom.\n\n4. Composition Process (200-250 words):\n   a) Provide a step-by-step description of how your algorithm would compose a short musical piece.\n   b) Explain how the quantum and classical components interact during this process.\n   c) Describe how the cognitive process simulation influences the composition.\n\n5. Output Analysis (150-200 words):\n   a) Describe the expected characteristics of the musical piece produced by your algorithm.\n   b) Explain how you would evaluate the quality and creativity of the composition.\n   c) Discuss potential unexpected or emergent properties in the output.\n\n6. Quantum Advantage (150-200 words):\n   a) Analyze the potential advantages of using a quantum algorithm for this task compared to classical approaches.\n   b) Discuss any trade-offs or limitations of your quantum approach.\n\n7. Future Implications (100-150 words):\n   a) Propose two potential applications of your quantum cognitive music synthesis system beyond composition.\n   b) Discuss how this approach might contribute to our understanding of human creativity and cognition.\n\nEnsure your response demonstrates a deep understanding of quantum computing, cognitive science, and music theory. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields.\n\nFormat your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1250-1600 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and word counts.",
            "The quantum algorithm design demonstrates a clear understanding of quantum computing principles and their application to cognitive process simulation.",
            f"The musical style implementation successfully incorporates key characteristics of the {t['style']} style.",
            f"The cognitive process simulation accurately represents the {t['process']} and its role in musical creativity.",
            "The composition process description is clear, logical, and integrates quantum and classical components.",
            "The response demonstrates creativity, scientific plausibility, and interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
