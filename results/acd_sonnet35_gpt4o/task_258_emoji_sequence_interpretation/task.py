import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emoji_sequences = [
            "🌍🔥🌡️↗️🌊↗️🏠💧",
            "🍎🍊🍌🔄🥤💰💹",
            "🏃‍♀️🏃‍♂️🏃🏆🎉🔁🌅🌆",
            "📱💬👥🔒🔓💻👀😨"
        ]
        return {str(i+1): {"sequence": seq} for i, seq in enumerate(random.sample(emoji_sequences, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system for interpreting complex emoji sequences as a form of pictographic language. Your task is to analyze and explain the given emoji sequence: {t['sequence']}

1. Sequence Interpretation (150-200 words):
   Provide a detailed interpretation of the emoji sequence, considering potential semantic relationships, pragmatic implications, and cultural context. Explain how each emoji contributes to the overall meaning.

2. Linguistic Analysis (200-250 words):
   Analyze the emoji sequence from a linguistic perspective. Discuss:
   a) How the sequence functions as a form of syntax
   b) The role of iconicity and symbolism in conveying meaning
   c) Any ambiguities or cultural-specific interpretations
   d) How context might affect the interpretation

3. AI System Design (250-300 words):
   Propose an AI system capable of interpreting such emoji sequences. Describe:
   a) The overall architecture of the system
   b) Key components and their functions
   c) Types of data the system would need for training
   d) Potential challenges in implementation and proposed solutions
   e) How the system would handle ambiguity and context-dependence

4. Cross-Cultural Considerations (150-200 words):
   Discuss how your system would address cross-cultural differences in emoji interpretation. Consider:
   a) Strategies for handling culture-specific emoji usage
   b) Methods for adapting to evolving emoji meanings over time
   c) Ethical considerations in developing a 'universal' emoji interpreter

5. Practical Application (100-150 words):
   Suggest a practical application for your emoji sequence interpretation system. Explain its potential benefits and any limitations or risks that should be considered.

Ensure your response demonstrates a deep understanding of visual language processing, semantic reasoning, and cross-cultural communication. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation of the emoji sequence is detailed and considers semantic relationships, pragmatics, and cultural context",
            "The linguistic analysis thoroughly examines the sequence's syntax, iconicity, ambiguities, and context-dependence",
            "The proposed AI system design is comprehensive, addressing architecture, key components, data requirements, and challenges",
            "Cross-cultural considerations are well-explored, including strategies for handling cultural differences and ethical implications",
            "A practical application is suggested with a thoughtful discussion of its benefits and potential risks",
            "The response demonstrates deep understanding of visual language processing, semantic reasoning, and cross-cultural communication",
            "The answer is creative while maintaining scientific and technological plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
