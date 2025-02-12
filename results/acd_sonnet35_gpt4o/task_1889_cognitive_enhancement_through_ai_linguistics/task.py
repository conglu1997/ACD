import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_domain": "Spatial reasoning",
                "linguistic_feature": "Spatial frames of reference",
                "target_language": "English",
                "example_phrase": "The cup is to the left of the plate."
            },
            {
                "cognitive_domain": "Time perception",
                "linguistic_feature": "Tense and aspect systems",
                "target_language": "Mandarin Chinese",
                "example_phrase": "我正在吃饭 (Wǒ zhèngzài chīfàn - I am eating)"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that leverages the principle of linguistic relativity to enhance human cognitive abilities in the domain of {t['cognitive_domain']}, focusing on the linguistic feature of {t['linguistic_feature']} in {t['target_language']}. Your response should include:

1. Linguistic Relativity Analysis (250-300 words):
   a) Explain the concept of linguistic relativity and its relevance to {t['cognitive_domain']}.
   b) Analyze how {t['linguistic_feature']} in {t['target_language']} might influence cognition in this domain.
   c) Provide examples of how speakers of {t['target_language']} might think differently due to this linguistic feature.
   d) Analyze the given example phrase: "{t['example_phrase']}" in the context of linguistic relativity.

2. AI System Design (300-350 words):
   a) Propose an AI system that could enhance {t['cognitive_domain']} abilities by manipulating or augmenting {t['linguistic_feature']}.
   b) Describe the key components and architecture of your AI system.
   c) Explain how the system would interact with users to achieve cognitive enhancement.
   d) Discuss any novel algorithms or techniques your system would employ.

3. Cognitive Enhancement Mechanism (200-250 words):
   a) Detail the specific cognitive processes your system aims to enhance.
   b) Explain how manipulation of {t['linguistic_feature']} could lead to these enhancements.
   c) Propose a method to measure and quantify the cognitive improvements.
   d) Provide a hypothetical example of how your system might transform the given example phrase to enhance cognition.

4. Potential Applications (150-200 words):
   a) Suggest three potential real-world applications of your AI system.
   b) Explain how each application could benefit from enhanced {t['cognitive_domain']} abilities.
   c) Discuss any challenges in implementing these applications.

5. Ethical Implications (200-250 words):
   a) Identify potential ethical concerns related to cognitive enhancement through linguistic manipulation.
   b) Discuss how your system might impact cultural diversity and linguistic heritage.
   c) Propose guidelines for responsible development and use of such technology.
   d) Address potential misuse scenarios and suggest safeguards.

6. Limitations and Future Directions (150-200 words):
   a) Acknowledge any limitations or potential drawbacks of your proposed system.
   b) Suggest how these limitations might be addressed in future iterations.
   c) Propose a research agenda for further exploring the intersection of linguistic relativity and AI.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and AI. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately covers all six required sections, addressing {t['cognitive_domain']}, {t['linguistic_feature']}, and {t['target_language']}.",
            "The AI system design demonstrates a clear understanding of linguistic relativity and its potential applications in cognitive enhancement.",
            "The response shows creativity and innovation in the proposed AI system and its applications.",
            "The submission includes a thoughtful analysis of ethical implications and proposes responsible guidelines.",
            "The response maintains scientific plausibility while exploring novel ideas in cognitive enhancement through AI linguistics.",
            f"The response analyzes the given example phrase: \"{t['example_phrase']}\" in the context of linguistic relativity.",
            "The submission provides a hypothetical example of how the AI system might transform the given example phrase to enhance cognition.",
            "The response addresses potential misuse scenarios and suggests safeguards.",
            "The submission includes a word count and falls within the specified range of 1250-1550 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
