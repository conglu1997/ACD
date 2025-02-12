class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "scenario": "A detective investigating a complex crime scene with multiple witnesses and conflicting evidence.",
                "decision_goal": "Identify the most likely suspect and provide a justification for the conclusion."
            },
            "2": {
                "scenario": "A diplomat navigating a delicate international negotiation with multiple stakeholders and hidden agendas.",
                "decision_goal": "Propose a resolution that satisfies the most critical needs of all parties involved."
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that integrates natural language processing, episodic memory, and decision-making processes to solve complex narrative-based problems. Then, apply your system to the following scenario:

{t['scenario']}

Your task is to {t['decision_goal']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system, including the natural language processing, episodic memory, and decision-making modules.
   b) Explain how these components interact and integrate to process information and make decisions.
   c) Discuss any novel techniques or approaches used in your design to enable the integration of language, memory, and decision-making.
   d) Provide a high-level diagram or flowchart of your system (describe it textually).

2. Natural Language Processing (200-250 words):
   a) Explain how your system processes and understands complex narrative information.
   b) Describe any techniques used for handling ambiguity, context, and implicit information in the narratives.
   c) Discuss how your system extracts relevant facts and relationships from the input scenario.

3. Episodic Memory Formation and Retrieval (200-250 words):
   a) Describe how your system forms and stores episodic memories based on the processed narrative information.
   b) Explain the mechanisms for retrieving relevant memories during the decision-making process.
   c) Discuss how your system handles conflicting or inconsistent information in memory.

4. Decision-Making Process (250-300 words):
   a) Explain the decision-making algorithm or approach used by your system.
   b) Describe how your system integrates information from natural language processing and episodic memory to make decisions.
   c) Discuss any reasoning or inference mechanisms used to draw conclusions from the available information.
   d) Explain how your system handles uncertainty and weighs different pieces of evidence.

5. Application to the Scenario (300-350 words):
   a) Apply your AI system to the given scenario, walking through each step of the process.
   b) Explain how the system processes the narrative, forms memories, and makes decisions based on the available information.
   c) Provide the final output of your system, addressing the specified decision goal.
   d) Justify the system's conclusion, explaining how it arrived at its decision.

6. Evaluation and Limitations (200-250 words):
   a) Propose methods for evaluating the performance and effectiveness of your AI system.
   b) Discuss potential limitations or challenges in your approach.
   c) Suggest areas for future improvement or research in integrating language, memory, and decision-making in AI systems.

Ensure your response demonstrates a deep understanding of natural language processing, cognitive architectures, and decision-making algorithms. Be creative and innovative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of natural language processing, cognitive architectures, and decision-making algorithms.",
            "The proposed AI system effectively integrates language processing, episodic memory, and decision-making components.",
            "The application to the given scenario is thorough, logical, and addresses the specified decision goal.",
            "The response is creative and innovative while maintaining scientific and technological plausibility.",
            "The evaluation and limitations section provides insightful analysis of the system's performance and potential improvements.",
            "The response is well-structured, comprehensive, and adheres to the word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
