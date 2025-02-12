import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "quantum_concept": "superposition",
                "cognitive_process": "decision-making under uncertainty"
            },
            {
                "quantum_concept": "entanglement",
                "cognitive_process": "memory formation and retrieval"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework and experimental setup to investigate potential quantum effects in human cognition, focusing on the quantum concept of {t['quantum_concept']} and its possible role in the cognitive process of {t['cognitive_process']}. Your task has four parts:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen quantum concept and its potential relevance to the specified cognitive process.
   b) Propose a hypothesis for how this quantum phenomenon might influence or manifest in human cognition.
   c) Describe the key components of your theoretical model, including any mathematical or conceptual representations.

2. Experimental Design (250-300 words):
   a) Outline a detailed experimental setup to test your hypothesis.
   b) Describe the methodology, including participant selection, experimental conditions, and control measures.
   c) Explain how your experiment isolates and measures the proposed quantum effect in cognition.
   d) Address potential confounding factors and how you would control for them.

3. Data Analysis and Interpretation (200-250 words):
   a) Describe the types of data you expect to collect from your experiment.
   b) Explain the statistical or analytical methods you would use to process this data.
   c) Discuss how you would interpret different possible outcomes in relation to your hypothesis.
   d) Address potential alternative explanations for your findings.

4. Implications and Future Directions (150-200 words):
   a) Discuss the potential implications of your findings for our understanding of human cognition.
   b) Explain how your research might impact fields such as psychology, neuroscience, or artificial intelligence.
   c) Propose two follow-up studies or extensions of your research.

Ensure your response demonstrates a deep understanding of both quantum mechanics and cognitive science. Be creative and speculative in your approach while maintaining scientific rigor and plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 850-1050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum concept and cognitive process.",
            "The theoretical framework is well-developed, coherent, and scientifically plausible.",
            "The experimental design is detailed, feasible, and appropriately controls for confounding factors.",
            "The data analysis plan is comprehensive and aligned with the experimental design.",
            "The discussion of implications and future directions is insightful and demonstrates broad interdisciplinary thinking.",
            "The response is creative and original while maintaining scientific rigor."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
