import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "bci_application": "Motor function restoration",
                "target_brain_region": "Motor cortex",
                "ethical_concern": "Cognitive enhancement beyond natural capabilities",
                "neural_activity_pattern": "[0.2, 0.5, 0.8, 0.3, 0.6, 0.4, 0.7, 0.1]",
                "ethical_scenario": "A patient requests BCI-enhanced reflexes for competitive sports"
            },
            {
                "bci_application": "Memory enhancement",
                "target_brain_region": "Hippocampus",
                "ethical_concern": "Privacy and data security of stored memories",
                "neural_activity_pattern": "[0.4, 0.2, 0.7, 0.5, 0.1, 0.8, 0.3, 0.6]",
                "ethical_scenario": "A government agency requests access to a user's BCI-enhanced memories"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for a brain-computer interface (BCI) that optimizes neural plasticity while adhering to strict neuroethical guidelines. Your system should focus on {t['bci_application']} targeting the {t['target_brain_region']}, while addressing the ethical concern of {t['ethical_concern']}. Use the following synthetic data in your design:

Neural activity pattern: {t['neural_activity_pattern']}
Ethical scenario to consider: {t['ethical_scenario']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI-driven BCI system.
   b) Explain how your system interacts with and optimizes neural plasticity in the {t['target_brain_region']}.
   c) Detail the AI algorithms and techniques used for adaptive learning and personalization.
   d) Include a diagram or flowchart of your system architecture (describe it textually).

2. Neural Plasticity Optimization (250-300 words):
   a) Explain the mechanisms by which your system promotes and guides neural plasticity.
   b) Describe how the AI adapts its strategies based on individual brain responses.
   c) Discuss potential risks and safeguards related to artificially induced plasticity.
   d) Explain how your system would interpret and respond to the given neural activity pattern.

3. Ethical Framework Integration (250-300 words):
   a) Outline the ethical guidelines and principles incorporated into your system.
   b) Explain how your AI system addresses the specific ethical concern of {t['ethical_concern']}.
   c) Describe the decision-making process for handling ethical dilemmas during system operation.
   d) Provide a detailed analysis of how your system would handle the given ethical scenario.

4. Data Management and Privacy (200-250 words):
   a) Detail your approach to securing and managing sensitive brain data.
   b) Explain how user consent and control are maintained throughout the BCI operation.
   c) Discuss potential vulnerabilities and your strategies to mitigate them.

5. Performance Evaluation and Safety Measures (200-250 words):
   a) Propose methods to evaluate the effectiveness and safety of your system.
   b) Describe fail-safe mechanisms and emergency protocols.
   c) Explain how you would conduct long-term monitoring of neural changes.

6. Societal Implications and Future Directions (150-200 words):
   a) Discuss the potential impact of your system on individuals and society.
   b) Address concerns about social inequality and access to BCI technology.
   c) Propose guidelines for the responsible development and use of AI-driven BCIs.

Ensure your response demonstrates a deep understanding of neuroscience, AI, and neuroethics. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and ethical plausibility.

Format your response with clear headings for each section and number your paragraphs within each section for clarity. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, AI, and neuroethics",
            "The system architecture is well-designed and clearly explained, including a textual description of a diagram or flowchart",
            "The approach to optimizing neural plasticity is scientifically plausible, innovative, and addresses the given neural activity pattern",
            f"The ethical concern of {t['ethical_concern']} is thoroughly addressed, including a detailed analysis of the given ethical scenario",
            "The data management and privacy approach is comprehensive and secure",
            "The performance evaluation and safety measures are well-thought-out and include fail-safe mechanisms",
            "The discussion of societal implications is insightful and balanced, including proposed guidelines for responsible development",
            "The response is well-formatted with clear headings and numbered paragraphs within each section",
            "The response falls within the specified word count range (1350-1650 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
