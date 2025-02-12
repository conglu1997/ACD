import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_functions = [
            "memory enhancement",
            "attention control",
            "emotional regulation",
            "decision-making augmentation"
        ]
        ai_integration_methods = [
            "neural network symbiosis",
            "cognitive process offloading",
            "real-time data analysis and feedback",
            "predictive cognitive modeling"
        ]
        ethical_concerns = [
            "privacy and data security",
            "cognitive liberty and autonomy",
            "social inequality and access",
            "identity and authenticity"
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "cognitive_function": random.choice(cognitive_functions),
                "ai_integration": random.choice(ai_integration_methods),
                "ethical_concern": random.choice(ethical_concerns)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical brain-computer interface (BCI) system integrated with artificial intelligence that focuses on {t['cognitive_function']} using the AI integration method of {t['ai_integration']}. Then, analyze its impact on human cognition and society, with particular attention to the ethical concern of {t['ethical_concern']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure and components of your BCI-AI system.
   b) Explain how it interfaces with the human brain to enhance {t['cognitive_function']}.
   c) Detail how the {t['ai_integration']} method is implemented in your system.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture (describe this textually, do not attempt to generate an actual image).

2. Neuroscientific Basis (200-250 words):
   a) Explain the neuroscientific principles underlying your system's approach to {t['cognitive_function']}.
   b) Discuss how your system interacts with relevant brain regions and neural circuits.
   c) Address any potential neuroplasticity considerations or long-term effects on brain function.

3. AI Integration (200-250 words):
   a) Describe in detail how the {t['ai_integration']} method enhances or complements human cognitive processes.
   b) Explain any novel algorithms or techniques used in your AI system.
   c) Discuss how your system balances human and AI contributions to cognitive function.

4. Cognitive Impact Assessment (200-250 words):
   a) Analyze the potential short-term and long-term effects of your system on human cognition.
   b) Discuss how it might alter perception, thinking patterns, or decision-making processes.
   c) Consider both intended and possible unintended consequences on cognitive function.

5. Ethical Analysis (200-250 words):
   a) Examine the ethical implications of your system, focusing on {t['ethical_concern']}.
   b) Discuss potential risks and benefits to individuals and society.
   c) Propose guidelines or safeguards to address the identified ethical concerns.

6. Societal Impact (150-200 words):
   a) Predict potential changes in social dynamics, work environments, or educational systems.
   b) Discuss how your system might affect human relationships and communication.
   c) Consider potential legal or regulatory challenges that might arise.

7. Future Directions and Limitations (100-150 words):
   a) Identify current technological limitations and propose areas for future research.
   b) Suggest potential extensions or improvements to your system.
   c) Discuss any fundamental constraints or philosophical questions raised by your design.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and cognitive science. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above (1-7). Use subheadings (a, b, c, d) as outlined. Your total response should be between 1300-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, artificial intelligence, and cognitive science.",
            "The proposed BCI-AI system effectively addresses the specified cognitive function and AI integration method.",
            "The system architecture is clearly described and includes a textual representation of a high-level diagram or pseudocode.",
            "The neuroscientific basis is well-explained and addresses potential long-term effects on brain function.",
            "The AI integration section provides detailed explanations of novel algorithms or techniques.",
            "The cognitive impact assessment considers both short-term and long-term effects comprehensively.",
            "The ethical analysis thoroughly examines the given ethical concern and proposes meaningful safeguards.",
            "The societal impact analysis is insightful and well-reasoned, including legal and regulatory considerations.",
            "The response is innovative while maintaining scientific plausibility.",
            "The response adheres to the specified word count, formatting guidelines, and includes a word count at the end."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
