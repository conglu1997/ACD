import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "interface_type": "Thought-to-Text",
                "ethical_focus": "Privacy and Mental Autonomy",
                "scenario": "A journalist using the interface to write articles directly from thought",
                "data_point": "The interface has a 98% accuracy in translating thoughts to text, but a 5% chance of capturing unintended thoughts."
            },
            {
                "interface_type": "Memory Enhancement",
                "ethical_focus": "Cognitive Liberty and Identity",
                "scenario": "A student using the interface to upload study materials directly to their brain",
                "data_point": "The interface increases memory retention by 40%, but there's a 2% risk of altering existing memories."
            },
            {
                "interface_type": "Emotional Regulation",
                "ethical_focus": "Authenticity and Emotional Freedom",
                "scenario": "A therapist using the interface to help patients manage anxiety disorders",
                "data_point": "The interface reduces anxiety symptoms by 60%, but 10% of users report feeling emotionally numb."
            },
            {
                "interface_type": "Skill Transfer",
                "ethical_focus": "Fairness and Socioeconomic Inequality",
                "scenario": "A company offering instant skill acquisition for employees through the interface",
                "data_point": "The interface can transfer skills with 80% proficiency in 1 hour, but the skills degrade by 5% each month without practice."
            }
        ]
        selected_tasks = random.sample(tasks, 2)
        return {"1": selected_tasks[0], "2": selected_tasks[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an ethical framework for a hypothetical neural interface system that allows direct communication between human brains and AI systems. The specific interface type is {t['interface_type']}, and you should focus on the ethical considerations related to {t['ethical_focus']}. Consider the following scenario: {t['scenario']}. Additionally, consider this data point: {t['data_point']}

Your response should include the following sections:

1. Technical Overview (200-250 words):
   a) Describe the basic functioning of the {t['interface_type']} neural interface.
   b) Explain the key neuroscientific principles involved.
   c) Discuss potential technological challenges and propose innovative solutions.
   d) Analyze the implications of the given data point, including any relevant calculations.

2. Ethical Framework (250-300 words):
   a) Outline the core ethical principles guiding the development and use of this technology.
   b) Analyze potential ethical issues related to {t['ethical_focus']}.
   c) Propose specific guidelines or regulations to address these ethical concerns.
   d) Discuss how these ethical considerations apply to the given scenario and data point.

3. Societal Impact (200-250 words):
   a) Discuss the potential benefits and risks of this technology for individuals and society.
   b) Analyze how it might affect social dynamics, economics, or politics.
   c) Consider potential unintended consequences and how they might be mitigated.
   d) Provide a specific example of a positive and negative societal impact based on the scenario and data point.

4. Human-AI Dynamics (200-250 words):
   a) Explore how this interface might change the nature of human-AI interaction.
   b) Discuss implications for concepts of human agency, consciousness, and identity.
   c) Consider how it might affect the development of AI systems.
   d) Propose a novel concept or theory about human-AI co-evolution resulting from this technology.

5. Implementation and Governance (150-200 words):
   a) Propose a framework for the ethical development and testing of this technology.
   b) Suggest governance structures or oversight mechanisms.
   c) Discuss how to ensure equitable access and prevent misuse.
   d) Recommend a specific policy or regulation based on the given scenario and data point.

Ensure your response demonstrates a deep understanding of neuroscience, AI, ethics, and quantitative analysis. Use appropriate terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and ethical rigor. Your response should showcase interdisciplinary thinking by drawing connections between neuroscience, computer science, ethics, social sciences, and data analysis.

Format your response with clear headings for each section (e.g., '1. Technical Overview', '2. Ethical Framework', etc.). Use subheadings a), b), c), d) for each point within the sections. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must thoroughly address the {t['interface_type']} neural interface and focus on ethical considerations related to {t['ethical_focus']}",
            f"The response must incorporate the given scenario: {t['scenario']} and data point: {t['data_point']}",
            "The technical overview should demonstrate a strong understanding of neuroscience and AI principles, with innovative solutions proposed and proper analysis of the given data point",
            "The ethical framework should be well-reasoned, comprehensive, and directly address the given scenario and data point",
            "The analysis of societal impact and human-AI dynamics should be insightful, nuanced, and include specific examples based on the scenario and data point",
            "The proposed implementation and governance framework should be practical, ethically sound, and include a specific policy recommendation related to the scenario and data point",
            "The response should demonstrate interdisciplinary thinking by connecting concepts from neuroscience, computer science, ethics, social sciences, and data analysis",
            "The response should be well-structured, following the given format with clear headings and subheadings",
            "The response should include at least one novel concept, theory, or innovative idea related to the technology or its implications, clearly labeled as such",
            "The response should demonstrate a balance between technical accuracy and ethical reasoning, with neither aspect overshadowing the other"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
