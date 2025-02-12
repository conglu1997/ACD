import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "Language Processing",
            "Decision Making",
            "Social Interaction",
            "Memory Formation",
            "Perception",
            "Learning",
            "Emotional Processing"
        ]
        cognitive_processes = [
            "Attention",
            "Pattern Recognition",
            "Categorization",
            "Inference",
            "Prediction",
            "Abstraction",
            "Mental Simulation"
        ]
        tasks = {
            "1": {"domain": random.choice(domains), "process": random.choice(cognitive_processes)},
            "2": {"domain": random.choice(domains), "process": random.choice(cognitive_processes)}
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a novel artificial cognitive bias related to the domain of {t['domain']} and the cognitive process of {t['process']}. Your response should include the following sections:

1. Bias Description (200-250 words):
   a) Name your artificial cognitive bias.
   b) Provide a clear definition and explanation of how it operates.
   c) Describe the specific ways it influences {t['domain']} through the process of {t['process']}.
   d) Explain the potential evolutionary or cultural origins of this bias if it were to exist in humans.

2. Cognitive Mechanism (200-250 words):
   a) Detail the underlying cognitive mechanisms that would give rise to this bias.
   b) Explain how it interacts with other known cognitive processes or biases.
   c) Propose a simple cognitive model or framework to represent this bias.

3. Linguistic Impact (150-200 words):
   a) Analyze how this bias might influence language use and understanding.
   b) Provide specific examples of how it could affect vocabulary, syntax, or pragmatics.
   c) Discuss any potential long-term effects on language evolution.

4. Decision-Making Consequences (200-250 words):
   a) Examine how this bias would affect individual and group decision-making processes.
   b) Provide a hypothetical scenario demonstrating the bias in action.
   c) Discuss potential real-world implications in areas such as politics, economics, or social policy.

5. Social and Cultural Implications (150-200 words):
   a) Analyze how this bias might influence social interactions and cultural practices.
   b) Discuss potential effects on social structures, norms, or values.
   c) Consider how different cultures might be affected differently by this bias.

6. Potential Benefits and Risks (100-150 words):
   a) Identify any potential benefits this bias might offer to individuals or society.
   b) Discuss the risks or negative consequences associated with this bias.
   c) Propose methods for mitigating negative effects while preserving potential benefits.

7. Experimental Design (150-200 words):
   a) Propose an experimental setup to test for the existence of this bias in humans or AI systems.
   b) Describe the methodology, including control conditions and measured variables.
   c) Discuss potential challenges in isolating and measuring the effects of this bias.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and social psychology. Be creative in your bias design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1150-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate detail and adheres to the specified word count for each section.",
            f"The artificial cognitive bias is clearly related to the domain of {t['domain']} and the cognitive process of {t['process']}.",
            "The bias description is creative, plausible, and well-explained.",
            "The cognitive mechanism section demonstrates a deep understanding of cognitive processes.",
            "The linguistic impact, decision-making consequences, and social implications are thoroughly analyzed.",
            "The potential benefits and risks are thoughtfully considered.",
            "The proposed experimental design is scientifically sound and appropriate for testing the bias.",
            "The overall response shows creativity, scientific reasoning, and interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
