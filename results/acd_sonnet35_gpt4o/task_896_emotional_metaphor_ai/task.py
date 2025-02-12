import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            'ambivalence',
            'nostalgia',
            'schadenfreude',
            'sublime',
            'ennui',
            'saudade',
            'frisson',
            'mono no aware'
        ]
        contexts = [
            'personal relationship',
            'career decision',
            'global event',
            'artistic experience',
            'technological advancement',
            'environmental change',
            'philosophical realization',
            'cultural shift'
        ]
        tasks = [
            {
                'emotion': random.choice(emotions),
                'context': random.choice(contexts)
            },
            {
                'emotion': random.choice(emotions),
                'context': random.choice(contexts)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and interpret metaphors based on complex emotional states, grounded in cognitive linguistics and affective science theories. Your system should focus on the emotion of {t['emotion']} in the context of a {t['context']}.

Provide your response in the following format:

1. Theoretical Foundation (200-250 words):
   a) Explain the cognitive linguistic theories your system will use to generate and interpret metaphors.
   b) Describe the affective science models your system will incorporate to understand and represent the given emotion.
   c) Discuss how these theories will be integrated in your AI system.

2. System Architecture (250-300 words):
   a) Outline the main components of your AI system and their functions.
   b) Explain how your system processes emotional input and generates metaphorical output.
   c) Describe any novel algorithms or techniques your system uses for metaphor generation and interpretation.
   d) Discuss how your system ensures coherence and relevance of the generated metaphors.

3. Metaphor Generation (150-200 words):
   a) Provide two example metaphors your system might generate for the given emotion and context.
   b) Explain the cognitive and emotional reasoning behind each metaphor.
   c) Discuss how these metaphors capture the nuances of the given emotion.

4. Metaphor Interpretation (150-200 words):
   a) Describe how your system would interpret and analyze a given metaphor related to the specified emotion.
   b) Explain the process of extracting emotional meaning from metaphorical language.
   c) Discuss any challenges in metaphor interpretation and how your system addresses them.

5. Evaluation Metrics (100-150 words):
   a) Propose methods to evaluate the quality, creativity, and emotional accuracy of the generated metaphors.
   b) Describe how you would measure the system's interpretation capabilities.
   c) Discuss the challenges in evaluating such a system and how you'd address them.

6. Potential Applications (100-150 words):
   a) Suggest two potential applications of your emotional metaphor AI system.
   b) Explain how these applications could benefit fields such as psychology, education, or creative writing.

7. Ethical Considerations (100-150 words):
   a) Identify potential ethical concerns related to an AI system that generates and interprets emotional metaphors.
   b) Propose guidelines for responsible development and use of such a system.

Ensure your response demonstrates a deep understanding of cognitive linguistics, affective science, and AI technologies. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics and affective science theories.",
            "The proposed AI system architecture is innovative and coherently integrates linguistic and emotional processing.",
            "The example metaphors are creative, relevant to the given emotion and context, and well-explained.",
            "The metaphor interpretation process is clearly described and addresses potential challenges.",
            "The evaluation metrics are appropriate and comprehensive.",
            "The potential applications are innovative and well-reasoned.",
            "Ethical considerations are thoughtfully discussed and addressed.",
            f"The system adequately handles the complex emotion of {t['emotion']} in the context of a {t['context']}."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
