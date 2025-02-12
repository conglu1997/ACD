import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ethical_dilemmas = [
            "Trolley problem",
            "Lying to protect someone's feelings",
            "Stealing medicine for a sick relative",
            "Whistleblowing on corporate misconduct",
            "Euthanasia for a terminally ill patient",
            "Using animal testing for medical research",
            "Sacrificing privacy for national security",
            "Genetic engineering of human embryos"
        ]
        cultural_contexts = [
            "Individualistic Western society",
            "Collectivist East Asian culture",
            "Indigenous tribal community",
            "Secular European nation",
            "Religious Middle Eastern society",
            "Post-communist Eastern European country",
            "African ubuntu philosophy-based culture",
            "Multicultural metropolitan city"
        ]
        cognitive_processes = [
            "Emotional regulation",
            "Theory of mind",
            "Moral reasoning",
            "Cultural value integration",
            "Empathy and perspective-taking",
            "Conflict resolution",
            "Ethical principle application",
            "Consequentialist thinking"
        ]
        
        return {
            "1": {
                "dilemma": random.choice(ethical_dilemmas),
                "context": random.choice(cultural_contexts),
                "process": random.choice(cognitive_processes)
            },
            "2": {
                "dilemma": random.choice(ethical_dilemmas),
                "context": random.choice(cultural_contexts),
                "process": random.choice(cognitive_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and simulates moral decision-making processes across different cultures. Your system should address the ethical dilemma of {t['dilemma']} within the cultural context of {t['context']}, focusing on the cognitive process of {t['process']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the chosen ethical dilemma and its significance in moral decision-making.
   b) Describe the relevant cultural context and how it influences moral reasoning.
   c) Discuss the specified cognitive process and its role in ethical decision-making.
   d) Propose how these elements can be integrated into a coherent framework for your AI system.

2. AI System Architecture (300-350 words):
   a) Outline the overall structure of your cultural moral AI simulator.
   b) Explain how it incorporates the ethical dilemma, cultural context, and cognitive process.
   c) Describe the main components and their interactions.
   d) Discuss any novel algorithms or approaches used in your design.
   e) Include a simple diagram or flowchart of your system architecture.

3. Cultural-Cognitive Modeling (250-300 words):
   a) Detail how your system models the interaction between cultural influences and cognitive processes in moral decision-making.
   b) Explain how this approach enhances the analysis of the chosen ethical dilemma.
   c) Provide a specific example of how your system would process the ethical dilemma in the given cultural context.

4. Ethical Reasoning Simulation (200-250 words):
   a) Describe how your AI system simulates the ethical reasoning process for the given dilemma.
   b) Explain how it accounts for cultural variations in moral values and norms.
   c) Discuss any challenges in modeling complex ethical decision-making processes.

5. Potential Applications and Implications (200-250 words):
   a) Propose potential applications of your system in ethics research, cross-cultural studies, or AI ethics.
   b) Discuss how your approach could advance our understanding of moral decision-making across cultures.
   c) Address any ethical considerations or potential misuses of this technology.

6. Evaluation and Future Work (150-200 words):
   a) Suggest methods to evaluate the performance and validity of your cultural moral AI simulator.
   b) Identify limitations of your current design and areas for future research and improvement.
   c) Propose an experiment to test a specific hypothesis about cultural variations in moral decision-making using your system.

Ensure your response demonstrates a deep understanding of ethics, cultural anthropology, cognitive science, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The AI system effectively addresses the ethical dilemma of {t['dilemma']} within the cultural context of {t['context']}.",
            f"The system adequately incorporates and models the cognitive process of {t['process']} in ethical decision-making.",
            "The response demonstrates a deep understanding and integration of ethics, cultural anthropology, cognitive science, and artificial intelligence.",
            "The proposed AI system architecture is innovative, well-structured, and scientifically plausible.",
            "The cultural-cognitive modeling approach is clearly explained and enhances the analysis of the ethical dilemma.",
            "The ethical reasoning simulation accounts for cultural variations in moral values and norms.",
            "Potential applications, implications, and ethical considerations are thoughtfully discussed.",
            "The evaluation methods and future work proposals are relevant and well-reasoned.",
            "The response adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
