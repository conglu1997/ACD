import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_challenges = [
            'memory enhancement',
            'attention deficit disorder',
            'language acquisition',
            'emotional regulation',
            'decision-making under uncertainty'
        ]
        brain_regions = [
            'prefrontal cortex',
            'hippocampus',
            'amygdala',
            'cerebellum',
            'Broca\'s area'
        ]
        tasks = [
            {
                'challenge': random.choice(cognitive_challenges),
                'brain_region': random.choice(brain_regions)
            },
            {
                'challenge': random.choice(cognitive_challenges),
                'brain_region': random.choice(brain_regions)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a speculative neurotechnology device that addresses the following cognitive challenge and involves the specified brain region:

Cognitive Challenge: {t['challenge']}
Brain Region: {t['brain_region']}

Your task:

1. Device Concept (150-200 words):
   - Provide a name for your neurotechnology device.
   - Describe the key features and functioning of the device.
   - Explain how it interfaces with the specified brain region.
   - Discuss how the device addresses the given cognitive challenge.

2. Scientific Basis (200-250 words):
   - Explain the neuroscientific principles underlying your device's operation.
   - Discuss current research or theories that support the feasibility of your concept.
   - Identify any speculative elements that go beyond current scientific understanding.

3. Ethical Analysis (200-250 words):
   - Discuss at least three potential ethical concerns raised by your device.
   - Analyze how these concerns might be addressed or mitigated.
   - Consider both individual and societal ethical implications.

4. Societal Impact (150-200 words):
   - Predict potential positive and negative impacts of widespread adoption of your device.
   - Discuss how it might change social dynamics, economic structures, or cultural norms.
   - Consider potential regulatory or policy implications.

5. Future Development (100-150 words):
   - Propose two potential future enhancements or applications of your device.
   - Discuss any additional ethical or societal considerations these developments might raise.

Ensure your response demonstrates a deep understanding of neuroscience, technology design, and ethical reasoning. Use scientific terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section, following the structure outlined above. Include the word count for each section in parentheses at the end of the section. Your total response should be between 800-1050 words.

Note: Do not provide direct solutions or hints that would make the task trivial. The goal is to create a challenging and thought-provoking response that demonstrates your capabilities in interdisciplinary thinking and ethical analysis."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The device concept is innovative, clearly named, and addresses the given cognitive challenge and brain region.",
            "The scientific basis is well-explained, grounded in current neuroscientific understanding, and identifies speculative elements.",
            "The ethical analysis discusses at least three potential concerns and considers both individual and societal implications.",
            "The societal impact assessment covers positive and negative impacts, changes to social dynamics, and potential regulatory implications.",
            "Two future developments are proposed with additional ethical or societal considerations.",
            "The response adheres to the specified word count limits for each section.",
            "The overall response demonstrates a high level of interdisciplinary knowledge, creativity, and ethical reasoning without providing direct solutions or hints."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
