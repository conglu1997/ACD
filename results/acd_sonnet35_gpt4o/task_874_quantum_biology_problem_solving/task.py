import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "biological_process": "Photosynthesis",
                "quantum_concept": "Quantum coherence",
                "research_question": "How might quantum coherence contribute to the efficiency of energy transfer in photosynthetic systems?"
            },
            {
                "biological_process": "Enzyme catalysis",
                "quantum_concept": "Quantum tunneling",
                "research_question": "How could quantum tunneling explain the high efficiency of certain enzymatic reactions?"
            },
            {
                "biological_process": "Magnetoreception in birds",
                "quantum_concept": "Radical pair mechanism",
                "research_question": "How might the radical pair mechanism explain avian magnetoreception for navigation?"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the role of quantum mechanics in biological systems and propose a solution to a complex biological problem. Your task focuses on the biological process of {t['biological_process']} and the quantum concept of {t['quantum_concept']}. Address the following research question:

{t['research_question']}

Quantum biology is an emerging field that explores how quantum mechanical phenomena might play a role in biological processes. This interdisciplinary area combines principles from quantum physics, biology, and chemistry to investigate biological functions that cannot be fully explained by classical physics alone.

Your response should include:

1. Background (150-200 words):
   a) Explain the relevant biological process.
   b) Describe the key features of the quantum concept.
   c) Discuss why this particular quantum effect might be relevant to the biological process.

2. Hypothesis and Mechanism (200-250 words):
   a) Formulate a hypothesis that answers the research question.
   b) Propose a detailed mechanism by which the quantum effect could influence the biological process.
   c) Explain how this mechanism addresses any current gaps in our understanding of the process.

3. Experimental Design (200-250 words):
   a) Propose an experiment to test your hypothesis.
   b) Describe the methodology, including any specialized techniques or equipment needed.
   c) Explain how you would control for potential confounding factors.
   d) Discuss what results would support or refute your hypothesis.

4. Implications and Future Directions (150-200 words):
   a) Discuss the broader implications of your hypothesis for our understanding of quantum effects in biological systems.
   b) Propose two potential applications that could arise from this research.
   c) Suggest a future research direction that builds on your findings.

5. Interdisciplinary Connections (100-150 words):
   Explain how this research connects to at least two other scientific disciplines and how it might impact them.

Ensure your response demonstrates a deep understanding of both quantum mechanics and biology, as well as the ability to integrate these fields creatively. Use clear, scientifically accurate language and provide justifications for your proposals. Your total response should be between 800-1050 words.

Important: Throughout your response, cite relevant scientific literature to support your arguments and proposals. Use a consistent citation format (e.g., [Author, Year]) and include at least 5 citations from peer-reviewed sources."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both the biological process and the quantum concept",
            "The proposed mechanism logically connects the quantum effect to the biological process",
            "The experimental design is well-thought-out and addresses potential confounding factors",
            "The response shows creativity and originality in addressing the research question",
            "The implications and future directions are insightful and scientifically plausible",
            "The interdisciplinary connections are relevant and well-explained",
            "The response includes at least 5 relevant citations from peer-reviewed scientific literature"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0