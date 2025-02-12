import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "organ donation decision",
            "environmental policy implementation",
            "AI development regulation",
            "global wealth redistribution",
            "space colonization ethics"
        ]
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum interference",
            "quantum measurement"
        ]
        return {
            "1": {
                "scenario": random.choice(scenarios),
                "quantum_principle": random.choice(quantum_principles)
            },
            "2": {
                "scenario": random.choice(scenarios),
                "quantum_principle": random.choice(quantum_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses quantum computing principles to model and simulate human cognitive dissonance, then apply it to the complex ethical decision-making scenario of {t['scenario']}. Your system should specifically incorporate the quantum principle of {t['quantum_principle']}. Your response should include the following sections:

1. Quantum-Cognitive Architecture (300-350 words):
   a) Describe the overall structure of your AI system for modeling cognitive dissonance.
   b) Explain how you integrate quantum computing principles, particularly {t['quantum_principle']}, into your cognitive model.
   c) Detail how your system represents and processes conflicting beliefs or attitudes.
   d) Discuss how quantum effects might contribute to modeling the uncertainty and complexity of cognitive dissonance.

2. Cognitive Dissonance Simulation (250-300 words):
   a) Explain how your system simulates the experience of cognitive dissonance.
   b) Describe how it models the tension between conflicting cognitions and the drive for consistency.
   c) Detail how quantum effects enhance the simulation of cognitive dissonance compared to classical approaches.
   d) Provide a specific example of how your system would model a simple case of cognitive dissonance.

3. Ethical Scenario Analysis (250-300 words):
   a) Apply your quantum cognitive dissonance model to the {t['scenario']} scenario.
   b) Describe how your system would represent the conflicting values or beliefs in this scenario.
   c) Explain how the quantum aspects of your model contribute to a more nuanced understanding of the ethical dilemma.
   d) Discuss any novel insights or predictions your model generates about decision-making in this scenario.

4. Quantum-Classical Comparison (200-250 words):
   a) Compare your quantum-inspired approach to traditional classical AI models of decision-making.
   b) Discuss potential advantages and limitations of your quantum cognitive model.
   c) Propose an experiment to test whether your quantum model outperforms classical approaches in predicting human behavior in cognitive dissonance situations.

5. Ethical and Philosophical Implications (200-250 words):
   a) Discuss the ethical implications of using quantum AI systems to model human cognition.
   b) Explore how your system might impact our understanding of free will, consciousness, and decision-making.
   c) Propose guidelines for the responsible development and use of quantum cognitive AI systems.

6. Future Developments and Applications (150-200 words):
   a) Suggest two potential improvements or extensions to your quantum cognitive dissonance AI system.
   b) Propose a novel application of your system in a field other than ethics (e.g., healthcare, education, or business).
   c) Discuss any technical or conceptual challenges that need to be overcome for further advancement in this area.

Ensure your response demonstrates a deep understanding of quantum computing, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing principles, cognitive science, and artificial intelligence.",
            "The proposed AI system integrates quantum computing and cognitive modeling in a novel and plausible way.",
            "The application of the system to the given ethical scenario is thorough and insightful.",
            "The comparison between quantum and classical approaches is well-reasoned and balanced.",
            "The ethical and philosophical implications are thoughtfully considered.",
            "The response is well-structured, coherent, and adheres to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
