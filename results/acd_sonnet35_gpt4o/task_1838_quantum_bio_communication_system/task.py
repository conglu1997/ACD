import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Quantum Entanglement",
            "Quantum Superposition",
            "Quantum Tunneling"
        ]
        biological_structures = [
            "Mitochondria",
            "Cell Membrane",
            "Nucleus"
        ]
        communication_goals = [
            "Intercellular Signaling",
            "Intracellular Information Processing",
            "Environmental Sensing"
        ]
        
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_structure": random.choice(biological_structures),
                "communication_goal": random.choice(communication_goals)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "biological_structure": random.choice(biological_structures),
                "communication_goal": random.choice(communication_goals)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-biological communication system that could operate within living cells, integrating principles from quantum physics, information theory, and cellular biology. Your system should focus on the following specifications:

Quantum Principle: {t['quantum_principle']}
Biological Structure: {t['biological_structure']}
Communication Goal: {t['communication_goal']}

Your response should include the following sections:

1. Theoretical Foundation (250-300 words):
   a) Explain the key concepts of the specified quantum principle and how it relates to information theory.
   b) Describe the relevant aspects of the given biological structure and its role in cellular communication.
   c) Discuss how these elements could be integrated to achieve the specified communication goal.

2. System Design (300-350 words):
   a) Outline the main components of your quantum-biological communication system.
   b) Explain how your system would harness the quantum principle within the biological structure.
   c) Describe the mechanism by which your system would encode, transmit, and decode information.
   d) Address how your system would maintain quantum effects in a noisy cellular environment.

3. Theoretical Performance Analysis (200-250 words):
   a) Estimate the potential information capacity of your system, using appropriate units and comparisons.
   b) Discuss the theoretical speed and efficiency of your communication system.
   c) Compare your system's capabilities to existing biological communication mechanisms.

4. Challenges and Limitations (150-200 words):
   a) Identify potential obstacles in implementing your system in living cells.
   b) Discuss any theoretical limitations of your approach.
   c) Propose potential solutions or areas for future research to address these challenges.

5. Implications and Applications (200-250 words):
   a) Explore potential applications of your quantum-biological communication system in fields such as medicine, biotechnology, or computing.
   b) Discuss how your system might enhance our understanding of quantum effects in biological systems.
   c) Consider any ethical implications or potential risks associated with this technology.

6. Experimental Proposal (150-200 words):
   a) Design a hypothetical experiment to test a key aspect of your quantum-biological communication system.
   b) Describe the experimental setup, methodology, and expected results.
   c) Discuss how this experiment could validate or refine your theoretical model.

Ensure your response demonstrates a deep understanding of quantum physics, cellular biology, and information theory. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of the specified quantum principle, biological structure, and communication goal.",
            "The proposed quantum-biological communication system is innovative and scientifically plausible.",
            "The theoretical performance analysis is well-reasoned and uses appropriate scientific concepts and units.",
            "The challenges, limitations, and potential applications are thoughtfully considered and discussed.",
            "The experimental proposal is well-designed and relevant to validating the theoretical model.",
            "The response shows a high level of interdisciplinary integration between quantum physics, biology, and information theory."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
