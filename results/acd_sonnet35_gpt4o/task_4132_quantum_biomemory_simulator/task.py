import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_effect": "quantum coherence",
                "brain_region": "hippocampus",
                "memory_type": "episodic memory"
            },
            {
                "quantum_effect": "quantum entanglement",
                "brain_region": "prefrontal cortex",
                "memory_type": "working memory"
            },
            {
                "quantum_effect": "quantum tunneling",
                "brain_region": "amygdala",
                "memory_type": "emotional memory"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-biological model for memory formation and retrieval in the brain, focusing on the quantum effect of {t['quantum_effect']} in the {t['brain_region']}, specifically for {t['memory_type']}. Then, create a simulation to test its predictions against classical neuroscience models. Your response should include:

1. Quantum-Biological Model (300-350 words):
   a) Describe the key components of your quantum-biological memory model.
   b) Explain how {t['quantum_effect']} is incorporated into the memory processes in the {t['brain_region']}.
   c) Detail the mechanisms for memory formation and retrieval in your model.
   d) Discuss how your model differs from classical neuroscience models of {t['memory_type']}.

2. Simulation Design (250-300 words):
   a) Outline the architecture of your simulation, including key variables and parameters.
   b) Explain how you will model {t['quantum_effect']} computationally.
   c) Describe how your simulation will represent the neural structures of the {t['brain_region']}.
   d) Discuss any novel algorithms or techniques you'll use to simulate quantum effects in a biological context.

3. Experimental Setup (200-250 words):
   a) Propose a specific experiment to test your quantum-biological model against classical models.
   b) Describe the input data, control conditions, and output measurements for your experiment.
   c) Explain how your experiment specifically targets {t['memory_type']} processes.

4. Predictions and Hypotheses (200-250 words):
   a) State clear, testable hypotheses about how your quantum-biological model will perform compared to classical models.
   b) Predict potential differences in memory formation or retrieval processes.
   c) Discuss any unique phenomena or effects you expect to observe due to the quantum nature of your model.

5. Analysis and Interpretation (250-300 words):
   a) Describe your methods for analyzing the simulation results.
   b) Explain how you will compare the performance of your quantum-biological model to classical models.
   c) Discuss potential implications of your results for our understanding of {t['memory_type']} and quantum effects in the brain.
   d) Address possible limitations of your model and simulation.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using quantum-biological models to study human memory.
   b) Propose potential applications of your model in neuroscience or cognitive enhancement.
   c) Suggest future experiments or extensions of your work.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and computational modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a quantum-biological model incorporating {t['quantum_effect']} in the {t['brain_region']} for {t['memory_type']}",
            "The response should describe a simulation design to test the quantum-biological model",
            "The response should propose a specific experiment to compare the quantum-biological model with classical models",
            "The response should state clear, testable hypotheses and predictions",
            "The response should include methods for analyzing and interpreting simulation results",
            "The response should discuss ethical considerations and future directions",
            "The response should demonstrate understanding of quantum mechanics, neuroscience, and computational modeling",
            "The response should be innovative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
