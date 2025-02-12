import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_practices = [
            "traditional weaving techniques of the Navajo tribe",
            "ancient Polynesian navigation methods",
            "Kabuki theater makeup application",
            "Inuit throat singing",
            "Venetian glass blowing techniques"
        ]
        technologies = [
            "motion capture with skeletal tracking",
            "volumetric video capture",
            "neural radiance fields (NeRF)",
            "haptic feedback gloves",
            "spatial audio with head-related transfer function (HRTF)"
        ]
        tasks = {
            "1": {
                "cultural_practice": random.choice(cultural_practices),
                "technology": random.choice(technologies)
            },
            "2": {
                "cultural_practice": random.choice(cultural_practices),
                "technology": random.choice(technologies)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system using augmented reality and AI to preserve and recreate the endangered cultural practice of {t['cultural_practice']}, incorporating {t['technology']} as a key component. Your response should include:

1. System Design (300-350 words):
   a) Describe the overall architecture of your AR-AI system for cultural preservation.
   b) Explain how you incorporate {t['technology']} into your system.
   c) Detail the AI components used for capturing, processing, and recreating the cultural practice.
   d) Discuss any novel features or innovations in your design.
   e) Provide a high-level diagram of your system architecture (describe it textually).

2. Data Collection and Processing (250-300 words):
   a) Outline your approach to collecting data on the endangered cultural practice.
   b) Describe how you ensure the authenticity and accuracy of the captured information.
   c) Explain your data processing pipeline, including any AI-driven analysis or enhancement.
   d) Discuss how you handle potential biases or gaps in the collected data.

3. User Experience and Interaction (250-300 words):
   a) Describe how users would interact with your system to learn about or experience the cultural practice.
   b) Explain how your system adapts to different user skill levels or cultural backgrounds.
   c) Discuss how you balance technological immersion with cultural authenticity.
   d) Provide a detailed description or mock-up of the AR interface, including key features and interactions.

4. Cultural and Ethical Considerations (250-300 words):
   a) Analyze potential cultural sensitivities or ethical concerns in digitizing and recreating this practice.
   b) Discuss how you involve the cultural community in the preservation process.
   c) Propose guidelines for responsible use and distribution of the digitized cultural content.
   d) Address potential issues of intellectual property rights and cultural appropriation.

5. Evaluation and Impact Assessment (200-250 words):
   a) Propose metrics to evaluate the effectiveness of your system in preserving and transmitting cultural knowledge.
   b) Discuss potential positive and negative impacts on the cultural community and broader society.
   c) Suggest a method for long-term monitoring of your system's influence on cultural preservation.
   d) Describe a specific experiment to measure the educational effectiveness of your system.

6. Future Developments and Applications (150-200 words):
   a) Propose two potential extensions or improvements to your system.
   b) Discuss how your approach might be applied to other areas of cultural or historical preservation.
   c) Speculate on potential long-term effects of widespread adoption of AR cultural preservation systems.

7. Limitations and Failure Modes (100-150 words):
   a) Identify potential limitations or failure modes of your proposed system.
   b) Discuss how these limitations might impact the effectiveness of cultural preservation.
   c) Propose strategies to mitigate or address these potential issues.

Example Scenario (not a solution):
Imagine a system that allows users to virtually apprentice with a master Venetian glassblower. The system uses volumetric capture to record the master's movements and spatial audio to capture their instructions. Users wear AR glasses and haptic gloves to see and feel the glassblowing process. The system adapts to the user's skill level, providing more or less guidance as needed.

Ensure your response demonstrates a deep understanding of augmented reality, AI, and cultural anthropology. Be innovative in your approach while maintaining cultural sensitivity and ethical considerations. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of augmented reality, AI, and cultural anthropology, particularly in relation to {t['cultural_practice']} and {t['technology']}.",
            "The system design is innovative, technically feasible, and effectively incorporates the specified technology.",
            "The system architecture diagram is clear and comprehensive.",
            "The approach to data collection and processing is comprehensive, culturally sensitive, and addresses potential biases.",
            "The user experience design balances technological immersion with cultural authenticity, and includes a detailed AR interface description.",
            "The response thoroughly addresses cultural and ethical considerations, including community involvement, intellectual property rights, and cultural appropriation.",
            "The proposed evaluation metrics, impact assessment, and educational experiment are well-thought-out and relevant.",
            "The suggested future developments and applications are creative, plausible, and consider long-term societal effects.",
            "The response identifies and addresses potential limitations and failure modes of the proposed system.",
            "The writing is clear, well-structured, and uses appropriate technical terminology.",
            "The response follows the required format and word count (1500-1850 words)."
        ]
        score = sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria)
        return score
