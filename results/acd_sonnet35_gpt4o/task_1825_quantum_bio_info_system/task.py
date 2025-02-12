import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "component": "DNA",
                "quantum_property": "superposition",
                "info_process": "error correction"
            },
            {
                "component": "protein",
                "quantum_property": "entanglement",
                "info_process": "signal transduction"
            },
            {
                "component": "cell membrane",
                "quantum_property": "tunneling",
                "info_process": "selective permeability"
            },
            {
                "component": "mitochondria",
                "quantum_property": "coherence",
                "info_process": "energy transfer"
            }
        ]
        
        tasks = {}
        selected_scenarios = random.sample(scenarios, 2)
        for i, scenario in enumerate(selected_scenarios, 1):
            tasks[str(i)] = scenario
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-biological information processing system that could exist within living cells, focusing on the following elements:

Biological Component: {t['component']}
Quantum Property: {t['quantum_property']}
Information Process: {t['info_process']}

Your response should include:

1. System Design (250-300 words):
   a) Describe the overall structure and function of your quantum-biological system.
   b) Explain how it incorporates the specified biological component, quantum property, and information process.
   c) Detail the theoretical mechanisms by which quantum effects could manifest in this biological context.

2. Quantum-Biological Interface (200-250 words):
   a) Explain how your system bridges the gap between quantum and biological scales.
   b) Describe how the specified quantum property enhances or enables the given information process.
   c) Discuss any challenges in maintaining quantum effects in a biological environment and how your system addresses them.

3. Information Processing Mechanism (200-250 words):
   a) Provide a step-by-step explanation of how information is processed in your system.
   b) Describe how this mechanism differs from classical biological information processing.
   c) Explain any unique capabilities or advantages provided by the quantum-biological integration.

4. Theoretical Implications (150-200 words):
   a) Discuss the potential implications of your system for our understanding of biology, quantum physics, or information theory.
   b) Propose a hypothesis about how this system might affect cellular function or evolution.
   c) Suggest potential applications or future research directions based on your design.

5. Experimental Approach (150-200 words):
   a) Propose an experimental setup that could potentially detect or verify the quantum effects in your biological system.
   b) Describe the expected results and how they would support your theoretical model.
   c) Discuss any technical challenges in implementing such an experiment.

Ensure your response demonstrates a deep understanding of quantum physics, molecular biology, and information theory. Be creative and speculative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics, molecular biology, and information theory",
            "The proposed system creatively integrates the specified biological component, quantum property, and information process",
            "The explanation of the quantum-biological interface is scientifically plausible and well-reasoned",
            "The information processing mechanism is clearly described and highlights unique quantum advantages",
            "The theoretical implications and experimental approach are insightful and demonstrate advanced scientific thinking",
            "The response is well-structured, within the specified word limit, and uses technical terminology appropriately"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
