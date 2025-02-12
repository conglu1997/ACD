import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        themes = [
            {
                "theme": "The Butterfly Effect",
                "description": "Small actions leading to significant consequences across multiple timelines."
            },
            {
                "theme": "Parallel Universes",
                "description": "The same event unfolding differently in alternate realities."
            },
            {
                "theme": "Time Loops",
                "description": "Characters trapped in repeating time cycles with subtle variations."
            },
            {
                "theme": "Interconnected Strangers",
                "description": "Seemingly unrelated characters whose lives intersect in unexpected ways."
            }
        ]
        return {str(i+1): theme for i, theme in enumerate(random.sample(themes, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and analyzing complex non-linear narratives across multiple timelines and perspectives, then use it to create a multi-dimensional story based on the theme: {t['theme']} - {t['description']}. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for non-linear narrative generation and analysis.
   b) Explain how your system represents and manages multiple timelines, perspectives, and narrative threads.
   c) Detail the process of generating coherent non-linear narratives while maintaining thematic consistency.
   d) Discuss any novel techniques or approaches used in your design, such as neural networks, knowledge graphs, or other AI technologies.

2. Narrative Structure and Analysis (250-300 words):
   a) Explain how your system analyzes and understands complex narrative structures.
   b) Describe the methods used to ensure coherence and consistency across non-linear elements.
   c) Discuss how your system incorporates principles of human psychology and cultural contexts in narrative creation.

3. Story Generation (400-450 words):
   Generate a brief multi-dimensional story based on the given theme. Your story should include:
   a) At least three interconnected timelines or perspectives.
   b) Non-linear elements such as time jumps, parallel universes, or intersecting character arcs.
   c) A coherent overarching narrative that ties the non-linear elements together.
   d) Thematic consistency with the given theme.

4. Narrative Analysis (200-250 words):
   a) Analyze the generated story, explaining how it demonstrates non-linear storytelling techniques.
   b) Discuss the challenges your AI system faced in creating this narrative and how it overcame them.
   c) Explain how the story reflects human psychology and cultural elements.

5. Evaluation and Refinement (150-200 words):
   a) Propose metrics to evaluate your AI system's performance in generating non-linear narratives.
   b) Describe how you would refine and improve your system based on these evaluations.
   c) Discuss potential biases or limitations in your approach and how you might address them.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical implications of using AI for creative writing and narrative generation.
   b) Explore the broader societal impacts of AI-generated non-linear narratives in literature, film, or other media.
   c) Propose guidelines for responsible development and use of such AI systems in creative industries.

Ensure your response demonstrates a deep understanding of narrative theory, creative writing, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining plausibility in both the AI system design and the generated story.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed description of an AI system architecture for non-linear narrative generation and analysis",
            "The system design demonstrates a deep understanding of narrative theory and AI technologies",
            "The generated story effectively incorporates the given theme and demonstrates non-linear storytelling techniques",
            "The narrative analysis shows insight into the challenges and solutions of non-linear storytelling",
            "The response addresses ethical implications and societal impacts of AI-generated narratives",
            "The overall submission is creative, well-structured, and within the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
