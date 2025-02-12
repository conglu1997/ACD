import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "Mental rotation",
            "Gestalt principles of perception",
            "Visuospatial working memory",
            "Attentional spotlight"
        ]
        programming_paradigms = [
            "Object-oriented programming",
            "Functional programming",
            "Logic programming",
            "Dataflow programming"
        ]
        return {
            "1": {
                "cognitive_principle": random.choice(cognitive_principles),
                "programming_paradigm": random.choice(programming_paradigms)
            },
            "2": {
                "cognitive_principle": random.choice(cognitive_principles),
                "programming_paradigm": random.choice(programming_paradigms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a visual programming language based on the cognitive principle of {t['cognitive_principle']} and incorporating elements of the {t['programming_paradigm']} paradigm. Your response should include the following sections:

1. Language Design (300-350 words):
   a) Describe the key features of your visual programming language and how it incorporates the given cognitive principle.
   b) Explain how you've integrated elements of the specified programming paradigm.
   c) Provide a high-level description or visual representation of your language's syntax and structure.
   d) Discuss any novel visual elements or interactions you've designed for this language.

2. Cognitive Science Foundation (200-250 words):
   a) Analyze how your language design reflects current understanding of {t['cognitive_principle']}.
   b) Explain how the visual nature of the language might enhance or challenge cognitive processes related to programming.
   c) Propose a hypothesis about how your language might affect learning and problem-solving in programming.

3. Implementation and Usage (200-250 words):
   a) Describe how programmers would create and edit code in your visual language.
   b) Explain the compilation or interpretation process for your language.
   c) Discuss potential advantages or limitations of your language compared to traditional text-based languages.

4. Application Domains (150-200 words):
   a) Suggest potential real-world applications or domains where your visual programming language would be particularly effective.
   b) Discuss how these applications might impact fields such as education, software development, or cognitive rehabilitation.

5. Comparative Analysis (200-250 words):
   a) Compare your language to existing visual programming languages or environments.
   b) Analyze how your language's cognitive basis might provide advantages over other approaches.
   c) Discuss any potential challenges or limitations of your approach.

6. Future Directions (150-200 words):
   a) Propose extensions or modifications to your language to incorporate other cognitive principles or programming paradigms.
   b) Discuss how advancements in display technology or input devices might enhance the capabilities of your language.
   c) Suggest areas of future research at the intersection of visual programming and cognitive science inspired by your work.

Ensure your response demonstrates a deep understanding of both programming language theory and cognitive science principles. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology from both fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections with appropriate content and word counts.",
            f"The language design clearly incorporates the cognitive principle of {t['cognitive_principle']}.",
            f"The language design integrates elements of the {t['programming_paradigm']} paradigm.",
            "The response demonstrates a deep understanding of both programming language theory and cognitive science.",
            "The proposed visual programming language is innovative and scientifically plausible.",
            "The response includes a clear analysis of potential applications, advantages, and limitations of the proposed language."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
