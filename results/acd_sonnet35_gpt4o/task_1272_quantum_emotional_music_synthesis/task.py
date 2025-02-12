import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            'superposition',
            'entanglement',
            'quantum tunneling',
            'quantum coherence'
        ]
        musical_elements = [
            'melody',
            'harmony',
            'rhythm',
            'timbre'
        ]
        emotional_states = [
            'joy',
            'sadness',
            'anger',
            'fear',
            'surprise',
            'disgust'
        ]
        constraints = [
            'limited to 50 qubits',
            'must operate at room temperature',
            'real-time generation required',
            'must be compatible with classical music notation'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'quantum_principle': random.choice(quantum_principles),
                'musical_element': random.choice(musical_elements),
                'emotional_state': random.choice(emotional_states),
                'constraint': random.choice(constraints)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that generates music based on emotional states, using principles from quantum mechanics and music theory. Your system should specifically incorporate the quantum principle of {t['quantum_principle']}, focus on the musical element of {t['musical_element']}, aim to express or evoke the emotional state of {t['emotional_state']}, and operate under the constraint: {t['constraint']}.

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your quantum music generation system.
   b) Explain how it incorporates the specified quantum principle in its design.
   c) Detail how the system will represent and manipulate the given musical element.
   d) Discuss how the system will encode and express the specified emotional state.
   e) Address how the system design accommodates the given constraint.

2. Quantum-Music-Emotion Interface (200-250 words):
   a) Explain how your system translates quantum states into musical parameters.
   b) Describe how these musical parameters are then mapped to emotional expressions.
   c) Discuss any challenges in bridging these three domains (quantum, musical, and emotional) and how you address them.

3. Music Generation Algorithm (200-250 words):
   a) Propose a quantum algorithm for generating music based on emotional input.
   b) Explain how this algorithm leverages the specified quantum principle.
   c) Describe how the algorithm ensures the output focuses on the given musical element.
   d) Discuss how the algorithm incorporates principles from music theory and emotional psychology.

4. Example Output (150-200 words):
   a) Provide a detailed description of a potential musical output from your system, based on the specified emotional state.
   b) Explain how this output reflects the quantum principle, musical element, and emotional state.

5. Implications and Applications (200-250 words):
   a) Discuss the potential implications of your system for our understanding of quantum phenomena, music perception, and emotional processing.
   b) Propose two novel applications of your quantum emotional music synthesis system outside of pure artistic creation.
   c) Speculate on how this technology might impact fields such as music therapy, emotional intelligence research, or quantum computing.

6. Limitations and Future Work (100-150 words):
   a) Discuss potential limitations or challenges of your proposed system.
   b) Suggest areas for future research or improvements.

Ensure your response demonstrates a deep understanding of quantum computing principles, music theory, and emotional psychology. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The System Architecture effectively incorporates the quantum principle of {t['quantum_principle']}.",
            f"The design focuses on the musical element of {t['musical_element']}.",
            f"The system convincingly aims to express or evoke the emotional state of {t['emotional_state']}.",
            f"The system design adequately addresses the constraint: {t['constraint']}.",
            "The Quantum-Music-Emotion Interface demonstrates a clear understanding of how to bridge these three domains.",
            "The Music Generation Algorithm is innovative and scientifically plausible.",
            "The Example Output description is detailed and coherently reflects the specified parameters.",
            "The Implications and Applications section proposes insightful and novel ideas.",
            "The Limitations and Future Work section addresses potential challenges and areas for improvement.",
            "The response demonstrates deep interdisciplinary knowledge and creative problem-solving.",
            "The ideas presented are scientifically grounded and well-explained.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
