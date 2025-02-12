import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "linguistic_domain": "Color perception",
                "cognitive_process": "Categorization",
                "target_language_family": "Austronesian"
            },
            {
                "linguistic_domain": "Spatial reasoning",
                "cognitive_process": "Navigation",
                "target_language_family": "Indo-European"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and analyzing linguistic relativity experiments, then use it to propose a novel experiment and analyze its potential implications. Your task should address the following components:

1. AI System Design (300-350 words):
   a) Describe the architecture of your AI system for generating linguistic relativity experiments.
   b) Explain how your system incorporates knowledge of linguistics, cognitive psychology, and experimental design.
   c) Detail how your system would generate hypotheses about linguistic relativity effects.
   d) Provide a high-level pseudocode or flowchart illustrating a key process in your system.

2. Experiment Generation (250-300 words):
   a) Use your AI system to propose a novel linguistic relativity experiment in the domain of {t['linguistic_domain']}.
   b) Explain how this experiment would investigate the relationship between language and the cognitive process of {t['cognitive_process']}.
   c) Describe the experimental design, including participants, methods, and measures.
   d) Discuss how your experiment controls for potential confounding variables.

3. Linguistic Analysis (200-250 words):
   a) Analyze how the linguistic features of the {t['target_language_family']} language family might influence {t['cognitive_process']}.
   b) Explain how your experiment would detect these potential effects.
   c) Discuss any challenges in isolating linguistic influences from cultural or environmental factors.

4. Cognitive Implications (200-250 words):
   a) Predict potential outcomes of your experiment and their implications for our understanding of linguistic relativity.
   b) Discuss how these findings might challenge or support existing theories in cognitive science.
   c) Explain how your experiment contributes to the broader debate on the relationship between language and thought.

5. AI Analysis Capabilities (200-250 words):
   a) Describe how your AI system would analyze and interpret the results of the experiment.
   b) Explain any novel data analysis techniques your system employs.
   c) Discuss how your AI's analysis might differ from or complement human analysis.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using AI to design and interpret cognitive experiments.
   b) Address any concerns related to studying linguistic relativity across different cultures.
   c) Propose guidelines for responsible use of AI in cognitive science research.

7. Future Directions (150-200 words):
   a) Suggest two potential improvements or extensions to your AI system.
   b) Propose a follow-up experiment that builds on the results of your initial study.
   c) Discuss the potential long-term impact of AI-driven research in linguistic relativity.

Ensure your response demonstrates a deep understanding of linguistic relativity, cognitive science, experimental design, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and word counts",
            "The AI system design demonstrates a deep understanding of linguistic relativity, cognitive science, and AI",
            "The proposed experiment is novel, well-designed, and specifically addresses the given linguistic domain and cognitive process",
            "The analysis of the target language family is thoughtful and relevant to the experiment",
            "The response demonstrates creativity and scientific plausibility throughout",
            "Ethical considerations and future directions are thoroughly explored"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
