import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "theory": "Structuralism",
                "text": "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair."
            },
            {
                "theory": "Postcolonialism",
                "text": "The white man's burden: Take up the White Man's burden— Send forth the best ye breed— Go bind your sons to exile To serve your captives' need; To wait in heavy harness, On fluttered folk and wild— Your new-caught, sullen peoples, Half-devil and half-child."
            },
            {
                "theory": "Feminist Criticism",
                "text": "A woman must have money and a room of her own if she is to write fiction."
            },
            {
                "theory": "Psychoanalytic Criticism",
                "text": "One day, in retrospect, the years of struggle will strike you as the most beautiful."
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given literary text using natural language processing techniques and interpret it through the lens of {t['theory']}. Your task is to:

1. Text Analysis (150-200 words):
   a) Perform a basic NLP analysis of the text, including tokenization, part-of-speech tagging, and named entity recognition.
   b) Identify key linguistic features such as word frequency, sentence structure, and any notable patterns.
   c) Explain how these features contribute to the overall meaning or effect of the text.

2. Literary Theory Application (200-250 words):
   a) Briefly explain the main principles of {t['theory']}.
   b) Apply these principles to interpret the given text.
   c) Identify specific elements in the text that align with or challenge the theory's assumptions.

3. Computational Creativity (150-200 words):
   a) Generate a creative interpretation or extension of the text based on your analysis and the applied theory.
   b) Explain how your interpretation builds on the original text and the principles of {t['theory']}.

4. Reflection (100-150 words):
   a) Discuss the strengths and limitations of using computational methods for literary analysis.
   b) Propose one way in which NLP techniques could be further developed to enhance literary interpretation.

Ensure your response demonstrates a deep understanding of both computational linguistics and literary theory. Be creative in your interpretation while maintaining analytical rigor.

The text to analyze is:
"{t['text']}"

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the given text and apply {t['theory']} in its analysis",
            "The NLP analysis should be accurate and insightful",
            "The literary theory application should demonstrate a deep understanding of the theory's principles",
            "The creative interpretation should be original and well-connected to both the text and the theory",
            "The reflection should show critical thinking about the use of computational methods in literary analysis"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
