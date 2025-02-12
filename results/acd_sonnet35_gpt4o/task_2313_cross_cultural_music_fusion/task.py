import random
import json

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_traditions = [
            {"tradition1": "Western Classical", "tradition2": "Indian Classical"},
            {"tradition1": "Jazz", "tradition2": "Traditional Chinese"}
        ]
        return {str(i+1): tradition for i, tradition in enumerate(musical_traditions)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You have 90 minutes to complete this task. Design and analyze a cross-cultural fusion music composition combining elements from {t['tradition1']} and {t['tradition2']} musical traditions. Then, use your analysis to generate variations or new compositions. Your response should include the following sections:

1. Composition Design (250-300 words):
   a) Describe the key elements you will incorporate from each musical tradition.
   b) Explain how you will fuse these elements in a coherent and innovative way.
   c) Outline the structure of your composition (e.g., movements, sections).
   d) Discuss the instrumentation and any novel techniques you will employ.
   e) Provide a detailed musical notation or diagram illustrating at least one full measure of your composition, including tempo, key signature, time signature, and any specific performance instructions.

2. Musical Analysis (200-250 words):
   a) Analyze the harmonic structure of your composition.
   b) Explain the rhythmic patterns and how they reflect each tradition.
   c) Discuss the melodic themes and their cultural significance.
   d) Describe how your composition achieves a balance between the two traditions.

3. Cultural and Emotional Expression (200-250 words):
   a) Explain the cultural significance of specific elements in your composition.
   b) Discuss how your composition expresses or evokes particular emotions.
   c) Analyze potential cultural implications or receptions of your fusion work.

4. Comparative Analysis (200-250 words):
   a) Compare your fusion approach to one historical and one contemporary cross-cultural music example.
   b) Discuss the similarities and differences in technique, cultural representation, and overall effectiveness.
   c) Explain how your approach contributes uniquely to the field of cross-cultural music.

5. Variation Generation (200-250 words):
   a) Propose two variations of your original composition, each emphasizing different aspects of the fusion.
   b) Explain the key changes in each variation and their musical and cultural implications.
   c) Discuss how these variations demonstrate the flexibility and richness of your fusion approach.

6. Novel Composition Generation (200-250 words):
   a) Based on your fusion approach, propose a completely new composition combining two different musical traditions.
   b) Briefly outline its structure, key elements, and cultural significance.
   c) Explain how this demonstrates the generalizability of your fusion technique.

7. Technological Implementation (150-200 words):
   a) Discuss the potential challenges in implementing your composition using AI or digital music tools.
   b) Propose innovative ways to overcome these challenges.
   c) Explain how technology could enhance or limit the cultural authenticity of your fusion.

8. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of cross-cultural music fusion, addressing issues such as cultural appropriation and representation.
   b) Explain how your composition navigates these ethical considerations.
   c) Propose guidelines for ethical practice in cross-cultural music fusion.

9. Reflection and Evaluation (150-200 words):
   a) Discuss the challenges you encountered in creating these cross-cultural fusion compositions.
   b) Reflect on the potential of AI in understanding and generating culturally nuanced music.
   c) Propose criteria for evaluating the success and authenticity of cross-cultural music fusion.

Ensure your response demonstrates a deep understanding of music theory, cultural studies, and creative composition. Use appropriate musical terminology and provide clear explanations for your creative decisions. Be innovative in your approach while respecting the integrity of each musical tradition.

Format your response with clear headings for each section. For the musical notation or diagram, you may use ASCII art or a text-based representation, but ensure it includes all required elements (tempo, key signature, time signature, and performance instructions)."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both musical traditions mentioned in the task. (0.1)",
            "The composition design effectively fuses elements from both traditions in an innovative way. (0.1)",
            "The musical analysis shows a strong grasp of music theory and cultural significance. (0.1)",
            "The comparative analysis effectively contrasts the proposed fusion with both historical and contemporary examples. (0.1)",
            "The variations and novel composition demonstrate creativity and understanding of the fusion technique. (0.1)",
            "The technological implementation section shows awareness of challenges and proposes innovative solutions. (0.1)",
            "The ethical considerations section thoughtfully addresses cultural appropriation and representation. (0.1)",
            "The reflection shows insight into the challenges and potential of cross-cultural music fusion. (0.1)",
            "The response uses appropriate musical terminology and provides clear explanations for creative decisions. (0.1)",
            "A detailed musical notation or diagram is provided, including tempo, key signature, time signature, and performance instructions. (0.1)",
            "All required sections (1-9) are addressed comprehensively and meet the specified word counts. (0.1)"
        ]
        score = sum([0.1 for criterion in criteria if eval_with_llm_judge(instructions, submission, [criterion])])
        return score
