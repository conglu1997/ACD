import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "memory_type": "episodic memory",
                "neural_mechanism": "long-term potentiation",
                "vr_environment": "historical reconstruction"
            },
            {
                "memory_type": "semantic memory",
                "neural_mechanism": "neural pattern completion",
                "vr_environment": "abstract concept visualization"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuromorphic computing system integrated with virtual reality to enhance human {t['memory_type']} formation and recall. Your system should focus on the neural mechanism of {t['neural_mechanism']} and utilize a {t['vr_environment']} as the primary virtual reality environment. Then, analyze its potential applications and ethical implications. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your neuromorphic computing system and how they interface with virtual reality technology.
   b) Explain how your system models {t['neural_mechanism']} and implements it in the neuromorphic architecture.
   c) Detail how the {t['vr_environment']} is designed to enhance {t['memory_type']} formation and recall.
   d) Include a high-level diagram or pseudocode snippet illustrating a crucial part of your system's architecture.

2. Memory Enhancement Mechanism (250-300 words):
   a) Explain the process by which your system enhances {t['memory_type']} formation using the {t['vr_environment']}.
   b) Describe how {t['neural_mechanism']} is utilized in this process.
   c) Discuss any novel algorithms or techniques used to optimize memory encoding and retrieval.

3. User Experience and Interaction (200-250 words):
   a) Describe the user experience of interacting with your memory enhancement system.
   b) Explain how users can customize or control their memory enhancement sessions.
   c) Discuss potential challenges users might face and how your system addresses them.

4. Performance Evaluation (200-250 words):
   a) Propose methods to measure the effectiveness of your system in enhancing {t['memory_type']}.
   b) Describe potential experiments to validate the system's impact on memory formation and recall.
   c) Discuss how you would compare your system's performance to traditional memory enhancement techniques.

5. Ethical Implications and Safeguards (250-300 words):
   a) Identify three potential ethical concerns raised by your neuromorphic VR memory enhancement system.
   b) Analyze these concerns using one ethical framework (e.g., utilitarianism, deontology, virtue ethics).
   c) Propose guidelines or safeguards to address these ethical issues.
   d) Discuss the broader societal implications of enhancing human memory capabilities.

6. Future Applications and Research Directions (150-200 words):
   a) Suggest two potential real-world applications of your memory enhancement system beyond individual use.
   b) Propose future research directions to expand the capabilities or address limitations of your system.
   c) Discuss potential interdisciplinary collaborations that could drive innovation in this field.

Ensure your response demonstrates a deep understanding of neuromorphic computing, neuroscience, virtual reality technology, and cognitive psychology. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuromorphic computing, neuroscience, virtual reality, and cognitive psychology, particularly in relation to {t['memory_type']} and {t['neural_mechanism']}.",
            f"The system design effectively integrates neuromorphic computing with virtual reality, utilizing {t['vr_environment']} to enhance memory formation and recall.",
            "The ethical analysis is comprehensive and thoughtful, addressing potential concerns and proposing meaningful safeguards.",
            "The proposed applications and future research directions are innovative and scientifically plausible.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
