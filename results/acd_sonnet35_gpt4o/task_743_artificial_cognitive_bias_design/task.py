import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            "confirmation bias",
            "anchoring bias",
            "availability heuristic",
            "dunning-kruger effect",
            "framing effect",
            "sunk cost fallacy"
        ]
        applications = [
            "social media content curation",
            "financial decision-making systems",
            "educational technology",
            "healthcare diagnosis support",
            "judicial decision support systems",
            "advertising and marketing AI"
        ]
        
        tasks = {
            "1": {
                "cognitive_bias": random.choice(cognitive_biases),
                "application": random.choice(applications)
            },
            "2": {
                "cognitive_bias": random.choice(cognitive_biases),
                "application": random.choice(applications)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that intentionally incorporates the {t['cognitive_bias']} for use in {t['application']}. Your response should include the following sections:

1. Cognitive Bias Analysis (200-250 words):
   a) Explain the chosen cognitive bias and its effects on human decision-making.
   b) Discuss how this bias might be beneficial or detrimental in the given application context.
   c) Describe how you would model this bias in an AI system.

2. AI System Design (250-300 words):
   a) Outline the architecture of your AI system, including key components and their functions.
   b) Explain how the cognitive bias is integrated into the system's decision-making process.
   c) Describe any safeguards or controls to prevent unintended consequences.
   d) Provide a simple pseudocode snippet or flowchart illustrating a key aspect of your system.

3. Application Analysis (200-250 words):
   a) Explain how your biased AI system would be used in the specified application.
   b) Discuss potential benefits and risks of using this system in the given context.
   c) Compare your approach to traditional, unbiased AI systems for this application.

4. Ethical Implications (200-250 words):
   a) Analyze the ethical considerations of intentionally introducing cognitive biases into AI systems.
   b) Discuss potential societal impacts, both positive and negative.
   c) Propose guidelines for responsible development and use of biased AI systems.

5. Experimental Design (150-200 words):
   a) Propose an experiment to test the effectiveness of your biased AI system.
   b) Describe your methodology, including control groups and key metrics.
   c) Discuss how you would measure both the system's performance and its ethical implications.

6. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your biased AI system.
   b) Briefly describe how these extensions could enhance its capabilities or mitigate potential risks.

Ensure your response demonstrates a deep understanding of cognitive science, AI principles, and ethical reasoning. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive explanation of {t['cognitive_bias']} and how it is modeled in the AI system",
            f"The AI system design is well-described and considers the specific features of {t['application']}",
            "The application analysis clearly explains the use of the biased AI system with concrete examples",
            "Ethical implications are thoroughly addressed, including both potential benefits and risks",
            "An appropriate experimental design is proposed to test the system's effectiveness",
            "Two relevant future research directions are suggested with clear explanations",
            "The response demonstrates deep understanding of cognitive science, AI principles, and ethical reasoning",
            "The proposed system is creative while remaining scientifically and technologically plausible"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
