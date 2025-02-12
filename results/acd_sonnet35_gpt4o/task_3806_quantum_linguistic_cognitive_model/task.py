import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_phenomena = [
            "metaphor comprehension",
            "semantic ambiguity resolution",
            "syntactic parsing",
            "pragmatic inference"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "interference",
            "measurement"
        ]
        cognitive_processes = [
            "working memory",
            "attention allocation",
            "concept formation",
            "decision making"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "linguistic_phenomenon": random.choice(linguistic_phenomena),
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired computational model of language processing that incorporates principles from quantum computing and cognitive linguistics to simulate and analyze complex language phenomena. Focus on the linguistic phenomenon of {t['linguistic_phenomenon']}, utilizing the quantum principle of {t['quantum_principle']}, and considering the cognitive process of {t['cognitive_process']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen linguistic phenomenon and its challenges in traditional computational models.
   b) Describe how the specified quantum principle can be applied to language processing.
   c) Discuss the role of the given cognitive process in language understanding and production.
   d) Propose a novel theoretical framework that integrates these three elements.

2. Quantum-Linguistic Model Architecture (300-350 words):
   a) Design a computational architecture that implements your theoretical framework.
   b) Explain how your model represents linguistic structures using quantum-inspired formalisms.
   c) Describe how the model simulates the specified cognitive process.
   d) Provide a high-level diagram or pseudocode of your model's key components and their interactions (describe this textually).

3. Simulation and Analysis (250-300 words):
   a) Describe how your model would simulate the chosen linguistic phenomenon.
   b) Explain the expected outcomes and how they differ from classical computational models.
   c) Propose methods to validate your model against empirical linguistic and cognitive data.
   d) Discuss potential insights your model could provide about language processing and cognition.

4. Quantum Advantage Analysis (200-250 words):
   a) Analyze the potential advantages of your quantum-inspired approach over classical models.
   b) Discuss any limitations or challenges in implementing your model.
   c) Explain how your model might handle linguistic phenomena not typically addressed by classical approaches.

5. Interdisciplinary Implications (200-250 words):
   a) Discuss the implications of your model for our understanding of language, cognition, and quantum systems.
   b) Explore potential applications in fields such as natural language processing, cognitive science, and quantum computing.
   c) Propose future research directions that could extend or refine your model.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to quantum-inspired models of cognition and language.
   b) Discuss the implications of your model for understanding human cognition and consciousness.
   c) Propose guidelines for responsible development and application of quantum-linguistic models.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive linguistics, and computational modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Use appropriate subheadings (a, b, c, d) within each section as outlined. Your total response should be between 1350-1650 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified linguistic phenomenon, quantum principle, and cognitive process.",
            "The proposed quantum-linguistic model is innovative, well-explained, and integrates concepts from quantum computing, linguistics, and cognitive science.",
            "The simulation and analysis section provides clear and plausible predictions about how the model would perform.",
            "The response addresses potential advantages, limitations, and ethical considerations of the proposed model.",
            "The writing is clear, well-structured, and uses appropriate technical terminology from all relevant fields.",
            "The response follows the specified format with clear headings and subheadings, and includes a word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
