import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum interference"
        ]
        linguistic_aspects = [
            "semantic ambiguity",
            "syntactic parsing",
            "pragmatic inference",
            "lexical entailment"
        ]
        cognitive_tasks = [
            "decision making",
            "problem solving",
            "language acquisition",
            "concept formation"
        ]
        
        tasks = {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "linguistic_aspect": random.choice(linguistic_aspects),
                "cognitive_task": random.choice(cognitive_tasks)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "linguistic_aspect": random.choice(linguistic_aspects),
                "cognitive_task": random.choice(cognitive_tasks)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a problem-solving framework that integrates the quantum computing principle of {t['quantum_principle']} with the linguistic aspect of {t['linguistic_aspect']} to address the cognitive task of {t['cognitive_task']}. Your response should include:

1. Framework Design (300-350 words):
   a) Describe the key components and structure of your quantum-linguistic problem-solving framework.
   b) Explain how it incorporates the specified quantum principle and linguistic aspect.
   c) Detail how the framework addresses the given cognitive task.
   d) Discuss any novel features that distinguish it from classical problem-solving approaches.

2. Quantum-Linguistic Mapping (200-250 words):
   a) Explain how quantum states or processes in your framework correspond to linguistic elements or processes.
   b) Provide a specific example of how this mapping works for the given cognitive task.
   c) Discuss potential advantages of this quantum-inspired approach over classical models.

3. Information Processing Mechanism (200-250 words):
   a) Describe how information flows and is processed in your framework.
   b) Explain how the quantum principle enhances or alters linguistic processing.
   c) Discuss any emergent properties that might arise from this quantum-linguistic integration.

4. Mathematical Representation (150-200 words):
   a) Provide a basic mathematical description of your framework.
   b) Include at least one equation that integrates quantum and linguistic elements.
   c) Explain the significance of each term in your equation(s).

5. Potential Applications (200-250 words):
   a) Propose three potential applications of your framework in cognitive science or artificial intelligence.
   b) Explain how each application leverages the unique features of your quantum-linguistic model.
   c) Discuss potential impacts and benefits of these applications.

6. Limitations and Challenges (150-200 words):
   a) Identify at least three potential limitations or challenges of your framework.
   b) Discuss any ethical concerns that may arise from its development or application.
   c) Propose potential solutions or areas for future research to address these issues.

7. Experimental Design (150-200 words):
   a) Propose an experiment to test the effectiveness of your framework in addressing the given cognitive task.
   b) Describe the methodology, including control conditions and measurable outcomes.
   c) Discuss how the results of this experiment could contribute to our understanding of quantum effects in cognition and language processing.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the quantum principle of {t['quantum_principle']}, the linguistic aspect of {t['linguistic_aspect']}, and how they can be applied to the cognitive task of {t['cognitive_task']}.",
            "The framework design is innovative, well-structured, and effectively integrates quantum and linguistic concepts.",
            "The quantum-linguistic mapping is clearly explained and provides a plausible connection between quantum states and linguistic processes.",
            "The mathematical representation is appropriate and effectively captures the key elements of the framework.",
            "The proposed applications are creative, well-reasoned, and demonstrate the potential impact of the framework.",
            "The response acknowledges limitations and ethical concerns, proposing thoughtful solutions or areas for future research.",
            "The experimental design is well-conceived and would effectively test the framework's efficacy.",
            "The overall response shows strong interdisciplinary thinking, connecting concepts from quantum physics, linguistics, and cognitive science in a novel and scientifically plausible manner."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
