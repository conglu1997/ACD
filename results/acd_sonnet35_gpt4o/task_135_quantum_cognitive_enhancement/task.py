import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_enhancements = [
            {
                "name": "Quantum Memory Amplification",
                "description": "A technology that uses quantum entanglement to enhance human memory capacity and recall speed."
            },
            {
                "name": "Superposition Decision Making",
                "description": "A neural implant that leverages quantum superposition to simultaneously process multiple decision pathways."
            },
            {
                "name": "Quantum Emotional Regulation",
                "description": "A non-invasive device that uses quantum fields to modulate neurotransmitter activity for precise emotional control."
            },
            {
                "name": "Entangled Creativity Booster",
                "description": "A quantum-based system that connects multiple minds through entanglement to enhance collaborative creativity."
            }
        ]
        return {str(i+1): enhancement for i, enhancement in enumerate(random.sample(cognitive_enhancements, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical quantum-based cognitive enhancement technology: {t['name']}. {t['description']}

Your task is to:

1. Quantum Mechanism (100-150 words):
   Explain the theoretical quantum mechanism behind this technology. How does it interact with the brain to produce the desired cognitive enhancement? Include at least two specific quantum principles in your explanation.

2. Cognitive Effects (100-150 words):
   Describe the primary and secondary effects of this enhancement on human cognition. How does it alter thought processes, decision-making, or other cognitive functions? Discuss both potential benefits and risks.

3. Neuroscientific Implications (100-150 words):
   Analyze how this technology might change our understanding of the brain and consciousness. Propose a specific neuroscientific research question that this technology could help answer.

4. Ethical Considerations (100-150 words):
   Discuss two major ethical issues arising from the use of this technology. Consider concepts such as cognitive liberty, fairness, and potential societal divides.

5. Societal Impact (100-150 words):
   Speculate on how widespread adoption of this technology might change society. Consider impacts on education, workforce, social interactions, or governance.

6. Technological Limitations (50-100 words):
   Identify at least one major technological hurdle that needs to be overcome for this enhancement to be realized. Suggest a potential approach to addressing this challenge.

7. Interdisciplinary Connections (50-100 words):
   Draw a connection between this quantum cognitive enhancement and another scientific or philosophical field not yet mentioned. How might insights from that field inform the development or understanding of this technology?

Ensure your response is creative yet grounded in current scientific understanding. Demonstrate clear reasoning about the potential implications and challenges of such a transformative technology.

Use clear headings for each section of your response. Your total response should be between 800-1000 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent description of a quantum-based cognitive enhancement technology named {t['name']}",
            "The explanation of the quantum mechanism is scientifically grounded and incorporates at least two specific quantum principles",
            "The cognitive effects are logically derived from the proposed mechanism and include both benefits and risks",
            "The neuroscientific implications are insightful and include a specific, relevant research question",
            "The ethical considerations are well-reasoned and explore significant moral issues",
            "The societal impact analysis is thoughtful and considers multiple aspects of society",
            "A plausible technological limitation is identified, with a suggested approach for addressing it",
            "An interesting interdisciplinary connection is drawn that is relevant to the proposed technology",
            "The overall response demonstrates both scientific understanding and creative, speculative thinking",
            "The response follows the specified format, uses clear headings for each section, and adheres to the 800-1000 word count guideline"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
