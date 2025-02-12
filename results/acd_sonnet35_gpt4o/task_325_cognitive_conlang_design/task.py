import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'purpose': 'enhancing spatial reasoning',
                'target_user': 'human learners'
            },
            {
                'purpose': 'facilitating human-AI communication',
                'target_user': 'AI systems'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) optimized for {t['purpose']}, targeting {t['target_user']}. Your task has six parts:

1. Language Design (300-350 words):
   a) Describe the key features of your conlang, including its phonology, morphology, and syntax.
   b) Explain how these features are specifically designed to serve the purpose of {t['purpose']}.
   c) Provide three example sentences in your conlang, with translations and explanations of how they demonstrate its unique features.

2. Cognitive Impact Analysis (250-300 words):
   a) Analyze how your conlang might influence or enhance cognitive processes related to {t['purpose']}.
   b) Discuss any potential cognitive trade-offs or limitations of your language design.
   c) Compare your conlang's potential cognitive effects with those of natural languages.

3. Implementation for {t['target_user']} (200-250 words):
   a) Propose a method for teaching or implementing your conlang for {t['target_user']}.
   b) Discuss potential challenges in adoption and how they might be overcome.
   c) Suggest an experiment to test the effectiveness of your conlang in achieving its purpose.

4. Broader Implications (200-250 words):
   a) Explore the potential impacts of widespread adoption of your conlang on society, education, or technology.
   b) Discuss ethical considerations related to designing languages for specific cognitive purposes.
   c) Propose how insights from your conlang design could inform natural language processing or AI development.

5. Interdisciplinary Connections (150-200 words):
   a) Explain how your conlang design incorporates principles from linguistics, cognitive science, and computer science.
   b) Discuss how this interdisciplinary approach contributes to the effectiveness of your language design.
   c) Suggest a potential collaboration between experts in different fields to further develop or study your conlang.

6. Critical Analysis (150-200 words):
   a) Discuss potential unintended consequences of your conlang design.
   b) Analyze possible ways in which the language might be misused or exploited.
   c) Propose safeguards or modifications to mitigate these risks.

7. Glossary (100-150 words):
   Provide a brief glossary of 5-7 key linguistic terms used in your response, demonstrating your understanding of these concepts.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and relevant aspects of computer science or AI. Be creative in your language design while maintaining scientific plausibility and addressing potential limitations or challenges.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a conlang optimized for {t['purpose']}, targeting {t['target_user']}.",
            "The language design is creative and demonstrates key features of phonology, morphology, and syntax.",
            "Three example sentences in the conlang are provided with translations and explanations.",
            "The cognitive impact analysis is thorough and considers both potential benefits and limitations.",
            f"A plausible implementation method for {t['target_user']} is proposed, along with an experimental design.",
            "The response explores broader implications and ethical considerations of the conlang.",
            "The design demonstrates integration of principles from linguistics, cognitive science, and computer science.",
            "Potential unintended consequences and safeguards are discussed.",
            "A glossary of 5-7 key linguistic terms is provided, demonstrating understanding of these concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
