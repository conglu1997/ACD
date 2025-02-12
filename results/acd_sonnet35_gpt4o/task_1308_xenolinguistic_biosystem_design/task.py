import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            "High-pressure gas giant with floating colonies",
            "Tidally locked planet with extreme temperature differences",
            "Subterranean world with complex cave systems"
        ]
        biological_features = [
            "Bioluminescent organs",
            "Electromagnetic field generation",
            "Distributed neural network throughout the body"
        ]
        problems = [
            "Coordinating large-scale migration",
            "Sharing complex scientific information",
            "Negotiating resource allocation"
        ]
        
        return {
            "1": {
                "environment": random.choice(environments),
                "biological_feature": random.choice(biological_features),
                "problem": random.choice(problems)
            },
            "2": {
                "environment": random.choice(environments),
                "biological_feature": random.choice(biological_features),
                "problem": random.choice(problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a communication system for a hypothetical alien species based on their unique biology and environment, then use this system to solve a complex problem. Use the following specifications:

Environment: {t['environment']}
Biological Feature: {t['biological_feature']}
Problem to Solve: {t['problem']}

Your task has the following parts:

1. Species and Environment Description (150-200 words):
   a) Describe the alien species, including their physical characteristics and how they've adapted to their environment.
   b) Explain how their unique biological feature could be utilized for communication.
   c) Discuss any environmental factors that might influence their communication system.

2. Communication System Design (250-300 words):
   a) Describe the fundamental principles of your communication system.
   b) Explain how it utilizes the species' biological feature and adapts to their environment.
   c) Outline the system's components (e.g., 'phonemes', syntax, pragmatics) and how they function.
   d) Discuss any novel concepts in your system that differ from human language.

3. Linguistic Examples (100-150 words):
   Provide three example 'utterances' in your alien language, including:
   a) A simple greeting or statement
   b) A complex sentence related to the species' environment
   c) A phrase specifically related to the problem they need to solve
   For each example, provide a translation and explain its structure.

4. Problem-Solving Application (200-250 words):
   a) Explain how your communication system would be used to address the given problem.
   b) Describe a specific scenario where the aliens use the system to coordinate or share information.
   c) Discuss any advantages your system has over human language for solving this particular problem.

5. Cultural and Cognitive Implications (150-200 words):
   a) Speculate on how this communication system might influence the aliens' culture and way of thinking.
   b) Discuss any potential limitations or challenges of the system.
   c) Propose how the system might evolve over time as the species advances.

6. Comparative Analysis (100-150 words):
   Briefly compare your alien communication system to human language, highlighting key similarities and differences.

Ensure your response demonstrates a deep understanding of linguistics, biology, and problem-solving. Be creative in your approach while maintaining scientific plausibility. Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a thorough understanding of linguistics, biology, and the given environment.",
            "The communication system design is creative, plausible, and effectively utilizes the species' biological feature.",
            "The linguistic examples are consistent with the described system and clearly explained.",
            "The problem-solving application is well-reasoned and demonstrates how the communication system addresses the given problem.",
            "The cultural and cognitive implications are thoughtfully considered and logically derived from the communication system.",
            "The comparative analysis provides insightful comparisons between the alien system and human language."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
