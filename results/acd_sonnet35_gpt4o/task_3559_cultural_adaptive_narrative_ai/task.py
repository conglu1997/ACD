import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'culture': 'Japanese',
                'narrative_structure': 'Kishotenketsu',
                'theme': 'harmony with nature',
                'genre': 'magical realism'
            },
            {
                'culture': 'West African',
                'narrative_structure': 'Call and Response',
                'theme': 'coming of age',
                'genre': 'folklore'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating culturally adaptive narratives based on the following parameters:

Culture: {t['culture']}
Narrative Structure: {t['narrative_structure']}
(Kishotenketsu: A four-act structure without conflict. Call and Response: A participatory pattern of alternating statements and replies.)
Theme: {t['theme']}
Genre: {t['genre']}

Your response should include the following sections, adhering to the specified word limits:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for generating culturally adaptive narratives.
   b) Explain how your system incorporates cultural knowledge, narrative theory, and the specified parameters.
   c) Detail any novel AI techniques or algorithms used in your design.
   d) Discuss how your system ensures cultural sensitivity and authenticity.

2. Cultural-Narrative Integration (250-300 words):
   a) Explain how your system represents and utilizes cultural knowledge specific to the given culture.
   b) Describe how the system implements the specified narrative structure.
   c) Discuss how the theme and genre are incorporated into the narrative generation process.

3. Generation Process (250-300 words):
   a) Provide a step-by-step explanation of how your AI system generates a narrative.
   b) Describe how the system adapts the narrative to the specified cultural context.
   c) Explain any techniques used to ensure coherence and engagement in the generated narratives.

4. Evaluation Metrics (200-250 words):
   a) Propose at least three quantitative metrics to evaluate the quality, cultural authenticity, and adherence to the specified parameters of the generated narratives.
   b) Describe a qualitative evaluation method involving human readers from the target culture.
   c) Explain how you would use these evaluations to improve your system.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues related to AI-generated culturally-specific narratives.
   b) Address concerns about cultural appropriation or misrepresentation.
   c) Propose guidelines for the responsible development and use of such AI systems.

6. Sample Output (200-250 words):
   a) Provide a brief outline or summary of a story that your system might generate based on the given parameters.
   b) Explain how this sample demonstrates the cultural adaptation and narrative structure specified.

Ensure your response demonstrates a deep understanding of cultural anthropology, narrative theory, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section (e.g., '1. System Architecture', '2. Cultural-Narrative Integration', etc.). Begin each subsection with the corresponding letter (a, b, c, etc.). Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and adheres to the specified word limits.",
            "The response is formatted with clear headings for each section and subsections labeled with letters.",
            "The system architecture demonstrates a clear understanding of AI, cultural knowledge representation, and narrative generation.",
            "The cultural-narrative integration section shows a deep understanding of the specified culture and narrative structure.",
            "The generation process is clearly explained and addresses cultural adaptation.",
            "Proposed evaluation metrics are relevant and well-justified.",
            "Ethical considerations are thoughtfully addressed.",
            "The sample output demonstrates appropriate cultural adaptation and use of the specified narrative structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
