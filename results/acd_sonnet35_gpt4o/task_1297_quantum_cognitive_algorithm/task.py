import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            'Working memory',
            'Attentional control'
        ]
        return {str(i+1): {'cognitive_process': process} for i, process in enumerate(cognitive_processes)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum algorithm that models the cognitive process of {t['cognitive_process']}. Your response should include:

1. Cognitive Process Analysis (150-200 words):
   a) Explain the key features and mechanisms of {t['cognitive_process']} in human cognition.
   b) Discuss current limitations in our understanding or modeling of this process.

2. Quantum Algorithm Design (250-300 words):
   a) Propose a quantum algorithm that models {t['cognitive_process']}.
   b) Explain the quantum gates and operations used in your algorithm. Include at least 3 qubits and use a minimum of 2 different types of quantum gates.
   c) Describe how your algorithm represents and manipulates information related to {t['cognitive_process']}.
   d) Discuss how quantum superposition, entanglement, or interference are utilized in your model.
   e) Provide a diagram or schematic representation of your quantum circuit (describe it textually).

   Example circuit diagram (for illustration, not a solution):
   q0: --H--CNOT--
   q1: -----*-----
   q2: --X--Z-----

3. Cognitive-Quantum Mapping (150-200 words):
   a) Explain how specific quantum operations in your algorithm correspond to cognitive sub-processes.
   b) Discuss any novel insights about {t['cognitive_process']} that emerge from this quantum perspective.

4. Potential Advantages and Limitations (150-200 words):
   a) Analyze potential advantages of your quantum cognitive model over classical computational models.
   b) Discuss limitations of your model and propose potential solutions or areas for improvement.

5. Implementation and Validation (200-250 words):
   a) Outline how your quantum algorithm could be implemented on current or near-future quantum hardware.
   b) Discuss potential sources of error in your quantum circuit and propose error mitigation strategies.
   c) Propose an experiment to validate your model against empirical data on human {t['cognitive_process']}.

6. Real-world Applications (100-150 words):
   Propose two potential real-world applications of your quantum cognitive model.

7. Ethical and Philosophical Implications (100-150 words):
   Discuss ethical considerations and philosophical implications of modeling cognitive processes with quantum algorithms.

Ensure your response demonstrates a deep understanding of both quantum computing and cognitive psychology. Use appropriate terminology from both fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Your total response should be between 1100-1450 words. Use clear headings for each section.

Hints:
- Consider how quantum superposition might represent multiple cognitive states simultaneously.
- Think about how entanglement could model connections between different aspects of cognition.
- Reflect on how quantum measurement might relate to decision-making or memory recall processes.

Sample Structure:
1. Cognitive Process Analysis
2. Quantum Algorithm Design
   - Circuit Description
   - Quantum Operations Explanation
   - Information Representation
   - Quantum Phenomena Utilization
   - Circuit Diagram
3. Cognitive-Quantum Mapping
4. Potential Advantages and Limitations
5. Implementation and Validation
6. Real-world Applications
7. Ethical and Philosophical Implications
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates understanding of {t['cognitive_process']} in human cognition. (0.1 points)",
            "The proposed quantum algorithm uses at least 3 qubits and 2 different types of quantum gates. (0.15 points)",
            "A diagram or schematic representation of the quantum circuit is provided. (0.1 points)",
            "The mapping between quantum operations and cognitive sub-processes is explained. (0.15 points)",
            "Potential advantages and limitations of the quantum model are discussed. (0.1 points)",
            "The implementation proposal includes a discussion of error sources and mitigation strategies. (0.1 points)",
            "A validation experiment is proposed. (0.1 points)",
            "Two real-world applications are suggested. (0.1 points)",
            "Ethical and philosophical implications are discussed. (0.1 points)",
            "The response adheres to the specified word limit (1100-1450 words) and uses clear headings for each section. (0.1 points)"
        ]
        score = 0.0
        for criterion in criteria:
            if eval_with_llm_judge(instructions, submission, [criterion]):
                score += float(criterion.split('(')[-1].split()[0])
        return score
