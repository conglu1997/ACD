import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_problems = [
            {
                "problem": "factoring",
                "number_to_factor": 143,
                "quantum_gate": "Hadamard",
                "linguistic_feature": "metaphor"
            },
            {
                "problem": "database search",
                "database_size": 1000000,
                "quantum_gate": "CNOT",
                "linguistic_feature": "metonymy"
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(quantum_problems)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum algorithm for {t['problem']} using a specialized linguistic representation. Your task has the following components:

1. Quantum Algorithm Design (250-300 words):
   a) Describe a quantum algorithm that addresses the {t['problem']} problem {'for the number ' + str(t['number_to_factor']) if 'number_to_factor' in t else 'in a database of size ' + str(t['database_size'])}.
   b) Explain how your algorithm utilizes quantum superposition and entanglement.
   c) Incorporate the {t['quantum_gate']} gate in your algorithm and explain its role.
   d) Provide a high-level pseudocode or circuit diagram of your algorithm.

2. Linguistic Representation (200-250 words):
   a) Create a unique linguistic representation for your quantum algorithm using {t['linguistic_feature']} as a key element.
   b) Explain how your linguistic system represents quantum states, operations, and measurements.
   c) Provide an example of how a specific step in your algorithm would be expressed in this linguistic system.

3. Complexity Analysis (150-200 words):
   a) Analyze the time and space complexity of your quantum algorithm.
   b) Compare its efficiency to the best known classical algorithm for the same problem.
   c) Discuss any limitations or potential improvements to your algorithm.

4. Natural Language Translation (200-250 words):
   a) Translate your quantum algorithm into a creative narrative or story.
   b) Ensure that each step of the algorithm is represented by an event or action in the narrative.
   c) Incorporate quantum computing concepts as metaphors or plot elements in your story.

5. Interdisciplinary Implications (150-200 words):
   a) Discuss how your linguistic representation of quantum algorithms might influence the development of quantum programming languages.
   b) Explore potential applications of your approach in quantum education or quantum algorithm visualization.
   c) Propose an experiment to test the effectiveness of your linguistic system in helping people understand quantum algorithms.

Ensure your response demonstrates a deep understanding of quantum computing principles, algorithmic design, and linguistic creativity. Use appropriate terminology from both quantum physics and linguistics. Be innovative in your approach while maintaining scientific accuracy and logical consistency.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Quantum Algorithm Design section must describe a valid quantum algorithm for {t['problem']} {'for the number ' + str(t['number_to_factor']) if 'number_to_factor' in t else 'in a database of size ' + str(t['database_size'])} that incorporates the {t['quantum_gate']} gate.",
            f"The Linguistic Representation must create a unique system using {t['linguistic_feature']} to represent quantum states and operations, with a specific example provided.",
            "The Complexity Analysis should provide a valid comparison between the quantum algorithm and classical algorithms, including time and space complexity.",
            "The Natural Language Translation must accurately represent each step of the quantum algorithm in a creative narrative, using quantum concepts as metaphors or plot elements.",
            "The Interdisciplinary Implications section should propose a plausible experiment to test the effectiveness of the linguistic system in helping people understand quantum algorithms.",
            "The overall response must demonstrate a deep understanding of quantum computing, algorithmic design, and linguistic creativity, with appropriate use of terminology from both quantum physics and linguistics.",
            "The response must be formatted with clear headings for each section and be between 950-1200 words in total length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
