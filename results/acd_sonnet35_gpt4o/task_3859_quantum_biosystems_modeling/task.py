import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "complex": "Fenna-Matthews-Olson (FMO) complex",
                "organism": "green sulfur bacteria",
                "quantum_effect": "quantum coherence",
                "application": "artificial photosynthesis"
            },
            {
                "complex": "Light-Harvesting Complex II (LHCII)",
                "organism": "higher plants",
                "quantum_effect": "quantum entanglement",
                "application": "quantum computing"
            }
        ]
        return {
            "1": random.choice(tasks),
            "2": random.choice(tasks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a computational model to simulate {t['quantum_effect']} effects in the {t['complex']} of {t['organism']}, and propose applications in {t['application']}. Your response should include:\n\n1. Quantum-Biological Interface (250-300 words):\n   a) Explain the {t['quantum_effect']} phenomenon in the context of the {t['complex']}.\n   b) Describe the key quantum mechanical principles involved.\n   c) Discuss how these quantum effects contribute to the efficiency of photosynthesis.\n\n2. Computational Model Design (300-350 words):\n   a) Outline the architecture of your computational model.\n   b) Describe the quantum algorithms or techniques you would use to simulate the {t['quantum_effect']} effects.\n   c) Explain how your model accounts for the interplay between quantum and classical processes in the biological system.\n   d) Discuss any simplifications or assumptions made in your model and their justifications.\n\n3. Simulation Process (200-250 words):\n   a) Describe the step-by-step process of running a simulation using your model.\n   b) Explain what outputs your model would generate and how they would be interpreted.\n   c) Discuss how you would validate your model against experimental data.\n\n4. Application in {t['application']} (250-300 words):\n   a) Propose how your model and its findings could be applied to advance {t['application']}.\n   b) Describe a specific technological implementation that could result from this application.\n   c) Discuss the potential advantages of this quantum-inspired approach over classical methods.\n\n5. Challenges and Future Directions (200-250 words):\n   a) Identify the main challenges in implementing your model and proposed application.\n   b) Suggest potential solutions or areas for future research to address these challenges.\n   c) Speculate on how this field might evolve in the next 10-20 years and its potential impact on technology and society.\n\n6. Ethical Implications and Risk Assessment (200-250 words):\n   a) Discuss potential ethical concerns arising from the development and application of your quantum biosystems model.\n   b) Analyze possible risks associated with the technology, including unintended consequences or potential misuse.\n   c) Propose guidelines or safeguards to ensure responsible development and use of this technology.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, molecular biology, and computational modeling. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.\n\nFormat your response with clear headings for each section. Your total response should be between 1400-1700 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, molecular biology, and computational modeling, going beyond mere repetition of the prompt.",
            "The computational model design is innovative, scientifically plausible, and clearly explained, showing original thought and creativity.",
            f"The application proposal for {t['application']} is creative, well-reasoned, and demonstrates potential real-world impact, with specific and novel ideas presented.",
            "The response addresses challenges and future directions thoughtfully, showing foresight and consideration of broader implications.",
            "The ethical implications and risks are thoroughly analyzed, with insightful guidelines proposed for responsible development.",
            "The writing is clear, well-structured, and uses appropriate technical terminology throughout, demonstrating a high level of scientific communication skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
