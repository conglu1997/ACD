import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_function": "working memory",
                "musical_element": "rhythm",
                "cognitive_state": "focus"
            },
            {
                "brain_function": "emotional regulation",
                "musical_element": "harmony",
                "cognitive_state": "relaxation"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that composes music to enhance {t['brain_function']} through the use of {t['musical_element']}, with the goal of inducing a state of {t['cognitive_state']}. Your response should include:\n\n" + \
               "1. Neuroscientific Foundation (250-300 words):\n" + \
               "   a) Explain the neural mechanisms involved in {t['brain_function']}.\n" + \
               "   b) Describe how {t['musical_element']} is processed in the brain.\n" + \
               "   c) Discuss the relationship between {t['brain_function']} and {t['cognitive_state']}.\n\n" + \
               "2. AI Composition System Architecture (300-350 words):\n" + \
               "   a) Design an AI architecture that generates music based on neuroscientific principles.\n" + \
               "   b) Explain how your system incorporates knowledge of {t['brain_function']} and {t['musical_element']}.\n" + \
               "   c) Describe how you've implemented mechanisms to induce {t['cognitive_state']}.\n" + \
               "   d) Provide a diagram or detailed description of your system's structure.\n\n" + \
               "3. Composition Process (250-300 words):\n" + \
               "   a) Explain the step-by-step process of how your AI system composes music.\n" + \
               "   b) Describe how {t['musical_element']} is specifically manipulated to enhance {t['brain_function']}.\n" + \
               "   c) Discuss how your system adapts its compositions to individual listeners or contexts.\n\n" + \
               "4. Evaluation and Feedback Mechanism (200-250 words):\n" + \
               "   a) Propose a method to measure the effectiveness of the composed music on {t['brain_function']} and {t['cognitive_state']}.\n" + \
               "   b) Describe how this feedback is incorporated into the AI's learning and composition process.\n" + \
               "   c) Discuss potential challenges in evaluating the system's effectiveness and how to address them.\n\n" + \
               "5. Ethical and Societal Implications (200-250 words):\n" + \
               "   a) Discuss ethical considerations in using AI-composed music for cognitive enhancement.\n" + \
               "   b) Explore potential societal impacts of widespread use of this technology.\n" + \
               "   c) Propose guidelines for responsible development and use of neurosonic AI systems.\n\n" + \
               "6. Future Applications and Research Directions (150-200 words):\n" + \
               "   a) Suggest two potential applications of your neurosonic composition system beyond cognitive enhancement.\n" + \
               "   b) Propose a novel research question that arises from the integration of neuroscience, music, and AI.\n" + \
               "   c) Discuss how advancements in brain-computer interfaces might further enhance this technology.\n\n" + \
               "Ensure your response demonstrates a deep understanding of neuroscience, music theory, and AI system design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\n" + \
               "Format your response with clear headings for each section. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, music theory, and AI system design.",
            f"The AI system effectively incorporates principles of {t['brain_function']} and {t['musical_element']}.",
            f"The design appropriately addresses the goal of inducing a state of {t['cognitive_state']}.",
            "The composition process and evaluation mechanism are well-explained and scientifically grounded.",
            "The ethical and societal implications are thoughtfully considered.",
            "The response is creative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
