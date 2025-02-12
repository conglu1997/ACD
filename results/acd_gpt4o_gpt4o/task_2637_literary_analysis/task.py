class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "literary_excerpt": "In this excerpt from 'To Kill a Mockingbird' by Harper Lee, Atticus Finch delivers his closing argument in the trial of Tom Robinson. Analyze the themes of racial injustice and moral integrity as presented in this passage.",
                "book_title": "To Kill a Mockingbird"
            },
            "2": {
                "literary_excerpt": "In this excerpt from '1984' by George Orwell, Winston Smith grapples with his thoughts on freedom and oppression. Discuss the motifs of totalitarianism and individualism in this passage.",
                "book_title": "1984"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        literary_excerpt = t["literary_excerpt"]
        book_title = t["book_title"]
        instructions = f"""Your task is to analyze and interpret the following literary excerpt from the book '{book_title}'.

Literary Excerpt: {literary_excerpt}

Provide your analysis in plain text format. Ensure that your analysis includes a discussion of the themes, motifs, and character development presented in the passage. Your response should demonstrate a deep understanding of the text and offer insightful interpretations. Structure your response as follows:
- Introduction: [Brief introduction to the passage and its context in the book]
- Themes: [Analysis of the key themes]
- Motifs: [Discussion of recurring motifs]
- Character Development: [Examination of character development in the passage]
- Conclusion: [Summary of your analysis]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be accurate and insightful.",
            "The analysis should demonstrate a deep understanding of the text.",
            "The response should be well-structured, following the given format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
