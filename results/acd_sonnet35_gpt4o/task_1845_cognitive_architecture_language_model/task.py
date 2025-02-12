import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_architectures = [
            {
                "architecture": "ACT-R",
                "focus": "memory",
                "linguistic_phenomenon": "lexical access"
            },
            {
                "architecture": "SOAR",
                "focus": "problem-solving",
                "linguistic_phenomenon": "syntactic parsing"
            },
            {
                "architecture": "CLARION",
                "focus": "implicit learning",
                "linguistic_phenomenon": "semantic processing"
            }
        ]
        return {
            "1": random.choice(cognitive_architectures),
            "2": random.choice(cognitive_architectures)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language model based on the {t['architecture']} cognitive architecture, focusing on {t['focus']} and addressing the linguistic phenomenon of {t['linguistic_phenomenon']}. Your response should include the following sections:

1. Cognitive Architecture Overview (200-250 words):
   a) Briefly describe the key principles and components of the {t['architecture']} architecture.
   b) Explain how this architecture models human cognition, particularly in relation to {t['focus']}.
   c) Discuss any existing applications or limitations of this architecture in language processing.

2. Language Model Design (300-350 words):
   a) Outline the structure of your language model, explaining how it incorporates principles from {t['architecture']}.
   b) Describe how your model addresses the linguistic phenomenon of {t['linguistic_phenomenon']}.
   c) Explain any novel features or modifications you've made to the architecture to better handle language processing.
   d) Discuss how your model integrates aspects of {t['focus']} into its language processing capabilities.
   e) Include a diagram or visual representation of your model's architecture.

3. Implementation and Training (250-300 words):
   a) Describe the data requirements and potential sources for training your model.
   b) Explain the training process, including any specific algorithms or techniques you would use.
   c) Discuss how you would evaluate the model's performance, particularly in relation to {t['linguistic_phenomenon']}.
   d) Address any technical challenges in implementing this model and propose solutions.

4. Comparative Analysis (200-250 words):
   a) Compare your cognitive architecture-based language model to traditional deep learning approaches (e.g., Transformers).
   b) Discuss potential advantages and limitations of your approach.
   c) Analyze how your model might perform differently from traditional models on tasks related to {t['linguistic_phenomenon']}.

5. Cognitive Science Implications (200-250 words):
   a) Discuss how your model could contribute to our understanding of human language processing.
   b) Propose an experiment that could test whether your model accurately reflects human cognitive processes in {t['linguistic_phenomenon']}.
   c) Explain how insights from your model could inform theories of language acquisition or processing.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of developing more cognitively-inspired AI language models.
   b) Propose two future research directions that could extend or improve your model.
   c) Speculate on the long-term implications of this approach for AI and cognitive science.

Ensure your response demonstrates a deep understanding of cognitive architectures, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and coherence.

Format your response with clear headings for each section, numbered as above (e.g., '1. Cognitive Architecture Overview'). Include a diagram or visual representation in the Language Model Design section. Your total response should be between 1300-1600 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['architecture']} cognitive architecture and its principles.",
            f"The language model design effectively incorporates elements of {t['architecture']} and addresses {t['linguistic_phenomenon']}.",
            "The implementation and training section provides a plausible and detailed approach.",
            "The comparative analysis shows critical thinking in evaluating the model against traditional approaches.",
            "The cognitive science implications are thoughtfully discussed and well-reasoned.",
            "Ethical considerations are addressed, and future directions are innovative and relevant.",
            "The response includes a diagram or visual representation of the model's architecture.",
            "The response follows the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
