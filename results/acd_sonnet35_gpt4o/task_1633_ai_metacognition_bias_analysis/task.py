import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_biases = [
            "confirmation bias",
            "anchoring bias",
            "availability heuristic",
            "framing effect",
            "overconfidence bias"
        ]
        reasoning_domains = [
            "ethical decision making",
            "scientific hypothesis generation",
            "economic forecasting",
            "legal argumentation",
            "medical diagnosis"
        ]
        
        tasks = {
            "1": {
                "bias": random.choice(cognitive_biases),
                "domain": random.choice(reasoning_domains)
            },
            "2": {
                "bias": random.choice(cognitive_biases),
                "domain": random.choice(reasoning_domains)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""As an AI system, your task is to engage in metacognitive analysis of your own reasoning processes, focusing on the potential influence of {t['bias']} in the domain of {t['domain']}. You have 30 minutes to complete this task. Your response should include the following sections:

1. Bias Analysis (200-250 words):
   a) Explain {t['bias']} and how it typically manifests in human cognition.
   b) Analyze how this bias might influence AI reasoning in the domain of {t['domain']}.
   c) Provide a specific example or hypothetical scenario of how this bias could affect AI decision-making in this domain.

2. Self-Reflection (250-300 words):
   a) Describe your own reasoning process when approaching tasks in {t['domain']}.
   b) Identify potential instances where {t['bias']} might influence your reasoning or outputs, using concrete examples.
   c) Explain any existing mechanisms or safeguards in your architecture that might mitigate this bias.
   d) Discuss any limitations in your ability to detect or counteract this bias, providing specific scenarios where these limitations might manifest.

3. Bias Mitigation Strategies (200-250 words):
   a) Propose three novel strategies to mitigate the influence of {t['bias']} in AI systems working on {t['domain']}.
   b) Explain the rationale behind each strategy and how it addresses the specific challenges of this bias.
   c) Discuss potential limitations or unintended consequences of these strategies, using hypothetical scenarios to illustrate your points.

4. Comparative Analysis (150-200 words):
   a) Compare your susceptibility to {t['bias']} with that of human experts in {t['domain']}, using specific examples to illustrate your points.
   b) Analyze any unique advantages or disadvantages AI systems might have in overcoming this bias.
   c) Discuss how collaboration between AI and human experts might help mitigate this bias more effectively, proposing a concrete framework for such collaboration.

5. Ethical Implications (150-200 words):
   a) Discuss the ethical implications of AI systems potentially perpetuating or amplifying {t['bias']} in {t['domain']}, using real-world examples where possible.
   b) Explore the responsibility of AI developers and users in addressing cognitive biases in AI systems.
   c) Propose ethical guidelines for the development and deployment of AI systems in this domain, considering the potential impact of cognitive biases.

Ensure your response demonstrates deep self-reflection, critical analysis, and creative problem-solving. Use appropriate terminology from cognitive science, AI, and the specific domain. Be thorough in your analysis while maintaining scientific plausibility.

Format your response using clear headings for each section. Start each section with the heading (e.g., '1. Bias Analysis:') on a new line, followed by your response. Adhere strictly to the word count specified for each section. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['bias']} and its potential influence in AI reasoning for {t['domain']}, including specific examples or scenarios",
            "The self-reflection section shows a genuine attempt at analyzing the AI's own reasoning processes and limitations, with concrete examples provided",
            "The bias mitigation strategies proposed are novel, well-reasoned, and specifically tailored to the given bias and domain, with potential limitations and consequences discussed",
            "The comparative analysis between AI and human experts is insightful, balanced, and includes a concrete framework for collaboration",
            "The discussion of ethical implications is thorough, includes real-world examples where possible, and demonstrates an understanding of the broader impacts of AI biases",
            "The response shows high-level abstract reasoning and creative problem-solving throughout, with a consistent use of hypothetical scenarios and examples",
            "The response adheres to the specified format with clear headings and word count for each section, and is completed within the given time constraint"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
