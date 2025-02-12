import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "quantum superposition",
            "quantum entanglement",
            "quantum tunneling"
        ]
        linguistic_features = [
            "semantic memory",
            "syntactic processing",
            "phonological encoding"
        ]
        cognitive_processes = [
            "working memory",
            "long-term potentiation",
            "spreading activation"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_process": random.choice(cognitive_processes)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that simulates human linguistic memory and language processing, incorporating the quantum principle of {t['quantum_principle']}, the linguistic feature of {t['linguistic_feature']}, and the cognitive process of {t['cognitive_process']}. Your response should include:

1. Quantum-Linguistic Interface (250-300 words):
   a) Describe how your system integrates quantum computing with linguistic processing.
   b) Explain how {t['quantum_principle']} is utilized in modeling {t['linguistic_feature']}.
   c) Discuss potential advantages of using quantum computing for this linguistic simulation.
   d) Provide a simple pseudocode snippet (5-10 lines) illustrating a key aspect of this integration.

2. Memory and Processing Architecture (250-300 words):
   a) Detail the structure of your quantum linguistic memory system.
   b) Explain how it simulates {t['cognitive_process']} in the context of language.
   c) Describe how information is encoded, stored, and retrieved in your system.
   d) Include a diagram or flowchart of your system architecture (describe it in words).

3. Linguistic Task Simulation (200-250 words):
   a) Propose a specific linguistic task that your system can perform (e.g., semantic categorization, syntactic parsing).
   b) Explain step-by-step how your system would approach this task.
   c) Discuss how the integration of quantum principles enhances the task performance.
   d) Provide a concrete example of how your system would process a specific input for this task.

4. Cognitive Implications (200-250 words):
   a) Analyze how your quantum linguistic system might provide insights into human language processing.
   b) Discuss potential implications for our understanding of {t['cognitive_process']} in relation to language.
   c) Propose a hypothesis about human cognition that could be tested using your system.

5. Technical Challenges and Solutions (150-200 words):
   a) Identify key technical challenges in implementing your quantum linguistic system.
   b) Propose innovative solutions to these challenges.
   c) Discuss any trade-offs or limitations in your approach.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of simulating human linguistic processes using quantum systems.
   b) Address potential concerns about privacy, cognitive manipulation, or altering natural language processes.
   c) Suggest future research directions or expansions of your system.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science. Be creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words. Stay within the specified word count for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of {t['quantum_principle']} and how it can be applied to linguistic processing, including a relevant pseudocode snippet.",
            f"The system design should effectively integrate {t['linguistic_feature']} and {t['cognitive_process']}, with a well-described architecture.",
            "The proposed quantum linguistic system should be innovative yet scientifically plausible, with a concrete example of task processing.",
            "The response should include a well-reasoned analysis of cognitive implications and a testable hypothesis.",
            "The technical challenges, proposed solutions, and ethical considerations should be thoughtfully addressed.",
            "The response should adhere to the specified format and word count limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
