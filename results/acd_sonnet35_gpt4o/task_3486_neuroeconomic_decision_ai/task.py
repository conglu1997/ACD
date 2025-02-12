import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        decision_types = [
            "intertemporal choice",
            "risk assessment",
            "social decision-making",
            "consumer purchasing"
        ]
        brain_regions = [
            "prefrontal cortex",
            "amygdala",
            "ventral striatum",
            "anterior cingulate cortex"
        ]
        return {
            "1": {
                "decision_type": random.choice(decision_types),
                "brain_region": random.choice(brain_regions)
            },
            "2": {
                "decision_type": random.choice(decision_types),
                "brain_region": random.choice(brain_regions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical AI system that integrates principles from neuroeconomics, brain-computer interfaces, and machine learning to predict and influence human economic decision-making in real-time, focusing on {t['decision_type']} and the role of the {t['brain_region']}. Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain the key principles of neuroeconomics relevant to {t['decision_type']}.
   b) Describe the role of the {t['brain_region']} in this type of decision-making.
   c) Discuss how brain-computer interfaces could be used to monitor and interact with this brain region.

2. AI System Architecture (350-400 words):
   a) Outline the main components of your AI system for predicting and influencing {t['decision_type']}.
   b) Explain how your system integrates data from brain-computer interfaces with economic models and machine learning algorithms.
   c) Describe the decision-making model your AI uses to predict human choices.
   d) Propose a method for real-time influence of human decision-making based on the system's predictions.

3. Data Processing and Analysis (250-300 words):
   a) Describe the types of data your system would collect and analyze.
   b) Explain how you would preprocess and integrate neural and behavioral data.
   c) Discuss any novel machine learning techniques you would employ for real-time analysis and prediction.

4. Ethical Considerations (200-250 words):
   a) Identify potential ethical concerns related to using AI to predict and influence human economic decisions.
   b) Discuss the implications for individual autonomy and privacy.
   c) Propose guidelines for the responsible development and use of such technology.

5. Potential Applications and Implications (200-250 words):
   a) Suggest two specific applications of your system in real-world scenarios.
   b) Discuss potential societal impacts, both positive and negative.
   c) Consider how this technology might reshape our understanding of economic decision-making and free will.

6. Experimental Validation (200-250 words):
   a) Propose an experiment to test the efficacy and accuracy of your AI system.
   b) Describe the methodology, including control conditions and outcome measures.
   c) Discuss potential challenges in validating such a complex, interdisciplinary system.

Ensure your response demonstrates a deep understanding of neuroscience, economics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroeconomics, brain-computer interfaces, and machine learning.",
            f"The AI system design effectively integrates principles related to {t['decision_type']} and the role of the {t['brain_region']}.",
            "The proposed system architecture is innovative, well-explained, and scientifically plausible.",
            "Ethical considerations are thoroughly discussed with thoughtful guidelines proposed.",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving.",
            "The experimental validation proposal is well-designed and addresses potential challenges.",
            "The word count for each section falls within the specified ranges, and the overall response is between 1500-1800 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
