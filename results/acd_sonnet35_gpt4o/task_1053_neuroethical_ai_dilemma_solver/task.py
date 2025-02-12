class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cognitive_process": "moral reasoning",
                "brain_region": "ventromedial prefrontal cortex",
                "ethical_framework": "utilitarianism",
                "dilemma": "trolley problem"
            },
            "2": {
                "cognitive_process": "empathy",
                "brain_region": "anterior insular cortex",
                "ethical_framework": "care ethics",
                "dilemma": "organ transplant dilemma"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates human {t['cognitive_process']} based on the functioning of the {t['brain_region']}, incorporating principles of {t['ethical_framework']}. Then, analyze how this system would approach the {t['dilemma']}. Your response should include:

1. Neuroscientific Basis (200-250 words):
   a) Explain the role of the {t['brain_region']} in {t['cognitive_process']}.
   b) Describe how this brain region's function relates to {t['ethical_framework']}.
   c) Propose a simplified computational model of this brain region's function.

2. AI System Design (250-300 words):
   a) Outline the key components of your AI system.
   b) Explain how it incorporates the neuroscientific principles and ethical framework.
   c) Describe the decision-making process of your AI system.
   d) Discuss how your system handles uncertainty or conflicting moral values.

3. Dilemma Analysis (200-250 words):
   a) Briefly describe the {t['dilemma']}.
   b) Explain how your AI system would approach this dilemma.
   c) Compare the AI's approach to typical human responses.
   d) Discuss any limitations or potential biases in your system's approach.

4. Ethical Implications (150-200 words):
   a) Discuss the ethical considerations of creating AI systems capable of moral reasoning.
   b) Analyze potential consequences of deploying such systems in real-world scenarios.
   c) Propose guidelines for the responsible development and use of these AI systems.

5. Future Research Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your AI system.
   b) Propose an experiment to test the effectiveness of your system in real-world ethical decision-making.

Ensure your response demonstrates a deep understanding of neuroscience, ethics, and AI principles. Be creative in your approach while maintaining scientific plausibility and ethical responsibility. Use appropriate terminology and provide clear explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified brain region and its role in the given cognitive process.",
            "The AI system design effectively incorporates both neuroscientific principles and the given ethical framework.",
            "The analysis of the ethical dilemma is thorough and compares the AI's approach to human responses.",
            "The ethical implications of creating moral reasoning AI are thoughtfully discussed.",
            "The proposed future research directions are innovative and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
