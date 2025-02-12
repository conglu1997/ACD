import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_movements = [
            "Impressionism",
            "Cubism",
            "Surrealism",
            "Abstract Expressionism"
        ]
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum Tunneling",
            "Quantum Annealing"
        ]
        return {
            "1": {"art_movement": random.choice(art_movements), "quantum_concept": random.choice(quantum_concepts)},
            "2": {"art_movement": random.choice(art_movements), "quantum_concept": random.choice(quantum_concepts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses quantum computing principles to analyze and restore historical artworks from the {t['art_movement']} movement, focusing on the quantum concept of {t['quantum_concept']}. Your response should include:

1. Quantum-Art Interface (250-300 words):
   a) Explain how the quantum concept of {t['quantum_concept']} can be applied to art analysis and restoration.
   b) Describe the key features of {t['art_movement']} that your system will focus on.
   c) Propose a novel mechanism for translating between quantum states and artistic elements.

2. AI System Architecture (300-350 words):
   a) Outline the main components of your quantum art restoration AI system.
   b) Explain how classical and quantum computing elements will interact in your system.
   c) Describe how your system will handle the unique challenges of {t['art_movement']} artworks.
   d) Discuss any potential quantum algorithms or techniques your system will employ.

3. Restoration Process Simulation (200-250 words):
   a) Provide a step-by-step explanation of how your system would approach restoring a hypothetical {t['art_movement']} artwork.
   b) Highlight where and how the quantum concept of {t['quantum_concept']} is utilized in this process.

4. Comparative Analysis (150-200 words):
   a) Compare your quantum AI approach to traditional art restoration techniques.
   b) Discuss potential advantages and limitations of your system.

5. Ethical and Cultural Implications (150-200 words):
   a) Analyze potential ethical concerns related to using quantum AI for art restoration.
   b) Discuss how your system might impact our understanding or appreciation of {t['art_movement']}.

6. Future Developments (100-150 words):
   a) Propose two potential advancements or extensions of your system.
   b) Speculate on how quantum art restoration AI might evolve in the next decade.

Ensure your response demonstrates a deep understanding of quantum computing principles, AI systems, and art history, particularly {t['art_movement']}. Be innovative in your approach while maintaining scientific and artistic plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of both the quantum concept of {t['quantum_concept']} and the art movement {t['art_movement']}.",
            "The proposed AI system should be innovative and well-explained, showing a clear integration of quantum computing and art restoration.",
            "The restoration process simulation should be detailed and highlight the use of quantum principles.",
            "The comparative analysis should provide thoughtful insights into the advantages and limitations of the quantum AI approach.",
            "Ethical and cultural implications must be considered thoroughly.",
            "The response should be well-structured, adhere to the word limits, and demonstrate interdisciplinary knowledge and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
