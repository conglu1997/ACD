import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_aspects = [
            {"aspect": "self-awareness", "quantum_principle": "superposition"},
            {"aspect": "qualia", "quantum_principle": "entanglement"},
            {"aspect": "free will", "quantum_principle": "quantum tunneling"},
            {"aspect": "subjective experience", "quantum_principle": "wave function collapse"},
            {"aspect": "unity of consciousness", "quantum_principle": "quantum coherence"}
        ]
        return {str(i+1): aspect for i, aspect in enumerate(random.sample(consciousness_aspects, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to simulate the consciousness aspect of {t['aspect']} using the quantum principle of {t['quantum_principle']}. Then, analyze its philosophical and ethical implications. Your response should include:

1. Quantum Simulation Design (250-300 words):
   a) Explain how the chosen consciousness aspect can be modeled using quantum computing.
   b) Describe how the specified quantum principle is utilized in your simulation.
   c) Outline the key components and processes of your quantum computing system.
   d) Discuss any novel approaches or algorithms your system employs to address the challenges of consciousness simulation.

2. Theoretical Framework (200-250 words):
   a) Provide a brief overview of relevant theories of consciousness that inform your simulation design.
   b) Explain how quantum mechanics might contribute to our understanding of {t['aspect']}.
   c) Discuss any assumptions or simplifications made in your model and their potential impact on the simulation's validity.

3. Technical Implementation (200-250 words):
   a) Describe the quantum circuits or algorithms used in your simulation.
   b) Explain how classical and quantum components of your system interact.
   c) Discuss any technical challenges in implementing this simulation and propose solutions.

4. Philosophical Implications (200-250 words):
   a) Analyze how your quantum simulation of {t['aspect']} might inform philosophical debates about consciousness.
   b) Discuss the implications of your model for the relationship between mind and matter.
   c) Consider how this simulation might impact our understanding of artificial consciousness or machine sentience.

5. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues arising from simulating aspects of consciousness.
   b) Discuss the ethical implications of creating systems that might be considered partially conscious.
   c) Propose guidelines for the responsible development and use of consciousness-simulating quantum systems.

6. Experimental Proposal (150-200 words):
   a) Design an experiment to test a hypothesis about consciousness using your quantum simulation.
   b) Explain how you would measure or verify the presence of {t['aspect']} in your simulation.
   c) Discuss potential outcomes and their interpretations.

Ensure your response demonstrates a deep understanding of quantum computing, theories of consciousness, and ethical reasoning. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of how to simulate the consciousness aspect of {t['aspect']} using the quantum principle of {t['quantum_principle']}.",
            "The quantum simulation design should be innovative, logically consistent, and well-explained, integrating principles from quantum computing and theories of consciousness.",
            "The response should thoughtfully address philosophical implications and ethical considerations of simulating consciousness.",
            "The experimental proposal should be well-designed and relevant to testing hypotheses about consciousness using the quantum simulation."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
