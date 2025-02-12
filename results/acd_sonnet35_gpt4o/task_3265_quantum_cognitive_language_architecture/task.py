import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = ['Superposition', 'Entanglement', 'Interference']
        cognitive_processes = ['Working Memory', 'Semantic Network', 'Attention']
        linguistic_phenomena = ['Ambiguity Resolution', 'Metaphor Comprehension', 'Syntactic Parsing']
        
        tasks = {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "linguistic_phenomenon": random.choice(linguistic_phenomena)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "cognitive_process": random.choice(cognitive_processes),
                "linguistic_phenomenon": random.choice(linguistic_phenomena)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired cognitive architecture for language processing that integrates the quantum computing principle of {t['quantum_principle']}, the cognitive process of {t['cognitive_process']}, and addresses the linguistic phenomenon of {t['linguistic_phenomenon']}. Your response should include the following sections:

1. Conceptual Framework (250-300 words):
   a) Explain how the chosen quantum principle can be applied to model cognitive processes in language.
   b) Describe how the selected cognitive process relates to the linguistic phenomenon.
   c) Propose a novel way to integrate these concepts into a cohesive architecture.

2. Architecture Design (300-350 words):
   a) Outline the key components of your quantum-inspired cognitive architecture.
   b) Explain how each component incorporates aspects of quantum computing and cognitive science.
   c) Describe the information flow and processing stages in your architecture.
   d) Include a diagram or flowchart of your architecture using ASCII art or Unicode characters.

3. Mathematical Formalization (200-250 words):
   a) Provide a mathematical representation of a key process in your architecture.
   b) Explain how this formalization captures both quantum and cognitive aspects.
   c) Discuss any novel mathematical approaches you've developed for this integration.

4. Simulated Experiment (250-300 words):
   a) Design a hypothetical experiment to test your architecture's performance on the chosen linguistic phenomenon.
   b) Describe the experimental setup, including input data and expected outputs.
   c) Explain how you would measure and analyze the results.
   d) Discuss potential insights this experiment could provide about human language processing.

5. Implications and Future Directions (200-250 words):
   a) Analyze the potential impact of your architecture on our understanding of language and cognition.
   b) Discuss how this approach might inform the development of quantum computing or AI systems.
   c) Propose two novel research questions that arise from your architecture.
   d) Suggest potential applications of your architecture beyond linguistic research.

Ensure your response demonstrates a deep understanding of quantum computing principles, cognitive science, and linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1200-1450 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections comprehensively",
            f"The architecture effectively integrates the specified quantum principle ({t['quantum_principle']}), cognitive process ({t['cognitive_process']}), and linguistic phenomenon ({t['linguistic_phenomenon']})",
            "The conceptual framework and architecture design demonstrate innovative thinking and scientific plausibility",
            "The mathematical formalization accurately represents key processes in the architecture",
            "The simulated experiment is well-designed and relevant to testing the architecture's performance",
            "The implications and future directions show insightful analysis and creative thinking",
            "The response demonstrates a deep understanding of quantum computing, cognitive science, and linguistics"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
