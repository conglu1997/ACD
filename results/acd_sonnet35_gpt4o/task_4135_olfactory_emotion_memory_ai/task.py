import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'olfactory_component': 'Amygdala',
                'emotion': 'Fear',
                'memory_type': 'Episodic',
                'scent_category': 'Woody',
                'example_scent': 'Pine',
                'example_memory': 'Getting lost in a dense forest'
            },
            {
                'olfactory_component': 'Piriform cortex',
                'emotion': 'Happiness',
                'memory_type': 'Semantic',
                'scent_category': 'Floral',
                'example_scent': 'Lavender',
                'example_memory': 'Knowledge about relaxation techniques'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models the relationship between olfactory perception, emotional response, and memory formation, then use it to analyze and generate scent-based experiences. Your system should focus on the {t['olfactory_component']} in olfactory processing, primarily address the emotion of {t['emotion']}, and be tailored for {t['memory_type']} memory. The system should work with scents in the {t['scent_category']} category.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI system and their functions.
   b) Explain how your system integrates principles from neuroscience, olfactory perception, and machine learning.
   c) Detail how the system incorporates the {t['olfactory_component']} in its olfactory processing model.
   d) Discuss how the system is adapted to work with the emotion of {t['emotion']} and {t['memory_type']} memory.
   e) Explain how the system accounts for the characteristics of {t['scent_category']} scents in its processing.

2. Olfactory-Emotion-Memory Mapping (250-300 words):
   a) Describe the process by which your system maps olfactory inputs to emotional responses and memory formation.
   b) Explain how the system models the interaction between the {t['olfactory_component']}, emotional processing, and {t['memory_type']} memory.
   c) Provide an example of how the system would process the scent of {t['example_scent']}, detailing the emotional and memory responses it would generate, such as {t['example_memory']}.

3. Scent Analysis and Generation (250-300 words):
   a) Explain how your system analyzes existing scents in terms of their emotional and memory-related properties.
   b) Describe how the system generates novel scent combinations to evoke specific emotional and memory responses.
   c) Discuss how the system ensures the generated scents remain within the {t['scent_category']} category while maximizing their impact on {t['emotion']} and {t['memory_type']} memory.
   d) Provide an example of a novel scent combination your system might generate to evoke {t['emotion']} and form a {t['memory_type']} memory.

4. Applications and Experiments (200-250 words):
   a) Propose three potential applications of your system in fields such as psychology, marketing, or therapy.
   b) Design a hypothetical experiment to test the efficacy of your system in evoking {t['emotion']} through {t['scent_category']} scents and forming {t['memory_type']} memories.
   c) Describe how you would measure and validate the emotional and memory-related outcomes of this experiment.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical issues related to using AI to manipulate emotions and memories through scent.
   b) Address concerns about privacy, consent, and potential misuse of the technology.
   c) Describe limitations of your system and areas for future improvement.

6. Future Research Directions (150-200 words):
   a) Suggest two potential expansions of your system to other olfactory components, emotions, or memory types.
   b) Propose a related research question that could further our understanding of the olfactory-emotion-memory relationship.
   c) Discuss how this technology might evolve in the next decade and its potential impact on neuroscience and AI.

Ensure your response demonstrates a deep understanding of neuroscience, olfactory perception, emotional processing, and artificial intelligence. Use appropriate technical terminology and provide clear explanations. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered subsections, and a brief conclusion summarizing the key innovations of your system. Your total response should be between 1350-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, olfactory perception, emotional processing, and artificial intelligence.",
            f"The system architecture effectively incorporates the {t['olfactory_component']} in its olfactory processing model, with clear explanations of its role.",
            f"The system appropriately addresses the emotion of {t['emotion']} and {t['memory_type']} memory, providing specific mechanisms for their interaction.",
            f"The response adequately explains how the system works with scents in the {t['scent_category']} category, including analysis and generation of novel scents.",
            "The olfactory-emotion-memory mapping is logically explained and scientifically plausible, with a clear example using the provided scent and memory.",
            "The scent analysis and generation processes are well-described, innovative, and include a concrete example of a novel scent combination.",
            "The proposed applications and experiments are relevant, well-designed, and include specific measurement and validation methods.",
            "Ethical considerations and limitations are thoroughly discussed, addressing privacy, consent, and potential misuse.",
            "Future research directions are insightful, demonstrate forward-thinking, and include a specific research question.",
            "The response is well-structured, within the specified word count, uses appropriate technical terminology, and includes a conclusion summarizing key innovations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
