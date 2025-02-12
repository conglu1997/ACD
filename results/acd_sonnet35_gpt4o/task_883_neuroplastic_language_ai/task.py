import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_challenges = [
            "Rapid acquisition of a constructed language",
            "Adapting to evolving internet slang",
            "Learning context-dependent communication in a professional field",
            "Mastering multiple dialects of a language simultaneously",
            "Deciphering and adapting to coded language in sensitive communications"
        ]
        neural_plasticity_mechanisms = [
            "Synaptic pruning",
            "Long-term potentiation",
            "Neurogenesis",
            "Axonal sprouting",
            "Dendritic remodeling"
        ]
        tasks = [
            {
                "linguistic_challenge": challenge,
                "neural_plasticity_mechanism": mechanism
            }
            for challenge in linguistic_challenges
            for mechanism in neural_plasticity_mechanisms
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics neural plasticity for adaptive language acquisition, focusing on the neural plasticity mechanism of {t['neural_plasticity_mechanism']}. Then, apply this system to the linguistic challenge of {t['linguistic_challenge']}. Your response should include:

1. Neural Plasticity Mechanism (200-250 words):
   a) Explain the biological basis of {t['neural_plasticity_mechanism']} in human brains.
   b) Describe how this mechanism contributes to language learning in humans.
   c) Propose how this mechanism could be computationally modeled in an AI system.

2. AI System Architecture (250-300 words):
   a) Design an AI architecture that incorporates your computational model of {t['neural_plasticity_mechanism']}.
   b) Explain how this architecture enables adaptive language acquisition.
   c) Describe the key components and their interactions within your system.

3. Application to Linguistic Challenge (200-250 words):
   a) Analyze the specific requirements and difficulties of {t['linguistic_challenge']}.
   b) Explain how your AI system would approach this challenge using its neuroplastic capabilities.
   c) Provide a step-by-step description of the learning process your AI would undergo.

4. Performance Evaluation (150-200 words):
   a) Propose metrics to evaluate your AI system's performance on the given linguistic challenge.
   b) Describe an experiment to test the effectiveness of your system compared to traditional language models.
   c) Discuss potential limitations of your approach and how they might be addressed.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to AI systems with human-like neural plasticity.
   b) Explore the societal impacts of AI capable of rapid, adaptive language acquisition.
   c) Propose guidelines for responsible development and use of such AI systems.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and artificial intelligence. Be creative and innovative in your approach while maintaining scientific plausibility. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains the biological basis of {t['neural_plasticity_mechanism']} and its role in human language learning",
            "The AI system architecture creatively and plausibly incorporates the neural plasticity mechanism",
            f"The application to {t['linguistic_challenge']} is well-reasoned and demonstrates how the AI's neuroplastic capabilities would be utilized",
            "The proposed evaluation metrics and experiment are appropriate and well-designed",
            "The discussion of ethical and societal implications is thoughtful and comprehensive",
            "The response demonstrates a deep understanding of neuroscience, linguistics, and AI throughout all sections",
            "The proposed AI system is innovative while remaining scientifically plausible",
            "The response adheres to the specified format and word count guidelines for each section",
            "The total response is between 950-1200 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
