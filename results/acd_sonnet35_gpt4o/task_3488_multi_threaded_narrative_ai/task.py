import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        genres = [
            "science fiction",
            "historical fiction",
            "magical realism",
            "cyberpunk",
            "gothic horror"
        ]
        themes = [
            "identity and self-discovery",
            "power and corruption",
            "love and sacrifice",
            "technology and humanity",
            "memory and perception"
        ]
        narrative_structures = [
            "parallel storylines",
            "non-linear timeline",
            "nested narratives",
            "multiple perspectives",
            "frame narrative"
        ]
        
        tasks = {
            "1": {
                "genre": random.choice(genres),
                "theme": random.choice(themes),
                "narrative_structure": random.choice(narrative_structures)
            },
            "2": {
                "genre": random.choice(genres),
                "theme": random.choice(themes),
                "narrative_structure": random.choice(narrative_structures)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and analyzing complex multi-threaded narratives with intertwining plot lines and character arcs, then use it to create and deconstruct a story in the {t['genre']} genre. Your task involves the following steps:

1. AI Narrative System Design (250-300 words):
   a) Describe the key components and architecture of your AI narrative system.
   b) Explain how your system models and generates complex plot structures and character arcs.
   c) Detail how it incorporates knowledge of literary techniques, human psychology, and social dynamics.

2. Story Generation Process (200-250 words):
   a) Explain how your AI system would generate a story in the {t['genre']} genre, exploring the theme of {t['theme']}.
   b) Describe how it would implement a {t['narrative_structure']} structure.
   c) Discuss how the system ensures consistency and interconnectedness between multiple plot threads.

3. Generated Story Overview (250-300 words):
   a) Provide a brief synopsis of the generated story, highlighting its key plot threads and character arcs.
   b) Explain how the story incorporates the specified genre, theme, and narrative structure.

4. Narrative Analysis (200-250 words):
   a) Use your AI system to analyze the generated story's structure, themes, and character development.
   b) Explain how the system identifies and evaluates the interconnections between different narrative threads.

5. Comparative Evaluation and Ethical Implications (200-250 words):
   a) Compare the AI-generated story to human-authored works in the same genre.
   b) Discuss the ethical implications of using AI for creative writing and narrative analysis.
   c) Propose guidelines for the responsible development and use of narrative AI systems.

Ensure your response demonstrates an understanding of narrative theory, creative writing, and artificial intelligence. Use appropriate literary and technical terminology, providing explanations where necessary. Be creative in your approach while maintaining plausibility and addressing potential limitations.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a design of an AI system for generating and analyzing complex narratives",
            f"The generated story is in the {t['genre']} genre and explores the theme of {t['theme']}",
            f"The narrative uses a {t['narrative_structure']} structure",
            "The response includes an analysis of the generated story",
            "The comparative evaluation and ethical implications are discussed",
            "The response demonstrates understanding of narrative theory, creative writing, and AI",
            "The response is well-structured with clear headings for each numbered section",
            "The total response falls within the specified word count range of 1100-1350 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
