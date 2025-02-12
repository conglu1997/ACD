class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "extinct_language": "Linear A",
                "modern_language": "Mandarin Chinese",
                "linguistic_feature": "Tonal patterns",
                "application": "Deciphering ancient texts"
            },
            "2": {
                "extinct_language": "Proto-Indo-European",
                "modern_language": "Arabic",
                "linguistic_feature": "Verb conjugation systems",
                "application": "Automated translation of legal documents"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical universal language model capable of understanding and generating all human languages, past and present, then apply it to solve a complex linguistic puzzle. Your task involves the extinct language {t['extinct_language']}, the modern language {t['modern_language']}, and focuses on the linguistic feature of {t['linguistic_feature']}. The model should be applied to the task of {t['application']}.

Your response should include the following sections:

1. Universal Language Model Architecture (300-350 words):
   a) Describe the key components and mechanisms of your universal language model.
   b) Explain how your model incorporates both synchronic and diachronic linguistic knowledge.
   c) Detail how your model handles the specified linguistic feature across different language families.
   d) Discuss any novel elements in your design that enable true language universality.
   e) Include a conceptual diagram or flowchart of your model's architecture (describe it textually).

2. Linguistic Analysis (250-300 words):
   a) Compare and contrast the specified linguistic feature in the extinct and modern languages.
   b) Analyze how your model would approach understanding this feature in the extinct language.
   c) Explain how knowledge from the modern language could aid in analyzing the extinct language.
   d) Discuss any challenges in bridging the gap between these two languages and how your model addresses them.

3. Application to Linguistic Puzzle (250-300 words):
   a) Describe a specific linguistic puzzle related to {t['application']} that your model would solve.
   b) Provide a step-by-step explanation of how your model would approach and solve this puzzle.
   c) Discuss how your model's universal nature contributes to solving this puzzle more effectively than traditional methods.
   d) Address any limitations or potential errors in your model's approach to this task.

4. Cognitive and Computational Foundations (200-250 words):
   a) Explain the cognitive principles underlying your universal language model.
   b) Discuss how your model relates to theories of human language acquisition and processing.
   c) Describe the computational techniques and algorithms that would be necessary to implement your model.

5. Ethical Implications and Societal Impact (200-250 words):
   a) Analyze the potential ethical concerns of a truly universal language model.
   b) Discuss how your model might impact linguistic diversity and cultural preservation.
   c) Consider the potential misuse of such a powerful linguistic tool and propose safeguards.
   d) Explore the implications of your model for interlingual communication and global understanding.

6. Future Developments and Research Directions (150-200 words):
   a) Suggest potential enhancements or extensions to your universal language model.
   b) Propose specific experiments or case studies to further validate your model's effectiveness.
   c) Speculate on how this technology might influence the fields of linguistics and artificial intelligence in the coming decades.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence.",
            "The universal language model design is innovative, plausible, and addresses the specified linguistic feature and languages.",
            "The linguistic analysis effectively compares and contrasts the extinct and modern languages.",
            "The application to the linguistic puzzle is well-explained and demonstrates the model's capabilities.",
            "The cognitive and computational foundations are clearly described and grounded in established theories.",
            "Ethical implications and societal impacts are thoroughly discussed with thoughtful safeguards proposed.",
            "Future developments and research directions are insightfully explored.",
            "The response is well-structured, within the specified word count, and uses appropriate terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
