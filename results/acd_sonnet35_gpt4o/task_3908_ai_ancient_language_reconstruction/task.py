import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "ancient_culture": "Sumerian",
                "time_period": "3rd millennium BCE",
                "linguistic_features": ["agglutinative morphology", "ergative-absolutive alignment", "cuneiform script"],
                "ai_technique": "Recurrent Neural Networks (RNN)",
                "puzzle_type": "deciphering an ancient inscription",
                "example_word": "lugal (king)",
                "example_sentence": "lugal-e e2 mu-du3 (The king built the house)",
                "contrast_culture": "Mayan",
                "contrast_technique": "Transformer models"
            },
            {
                "ancient_culture": "Mayan",
                "time_period": "Classical period (250-900 CE)",
                "linguistic_features": ["ergative alignment", "head-marking", "hieroglyphic writing system"],
                "ai_technique": "Transformer models",
                "puzzle_type": "solving a calendar-based prophecy",
                "example_word": "ajaw (lord, ruler)",
                "example_sentence": "u-CHOK-wa AJAW (The lord scatters it)",
                "contrast_culture": "Sumerian",
                "contrast_technique": "Recurrent Neural Networks (RNN)"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a computational linguist and AI researcher tasked with reconstructing an ancient language and using it to solve a historical puzzle. Your task is divided into four main parts:

1. Language Reconstruction (400-500 words):
   a) Describe an AI-based approach to reconstructing the {t['ancient_culture']} language from the {t['time_period']}.
   b) Explain in detail how you would use {t['ai_technique']} in this reconstruction process. Include specifics on model architecture, training data, and any pre-processing steps.
   c) Detail how your AI system would account for the following linguistic features: {', '.join(t['linguistic_features'])}.
   d) Discuss potential challenges in the reconstruction process and how your AI system might overcome them.
   e) Provide an example of how the word "{t['example_word']}" and the sentence "{t['example_sentence']}" might be processed and represented in your AI system.
   f) Compare and contrast your approach using {t['ai_technique']} for {t['ancient_culture']} with how you might use {t['contrast_technique']} for reconstructing the {t['contrast_culture']} language. Explain the key differences and why each technique might be more suitable for its respective language.

2. Puzzle Creation (200-250 words):
   a) Create a plausible historical puzzle or riddle related to {t['puzzle_type']} that would require knowledge of the reconstructed {t['ancient_culture']} language to solve.
   b) The puzzle should be 50-100 words long and include at least three distinct linguistic features of the reconstructed language.
   c) Present the puzzle in both the reconstructed language and English translation.
   d) Explain the cultural and historical context of this puzzle.

3. Puzzle Solving (200-250 words):
   a) Describe how your AI system would approach solving this puzzle using the reconstructed language.
   b) Detail the step-by-step process of solving the puzzle, including any linguistic analysis or decoding required.
   c) Provide the solution to the puzzle in both the reconstructed language and English.
   d) Justify your solution by explaining how specific linguistic features of the reconstructed language were crucial in solving the puzzle.

4. Reflection and Analysis (200-300 words):
   a) Analyze the potential impact of AI-driven ancient language reconstruction on the field of historical linguistics.
   b) Discuss ethical considerations in using AI to reconstruct and interpret ancient languages and cultural artifacts.
   c) Propose a future research direction that could build upon this work, specifically addressing how it might improve the accuracy or efficiency of ancient language reconstruction.

Ensure your response demonstrates a deep understanding of linguistics, artificial intelligence, and the specified ancient culture. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and historical accuracy.

Format your response with clear headings for each section and subsections as outlined above. Your total response should be between 1000-1300 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively describes an AI-based approach to reconstructing the {t['ancient_culture']} language using {t['ai_technique']}, including specific details on model architecture and training process. (0.2 points)",
            f"The AI system accurately accounts for the linguistic features: {', '.join(t['linguistic_features'])}. (0.1 points)",
            f"The response includes a plausible example of processing the word '{t['example_word']}' and the sentence '{t['example_sentence']}' in the AI system. (0.1 points)",
            f"The response effectively compares and contrasts {t['ai_technique']} for {t['ancient_culture']} with {t['contrast_technique']} for {t['contrast_culture']}. (0.1 points)",
            "The proposed puzzle is historically plausible, linguistically consistent, 50-100 words long, and includes at least three distinct linguistic features of the reconstructed language. (0.1 points)",
            "The puzzle-solving process is logically explained with a clear step-by-step breakdown of the linguistic analysis required. (0.1 points)",
            "The solution is justified by explaining how specific linguistic features were crucial in solving the puzzle. (0.1 points)",
            "The reflection section provides insightful analysis of the impact and ethical considerations of AI in historical linguistics, and proposes a relevant future research direction. (0.1 points)",
            "The response maintains scientific plausibility and historical accuracy throughout. (0.05 points)",
            "The response follows the required format with clear headings and subsections, and falls within the specified word count. (0.05 points)"
        ]
        return sum([float(c.split('(')[-1].split()[0]) for c in criteria if eval_with_llm_judge(instructions, submission, [c.split('(')[0].strip()])])
