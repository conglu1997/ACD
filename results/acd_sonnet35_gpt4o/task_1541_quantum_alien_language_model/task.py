import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        alien_species = [
            {
                "name": "Quantum Entanglers",
                "cognitive_basis": "Quantum entanglement-based distributed cognition",
                "communication_mode": "Manipulation of quantum states"
            },
            {
                "name": "Probability Weavers",
                "cognitive_basis": "Superposition-based parallel processing",
                "communication_mode": "Quantum interference patterns"
            }
        ]
        return {
            "1": random.choice(alien_species),
            "2": random.choice(alien_species)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing-based language model for the {t['name']} alien species with {t['cognitive_basis']} and {t['communication_mode']}. Then, use this model to translate and analyze interspecies communication. Your response should include:

1. Quantum Language Model Design (300-350 words):
   a) Describe the key components of your quantum language model.
   b) Explain how it incorporates the alien species' cognitive basis and communication mode.
   c) Detail how quantum computing principles are used to process and generate language.
   d) Discuss how this model differs from classical NLP approaches.

2. Alien Cognition Representation (250-300 words):
   a) Explain how your model represents the alien species' non-human cognition.
   b) Describe any novel quantum data structures or algorithms used to model this cognition.
   c) Discuss potential challenges in accurately representing non-human thought processes.

3. Interspecies Translation Mechanism (250-300 words):
   a) Describe how your model would translate between human language and the alien species' communication.
   b) Provide a specific example of translating a simple human phrase into the alien language, explaining the quantum states involved.
   c) Discuss potential limitations or ambiguities in this translation process.

4. Communication Analysis (200-250 words):
   a) Explain how your model could be used to analyze patterns or structures in the alien communication.
   b) Propose a method for identifying semantic or pragmatic content in the quantum-based language.
   c) Discuss how this analysis could contribute to our understanding of non-human cognition and language.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical considerations of modeling and potentially altering alien cognition.
   b) Explore the philosophical implications of quantum-based language and cognition.
   c) Consider potential risks or benefits of developing such advanced interspecies communication technology.

6. Future Research Directions (150-200 words):
   a) Propose two potential applications of your quantum language model beyond interspecies communication.
   b) Suggest areas for future research to improve or expand the capabilities of your model.
   c) Discuss how this technology might contribute to our understanding of the relationship between quantum mechanics, cognition, and language.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles and their application to language modeling.",
            "The alien cognition representation is creative, plausible, and well-integrated with the quantum language model.",
            "The interspecies translation mechanism is clearly explained and includes a specific, well-reasoned example.",
            "The communication analysis approach is innovative and demonstrates potential for gaining insights into non-human cognition and language.",
            "The ethical and philosophical implications are thoughtfully considered and discussed.",
            "The proposed future research directions are novel and promising."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
