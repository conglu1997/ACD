class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "domain1": "Quantum Physics",
                "domain2": "Social Media",
                "target_genre": "Science Fiction Short Story"
            },
            "2": {
                "domain1": "Renaissance Art",
                "domain2": "Artificial Intelligence",
                "target_genre": "Academic Essay"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a conceptual blend combining {t['domain1']} and {t['domain2']}, and then use this blend to generate a creative {t['target_genre']}. Follow these steps:

1. Conceptual Blend Design (200-250 words):
   a) Identify key concepts, structures, or elements from both {t['domain1']} and {t['domain2']}.
   b) Explain how you will integrate these elements to create a novel conceptual blend.
   c) Describe the emergent structure that arises from this blend.

2. Blend Analysis (150-200 words):
   a) Discuss how your blend adheres to principles of conceptual integration theory.
   b) Explain any conceptual clashes or resolutions in your blend.
   c) Analyze the potential cognitive implications of your blend.

3. Creative Text Generation (300-400 words):
   Write a {t['target_genre']} that incorporates your conceptual blend. Ensure that the text demonstrates a deep understanding of both source domains and creatively explores the emergent structure of the blend.

4. Language Model Evaluation (200-250 words):
   a) Propose three questions or tasks that would test a language model's understanding of your conceptual blend.
   b) For each question/task, explain what aspect of conceptual integration it evaluates and what would constitute a successful response.

5. Reflection and Extension (100-150 words):
   a) Discuss the potential applications or implications of your conceptual blend beyond this task.
   b) Propose one way to extend or modify your blend to create an even more complex integration.

Ensure your response demonstrates creativity, coherence, and a deep understanding of both source domains and conceptual blending principles. Use appropriate terminology from cognitive science and the relevant domains."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conceptual blend effectively combines elements from {t['domain1']} and {t['domain2']}.",
            "The blend analysis demonstrates understanding of conceptual integration theory.",
            f"The generated {t['target_genre']} creatively incorporates the conceptual blend.",
            "The proposed language model evaluation questions are relevant and well-explained.",
            "The reflection shows insight into broader applications of the conceptual blend."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
