import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "language_pair": "Mandarin Chinese and Spanish",
                "cognitive_function": "executive control",
                "brain_region": "prefrontal cortex",
                "linguistic_feature": "tonal system"
            },
            {
                "language_pair": "Arabic and Japanese",
                "cognitive_function": "working memory",
                "brain_region": "hippocampus",
                "linguistic_feature": "script differences"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates neural processes involved in language acquisition and multilingualism, then use it to explore the implications of multilingual experience on cognitive functions. Focus on the language pair: {t['language_pair']}, the cognitive function of {t['cognitive_function']}, and incorporate neural activity in the {t['brain_region']}. Pay special attention to the linguistic feature of {t['linguistic_feature']}. Your response should include:

1. Neurolinguistic Framework (300-350 words):
   a) Explain the current understanding of neural processes involved in acquiring and using the specified language pair.
   b) Describe how the {t['brain_region']} is involved in language processing and {t['cognitive_function']}.
   c) Discuss how the {t['linguistic_feature']} might influence neural activity and language acquisition.

2. AI System Architecture (300-350 words):
   a) Outline the key components of your AI system for simulating neurolinguistic processes.
   b) Explain how your system models neural activity in the {t['brain_region']}.
   c) Describe how the AI integrates linguistic data and cognitive function measurements.
   d) Discuss any novel features or innovations in your AI design for this specific application.

3. Language Acquisition Simulation (250-300 words):
   a) Explain how your AI system simulates the acquisition of the specified language pair.
   b) Describe how it models the learning of the {t['linguistic_feature']}.
   c) Discuss how your approach differs from traditional language acquisition models.
   d) Provide a hypothetical example of a specific insight your system might generate about language acquisition.

4. Multilingualism and Cognitive Function Analysis (250-300 words):
   a) Describe how your system analyzes the impact of multilingualism on {t['cognitive_function']}.
   b) Explain the methods used to simulate and measure changes in cognitive function.
   c) Discuss potential findings about how mastering the specified language pair might affect {t['cognitive_function']}.
   d) Propose a novel hypothesis about multilingualism and cognition that your system could test.

5. Data Requirements and Challenges (200-250 words):
   a) Specify the types of data your AI system would require for training and operation.
   b) Discuss challenges in obtaining or generating relevant neurolinguistic and cognitive data.
   c) Propose innovative solutions to address these data-related challenges.

6. Ethical Considerations and Societal Impact (200-250 words):
   a) Identify potential ethical issues in using AI to simulate and analyze neurolinguistic processes.
   b) Discuss the potential societal impacts of your system's findings on language education and cognitive health.
   c) Propose guidelines for responsible development and use of such advanced neurolinguistic AI systems.

7. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or modifications to your system for future research.
   b) Discuss how your approach could be applied to other areas of cognitive science or linguistics.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, artificial intelligence, and cognitive science. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering to the word limits provided. Your total response should be between 1650-2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neurolinguistics, AI system design, and cognitive science.",
            "The proposed AI system effectively integrates knowledge from multiple disciplines and simulates neural processes involved in language acquisition and multilingualism.",
            "The analysis of multilingualism's impact on cognitive functions is well-reasoned and grounded in current scientific understanding.",
            "The response addresses the specific language pair, cognitive function, brain region, and linguistic feature mentioned in the prompt.",
            "The ethical considerations and societal impacts are thoughtfully discussed.",
            "The proposed future research directions are innovative and relevant.",
            "The response is well-structured, adhering to the specified format and word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
