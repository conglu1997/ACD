import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            "Urban heat island effect",
            "Water scarcity in agriculture",
            "Plastic pollution in oceans",
            "Air pollution in megacities"
        ]
        biomimetic_principles = [
            "Self-cleaning (Lotus effect)",
            "Thermoregulation (Termite mounds)",
            "Water harvesting (Namib desert beetle)",
            "Circular economy (Forest ecosystems)"
        ]
        resource_constraints = [
            "Limited energy availability",
            "Restricted material resources",
            "Financial budget constraints",
            "Time-sensitive implementation"
        ]
        changing_conditions = [
            "Increasing global temperatures",
            "Rapid urbanization",
            "Shifting precipitation patterns",
            "Evolving waste management regulations"
        ]
        return {
            "1": {
                "challenge": random.choice(environmental_challenges),
                "principle": random.choice(biomimetic_principles),
                "constraint": random.choice(resource_constraints),
                "condition": random.choice(changing_conditions)
            },
            "2": {
                "challenge": random.choice(environmental_challenges),
                "principle": random.choice(biomimetic_principles),
                "constraint": random.choice(resource_constraints),
                "condition": random.choice(changing_conditions)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an adaptive AI system that uses biomimicry principles to solve complex sustainability challenges, then apply it to the specific environmental problem of {t['challenge']}, focusing on the biomimetic principle of {t['principle']}, while considering the resource constraint of {t['constraint']} and adapting to the changing condition of {t['condition']}. Your response should include:

1. Adaptive Biomimetic AI System Architecture (300-350 words):
   a) Describe the key components of your adaptive AI system and how they integrate biomimicry with sustainability problem-solving.
   b) Explain how your system models and applies the specified biomimetic principle.
   c) Detail how your system analyzes and addresses complex environmental challenges while considering resource constraints and adapting to changing conditions.
   d) Include a high-level diagram or pseudocode illustrating your system's structure, processes, and adaptive mechanisms.

2. Biomimicry and Adaptive Implementation (250-300 words):
   a) Explain how the specified biomimetic principle is translated into adaptive computational models or algorithms.
   b) Describe how your AI system learns from and adapts natural processes to solve sustainability issues over time.
   c) Discuss any novel techniques you've developed to bridge the gap between biological systems, AI, and adaptive problem-solving.
   d) Explain how your system accounts for the given resource constraint and adapts to the specified changing condition.

3. Application to Dynamic Environmental Challenge (250-300 words):
   a) Apply your adaptive biomimetic AI system to the given environmental challenge.
   b) Provide a step-by-step explanation of how your system would approach, solve, and adapt to this problem over time.
   c) Describe the expected outcomes and how they address the sustainability issue in both short-term and long-term scenarios.
   d) Explain how your solution optimizes resource use and adapts to the changing condition over a 10-year period.

4. Comparative Analysis (200-250 words):
   a) Compare your adaptive biomimetic AI approach to traditional methods of addressing the given environmental challenge.
   b) Discuss the potential advantages and limitations of your approach, particularly in light of the resource constraint and changing condition.
   c) Analyze the scalability and adaptability of your solution to other sustainability issues and dynamic scenarios.

5. Ethical Considerations and Societal Impact (200-250 words):
   a) Discuss the ethical implications of using adaptive biomimetic AI for long-term environmental problem-solving.
   b) Address potential concerns about unintended consequences or ecological disruptions in a dynamic system.
   c) Analyze the broader societal impacts of implementing your adaptive solution, considering environmental, resource allocation, and social adaptation aspects.

6. Future Developments and Research Directions (150-200 words):
   a) Propose two potential enhancements or extensions to your adaptive biomimetic AI system that could further improve its long-term effectiveness.
   b) Suggest areas for further research in adaptive biomimicry, AI, sustainability, and resource management in dynamic environments.
   c) Speculate on how this technology might evolve and impact environmental conservation, resource allocation, and societal adaptation in the next two decades.

Ensure your response demonstrates a deep understanding of biomimicry, artificial intelligence, environmental science, resource management, and adaptive systems. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and ecological soundness.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the biomimetic principle of {t['principle']} and how it can be applied adaptively to address the environmental challenge of {t['challenge']} while considering the resource constraint of {t['constraint']} and adapting to the changing condition of {t['condition']}.",
            "The adaptive AI system architecture is well-explained and integrates biomimicry principles with AI techniques in a plausible manner, accounting for the specified resource constraint and changing condition over time.",
            "The application of the adaptive biomimetic AI system to the given environmental challenge is logical, detailed, and potentially effective, with clear consideration of resource optimization and long-term adaptation.",
            "The comparative analysis shows a thorough understanding of both traditional and adaptive biomimetic approaches to the environmental challenge, including their performance under resource constraints and changing conditions.",
            "Ethical considerations and societal impacts are thoughtfully discussed, showing an awareness of potential consequences related to environmental, resource allocation, and social adaptation aspects in a dynamic context.",
            "The response demonstrates creativity and innovation while maintaining scientific and ecological plausibility throughout, particularly in addressing the resource constraint and adapting to the changing condition over time."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
