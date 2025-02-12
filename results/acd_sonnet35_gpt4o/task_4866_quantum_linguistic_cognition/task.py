import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "superposition",
                "linguistic_phenomenon": "lexical ambiguity",
                "cognitive_aspect": "contextual disambiguation",
                "example_sentence": "The bank is closed."
            },
            {
                "quantum_principle": "entanglement",
                "linguistic_phenomenon": "semantic coherence",
                "cognitive_aspect": "conceptual integration",
                "example_sentence": "The light bulb went off in her head."
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that applies the quantum computing principle of {t['quantum_principle']} to model and process the linguistic phenomenon of {t['linguistic_phenomenon']}, focusing on the cognitive aspect of {t['cognitive_aspect']}. Use the example sentence "{t['example_sentence']}" to illustrate your system's capabilities.

Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain how {t['quantum_principle']} can be applied to model {t['linguistic_phenomenon']} in natural language processing.
   b) Describe the key components and mechanisms of your quantum linguistic system.
   c) Discuss how your framework addresses {t['cognitive_aspect']} in language understanding.
   d) Provide a mathematical or logical formulation that captures the essence of your framework.

2. System Architecture (250-300 words):
   a) Describe the main components of your AI system that implements this quantum linguistic framework.
   b) Explain how classical and quantum computing elements interact in your system.
   c) Discuss any novel algorithms or data structures used in your design.

3. Language Processing Mechanism (200-250 words):
   a) Detail how your system processes the example sentence using quantum principles.
   b) Explain how it handles {t['linguistic_phenomenon']} differently from classical NLP systems.
   c) Describe how {t['cognitive_aspect']} is achieved or enhanced in your system.

4. Advantages and Limitations (200-250 words):
   a) Analyze the potential advantages of your quantum linguistic system over classical approaches.
   b) Discuss any limitations or challenges in implementing and scaling your system.
   c) Address potential criticisms or skepticism about applying quantum principles to linguistics.

5. Experimental Design (250-300 words):
   a) Propose an experiment to test the effectiveness of your system in handling {t['linguistic_phenomenon']}.
   b) Describe the methodology, including data sources, evaluation metrics, and baseline comparisons.
   c) Discuss how you would measure improvements in {t['cognitive_aspect']} using your system.

6. Ethical and Philosophical Implications (150-200 words):
   a) Explore the ethical considerations of using quantum-inspired models for language understanding.
   b) Discuss the philosophical implications of your framework for our understanding of cognition and language.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistics, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the quantum principle of {t['quantum_principle']}, the linguistic phenomenon of {t['linguistic_phenomenon']}, and the cognitive aspect of {t['cognitive_aspect']}.",
            f"The example sentence \"{t['example_sentence']}\" should be used to illustrate the system's capabilities.",
            "The theoretical framework should be well-explained and scientifically plausible.",
            "The system architecture should be clearly described and integrate both classical and quantum elements.",
            "The language processing mechanism should demonstrate a novel approach using quantum principles.",
            "Advantages, limitations, and potential criticisms should be thoroughly discussed.",
            "The experimental design should be well-thought-out and feasible.",
            "Ethical and philosophical implications should be explored in depth.",
            "The response should demonstrate a high level of interdisciplinary knowledge integration.",
            "The response should follow the specified format with clear headings for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
