import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        narrative_elements = [
            {
                "cognitive_model": "Event-Indexing Model",
                "story_genre": "science fiction",
                "narrative_aspect": "temporal discontinuity"
            },
            {
                "cognitive_model": "Constructionist Theory",
                "story_genre": "mystery",
                "narrative_aspect": "unreliable narrator"
            }
        ]
        return {str(i+1): element for i, element in enumerate(narrative_elements)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for creative storytelling based on cognitive models of narrative comprehension, then analyze its potential impact on human creativity and storytelling traditions. Your task should incorporate the following elements:

1. Cognitive Model: {t['cognitive_model']}
2. Story Genre: {t['story_genre']}
3. Narrative Aspect to Explore: {t['narrative_aspect']}

Your response should include the following sections:

1. AI System Design (300-350 words):
   a) Describe the architecture of your AI storytelling system, including its key components and how they interact.
   b) Explain how the specified cognitive model is incorporated into the system's story generation process.
   c) Detail how your system would handle the given narrative aspect within the specified genre.
   d) Provide a high-level pseudocode or flowchart illustrating a key process in your system.

2. Cognitive Model Integration (250-300 words):
   a) Analyze how the specified cognitive model influences the AI's approach to storytelling.
   b) Discuss how this integration might lead to more 'human-like' narrative structures or comprehension.
   c) Explain any challenges in implementing this cognitive model in an AI system and how you addressed them.

3. Creative Output Analysis (250-300 words):
   a) Describe a sample story outline that your AI system might generate, highlighting its unique features.
   b) Analyze how the AI's output might differ from human-created stories in the same genre.
   c) Discuss how the system's handling of the specified narrative aspect contributes to the story's creativity or novelty.

4. Human-AI Collaboration (200-250 words):
   a) Propose a method for human writers to collaborate with your AI system.
   b) Discuss potential benefits and challenges of this collaboration.
   c) Explain how this collaboration might enhance or alter traditional storytelling processes.

5. Ethical Implications (200-250 words):
   a) Analyze the potential impact of your AI system on human creativity and traditional storytelling.
   b) Discuss any ethical concerns related to AI-generated narratives and how they might be addressed.
   c) Consider the long-term cultural implications of widespread use of AI in creative writing.

6. Evaluation and Future Directions (200-250 words):
   a) Propose a method to evaluate the creativity and quality of your AI system's outputs.
   b) Suggest two potential improvements or extensions to your system for future development.
   c) Discuss how your system might adapt to or incorporate other cognitive models of narrative comprehension.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and narrative theory. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your system design while maintaining scientific and technological plausibility.

Format your response with clear headings for each section and use numbered or bulleted lists where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI System Design section must clearly explain how the {t['cognitive_model']} is incorporated into the story generation process.",
            f"The Creative Output Analysis must provide a plausible sample story outline for the {t['story_genre']} genre, incorporating the {t['narrative_aspect']}.",
            "The Human-AI Collaboration section should propose a realistic method for writers to work with the AI system.",
            "The Ethical Implications section must thoughtfully consider the impact of AI-generated narratives on human creativity and culture.",
            "The overall response must demonstrate interdisciplinary knowledge, creativity, critical thinking, and ethical reasoning in the domains of cognitive science, AI, and narrative theory."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
