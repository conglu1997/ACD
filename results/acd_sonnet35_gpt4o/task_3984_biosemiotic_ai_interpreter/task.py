import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        species_pairs = [
            ('honeybees', 'plants'),
            ('dolphins', 'humans'),
            ('ants', 'fungi'),
            ('bacteria', 'human gut')
        ]
        return {
            "1": {"species_pair": random.choice(species_pairs)},
            "2": {"species_pair": random.choice(species_pairs)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        species1, species2 = t['species_pair']
        return f"""Design an AI system capable of interpreting and generating biosemiotic signals between {species1} and {species2}, then use it to propose novel interspecies communication methods. Your response should include:

1. Biosemiotic Analysis (200-250 words):
   a) Describe the key biosemiotic signals used by {species1} and {species2}.
   b) Explain how these signals function within each species' ecosystem.
   c) Discuss any existing interactions or communication between the two species.

2. AI System Architecture (250-300 words):
   a) Describe the overall structure of your AI system for interpreting biosemiotic signals.
   b) Explain how your system processes and analyzes signals from each species.
   c) Detail the mechanisms for generating novel biosemiotic signals.
   d) Include a diagram or pseudocode representation of your system's architecture.

3. Signal Interpretation Process (200-250 words):
   a) Walk through how your AI system would interpret a specific biosemiotic signal from each species.
   b) Explain how the system handles ambiguity or context-dependent meanings.
   c) Discuss how your system validates its interpretations.

4. Novel Interspecies Communication (250-300 words):
   a) Propose a method for facilitating communication between {species1} and {species2} using your AI system.
   b) Describe a specific scenario where this communication could be beneficial.
   c) Explain how your system would generate and interpret signals in this scenario.
   d) Discuss potential challenges and limitations of your proposed method.

5. Ethical and Ecological Implications (150-200 words):
   a) Discuss the potential ecological impacts of enabling interspecies communication.
   b) Address ethical concerns related to manipulating or interfering with natural communication systems.
   c) Propose guidelines for responsible development and use of biosemiotic AI systems.

6. Future Research Directions (150-200 words):
   a) Suggest two specific research directions to enhance your system's capabilities.
   b) Discuss potential applications of biosemiotic AI beyond interspecies communication.
   c) Speculate on how this technology might influence our understanding of cognition and communication in non-human species.

Ensure your response demonstrates a deep understanding of biosemiotics, artificial intelligence, and the biology of the specified species. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        species1, species2 = t['species_pair']
        criteria = [
            f"The response demonstrates a deep understanding of biosemiotics and the communication systems of {species1} and {species2}.",
            "The AI system architecture is innovative, well-explained, and plausible given current AI capabilities.",
            "The proposed interspecies communication method is creative, scientifically grounded, and addresses potential challenges.",
            "Ethical and ecological implications are thoroughly considered, with thoughtful guidelines proposed.",
            "The response shows interdisciplinary integration of biology, semiotics, and artificial intelligence concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
