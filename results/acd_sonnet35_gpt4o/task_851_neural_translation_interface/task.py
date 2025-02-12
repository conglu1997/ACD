import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            {'source': 'Mandarin Chinese', 'target': 'English'},
            {'source': 'Arabic', 'target': 'Spanish'},
            {'source': 'Russian', 'target': 'Japanese'},
            {'source': 'Hindi', 'target': 'French'}
        ]
        return {str(i+1): pair for i, pair in enumerate(random.sample(language_pairs, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical brain-computer interface (BCI) for real-time language translation from {t['source']} to {t['target']}. Your design should consider neurolinguistic principles and address computational challenges. Provide a comprehensive response covering the following aspects:

1. Neural Interface Design (250-300 words):
   a) Describe the key components of your BCI system for language translation.
   b) Explain how your interface would interact with relevant brain regions involved in language processing.
   c) Discuss any invasive or non-invasive technologies your system would employ and justify your choice.
   d) Address potential challenges in accurately detecting and interpreting neural signals related to language.

2. Language Processing Model (200-250 words):
   a) Outline the computational model your BCI would use for language translation.
   b) Explain how your model accounts for linguistic differences between {t['source']} and {t['target']} (e.g., syntax, semantics, phonology).
   c) Describe how your system would handle ambiguities, idioms, or cultural nuances in translation.
   d) Discuss any machine learning or AI components incorporated into your model.

3. Real-time Processing and Output (200-250 words):
   a) Explain how your BCI achieves real-time translation, considering both neural signal processing and language generation.
   b) Describe the output mechanism of your system (e.g., speech synthesis, text display).
   c) Address potential latency issues and propose solutions to minimize delay in translation.

4. Neurolinguistic Considerations (200-250 words):
   a) Discuss how your BCI design aligns with current understanding of bilingual language processing in the brain.
   b) Explain how your system accounts for individual variations in language representation and processing.
   c) Address any potential effects of long-term use of your BCI on the user's cognitive or linguistic abilities.

5. Ethical and Social Implications (150-200 words):
   a) Discuss potential ethical concerns related to your BCI for language translation (e.g., privacy, cognitive liberty).
   b) Explore possible social impacts of widespread use of such technology.
   c) Propose guidelines or safeguards to address these concerns in the development and use of your system.

6. Future Developments and Challenges (150-200 words):
   a) Identify key technological or scientific advancements needed to make your BCI system feasible.
   b) Propose two potential improvements or extensions to your system for future research.
   c) Discuss any limitations of your current design and how they might be addressed in future iterations.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and computational methods. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Format your response using clear headings for each section.

Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, linguistics, and computational methods.",
            "The BCI design is innovative yet scientifically plausible.",
            "The language processing model adequately addresses the specific challenges of translating between the given language pair.",
            "The response covers all required sections with appropriate depth and clarity.",
            "Ethical and social implications are thoughtfully considered.",
            "The proposed system addresses real-time processing challenges and output mechanisms.",
            "Future developments and challenges are realistically assessed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
