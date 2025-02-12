import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum coherence"
        ]
        genetic_elements = [
            "DNA base pairs",
            "RNA codons",
            "amino acids",
            "protein folding"
        ]
        linguistic_challenges = [
            "universal translation",
            "semantic ambiguity resolution",
            "context-dependent meaning extraction",
            "natural language generation"
        ]
        
        tasks = [
            {
                "quantum_principle": random.choice(quantum_principles),
                "genetic_element": random.choice(genetic_elements),
                "linguistic_challenge": random.choice(linguistic_challenges)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-biological hybrid system for information processing and communication based on the principles of quantum computing and the genetic code, then apply it to solve a complex linguistic challenge. Your system should incorporate the quantum principle of {t['quantum_principle']}, utilize the genetic element of {t['genetic_element']}, and address the linguistic challenge of {t['linguistic_challenge']}. Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum-biolinguistic processor.
   b) Explain how your system integrates quantum computing principles with biological information processing.
   c) Detail how you incorporate {t['quantum_principle']} and {t['genetic_element']} into your design.
   d) Discuss any novel concepts or technologies you've invented for this system.
   e) Provide a schematic representation of your system architecture (describe it in words).

2. Information Processing Mechanism (250-300 words):
   a) Explain how information is encoded, processed, and stored in your quantum-biological hybrid system.
   b) Describe how {t['quantum_principle']} enhances the information processing capabilities.
   c) Detail how {t['genetic_element']} is utilized in the information processing mechanism.
   d) Discuss any advantages your system might have over classical computing or biological systems.

3. Application to Linguistic Challenge (250-300 words):
   a) Explain how your quantum-biolinguistic processor addresses the challenge of {t['linguistic_challenge']}.
   b) Provide a step-by-step description of how your system would process and solve a specific example within this linguistic challenge.
   c) Discuss potential advantages of your approach compared to traditional computational linguistics methods.

4. Theoretical Implementation (200-250 words):
   a) Describe the theoretical physical or biological substrate required for your system.
   b) Explain how your system might be realized using current or near-future technologies.
   c) Discuss any significant technical or scientific challenges and propose potential solutions.

5. Implications and Future Directions (200-250 words):
   a) Analyze the potential impact of your quantum-biolinguistic processor on fields such as computational linguistics, artificial intelligence, and quantum biology.
   b) Discuss ethical considerations and potential societal implications of your system.
   c) Propose two future research directions or extensions of your quantum-biolinguistic processor.

Ensure your response demonstrates a deep understanding of quantum computing, molecular biology, and linguistics. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a quantum-biological hybrid system incorporating {t['quantum_principle']} and {t['genetic_element']}",
            f"The system should address the linguistic challenge of {t['linguistic_challenge']}",
            "The design should be scientifically plausible and clearly explained",
            "The response should demonstrate interdisciplinary knowledge integration across quantum computing, molecular biology, and linguistics",
            "The application to the linguistic challenge should be well-defined and logically incorporate both quantum and biological elements",
            "The implications and future directions should be thoughtfully addressed",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (1200-1450 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
