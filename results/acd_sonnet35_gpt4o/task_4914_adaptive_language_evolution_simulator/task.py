import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "Digital Technology Integration",
                "description": "Simulate how a pre-digital society's language evolves to incorporate concepts related to computers, the internet, and social media."
            },
            {
                "name": "Climate Change Adaptation",
                "description": "Model the evolution of language in a society facing rapid environmental changes, focusing on new terms for weather patterns, sustainable technologies, and ecological concepts."
            }
        ]
        linguistic_features = [
            "Phonological adaptation",
            "Semantic shift",
            "Morphological innovation",
            "Syntactic restructuring"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "scenario": random.choice(scenarios),
                "linguistic_feature": random.choice(linguistic_features)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution and adaptation of languages in a multi-agent environment, focusing on how languages incorporate new concepts or technologies. Your task is to model language evolution in the following scenario: {t['scenario']['name']} - {t['scenario']['description']}

Your system should emphasize the linguistic feature of {t['linguistic_feature']}.

Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI system for simulating language evolution.
   b) Explain how these components interact to model linguistic changes over time.
   c) Detail how your system incorporates multi-agent interactions and cognitive processes.
   d) Discuss how your system models the introduction and spread of new concepts or terms.

2. Language Adaptation Mechanism (250-300 words):
   a) Explain how your system models the process of language adaptation, focusing on {t['linguistic_feature']}.
   b) Describe the algorithms or methods used to simulate linguistic innovations and their propagation.
   c) Discuss how your system accounts for sociolinguistic factors in language change.

3. Scenario-Specific Modeling (200-250 words):
   a) Detail how your system would model language evolution in the given scenario.
   b) Provide examples of potential linguistic changes your system might predict.
   c) Explain how these changes reflect the adaptation to new concepts or technologies.

4. Data and Training Approach (200-250 words):
   a) Describe the types of data your system would require for training and validation.
   b) Explain your approach to generating or collecting this data.
   c) Discuss any ethical considerations in data collection or use.

5. Evaluation and Analysis (200-250 words):
   a) Propose methods for evaluating the accuracy and plausibility of your system's predictions.
   b) Describe how you would analyze the simulated language evolution over time.
   c) Suggest ways to validate your model against real-world language change data.

6. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your system for understanding real-world language evolution.
   b) Propose two novel applications of your system in linguistics or cognitive science research.
   c) Consider how your system might inform language policy or preservation efforts.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections and topics",
            "The system design demonstrates interdisciplinary knowledge integration",
            "The approach to language evolution simulation is creative and scientifically plausible",
            "The response shows a deep understanding of linguistics, cognitive science, and AI",
            f"The system effectively models the given scenario: {t['scenario']['name']}",
            f"The response emphasizes the specified linguistic feature: {t['linguistic_feature']}",
            "The proposed evaluation methods and applications are well-reasoned and innovative"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
