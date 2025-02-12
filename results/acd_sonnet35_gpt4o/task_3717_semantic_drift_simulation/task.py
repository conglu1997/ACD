import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        words = [
            "awesome",
            "literally",
            "algorithm",
            "cloud",
            "viral"
        ]
        time_periods = [
            "50 years",
            "100 years",
            "200 years"
        ]
        domains = [
            "social media",
            "scientific literature",
            "everyday conversation"
        ]
        return {
            "1": {
                "word": random.choice(words),
                "time_period": random.choice(time_periods),
                "domain": random.choice(domains)
            },
            "2": {
                "word": random.choice(words),
                "time_period": random.choice(time_periods),
                "domain": random.choice(domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates semantic drift in language evolution, then use it to predict and analyze potential future changes in word meanings. Focus on the word '{t['word']}', projecting its semantic evolution over the next {t['time_period']} in the domain of {t['domain']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating semantic drift.
   b) Explain how your system incorporates historical linguistic data and current usage patterns.
   c) Detail the algorithms or models used for predicting semantic changes.
   d) Discuss how your system accounts for social and technological factors influencing language evolution.
   e) Include a simple pseudocode snippet (5-10 lines) illustrating a key aspect of your system.

2. Semantic Drift Simulation (250-300 words):
   a) Provide a brief etymology and current usage of the word '{t['word']}'.
   b) Simulate the potential semantic drift of '{t['word']}' over the next {t['time_period']}.
   c) Explain the reasoning behind your predicted changes, considering linguistic and social factors.
   d) Discuss any potential new meanings or contexts for the word that your system predicts.

3. Domain-Specific Analysis (200-250 words):
   a) Analyze how the domain of {t['domain']} might specifically influence the semantic drift of '{t['word']}'.
   b) Compare your predictions for this domain with potential changes in other contexts.
   c) Discuss any challenges or unique considerations for simulating semantic drift in this domain.

4. Linguistic Implications (200-250 words):
   a) Discuss the broader implications of your simulated semantic drift for language evolution.
   b) Analyze how changes in the meaning of '{t['word']}' might affect related words or expressions.
   c) Consider potential impacts on communication and understanding across generations.

5. Evaluation and Validation (150-200 words):
   a) Propose a method for evaluating the accuracy of your semantic drift predictions.
   b) Discuss the challenges in validating long-term linguistic predictions.
   c) Suggest how your system could be refined based on ongoing language data collection.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of predicting and potentially influencing language evolution.
   b) Consider issues of linguistic prescriptivism vs. descriptivism in the context of your system.
   c) Propose guidelines for the responsible use of semantic drift simulation technologies.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistic change, cognitive science, and AI technologies.",
            "The system architecture is well-designed and clearly explained, showing how it simulates and predicts semantic drift.",
            "The semantic drift simulation for the given word is plausible and well-reasoned, considering relevant factors.",
            "The domain-specific analysis shows insight into how different contexts can influence language evolution.",
            "The discussion of linguistic implications is thoughtful and considers broader impacts on language and communication.",
            "The proposed evaluation method and ethical considerations demonstrate critical thinking about the implications of the technology.",
            "The response is innovative while maintaining scientific plausibility.",
            "The response falls within the specified word count range of 1250-1550 words.",
            "The pseudocode snippet is relevant and illustrates a key aspect of the system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
