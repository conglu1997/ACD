import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Superposition",
                "evolutionary_process": "Natural Selection"
            },
            {
                "quantum_principle": "Entanglement",
                "evolutionary_process": "Genetic Drift"
            }
        ]
        return {
            "1": random.choice(tasks),
            "2": random.choice(tasks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that applies the quantum information principle of {t['quantum_principle']} to model the evolutionary process of {t['evolutionary_process']} in biological systems. Your task is to:

1. Conceptual Foundation (200-250 words):
   a) Explain the key aspects of the given quantum principle and evolutionary process.
   b) Propose a novel way to map the quantum principle onto the evolutionary process.
   c) Describe how this mapping could provide new insights into biological evolution.

2. Mathematical Framework (200-250 words):
   a) Develop a mathematical representation of your framework, using both quantum mechanical and evolutionary biological formalisms.
   b) Explain the key variables, operators, or equations in your framework.
   c) Discuss how your framework captures the essential features of both the quantum principle and the evolutionary process.

3. Predictions and Implications (200-250 words):
   a) Describe at least two novel predictions or insights that your framework generates about evolutionary processes.
   b) Explain how these predictions differ from those of classical evolutionary theory.
   c) Discuss the potential implications of your framework for our understanding of biological complexity and adaptation.

4. Experimental Design (150-200 words):
   Propose an experiment or observational study that could test a key prediction of your framework. Include:
   a) The hypothesis being tested
   b) The basic experimental setup or observational methodology
   c) The expected results if your framework is correct
   d) Potential challenges in conducting this test

5. Interdisciplinary Connections (150-200 words):
   Explore how your framework might inform or be informed by other scientific disciplines not yet mentioned (e.g., complexity theory, information theory, thermodynamics).

6. Limitations and Future Directions (100-150 words):
   Discuss potential limitations of your framework and suggest directions for future research or refinement.

Ensure your response demonstrates a deep understanding of both quantum mechanics and evolutionary biology. Be creative in your approach while maintaining scientific plausibility and rigor. Use appropriate scientific terminology and provide clear explanations of complex concepts.

Format your response with clear headings for each section. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of both {t['quantum_principle']} and {t['evolutionary_process']}.",
            "The proposed framework should be innovative and scientifically plausible.",
            "The mathematical representation should be coherent and integrate both quantum and evolutionary principles.",
            "The predictions and implications should be logical and offer novel insights.",
            "The experimental design should be feasible and directly test the framework's predictions.",
            "The interdisciplinary connections should be meaningful and well-reasoned.",
            "The limitations and future directions should demonstrate critical thinking about the framework.",
            "The overall response should be well-structured, clear, and demonstrate strong scientific reasoning and creativity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
