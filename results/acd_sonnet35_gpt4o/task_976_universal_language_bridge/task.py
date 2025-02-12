import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "Embodied cognition",
            "Predictive processing",
            "Dual-process theory",
            "Connectionism"
        ]
        language_features = [
            "Recursion",
            "Compositionality",
            "Polysemy",
            "Pragmatics"
        ]
        tasks = {}
        for i in range(2):  # Ensure exactly two tasks are generated
            tasks[str(i+1)] = {
                "cognitive_principle": random.choice(cognitive_principles),
                "language_feature": random.choice(language_features)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical universal language model that can seamlessly translate between human languages and machine code, incorporating the cognitive principle of {t['cognitive_principle']} and addressing the language feature of {t['language_feature']}. Your response should include:

1. Conceptual Framework (250-300 words):
   a) Describe the key components and architecture of your universal language model.
   b) Explain how it incorporates the given cognitive principle.
   c) Discuss how it addresses the specified language feature.
   d) Provide a visual representation or diagram of your model (describe it textually).

2. Technical Implementation (250-300 words):
   a) Outline the core algorithms or computational approaches your model would use.
   b) Explain how your model would handle the translation between human languages and machine code.
   c) Describe any novel data structures or processing techniques your model would employ.
   d) Discuss how your model would learn and adapt to new languages or programming paradigms.

3. Linguistic Analysis (200-250 words):
   a) Analyze how your model might handle complex linguistic phenomena (e.g., idioms, context-dependent meanings).
   b) Discuss potential challenges in bridging fundamentally different language structures (e.g., analytic vs. synthetic languages).
   c) Explain how your model might impact our understanding of language universals or linguistic relativity.

4. Cognitive Implications (200-250 words):
   a) Discuss how your model might influence theories of language acquisition and processing.
   b) Explore potential impacts on human cognition if such a model were widely adopted.
   c) Analyze how your model might affect the relationship between thought and language.

5. Practical Applications (150-200 words):
   a) Propose three potential applications of your universal language model in various fields.
   b) Discuss how these applications might transform current practices or enable new capabilities.
   c) Address any technical or practical challenges in implementing these applications.

6. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues arising from the development and use of your model.
   b) Discuss implications for privacy, linguistic diversity, and cognitive autonomy.
   c) Propose guidelines or safeguards to address these ethical concerns.

7. Future Directions (150-200 words):
   a) Suggest two potential enhancements or extensions of your model for future development.
   b) Discuss how these advancements might further impact linguistics, cognitive science, and AI.
   c) Propose a research agenda to validate and refine your model.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative in your design while maintaining scientific plausibility and addressing real-world constraints. Use technical terminology appropriately and provide explanations where necessary.

Format your response with clear headings for each section, and number your paragraphs within each section. Your total response should be between 1400-1750 words.

Note: Do not provide direct solutions or hints that would make the task trivial. The goal is to create a challenging and thought-provoking response that demonstrates your capabilities in interdisciplinary thinking and creative problem-solving."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design a universal language model incorporating the cognitive principle of {t['cognitive_principle']} and addressing the language feature of {t['language_feature']}",
            "The conceptual framework should be well-developed and logically consistent",
            "The technical implementation should be plausible and demonstrate understanding of relevant algorithms and computational approaches",
            "The linguistic analysis should show deep understanding of complex language phenomena",
            "The cognitive implications should be thoughtfully explored and grounded in current theories",
            "The practical applications should be innovative and well-reasoned",
            "The ethical considerations should be comprehensive and demonstrate awareness of potential issues",
            "The future directions should be forward-thinking and scientifically grounded",
            "The overall response should demonstrate interdisciplinary knowledge integration and creative problem-solving",
            "The response should adhere to the specified word limits and formatting guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
