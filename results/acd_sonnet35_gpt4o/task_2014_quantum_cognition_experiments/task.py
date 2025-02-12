import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        experiments = [
            {
                "cognitive_process": "Decision Making",
                "quantum_principle": "Superposition",
                "brain_region": "Prefrontal Cortex"
            },
            {
                "cognitive_process": "Memory Formation",
                "quantum_principle": "Entanglement",
                "brain_region": "Hippocampus"
            }
        ]
        return {str(i+1): experiment for i, experiment in enumerate(random.sample(experiments, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an experiment to detect potential quantum effects in human cognition, focusing on {t['cognitive_process']} and the quantum principle of {t['quantum_principle']} in the {t['brain_region']}. Then, explore the implications of your findings. Your response should follow this structure:

1. Experimental Design (300-350 words):
   a) Hypothesis: State your hypothesis about how {t['quantum_principle']} might influence {t['cognitive_process']}.
   b) Method: Describe a detailed experimental setup to test your hypothesis.
   c) Measurements: Explain the specific measurements you would take and how they relate to quantum effects.
   d) Controls: Address potential confounding factors and how you would control for them.

2. Data Analysis (200-250 words):
   a) Expected Data: Describe the data you expect to collect from your experiment.
   b) Analysis Methods: Explain how you would analyze this data to identify quantum signatures.
   c) Interpretation: Discuss how you would differentiate quantum effects from classical explanations.

3. Implications (300-350 words):
   a) Scientific Impact: Discuss how positive results would impact our understanding of cognition and consciousness.
   b) Technological Applications: Speculate on potential technologies that could arise from your research.
   c) Philosophical Considerations: Analyze how your findings might impact concepts of free will or the nature of consciousness.
   d) Ethical Concerns: Identify potential ethical issues arising from your research and its implications.

4. Limitations and Future Directions (150-200 words):
   a) Limitations: Discuss any limitations of your experimental design or potential challenges in implementation.
   b) Future Research: Propose next steps or follow-up studies to further explore quantum effects in cognition.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world implications.

Your total response should be between 950-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a well-formulated hypothesis linking {t['quantum_principle']} to {t['cognitive_process']}",
            "The experimental design is scientifically plausible and specifically addresses the stated hypothesis",
            "The data analysis section includes appropriate methods for identifying quantum signatures",
            "The implications section thoughtfully explores scientific, technological, philosophical, and ethical aspects",
            "The response demonstrates a clear understanding of both quantum mechanics and cognitive science",
            "The proposed experiment and analysis are innovative while remaining scientifically grounded",
            "The limitations and future directions are thoughtfully considered",
            "The response follows the specified format and is within the word count range (950-1150 words)"
        ]
        score = sum([eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria])
        return score / len(criteria)
