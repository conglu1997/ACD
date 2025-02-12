import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "quantum_principle": "Superposition",
                "linguistic_aspect": "Semantic ambiguity",
                "cognitive_domain": "Decision making"
            },
            {
                "quantum_principle": "Entanglement",
                "linguistic_aspect": "Syntactic dependencies",
                "cognitive_domain": "Memory formation"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-based language processing system that applies the quantum principle of {t['quantum_principle']} to the linguistic aspect of {t['linguistic_aspect']}, and analyze its potential impacts on {t['cognitive_domain']}. Your response should include:

1. Quantum-Linguistic System Design (250-300 words):
   a) Describe the key components of your quantum-based language processing system.
   b) Explain how {t['quantum_principle']} is applied to {t['linguistic_aspect']}.
   c) Discuss any novel features that distinguish it from classical language processing systems.
   d) Provide a high-level schematic or detailed description of the system's architecture.

2. Quantum Mechanism (200-250 words):
   a) Explain the theoretical quantum mechanism underlying your system.
   b) Describe how quantum states or operations are mapped to linguistic elements.
   c) Discuss any challenges in maintaining quantum coherence in a linguistic context and how you address them.

3. Linguistic Processing (200-250 words):
   a) Detail how your system processes language differently from classical systems.
   b) Provide an example of how a specific linguistic input would be processed.
   c) Explain any advantages or limitations of your quantum approach to {t['linguistic_aspect']}.

4. Cognitive Impact Analysis (250-300 words):
   a) Analyze how your system might impact {t['cognitive_domain']}.
   b) Discuss potential changes in language comprehension or production.
   c) Explore any ethical considerations or societal implications of your system.

5. Experimental Proposal (150-200 words):
   a) Design an experiment to test the effectiveness of your quantum-linguistic system.
   b) Describe the methodology, including how you would measure improvements in {t['cognitive_domain']}.
   c) Discuss potential challenges in experimentally validating a quantum-based cognitive system.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics, and cognitive science. Use technical terminology appropriately and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding and creative application of {t['quantum_principle']} to {t['linguistic_aspect']}.",
            f"The analysis of cognitive impacts on {t['cognitive_domain']} is thorough and scientifically grounded.",
            "The proposed system and its potential impacts are described in a clear, logical, and scientifically plausible manner.",
            "The response shows a deep integration of concepts from quantum physics, linguistics, and cognitive science.",
            "The experimental proposal is well-designed and addresses the challenges of testing a quantum-based cognitive system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
