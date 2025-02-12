import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_elements = [
            "language",
            "religion",
            "social norms",
            "artistic expression",
            "political structures",
            "economic systems"
        ]
        cognitive_processes = [
            "memory consolidation",
            "social learning",
            "belief formation",
            "emotional regulation",
            "decision making",
            "identity formation"
        ]
        technological_features = [
            "immersive environments",
            "avatar customization",
            "real-time interaction",
            "data visualization",
            "AI-driven NPCs",
            "haptic feedback"
        ]
        research_questions = [
            "How do collective memories shape cultural identity?",
            "What factors influence the spread of cultural narratives?",
            "How do virtual experiences impact real-world beliefs and behaviors?",
            "What role does technology play in shaping cultural evolution?",
            "How do cognitive biases affect cultural transmission in virtual spaces?",
            "Can virtual societies provide insights into real-world cultural conflicts and resolutions?"
        ]
        challenges = [
            "rapid technological advancement",
            "cultural clash between two distinct groups",
            "environmental disaster",
            "introduction of a new religion",
            "shift in economic paradigm",
            "discovery of an advanced alien civilization"
        ]
        return {
            "1": {
                "cultural_element": random.choice(cultural_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "technological_feature": random.choice(technological_features),
                "research_question": random.choice(research_questions),
                "challenge": random.choice(challenges),
                "population_size": random.randint(1000, 10000),
                "initial_cultural_diversity": random.uniform(0.1, 0.9),
                "simulation_duration": random.randint(50, 500)
            },
            "2": {
                "cultural_element": random.choice(cultural_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "technological_feature": random.choice(technological_features),
                "research_question": random.choice(research_questions),
                "challenge": random.choice(challenges),
                "population_size": random.randint(1000, 10000),
                "initial_cultural_diversity": random.uniform(0.1, 0.9),
                "simulation_duration": random.randint(50, 500)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven virtual reality system that simulates the formation and evolution of collective memories and cultural narratives in artificial societies, then analyze its implications for understanding real-world cultural dynamics and social cognition. Your system should focus on the cultural element of {t['cultural_element']}, the cognitive process of {t['cognitive_process']}, and utilize the technological feature of {t['technological_feature']}. Address the research question: {t['research_question']}

Simulation Parameters:
- Population size: {t['population_size']} individuals
- Initial cultural diversity: {t['initial_cultural_diversity']:.2f} (0 = homogeneous, 1 = maximum diversity)
- Simulation duration: {t['simulation_duration']} time units
- Challenge: Your simulation must incorporate and analyze the effects of {t['challenge']}

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI-driven virtual reality system.
   b) Explain how your system models and simulates the specified cultural element and cognitive process.
   c) Detail how the specified technological feature is integrated into your system.
   d) Provide a high-level diagram or flowchart of your system architecture (describe it textually).

2. Simulation Mechanics (250-300 words):
   a) Explain the algorithms or mechanisms used to simulate cultural evolution and collective memory formation.
   b) Describe how individual and group behaviors are modeled within your virtual society.
   c) Discuss how your system handles the emergence and transmission of cultural narratives.
   d) Explain how your system incorporates and simulates the specified challenge.

3. Data Collection and Analysis (200-250 words):
   a) Outline the types of data your system collects during simulations.
   b) Describe the analytical methods used to interpret this data.
   c) Explain how your system identifies patterns or trends in cultural evolution.

4. Case Study (250-300 words):
   a) Present a detailed scenario demonstrating how your system would be applied to address the specified research question.
   b) Analyze the potential insights gained from this application, including the effects of the specified challenge.
   c) Discuss any limitations or challenges in extrapolating these findings to real-world cultures.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues in simulating and analyzing cultural dynamics.
   b) Discuss the implications of using AI to model human cultural processes.
   c) Propose guidelines for the responsible use of your system in cultural research.

6. Real-World Applications (200-250 words):
   a) Suggest at least three potential applications of your system in fields such as anthropology, sociology, or public policy.
   b) Explain how insights from your virtual cultures could inform real-world decision-making or cultural interventions.
   c) Discuss any potential risks or benefits of applying virtual cultural models to real societies.

7. Future Developments (150-200 words):
   a) Propose two potential enhancements or extensions to your system.
   b) Discuss how emerging technologies might further improve cultural simulation and analysis.
   c) Suggest future research directions based on your system's approach.

Ensure your response demonstrates a deep understanding of cultural anthropology, cognitive psychology, and virtual reality technology. Use appropriate terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and cultural sensitivity.

Format your response with clear headings for each section, numbered as above. Adhere strictly to the word count ranges provided for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cultural anthropology, cognitive psychology, and virtual reality technology.",
            f"The system architecture clearly integrates the specified cultural element ({t['cultural_element']}), cognitive process ({t['cognitive_process']}), and technological feature ({t['technological_feature']}).",
            "The simulation mechanics are well-explained and plausible for modeling cultural evolution and collective memory formation.",
            f"The system effectively incorporates and analyzes the effects of the specified challenge: {t['challenge']}.",
            "The data collection and analysis methods are appropriate and well-justified.",
            f"The case study effectively addresses the specified research question: {t['research_question']}",
            "Ethical considerations are thoroughly discussed with thoughtful guidelines proposed.",
            "At least three creative and well-explained real-world applications are provided.",
            "Future developments are innovative and build upon the proposed system in meaningful ways.",
            "The response is well-structured, adhering to the specified format and word count ranges.",
            "The overall approach is creative and innovative while maintaining scientific plausibility and cultural sensitivity."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
