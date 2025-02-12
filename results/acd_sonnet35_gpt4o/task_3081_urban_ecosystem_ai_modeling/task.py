import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_elements = ['green spaces', 'water systems', 'urban wildlife', 'air quality', 'energy flow']
        ecological_processes = ['nutrient cycling', 'species interactions', 'habitat fragmentation', 'pollution dynamics', 'urban heat island effect']
        ai_techniques = ['machine learning', 'agent-based modeling', 'neural networks', 'evolutionary algorithms', 'fuzzy logic']
        management_goals = ['biodiversity conservation', 'climate resilience', 'resource efficiency', 'human well-being', 'ecosystem services optimization']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "urban_element": random.choice(urban_elements),
                "ecological_process": random.choice(ecological_processes),
                "ai_technique": random.choice(ai_techniques),
                "management_goal": random.choice(management_goals)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for modeling and managing urban ecosystems, focusing on {t['urban_element']} and the ecological process of {t['ecological_process']}. Your system should use {t['ai_technique']} as its primary AI approach and aim to achieve the management goal of {t['management_goal']}. Provide a comprehensive response addressing the following points:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for urban ecosystem modeling and management.
   b) Explain how your system integrates knowledge from ecology, complex systems theory, and artificial intelligence.
   c) Detail how your system models the specified urban element and ecological process.
   d) Discuss how the chosen AI technique is applied in your system's design and operation.

2. Data Integration and Analysis (200-250 words):
   a) Describe the types of data your system would collect and analyze.
   b) Explain how your system would integrate data from various sources (e.g., sensors, satellite imagery, citizen science).
   c) Discuss any novel data analysis techniques your system employs to understand urban ecosystem dynamics.

3. Predictive Modeling and Simulation (200-250 words):
   a) Explain how your system models and simulates the specified ecological process within the urban context.
   b) Describe how your system accounts for the complexity and emergent properties of urban ecosystems.
   c) Discuss how your system handles uncertainty and variability in ecological processes and urban dynamics.

4. Management Strategies and Decision Support (200-250 words):
   a) Describe how your system generates and evaluates management strategies to achieve the specified goal.
   b) Explain how your system balances multiple objectives and handles trade-offs in urban ecosystem management.
   c) Discuss how your system adapts its recommendations based on feedback and changing conditions.

5. Ethical Considerations and Stakeholder Engagement (150-200 words):
   a) Identify potential ethical issues related to using AI for urban ecosystem management.
   b) Discuss how your system addresses concerns about data privacy, environmental justice, and unintended consequences.
   c) Propose methods for incorporating stakeholder input and ensuring transparency in the AI's decision-making process.

6. System Evaluation and Validation (150-200 words):
   a) Propose methods for evaluating the accuracy and effectiveness of your AI system in real-world urban environments.
   b) Discuss challenges in validating complex ecosystem models and how your system addresses them.
   c) Suggest approaches for continuous learning and improvement of your system over time.

7. Future Directions and Broader Impact (100-150 words):
   a) Suggest two potential extensions or improvements to your urban ecosystem AI system.
   b) Discuss how your approach could be applied to other environmental management challenges.
   c) Reflect on the potential long-term impacts of AI-driven urban ecosystem management on cities and society.

Ensure your response demonstrates a deep understanding of urban ecology, complex systems theory, and artificial intelligence. Use appropriate terminology from relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of urban ecology, complex systems theory, and artificial intelligence.",
            "The system architecture effectively integrates knowledge from multiple disciplines and addresses the specified urban element and ecological process.",
            "The data integration and analysis approach is comprehensive and innovative.",
            "The predictive modeling and simulation methods account for the complexity of urban ecosystems.",
            "The management strategies and decision support features are well-designed and adaptive.",
            "Ethical considerations and stakeholder engagement are thoroughly addressed.",
            "The proposed evaluation and validation methods are appropriate and address the challenges of complex ecosystem modeling.",
            "Future directions and broader impact are insightful and well-reasoned.",
            "The response is creative and demonstrates effective interdisciplinary knowledge integration.",
            "The response follows the required format and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
