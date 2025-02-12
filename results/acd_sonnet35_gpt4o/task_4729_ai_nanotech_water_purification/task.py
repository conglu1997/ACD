import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "environment": "Urban wastewater treatment plant in a megacity",
                "primary_contaminant": "Heavy metals (lead, mercury)",
                "secondary_contaminant": "Antibiotic-resistant bacteria",
                "local_constraint": "High population density and limited land availability",
                "climate_condition": "Tropical monsoon climate"
            },
            {
                "environment": "Remote arctic research station",
                "primary_contaminant": "Microplastics",
                "secondary_contaminant": "Persistent organic pollutants",
                "local_constraint": "Extreme cold temperatures and limited energy resources",
                "climate_condition": "Polar climate"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven nanotechnology system for water purification that adapts to local environmental conditions and contaminants, then create a global implementation strategy. Your system should be tailored for a {t['environment']} dealing primarily with {t['primary_contaminant']} and {t['secondary_contaminant']}, while considering the local constraint of {t['local_constraint']} and the {t['climate_condition']}. Your response should include the following sections:

1. Nanotechnology Design (300-350 words):
   a) Describe the key components of your nanotechnology-based water purification system.
   b) Explain how your system targets and removes {t['primary_contaminant']} and {t['secondary_contaminant']}.
   c) Discuss any novel materials or structures you've incorporated for improved efficiency.
   d) Include a detailed description of your system's architecture.
   e) Provide quantitative estimates for the system's purification efficiency (e.g., percentage of contaminants removed).

2. AI Integration (250-300 words):
   a) Explain how AI is integrated into your water purification system.
   b) Describe how the AI adapts the system to changing environmental conditions and contaminant levels.
   c) Discuss specific machine learning techniques or algorithms used in your design.
   d) Explain how the AI system handles the local constraint of {t['local_constraint']} and adapts to the {t['climate_condition']}.
   e) Provide quantitative predictions for system performance improvements due to AI adaptation.

3. Environmental Impact and Sustainability (200-250 words):
   a) Analyze the environmental impact of your nanotechnology system.
   b) Discuss the system's energy efficiency and resource requirements.
   c) Explain how your design minimizes potential negative impacts on ecosystems.
   d) Provide quantitative estimates for the system's carbon footprint and resource consumption.

4. Scalability and Global Implementation (250-300 words):
   a) Outline a strategy for implementing your system globally, considering various environmental and economic contexts.
   b) Discuss how your system can be scaled up or down to meet different community sizes and needs.
   c) Address potential challenges in global adoption and propose solutions.
   d) Provide quantitative projections for global implementation timelines and coverage.

5. Economic Viability (150-200 words):
   a) Provide a detailed cost-benefit analysis of your water purification system.
   b) Discuss potential funding sources or business models for widespread implementation.
   c) Compare the economic viability of your system to traditional water treatment methods.
   d) Include quantitative estimates for implementation costs and potential economic benefits.

6. Ethical Considerations and Social Impact (200-250 words):
   a) Discuss ethical implications of using AI and nanotechnology for water purification.
   b) Address potential concerns about data privacy and security in your AI system.
   c) Analyze the potential social impact of your technology, including effects on water accessibility and public health.
   d) Provide quantitative predictions for improvements in public health outcomes.

Ensure your response demonstrates a deep understanding of nanotechnology, environmental science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and considering real-world constraints.

Format your response with clear headings for each section, numbered as outlined above. Within each section, use lettered subheadings (a, b, c, etc.) to organize your thoughts. Your total response should be between 1350-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed design of an AI-driven nanotechnology system for water purification tailored to a {t['environment']}",
            f"The system should effectively target and remove {t['primary_contaminant']} and {t['secondary_contaminant']}",
            f"The design must address the local constraint of {t['local_constraint']} and adapt to the {t['climate_condition']}",
            "The response should demonstrate a deep understanding of nanotechnology, environmental science, and artificial intelligence",
            "The proposed system should be innovative while maintaining scientific plausibility",
            "The response should include all required sections with appropriate detail, quantitative estimates, and word count",
            "The response should be formatted according to the given instructions, with clear headings and subheadings"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
