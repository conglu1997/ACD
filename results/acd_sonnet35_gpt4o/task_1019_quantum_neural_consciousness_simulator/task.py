import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "moral decision-making",
                "quantum_principle": "quantum superposition"
            },
            {
                "scenario": "creative problem-solving",
                "quantum_principle": "quantum entanglement"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing-based simulator that models consciousness and decision-making processes in the context of {t['scenario']}, using principles from neuroscience and quantum mechanics. Your simulator should incorporate the quantum principle of {t['quantum_principle']}. Provide your response in the following format:

1. Quantum Neural Architecture (250-300 words):
   a) Describe the key components of your quantum neural simulator.
   b) Explain how your model incorporates principles from neuroscience and quantum mechanics.
   c) Detail how you represent and simulate consciousness and decision-making processes.
   d) Explain how your model utilizes the specified quantum principle.

2. Consciousness Simulation (200-250 words):
   a) Describe how your model simulates key aspects of consciousness (e.g., self-awareness, subjective experience).
   b) Explain how quantum effects contribute to the emergence of consciousness in your model.
   c) Discuss any novel predictions your model makes about the nature of consciousness.

3. Decision-Making Process (200-250 words):
   a) Explain how your model simulates decision-making in the given scenario.
   b) Describe how quantum effects influence the decision-making process.
   c) Compare your quantum approach to classical models of decision-making.

4. Experimental Design (150-200 words):
   a) Propose an experiment to test a key prediction of your model.
   b) Describe the methodology and expected outcomes.
   c) Discuss potential challenges in verifying quantum effects in consciousness.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical implications of simulating consciousness and decision-making.
   b) Explore how your model might impact our understanding of free will and determinism.
   c) Address potential societal impacts of advanced quantum neural simulations.

Ensure your response demonstrates a deep understanding of neuroscience, quantum mechanics, and consciousness theories. Be innovative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide clear explanations for complex concepts.

Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neuroscience, quantum mechanics, and consciousness theories.",
            "The proposed quantum neural simulator is innovative, scientifically plausible, and effectively incorporates the specified quantum principle.",
            "The simulation of consciousness and decision-making processes is well-reasoned and considers both neuroscientific and quantum mechanical aspects.",
            "The experimental design is thoughtful and addresses the challenges of verifying quantum effects in consciousness.",
            "The ethical and philosophical implications are thoroughly explored and demonstrate critical thinking.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
