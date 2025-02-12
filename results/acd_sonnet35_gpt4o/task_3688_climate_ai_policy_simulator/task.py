import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "region": "Southeast Asia",
                "time_frame": "2050",
                "challenge": "Rising sea levels and increased typhoon intensity"
            },
            {
                "region": "Sub-Saharan Africa",
                "time_frame": "2040",
                "challenge": "Prolonged droughts and agricultural disruption"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates global climate patterns, predicts outcomes of policy interventions, and generates policy recommendations for addressing climate challenges. Apply your system to the following scenario:

Region: {t['region']}
Time Frame: {t['time_frame']}
Challenge: {t['challenge']}

Your response should include:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for climate simulation and policy analysis.
   b) Explain how it integrates climate models with policy impact assessment.
   c) Detail how the system handles uncertainty and long-term projections.
   d) Discuss any novel approaches or mechanisms in your design.
   e) Provide a small code snippet or pseudocode (30-50 lines) demonstrating a key aspect of your system's implementation.

2. Climate Simulation and Prediction (250-300 words):
   a) Explain how your system models and simulates global climate patterns.
   b) Describe how it incorporates various data sources and handles data uncertainty.
   c) Discuss the system's approach to long-term climate projections.

3. Policy Intervention Analysis (300-350 words):
   a) Detail how your AI system evaluates the potential impact of different policy interventions.
   b) Explain how it considers interactions between climate, economic, and social factors.
   c) Describe the metrics used to assess policy effectiveness.
   d) Provide an example of how the system would analyze a specific policy intervention.

4. Ethical Considerations and Bias Mitigation (200-250 words):
   a) Discuss potential ethical issues in using AI for climate policy recommendations.
   b) Explain how your system addresses potential biases in data or algorithms.
   c) Describe safeguards to ensure transparency and accountability in the system's recommendations.

5. Scenario Application (250-300 words):
   a) Apply your AI system to the given scenario.
   b) Provide a sample output of policy recommendations for addressing the specified challenge.
   c) Explain the reasoning behind these recommendations.

6. Global Cooperation and Implementation (200-250 words):
   a) Discuss how your system could facilitate international cooperation on climate policy.
   b) Address challenges in implementing AI-generated policy recommendations across different political systems.
   c) Propose mechanisms for integrating local knowledge and preferences into the system's recommendations.

7. Limitations and Future Improvements (150-200 words):
   a) Discuss the limitations of your proposed AI system.
   b) Suggest areas for future research or improvement.
   c) Speculate on potential long-term impacts of using AI in climate policy-making.

Ensure your response demonstrates a deep understanding of climate science, policy analysis, and AI capabilities. Be creative and original in your approach while maintaining scientific plausibility. Use clear headings for each section of your response.

Your total response should be between 1650-2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include all seven required sections with appropriate content and word counts.",
            "The AI system design must be innovative, coherent, and demonstrate a deep understanding of climate science, policy analysis, and AI capabilities.",
            "The response must provide a relevant code snippet or pseudocode as specified.",
            "The application to the given scenario must be thoughtful and demonstrate how the AI system would address the specific challenge.",
            "The response must thoroughly discuss ethical considerations, bias mitigation, and challenges in global cooperation.",
            "The overall response must be creative, scientifically plausible, and demonstrate interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
