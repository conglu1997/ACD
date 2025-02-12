import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        decision_scenarios = [
            {
                "scenario": "Global climate policy",
                "constraint": "Uncertainty in long-term climate models",
                "cognitive_bias": "Hyperbolic discounting"
            },
            {
                "scenario": "Pandemic response strategy",
                "constraint": "Limited real-time data availability",
                "cognitive_bias": "Availability heuristic"
            },
            {
                "scenario": "Interstellar colonization planning",
                "constraint": "Multi-generational timescales",
                "cognitive_bias": "Optimism bias"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(decision_scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical brain-computer interface (BCI) that integrates human decision-making processes with AI algorithms to enhance complex problem-solving capabilities. Your BCI should address the scenario of {t['scenario']}, considering the constraint of {t['constraint']} and mitigating the cognitive bias of {t['cognitive_bias']}. Your response should include the following sections:

1. BCI System Architecture (300-350 words):
   a) Describe the key components of your BCI, including both neural interfaces and AI modules.
   b) Explain how your system integrates human neural signals with AI algorithms.
   c) Discuss how your BCI addresses the specific scenario, constraint, and cognitive bias.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Neuroscientific Basis (250-300 words):
   a) Explain the neuroscientific principles underlying your BCI's interaction with human decision-making processes.
   b) Describe how your system interfaces with specific brain regions or networks involved in decision-making.
   c) Discuss how your BCI mitigates the specified cognitive bias at a neural level.

3. AI Algorithm Integration (250-300 words):
   a) Detail the AI algorithms and techniques used in your BCI system.
   b) Explain how these algorithms complement and enhance human decision-making capabilities.
   c) Describe how the AI component addresses the given scenario and constraint.
   d) Provide a brief pseudocode or mathematical representation of a key algorithm in your approach.

4. Decision-Making Process (200-250 words):
   a) Outline the step-by-step process of how a decision is made using your BCI system.
   b) Explain how human intuition and AI-driven analysis are balanced in the decision-making process.
   c) Discuss how your system handles potential conflicts between human and AI-generated decisions.

5. Ethical Considerations and Limitations (200-250 words):
   a) Identify potential ethical issues in using BCIs for decision-making enhancement.
   b) Discuss how your system ensures user autonomy and prevents undue AI influence.
   c) Address potential risks or limitations of your BCI system.
   d) Propose guidelines for the responsible development and use of such technology.

6. Performance Evaluation (200-250 words):
   a) Propose a method for evaluating the effectiveness of your BCI system in enhancing decision-making.
   b) Describe potential metrics for measuring improvements in decision quality and mitigation of cognitive bias.
   c) Suggest an experimental design to test your BCI system's performance in the given scenario.

7. Future Implications (150-200 words):
   a) Speculate on how your BCI technology might evolve and impact society in the long term.
   b) Discuss potential applications of your system beyond the given scenario.
   c) Consider how this technology might change our understanding of human cognition and AI integration.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and decision theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1550-1900 words. Each section must meet the minimum word count specified. Additionally, cite at least two relevant scientific papers or theories in your response to support your design or analysis."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, artificial intelligence, and decision theory, with at least two relevant scientific papers or theories cited",
            "The BCI design is innovative, well-described, and plausibly addresses the given scenario, constraint, and cognitive bias",
            "The integration of human neural processes and AI algorithms is logically explained and scientifically grounded",
            "The ethical considerations and limitations are thoughtfully addressed, with specific guidelines proposed",
            "The performance evaluation proposal is well-designed, with clear metrics and an experimental design addressing the given scenario",
            "The response is well-structured, adheres to the word count guidelines for each section, and uses appropriate technical terminology",
            "The future implications section provides insightful speculation on the long-term impact and potential applications of the technology"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
