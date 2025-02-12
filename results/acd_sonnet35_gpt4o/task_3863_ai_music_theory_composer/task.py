import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_styles = [
            "Baroque",
            "Romantic",
            "Jazz",
            "Minimalist",
            "Electronic"
        ]
        emotions = [
            "Joy",
            "Melancholy",
            "Tension",
            "Serenity",
            "Excitement"
        ]
        advanced_techniques = [
            "Polyrhythms",
            "Modulations",
            "Extended harmonies",
            "Microtonal intervals",
            "Aleatoric elements"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "musical_style": random.choice(musical_styles),
                "target_emotion": random.choice(emotions),
                "advanced_technique": random.choice(advanced_techniques)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze complex musical structures and emotional content, then use it to compose original music in the {t['musical_style']} style while evoking the emotion of {t['target_emotion']} and incorporating the advanced technique of {t['advanced_technique']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI music analysis and composition system.
   b) Explain how your system integrates music theory knowledge with emotional intelligence.
   c) Detail the machine learning techniques or algorithms used in your system.
   d) Provide a high-level diagram or pseudocode (10-15 lines) illustrating your system's structure.

2. Musical Analysis Approach (250-300 words):
   a) Explain how your system analyzes existing music in the specified style.
   b) Describe the features or patterns your system would identify to capture the essence of the style.
   c) Discuss how your system recognizes and quantifies emotional content in music.
   d) Explain how your system identifies and analyzes the specified advanced technique.

3. Composition Process (250-300 words):
   a) Detail how your AI system generates original music in the specified style.
   b) Explain the methods used to ensure the composition evokes the target emotion.
   c) Describe how your system incorporates the specified advanced technique in the composition.
   d) Discuss any novel techniques your system employs to balance stylistic accuracy with creativity.

4. Sample Output Description (150-200 words):
   Provide a detailed description of what a sample AI-generated composition might sound like, including:
   a) The overall structure and progression of the piece.
   b) Specific musical elements that reflect the chosen style and emotion.
   c) How the advanced technique is manifested in the composition.

5. Evaluation Metrics (200-250 words):
   a) Propose specific metrics to evaluate the stylistic accuracy of the AI-generated compositions.
   b) Suggest methods to assess the emotional impact of the generated music.
   c) Describe how you would validate the originality of the AI's compositions.
   d) Propose a method to evaluate the effective use of the specified advanced technique.

6. Challenges and Solutions (200-250 words):
   a) Identify potential challenges in implementing your AI music composition system.
   b) Propose solutions or approaches to address these challenges.
   c) Discuss any ethical considerations related to AI-generated music and how you'd address them.

7. Broader Implications (150-200 words):
   a) Explore how your AI system might impact the field of music composition and theory.
   b) Discuss potential applications of your system beyond music composition.
   c) Reflect on how this technology might influence our understanding of creativity and emotion in music.

Ensure your response demonstrates a deep understanding of both music theory and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and artistic plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both music theory and artificial intelligence",
            "The proposed AI system effectively integrates analysis of musical structures with emotional content",
            "The composition process is well-explained and plausibly combines stylistic accuracy with creativity",
            "The system adequately incorporates and explains the use of the specified advanced technique",
            "The sample output description vividly illustrates the AI-generated composition",
            "The evaluation metrics and challenges are thoughtfully considered and addressed",
            "The response is well-structured, clear, uses appropriate technical terminology, and meets the word count requirement"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
