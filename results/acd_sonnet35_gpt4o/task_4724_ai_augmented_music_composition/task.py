import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        music_genres = ['Jazz', 'Classical', 'Electronic', 'Rock', 'World Music']
        emotional_states = ['Joy', 'Melancholy', 'Excitement', 'Calm', 'Anger']
        tasks = [
            {
                "genre": genre,
                "emotional_state": state
            }
            for genre in music_genres
            for state in emotional_states
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that collaborates with human musicians in real-time to compose and perform original music in the {t['genre']} genre, adapting to the musician's style and {t['emotional_state']} emotional state. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI music collaboration system.
   b) Explain how the system interprets and responds to the human musician's input in real-time.
   c) Detail how the AI adapts to the {t['genre']} genre and {t['emotional_state']} emotional state.
   d) Include a simple diagram or flowchart of your system architecture (describe this verbally).

2. Music Analysis and Generation (250-300 words):
   a) Explain how your system analyzes the human musician's playing style and emotional expression.
   b) Describe the AI's process for generating complementary musical elements.
   c) Discuss how machine learning techniques are used in the music generation process.

3. Real-time Adaptation (200-250 words):
   a) Detail how your system maintains synchronization with the human musician.
   b) Explain the mechanisms for real-time adjustment of tempo, key, and other musical parameters.
   c) Describe how the AI handles unexpected changes or improvisations by the human musician.

4. Emotional and Stylistic Coherence (200-250 words):
   a) Explain how your system ensures emotional coherence with the {t['emotional_state']} state.
   b) Describe techniques used to maintain stylistic consistency within the {t['genre']} genre.
   c) Discuss how the AI balances between following the human's lead and contributing its own ideas.

5. User Interface and Interaction (150-200 words):
   a) Describe the interface through which the human musician interacts with the AI system.
   b) Explain how the system provides feedback or cues to the human performer.
   c) Discuss any novel interaction methods your system employs.

6. Evaluation and Learning (150-200 words):
   a) Propose methods for evaluating the quality and coherence of the AI-human collaborative compositions.
   b) Explain how your system could learn and improve from each performance experience.
   c) Discuss potential challenges in evaluating AI-generated music and how you would address them.

7. Ethical and Creative Implications (150-200 words):
   a) Discuss the ethical implications of AI co-creation in music.
   b) Explore how this technology might impact the creative process and the role of human musicians.
   c) Propose guidelines for responsible use of AI in musical composition and performance.

Ensure your response demonstrates a deep understanding of both music theory and AI technologies. Use appropriate technical terminology from both fields and provide clear explanations for complex concepts. Be innovative in your approach while considering practical implementation.

Format your response with clear headings for each section. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the {t['genre']} genre and {t['emotional_state']} emotional state throughout the system design",
            "The system architecture is well-designed and clearly explained, with all key components addressed",
            "The music analysis and generation process is technically sound and innovative",
            "The real-time adaptation mechanisms are well-thought-out and practical",
            "The approach to maintaining emotional and stylistic coherence is well-explained and plausible",
            "The user interface and interaction design is intuitive and enhances the collaborative experience",
            "The evaluation methods and learning processes are appropriate and well-designed",
            "The discussion of ethical and creative implications is thoughtful and comprehensive",
            "The response demonstrates a deep understanding of both music theory and AI technologies",
            "The proposed system is innovative while remaining technically feasible",
            "The response adheres to the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
