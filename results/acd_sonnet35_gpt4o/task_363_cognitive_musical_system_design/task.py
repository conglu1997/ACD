import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "working memory limitations",
            "pattern recognition",
            "emotional processing",
            "attention and focus",
            "synesthesia"
        ]
        mathematical_concepts = [
            "Fibonacci sequence",
            "prime numbers",
            "fractal geometry",
            "non-Euclidean geometry",
            "complex numbers"
        ]
        musical_elements = [
            "scale structure",
            "harmonic relationships",
            "rhythm and meter",
            "timbre",
            "pitch perception"
        ]
        return {
            "1": {
                "cognitive_principle": random.choice(cognitive_principles),
                "mathematical_concept": random.choice(mathematical_concepts),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "cognitive_principle": random.choice(cognitive_principles),
                "mathematical_concept": random.choice(mathematical_concepts),
                "musical_element": random.choice(musical_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical scale or tuning system based on the cognitive principle of {t['cognitive_principle']}, incorporating the mathematical concept of {t['mathematical_concept']}, and focusing on the musical element of {t['musical_element']}. Your response should include:

1. System Design (300-350 words):
   a) Describe your musical scale or tuning system in detail.
   b) Explain how it incorporates the specified cognitive principle and mathematical concept.
   c) Discuss how it addresses or manipulates the given musical element.
   d) Provide a visual or mathematical representation of your system (using ASCII art or mathematical notation).
   e) Include a concrete example of a short musical phrase or composition (4-8 measures) using your system, with notation or a clear textual description (minimum 50 words).

2. Cognitive Analysis (250-300 words):
   a) Analyze how your system might influence human cognition and perception of music.
   b) Discuss potential cognitive benefits or challenges for listeners and musicians.
   c) Compare your system's cognitive effects with those of traditional Western music.

3. Cultural and Artistic Implications (200-250 words):
   a) Explore how your system might impact musical composition and performance.
   b) Discuss potential cultural or artistic movements that could arise from your system.
   c) Consider how it might influence cross-cultural musical exchange.

4. Practical Application (150-200 words):
   a) Propose a method for implementing your system in musical instruments or digital audio.
   b) Discuss challenges in adoption and how they might be overcome.
   c) Suggest an experiment to test the effects of your system on listeners or performers.

5. Interdisciplinary Connections (100-150 words):
   a) Explain how your system integrates principles from music theory, mathematics, and cognitive science.
   b) Propose a potential collaboration between experts in different fields to further develop or study your system.

6. Critical Reflection (150-200 words):
   a) Discuss potential limitations or drawbacks of your system.
   b) Analyze possible ways in which the system might be misused or have unintended consequences.
   c) Propose modifications or areas for further research to address these issues.

7. Glossary (100-150 words):
   Provide a brief glossary of 5-7 key technical terms used in your response, demonstrating your understanding of concepts from music theory, mathematics, and cognitive science.

Ensure your response demonstrates a deep understanding of music theory, mathematics, and cognitive science. Be creative in your design while maintaining scientific plausibility and addressing potential limitations or challenges.

Format your response with clear headings for each section, and number your paragraphs within each section. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The musical system effectively incorporates the cognitive principle of {t['cognitive_principle']} and the mathematical concept of {t['mathematical_concept']}.",
            f"The design clearly addresses the musical element of {t['musical_element']} and includes a concrete example of a musical phrase or composition (minimum 50 words) using the system.",
            "The cognitive analysis demonstrates a deep understanding of how the system might affect human cognition and perception, with clear comparisons to traditional Western music.",
            "The cultural and artistic implications are thoughtfully explored and logically derived from the system's properties.",
            "The practical application and implementation suggestions are feasible, well-reasoned, and include a specific experimental proposal.",
            "The response shows strong interdisciplinary integration of music theory, mathematics, and cognitive science, with a clear proposal for expert collaboration.",
            "The critical reflection demonstrates awareness of potential limitations, ethical considerations, and proposes specific areas for further research.",
            "The glossary includes 5-7 key technical terms with accurate and concise definitions.",
            "The overall response is creative, scientifically plausible, well-structured, and adheres to the specified format and word count (1250-1600 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
