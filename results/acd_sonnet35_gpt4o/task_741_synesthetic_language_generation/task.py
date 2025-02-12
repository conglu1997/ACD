import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        sensory_mappings = [
            {"phoneme": "a", "sensation": "red"},
            {"phoneme": "e", "sensation": "green"},
            {"phoneme": "i", "sensation": "white"},
            {"phoneme": "o", "sensation": "blue"},
            {"phoneme": "u", "sensation": "brown"},
            {"phoneme": "s", "sensation": "smooth"},
            {"phoneme": "r", "sensation": "rough"},
            {"phoneme": "l", "sensation": "liquid"},
            {"phoneme": "m", "sensation": "sweet"},
            {"phoneme": "t", "sensation": "sharp"},
            {"phoneme": "n", "sensation": "soft"},
            {"phoneme": "k", "sensation": "crisp"},
            {"phoneme": "f", "sensation": "fuzzy"},
            {"phoneme": "p", "sensation": "popping"},
            {"phoneme": "b", "sensation": "bouncy"}
        ]
        
        texts = [
            "The quick brown fox jumps over the lazy dog.",
            "To be or not to be, that is the question.",
            "All that glitters is not gold.",
            "I think, therefore I am.",
            "In the beginning was the Word, and the Word was with God."
        ]
        
        contexts = [
            "a society where emotions are communicated through color",
            "a world where written language is outlawed, but sensory experiences are not",
            "a future where humans have developed additional sensory organs",
            "an alien civilization that communicates primarily through tactile sensations"
        ]
        
        return {
            "1": {"mappings": sensory_mappings, "text": random.choice(texts), "context": random.choice(contexts)},
            "2": {"mappings": sensory_mappings, "text": random.choice(texts), "context": random.choice(contexts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a synesthetic language system based on the given phoneme-sensation mappings, then use it to translate and analyze the provided text within the given context. Your task has five parts:

1. Synesthetic Language System Design (200-250 words):
   a) Explain how you will use the given phoneme-sensation mappings to create a synesthetic language system.
   b) Describe additional rules or principles you'll implement to handle more complex linguistic structures (e.g., grammar, syntax).
   c) Discuss how your system accounts for words that combine multiple mapped phonemes.
   d) Explain how your system adapts to the context: {t['context']}

2. Text Translation (200-250 words):
   Translate the following text into your synesthetic language system:
   "{t['text']}"
   a) Provide the translation, explaining how each word or phrase maps to sensory experiences.
   b) Describe the overall sensory "image" or experience that the translated text evokes.
   c) Explain how the context influences your translation.

3. Cognitive Analysis (200-250 words):
   a) Analyze how processing language through your synesthetic system might affect cognition and understanding.
   b) Discuss potential advantages and disadvantages of using this system for communication or information processing.
   c) Propose a hypothesis about how regular use of this system might impact memory, learning, or creativity.
   d) Explain how the given context might influence these cognitive effects.

4. AI Implications (150-200 words):
   a) Explain how an AI language model could be trained or adapted to understand and generate text in your synesthetic language system.
   b) Discuss potential challenges and opportunities in implementing this system in AI, particularly in natural language processing tasks.
   c) Propose an experiment to test an AI's ability to use and understand your synesthetic language system.

5. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues that might arise from the widespread adoption of your synesthetic language system.
   b) Discuss how these ethical concerns might be addressed or mitigated.

Format your response with clear headings for each section and subheadings for each point. Use bullet points or numbered lists where appropriate. Your total response should be between 850-1100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear, creative, and context-appropriate design for a synesthetic language system based on the given mappings.",
            "The text translation correctly applies the designed system, provides a vivid sensory description, and considers the given context.",
            "The cognitive analysis shows a deep understanding of how language processing might be affected by synesthesia and the given context.",
            "The AI implications section provides insightful ideas about implementing the system in language models and proposes a feasible experiment.",
            "The ethical considerations section identifies relevant issues and proposes thoughtful mitigation strategies.",
            "The overall response is well-structured, coherent, and demonstrates interdisciplinary knowledge and creative problem-solving.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
