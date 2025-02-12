import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "decision making",
            "emotional processing",
            "memory formation",
            "spatial navigation",
            "abstract reasoning"
        ]
        brain_regions = [
            "prefrontal cortex",
            "hippocampus",
            "amygdala",
            "parietal lobe",
            "cerebellum"
        ]
        return {
            "1": {
                "process": random.choice(cognitive_processes),
                "region": random.choice(brain_regions)
            },
            "2": {
                "process": random.choice(cognitive_processes),
                "region": random.choice(brain_regions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate neural activity patterns into natural language, focusing on the cognitive process of {t['process']} in the {t['region']}. This task is inspired by the Sapir-Whorf hypothesis, which suggests that the structure of a language affects its speakers' worldview and cognition. In this case, we're exploring how the 'language' of neural activity might be translated into natural language, and how this translation might influence our understanding of cognitive processes.

Your system must be designed to operate with limited computational resources and process neural signals in real-time.

Your response should include the following sections:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system for neural-to-language translation.
   b) Explain how it integrates neuroscientific principles and linguistic models.
   c) Discuss any novel technologies or theoretical concepts it employs.
   d) Explain how your system achieves real-time processing with limited computational resources.

2. Neural Signal Processing (150-200 words):
   a) Explain how your system would process and interpret neural signals from the {t['region']}.
   b) Discuss challenges specific to decoding {t['process']} and how your system addresses them.
   c) Propose a method for distinguishing relevant neural activity from background noise.

3. Language Generation (150-200 words):
   a) Describe how your system would convert processed neural signals into coherent language.
   b) Explain how it handles the complexity and abstraction of {t['process']}.
   c) Discuss any linguistic models or theories your system incorporates.

4. Example Translation (100-150 words):
   Provide a concrete example of how your system might translate a specific pattern of neural activity related to {t['process']} into a natural language description. Include:
   a) A brief description of the neural activity pattern.
   b) The resulting natural language translation.
   c) An explanation of your reasoning for this translation.

5. Comparative Analysis (150-200 words):
   a) Propose a hypothetical alternative approach to neural-to-language translation.
   b) Compare and contrast this alternative with your proposed system.
   c) Discuss the potential advantages and disadvantages of each approach.

6. Limitations and Challenges (100-150 words):
   a) Identify potential limitations of your proposed system.
   b) Discuss challenges in accurately translating subjective experiences into language.
   c) Propose solutions or areas for future research to address these issues.

7. Ethical Considerations (150-200 words):
   a) Discuss privacy concerns related to decoding neural activity.
   b) Analyze potential misuse of this technology and propose safeguards.
   c) Consider the implications for concepts of thought privacy and cognitive liberty.

8. Interdisciplinary Implications (100-150 words):
   a) Explore how this technology might impact fields such as psychology, philosophy, or law.
   b) Propose novel research questions that arise from the development of this system.

9. Key Innovations Summary (50-100 words):
   Provide a concise summary of the key innovations in your proposed system.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and AI. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section and number your points where appropriate. Aim for a total response between 1150-1600 words.

Your response will be evaluated based on the completeness and quality of each section, the integration of concepts from multiple disciplines, the creativity and plausibility of your system design, your comparative analysis, and your consideration of ethical implications and future research directions."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all nine required sections with appropriate content and word counts.",
            f"The system design specifically addresses the cognitive process of {t['process']} in the {t['region']}.",
            "The proposed AI system integrates concepts from neuroscience, linguistics, and artificial intelligence.",
            "The system design accounts for real-time processing with limited computational resources.",
            "The response demonstrates creativity and plausibility in the system design.",
            "A concrete example of translated neural activity to natural language is provided, including a description of the neural activity pattern, the resulting translation, and an explanation of the reasoning.",
            "The comparative analysis section effectively contrasts the proposed system with a hypothetical alternative approach.",
            "Ethical considerations and potential misuse of the technology are thoroughly discussed, including proposed safeguards.",
            "The response proposes specific, novel research questions or future directions.",
            "A concise summary of key innovations is provided.",
            "The total word count is between 1150-1600 words."
        ]
        score = sum([eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria]) / len(criteria)
        return score
