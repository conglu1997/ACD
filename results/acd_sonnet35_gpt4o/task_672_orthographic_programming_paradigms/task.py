import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        writing_systems = [
            "Chinese characters",
            "Arabic abjad",
            "Devanagari abugida",
            "Korean Hangul",
            "Egyptian hieroglyphs"
        ]
        programming_concepts = [
            "variable declaration and assignment",
            "control structures (if-else, loops)",
            "function definitions and calls",
            "object-oriented programming constructs",
            "error handling and exceptions"
        ]
        
        return {
            "1": {
                "writing_system": random.choice(writing_systems),
                "programming_concept": random.choice(programming_concepts)
            },
            "2": {
                "writing_system": random.choice(writing_systems),
                "programming_concept": random.choice(programming_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a programming language paradigm based on the {t['writing_system']} writing system, focusing on the implementation of {t['programming_concept']}. Your response should include:\n\n" \
               f"1. Writing System Analysis (150-200 words):\n" \
               f"   a) Briefly describe the key features of the {t['writing_system']}.\n" \
               f"   b) Explain how these features might influence programming language design.\n\n" \
               f"2. Programming Paradigm Design (250-300 words):\n" \
               f"   a) Describe your programming paradigm based on {t['writing_system']}.\n" \
               f"   b) Explain how it implements {t['programming_concept']}.\n" \
               f"   c) Provide a simple code example (3-5 lines) demonstrating your paradigm.\n\n" \
               f"3. Cognitive Analysis (200-250 words):\n" \
               f"   a) Discuss how your paradigm might affect code readability and comprehension.\n" \
               f"   b) Analyze potential cognitive advantages or challenges for programmers.\n\n" \
               f"4. Cross-cultural Implications (150-200 words):\n" \
               f"   a) Explore how your paradigm might impact global software development.\n" \
               f"   b) Discuss potential benefits or challenges in cross-cultural programming contexts.\n\n" \
               f"5. Technical Feasibility (150-200 words):\n" \
               f"   a) Analyze the technical challenges in implementing your paradigm.\n" \
               f"   b) Propose solutions to overcome these challenges.\n\n" \
               f"Ensure your response demonstrates a deep understanding of both linguistics and computer science. Use appropriate terminology from both fields and provide clear explanations where necessary. Be creative in your approach while maintaining technical feasibility.\n\n" \
               f"Format your response with clear headings for each section, numbered as above."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both the {t['writing_system']} writing system and programming language design principles.",
            f"The proposed programming paradigm creatively and feasibly incorporates features of the {t['writing_system']} into its design.",
            f"The implementation of {t['programming_concept']} in the new paradigm is clearly explained and demonstrated.",
            "The cognitive analysis provides insightful discussion on how the new paradigm might affect code comprehension and programmer thinking.",
            "The cross-cultural implications are thoughtfully explored, considering both potential benefits and challenges.",
            "The technical feasibility analysis identifies realistic challenges and proposes plausible solutions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
