import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_focus': 'Working memory enhancement',
                'linguistic_feature': 'Morphological system',
                'cognitive_principle': 'Chunking: grouping individual pieces of information into larger units'
            },
            {
                'cognitive_focus': 'Spatial reasoning improvement',
                'linguistic_feature': 'Grammatical structure',
                'cognitive_principle': 'Mental rotation: the ability to rotate mental representations of objects'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) optimized for human cognitive processing, focusing on {t['cognitive_focus']} through its {t['linguistic_feature']}. Your conlang should incorporate the cognitive principle of {t['cognitive_principle']}.

Your task has five parts:

1. Conlang Overview (100-150 words):
   a) Provide a name for your conlang and explain its intended purpose.
   b) Briefly describe how it aims to enhance {t['cognitive_focus']}.
   c) Explain how the {t['linguistic_feature']} of your conlang relates to the cognitive principle.

2. Linguistic Feature Design (200-250 words):
   a) Describe in detail how the {t['linguistic_feature']} of your conlang is structured.
   b) Explain how this structure incorporates the cognitive principle of {t['cognitive_principle']}.
   c) Provide at least three examples of this feature in use, with translations and explanations.

3. Cognitive Enhancement Analysis (150-200 words):
   a) Analyze how your conlang's design could potentially enhance {t['cognitive_focus']}.
   b) Discuss any potential challenges or limitations of your approach.
   c) Propose a hypothetical experiment to test the cognitive benefits of your conlang.

4. Comparative Analysis (100-150 words):
   a) Compare your conlang to an existing natural language in terms of its approach to {t['cognitive_focus']}.
   b) Identify at least one similarity and one significant difference.

5. Practical Application (100-150 words):
   a) Suggest a real-world scenario where your conlang could be particularly useful.
   b) Explain how its cognitive optimization features would provide advantages in this context.

Ensure your response demonstrates a deep understanding of linguistic principles, cognitive science, and their practical applications. Be creative in your language design while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang design is creative and original, while being grounded in linguistic and cognitive science principles.",
            f"The {t['linguistic_feature']} of the conlang clearly incorporates the cognitive principle of {t['cognitive_principle']}.",
            f"The conlang design demonstrates a plausible approach to enhancing {t['cognitive_focus']}.",
            "The response includes clear examples and explanations for all required components.",
            "The comparative analysis and practical application sections show insightful understanding of the conlang's potential impacts and uses.",
            "The overall response demonstrates strong interdisciplinary thinking and application of knowledge from linguistics and cognitive science."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
