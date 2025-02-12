import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'target_language': 'Mandarin Chinese',
                'learning_focus': 'tonal pronunciation',
                'neural_target': 'auditory cortex'
            },
            {
                'target_language': 'Arabic',
                'learning_focus': 'script recognition',
                'neural_target': 'visual word form area'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical brain-computer interface (BCI) for accelerated acquisition of {t['target_language']}, focusing on {t['learning_focus']} and targeting the {t['neural_target']}. Your response should include:

1. BCI System Architecture (250-300 words):
   a) Describe the key components of your BCI system for language acquisition.
   b) Explain how your system interfaces with the targeted brain region.
   c) Detail the data flow between the brain, the BCI, and any external systems.

2. Neurolinguistic Mechanism (200-250 words):
   a) Explain the neuroscientific principles underlying your BCI's approach to language acquisition.
   b) Describe how your system leverages neuroplasticity to enhance learning.
   c) Discuss any potential neurological risks and how they are mitigated.

3. AI Integration (200-250 words):
   a) Detail how AI algorithms are incorporated into your BCI system.
   b) Explain how the AI component adapts to individual learners' needs and progress.
   c) Describe any novel machine learning approaches used in your design.

4. Language Acquisition Process (150-200 words):
   a) Outline the step-by-step process of how a user would learn using your BCI.
   b) Explain how your system specifically addresses the given learning focus.
   c) Discuss how your BCI might complement or replace traditional language learning methods.

5. Ethical Considerations (100-150 words):
   a) Identify potential ethical issues related to using BCIs for cognitive enhancement.
   b) Propose guidelines for responsible development and use of such technology.

6. Future Research Directions (100-150 words):
   a) Suggest two potential expansions or modifications to your BCI design.
   b) Discuss how empirical research could validate or improve your system.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, and AI technologies. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of neuroscience, linguistics, and AI as applied to {t['target_language']} acquisition",
            f"The BCI design effectively addresses the learning focus of {t['learning_focus']}",
            f"The system architecture includes a plausible interface with the {t['neural_target']}",
            "The AI integration is well-explained and innovative",
            "Ethical considerations are thoroughly addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
