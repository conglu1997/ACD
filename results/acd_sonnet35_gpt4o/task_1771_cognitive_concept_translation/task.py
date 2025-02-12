import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "concept": "time",
                "source_framework": "human linear perception",
                "target_framework": "AI non-linear processing",
                "application_scenario": "optimizing AI decision-making in dynamic environments"
            },
            {
                "concept": "causality",
                "source_framework": "human intuitive understanding",
                "target_framework": "potential alien non-causal cognition",
                "application_scenario": "establishing communication protocols with extraterrestrial intelligence"
            },
            {
                "concept": "ethics",
                "source_framework": "human cultural values",
                "target_framework": "AI decision-making algorithms",
                "application_scenario": "developing ethical AI systems for autonomous vehicles"
            },
            {
                "concept": "consciousness",
                "source_framework": "human subjective experience",
                "target_framework": "AI self-awareness models",
                "application_scenario": "creating more empathetic AI assistants"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system for translating the abstract concept of {t['concept']} from {t['source_framework']} to {t['target_framework']}, and apply it to the scenario of {t['application_scenario']}. Your response should include:

1. Conceptual Framework (250-300 words):
   a) Analyze the key characteristics of {t['concept']} within {t['source_framework']}.
   b) Identify the challenges in translating this concept to {t['target_framework']}.
   c) Propose a novel approach for bridging these cognitive frameworks.

2. Translation Mechanism (200-250 words):
   a) Describe the core components of your translation system.
   b) Explain how your system accounts for fundamental differences between the frameworks.
   c) Provide an example of how a specific aspect of {t['concept']} would be translated.

3. Application Scenario (200-250 words):
   a) Apply your translation system to the scenario of {t['application_scenario']}.
   b) Discuss potential benefits and risks of this application.
   c) Describe how your system might evolve or adapt through this application.

4. Cognitive Implications (150-200 words):
   a) Analyze how your translation system might influence cognition in both frameworks.
   b) Discuss potential emergent properties or new understandings that could arise.
   c) Consider the long-term implications for the development of AI or human-AI interaction.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to translating {t['concept']} between these frameworks.
   b) Discuss the implications of potentially altering fundamental cognitive processes.
   c) Propose guidelines for the responsible development and use of your translation system.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['concept']} in both {t['source_framework']} and {t['target_framework']}.",
            "The proposed translation system is innovative, coherent, and scientifically plausible.",
            f"The application to {t['application_scenario']} is well-developed and considers both benefits and risks.",
            "The analysis of cognitive implications is insightful and considers long-term effects.",
            "Ethical considerations are thoroughly addressed with thoughtful guidelines proposed.",
            "The overall response showcases interdisciplinary knowledge synthesis and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
