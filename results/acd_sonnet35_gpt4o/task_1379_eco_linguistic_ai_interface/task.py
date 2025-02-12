import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "ecosystem": "Coral reef",
                "environmental_change": "Ocean acidification",
                "linguistic_focus": "Verb tense system"
            },
            {
                "ecosystem": "Boreal forest",
                "environmental_change": "Permafrost thaw",
                "linguistic_focus": "Noun classification system"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-powered linguistic interface that translates the dynamics of a {t['ecosystem']} ecosystem into a constructed language, with a focus on representing {t['environmental_change']} through the language's {t['linguistic_focus']}. Then, use this interface to analyze and communicate the complex environmental changes occurring in the ecosystem.

Your response should include the following sections:

1. Linguistic Interface Design (200-250 words):
   a) Describe the key features of your constructed language, focusing on how the {t['linguistic_focus']} represents ecosystem dynamics.
   b) Explain how your language specifically encodes information about {t['environmental_change']}.
   c) Provide examples of how key ecological concepts are expressed in your language.
   d) Describe how the AI system translates between ecosystem data and your constructed language.

2. Ecosystem Representation (150-200 words):
   a) Explain how your language captures the complexity of the {t['ecosystem']} ecosystem.
   b) Describe how interactions between different components of the ecosystem are represented.
   c) Provide an example sentence or phrase in your language that describes a specific aspect of {t['environmental_change']}, with a translation and explanation.

3. AI Translation Process (150-200 words):
   a) Outline the AI system's process for translating ecological data into your constructed language.
   b) Describe how the AI handles uncertainty or incomplete data in the translation process.
   c) Explain how the system ensures accuracy and consistency in its translations.

4. Environmental Analysis Application (150-200 words):
   a) Describe how your AI-powered linguistic interface could be used to analyze {t['environmental_change']} in the {t['ecosystem']}.
   b) Provide an example of an insight about {t['environmental_change']} that might be revealed through this linguistic analysis.
   c) Explain how this system could aid in communicating complex environmental changes to different audiences (e.g., scientists, policymakers, public).

5. Limitations and Ethical Considerations (100-150 words):
   a) Discuss potential limitations of your linguistic interface in representing ecosystem dynamics.
   b) Address any ethical concerns related to using AI and constructed languages for environmental analysis.
   c) Propose safeguards or guidelines for the responsible use of this technology.

6. Visual Representation (Include as ASCII art or text-based diagram):
   Provide a visual representation of your linguistic interface, showing how it connects ecosystem dynamics, AI processing, and language output. This should be a flowchart or concept map that includes at least 5 key components and their relationships.

7. Glossary (5-10 terms):
   Provide a brief glossary of key terms in your constructed language, including their meanings and how they relate to the {t['ecosystem']} and {t['environmental_change']}.

Ensure your response demonstrates a deep understanding of linguistics, artificial intelligence, and environmental science. Be creative in your approach while maintaining scientific plausibility and rigor. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Your total response should be between 750-1000 words, excluding the visual representation and glossary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, AI, and environmental science, integrating concepts from all three fields.",
            "The linguistic interface design is creative, coherent, and effectively represents ecosystem dynamics, with a clear focus on the specified linguistic aspect.",
            "The AI translation process is well-explained, plausible, and addresses issues of uncertainty and consistency.",
            "The application to environmental analysis is insightful and demonstrates the potential of the system for both analysis and communication.",
            "Limitations and ethical considerations are thoughtfully addressed with specific examples and proposed solutions.",
            "A visual representation of the linguistic interface is provided and effectively communicates the system's structure, including at least 5 key components and their relationships.",
            "The glossary of key terms is coherent, creative, and clearly relates to the specified ecosystem and environmental change."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
