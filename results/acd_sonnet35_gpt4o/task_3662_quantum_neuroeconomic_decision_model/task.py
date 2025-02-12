import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "interference"
        ]
        decision_contexts = [
            "financial investment",
            "health care choices",
            "environmental policy"
        ]
        brain_regions = [
            "prefrontal cortex",
            "amygdala",
            "anterior cingulate cortex"
        ]
        tasks = {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "decision_context": random.choice(decision_contexts),
                "brain_region": random.choice(brain_regions)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "decision_context": random.choice(decision_contexts),
                "brain_region": random.choice(brain_regions)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum-inspired neuroeconomic model of decision-making under uncertainty, focusing on {t['decision_context']} decisions. Your model should incorporate the quantum principle of {t['quantum_principle']} and consider the role of the {t['brain_region']} in the decision-making process. Your response should include the following sections:

1. Model Overview (250-300 words):
   a) Describe the key components of your quantum-inspired neuroeconomic model.
   b) Explain how it incorporates the specified quantum principle into decision-making processes.
   c) Discuss how your model accounts for the role of the given brain region.
   d) Provide a high-level mathematical or conceptual representation of your model.

2. Quantum-Neuroeconomic Integration (200-250 words):
   a) Explain the theoretical basis for applying {t['quantum_principle']} to {t['decision_context']} decisions.
   b) Describe how this integration could potentially outperform classical decision-making models.
   c) Discuss any challenges in implementing this quantum-inspired approach in neuroeconomics.

3. Neural Basis and Predictions (200-250 words):
   a) Describe how the {t['brain_region']} contributes to decision-making in your model.
   b) Explain how quantum effects might manifest in neural activity.
   c) Make specific predictions about neural activity patterns based on your model.

4. Experimental Design (250-300 words):
   a) Propose an experimental paradigm to test your model's predictions.
   b) Describe the behavioral tasks participants would perform.
   c) Explain how you would collect and analyze neural data (e.g., fMRI, EEG) in the context of your model.
   d) Discuss how you would distinguish quantum effects from classical decision-making processes.

5. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your model for understanding human decision-making.
   b) Propose two specific applications of your model in real-world scenarios.
   c) Explain how these applications could benefit from the quantum-inspired approach.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical implications of your quantum-inspired neuroeconomic model.
   b) Propose guidelines for responsible development and use of this approach in decision-making research and applications.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and economic decision-making theories. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, neuroscience, and economic decision-making theories",
            "The proposed model innovatively integrates quantum principles with neuroeconomic concepts",
            "The explanation of how the model incorporates the specified brain region is clear and plausible",
            "The experimental design effectively tests the model's predictions and distinguishes quantum effects",
            "The discussion of implications and applications is insightful and relevant",
            "The ethical considerations are thoughtfully addressed",
            "The overall response is creative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
