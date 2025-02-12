import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Quantum entanglement",
            "Quantum superposition",
            "Quantum tunneling",
            "Quantum decoherence",
            "Quantum teleportation"
        ]
        philosophical_concepts = [
            "Free will",
            "The nature of reality",
            "Consciousness",
            "Personal identity",
            "The concept of time"
        ]
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "philosophical_concept": random.choice(philosophical_concepts)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "philosophical_concept": random.choice(philosophical_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a thought experiment that explores the intersection of {t['quantum_concept']} and the philosophical concept of {t['philosophical_concept']}. Then, analyze its implications for our understanding of reality and consciousness. Your response should include:

1. Thought Experiment Design (300-350 words):
   a) Describe your thought experiment in detail, explaining how it incorporates both {t['quantum_concept']} and {t['philosophical_concept']}.
   b) Explain the key components and mechanisms of your thought experiment.
   c) Discuss how your thought experiment challenges or extends current understanding of either or both concepts.

2. Quantum Information Analysis (250-300 words):
   a) Analyze how information is processed, stored, or transmitted in your thought experiment from a quantum perspective.
   b) Explain any quantum information paradoxes or unique phenomena that arise in your thought experiment.
   c) Discuss how classical information theory might be insufficient to fully describe the information dynamics in your experiment.

3. Philosophical Implications (250-300 words):
   a) Explore the philosophical implications of your thought experiment, focusing on {t['philosophical_concept']}.
   b) Discuss how your thought experiment might challenge or support existing philosophical theories related to {t['philosophical_concept']}.
   c) Propose a new philosophical insight or question that arises from your thought experiment.

4. Consciousness and Reality (200-250 words):
   a) Analyze how your thought experiment might influence our understanding of consciousness.
   b) Discuss potential implications for our perception of reality.
   c) Explore any paradoxes or counterintuitive conclusions that arise from your analysis.

5. Experimental Approach (150-200 words):
   a) Propose a hypothetical experimental setup that could test or validate aspects of your thought experiment.
   b) Discuss the technical challenges and limitations of implementing such an experiment.
   c) Suggest how advances in quantum computing or other technologies might enable future testing of your ideas.

6. Interdisciplinary Connections (150-200 words):
   a) Explore how your thought experiment might impact or be applied in fields beyond physics and philosophy (e.g., cognitive science, computer science, or neurobiology).
   b) Discuss potential technological applications or innovations that could arise from your thought experiment.

Ensure your response demonstrates a deep understanding of both quantum mechanics and philosophy. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and original in your approach while maintaining scientific and philosophical rigor.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The thought experiment clearly incorporates both {t['quantum_concept']} and {t['philosophical_concept']}.",
            "The response includes a detailed analysis of quantum information processing in the thought experiment.",
            "The philosophical implications of the thought experiment are thoroughly explored.",
            "The response discusses the impact on our understanding of consciousness and reality.",
            "A hypothetical experimental approach is proposed to test aspects of the thought experiment.",
            "The response explores interdisciplinary connections and potential applications.",
            "The response demonstrates a deep understanding of both quantum mechanics and philosophy.",
            "The thought experiment and analysis are creative and original while maintaining scientific and philosophical rigor.",
            "The response is well-structured with clear headings for each required section.",
            "The total response is between 1300-1600 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
