import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "target": "protein-ligand binding",
                "quantum_approach": "variational quantum eigensolver (VQE)",
                "molecule": "remdesivir",
                "protein": "SARS-CoV-2 main protease"
            },
            {
                "target": "transition state identification",
                "quantum_approach": "quantum approximate optimization algorithm (QAOA)",
                "molecule": "amlodipine",
                "protein": "calcium channel blocker"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel quantum algorithm for simulating {t['target']} in drug discovery, incorporating principles from the {t['quantum_approach']}. Focus on the interaction between {t['molecule']} and {t['protein']}. Then, analyze its potential impact on pharmaceutical research. Your response should include the following sections:

1. Quantum Algorithm Design (300-350 words):
   a) Describe the key components and steps of your quantum algorithm.
   b) Explain how your algorithm incorporates principles from the {t['quantum_approach']}.
   c) Detail how your algorithm addresses the specific challenges of simulating {t['target']} for {t['molecule']} and {t['protein']}.
   d) Include a text-based description of your algorithm's quantum circuit, using standard quantum gate notation (e.g., H for Hadamard, CNOT for controlled-NOT).

2. Quantum-Classical Hybrid Approach (200-250 words):
   a) Explain how your algorithm integrates quantum and classical computing elements.
   b) Discuss the advantages of this hybrid approach for drug discovery applications.
   c) Describe any novel techniques used to mitigate quantum noise or errors.

3. Computational Complexity Analysis (200-250 words):
   a) Analyze the time and space complexity of your algorithm.
   b) Compare its theoretical performance to classical algorithms for similar tasks.
   c) Discuss any quantum speedup or advantage your algorithm provides.

4. Implementation and Scalability (200-250 words):
   a) Describe the quantum hardware requirements for implementing your algorithm.
   b) Discuss the scalability of your approach to larger molecular systems.
   c) Propose strategies for running your algorithm on near-term quantum devices.

5. Drug Discovery Applications (250-300 words):
   a) Explain how your algorithm could be applied in real-world drug discovery processes.
   b) Discuss the potential impact on lead optimization and candidate selection.
   c) Describe how your approach might accelerate or improve pharmaceutical research.
   d) Provide a specific example of how your algorithm could be used in a drug discovery pipeline involving {t['molecule']} and {t['protein']}.

6. Challenges and Future Directions (200-250 words):
   a) Identify key challenges in implementing and adopting your quantum algorithm.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss how your algorithm might evolve with advancements in quantum hardware.

7. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using quantum computing in drug discovery.
   b) Address concerns about equitable access to this advanced technology in pharmaceutical research.
   c) Propose guidelines for responsible development and use of quantum algorithms in healthcare.

Ensure your response demonstrates a deep understanding of quantum computing, chemistry, and drug discovery processes. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a novel quantum algorithm design for simulating {t['target']} in drug discovery, focusing on the interaction between {t['molecule']} and {t['protein']}",
            f"The algorithm incorporates principles from the {t['quantum_approach']}",
            "The response covers all required sections: Quantum Algorithm Design, Quantum-Classical Hybrid Approach, Computational Complexity Analysis, Implementation and Scalability, Drug Discovery Applications, Challenges and Future Directions, and Ethical Considerations",
            "The proposed algorithm is innovative yet scientifically plausible",
            "The response demonstrates a deep understanding of quantum computing, chemistry, and drug discovery processes",
            "The analysis includes a thoughtful discussion of the potential impact on pharmaceutical research",
            "The response includes a text-based description of the algorithm's quantum circuit using standard quantum gate notation",
            "The total word count is between 1500-1850 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
