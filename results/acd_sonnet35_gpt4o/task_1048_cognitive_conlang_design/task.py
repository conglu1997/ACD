import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_aspects = [
            "working memory",
            "pattern recognition",
            "logical reasoning",
            "spatial cognition"
        ]
        machine_processing_goals = [
            "natural language understanding",
            "machine translation",
            "semantic parsing",
            "knowledge representation"
        ]
        return {
            "1": {
                "cognitive_aspect": random.choice(cognitive_aspects),
                "machine_processing_goal": random.choice(machine_processing_goals)
            },
            "2": {
                "cognitive_aspect": random.choice(cognitive_aspects),
                "machine_processing_goal": random.choice(machine_processing_goals)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) that optimizes for the cognitive aspect of {t['cognitive_aspect']} in humans and the machine processing goal of {t['machine_processing_goal']}. Your response should include:

1. Language Structure (250-300 words):
   a) Describe the phonology, morphology, and syntax of your conlang.
   b) Explain how these elements are specifically designed to enhance {t['cognitive_aspect']} in human users.
   c) Discuss how the language structure facilitates {t['machine_processing_goal']} for AI systems.

2. Vocabulary and Semantics (200-250 words):
   a) Explain the principles behind your conlang's vocabulary design.
   b) Describe any unique semantic features that aid in {t['cognitive_aspect']} or {t['machine_processing_goal']}.
   c) Provide 3-5 example words or phrases in your conlang, with translations and explanations of their cognitive/computational significance.

3. Cognitive Analysis (200-250 words):
   a) Analyze how your conlang might affect cognitive processes related to {t['cognitive_aspect']}.
   b) Discuss potential cognitive advantages or challenges for human users of this language.
   c) Compare your conlang's cognitive impacts to those of natural languages.

4. Computational Analysis (200-250 words):
   a) Explain how your conlang facilitates {t['machine_processing_goal']} for AI systems.
   b) Describe potential algorithms or data structures that would be particularly effective for processing this language.
   c) Discuss any trade-offs between human usability and machine processability in your design.

5. Learning and Adoption (150-200 words):
   a) Propose a method for teaching this language to human learners.
   b) Discuss potential challenges in widespread adoption of the language.
   c) Suggest applications where your conlang would be particularly beneficial.

6. Ethical and Societal Implications (100-150 words):
   a) Discuss potential ethical concerns of a language designed to optimize cognition and machine processing.
   b) Consider the societal impacts of widespread use of such a language.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and natural language processing. Be creative in your language design while maintaining scientific plausibility. Use appropriate terminology from each field and provide clear explanations where necessary.

Format your response with clear headings for each section and adhere to the specified word counts. The total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang design demonstrates a clear understanding of the specified cognitive aspect and machine processing goal.",
            "The language structure and vocabulary are creative and well-reasoned, with clear explanations of their cognitive and computational benefits.",
            "The analysis of cognitive and computational impacts is thorough and scientifically plausible.",
            "The response addresses all six points in the instructions comprehensively.",
            "The explanation demonstrates interdisciplinary knowledge of linguistics, cognitive science, and computer science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
