import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        archaeological_sites = [
            "Göbekli Tepe, Turkey",
            "Mohenjo-daro, Pakistan",
            "Nan Madol, Micronesia",
            "Great Zimbabwe, Zimbabwe",
            "Cahokia, United States"
        ]
        
        historical_mysteries = [
            "Purpose of the site",
            "Societal structure",
            "Technological capabilities",
            "Environmental changes",
            "Reasons for abandonment"
        ]
        
        ai_techniques = [
            "Computer vision and image recognition",
            "Natural language processing of historical texts",
            "Generative adversarial networks for reconstruction",
            "Reinforcement learning for simulating historical scenarios",
            "Knowledge graphs for connecting archaeological evidence"
        ]
        
        vr_features = [
            "Haptic feedback for artifact examination",
            "Time-lapse visualization of site changes",
            "Multi-user collaborative exploration",
            "AI-guided virtual tour and narration",
            "Interactive simulation of daily life in the past"
        ]
        
        return {
            "1": {
                "archaeological_site": random.choice(archaeological_sites),
                "historical_mystery": random.choice(historical_mysteries),
                "ai_technique": random.choice(ai_techniques),
                "vr_feature": random.choice(vr_features)
            },
            "2": {
                "archaeological_site": random.choice(archaeological_sites),
                "historical_mystery": random.choice(historical_mysteries),
                "ai_technique": random.choice(ai_techniques),
                "vr_feature": random.choice(vr_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven virtual reality system for reconstructing and exploring ancient archaeological sites, then use it to analyze a specific historical mystery. Your system should focus on the archaeological site of {t['archaeological_site']}, addressing the historical mystery of {t['historical_mystery']}. Incorporate the AI technique of {t['ai_technique']} and the VR feature of {t['vr_feature']} in your design.

Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI-driven VR system for archaeological reconstruction and exploration.
   b) Explain how your system integrates AI, VR, and archaeological data processing.
   c) Detail how {t['ai_technique']} is incorporated into your system's functionality.
   d) Discuss how {t['vr_feature']} enhances the user experience and archaeological analysis.
   e) Address any technical challenges in implementing this system and propose solutions.

2. Archaeological Data Processing (250-300 words):
   a) Explain how your system would gather and process archaeological data from {t['archaeological_site']}.
   b) Describe the AI algorithms used for analyzing and interpreting this data.
   c) Discuss how your system handles uncertainties or gaps in the archaeological record.
   d) Explain how the system ensures accuracy and authenticity in its reconstructions.

3. Virtual Reconstruction and Exploration (250-300 words):
   a) Describe the process of creating a virtual reconstruction of {t['archaeological_site']}.
   b) Explain how users can interact with and explore the virtual environment.
   c) Detail how {t['vr_feature']} is implemented and its benefits for users and researchers.
   d) Discuss any novel visualization techniques used in your system.

4. Historical Mystery Analysis (250-300 words):
   a) Apply your AI-VR system to analyze the historical mystery of {t['historical_mystery']} at {t['archaeological_site']}.
   b) Describe the specific tools or features of your system that aid in this analysis.
   c) Propose a hypothesis or solution to the mystery based on your system's analysis.
   d) Explain how your system's approach differs from traditional archaeological methods.

5. Ethical Considerations and Limitations (200-250 words):
   a) Discuss potential ethical issues in using AI and VR for archaeological reconstruction and analysis.
   b) Address concerns about cultural sensitivity and representation in virtual reconstructions.
   c) Analyze potential biases in AI reconstruction and propose mitigation strategies.
   d) Explain how your system ensures responsible use and interpretation of archaeological data.
   e) Discuss any limitations of your system and areas for future improvement.

6. Educational and Research Applications (150-200 words):
   a) Propose ways your system could be used in educational settings or public outreach.
   b) Discuss potential research applications beyond the specific case study.
   c) Suggest how your system could contribute to the broader field of digital archaeology.

7. Case Study Example (200-250 words):
   Provide a brief case study illustrating how your AI-VR system might be used to investigate a specific artifact or feature at {t['archaeological_site']}. Include details on the data input, AI analysis process, VR visualization, and potential insights gained.

Ensure your response demonstrates a deep understanding of artificial intelligence, virtual reality technology, and archaeological methods. Use appropriate terminology from all relevant fields and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific and historical plausibility.

Format your response with clear headings for each section, and include the word count for each section in parentheses at the end of the section. Your total response should be between 1600-1950 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of AI, VR, and archaeological principles and methods.",
            "The proposed AI-VR system is innovative, scientifically plausible, and effectively incorporates the specified AI technique and VR feature.",
            "The analysis of the historical mystery is thorough, creative, and grounded in archaeological evidence and AI-assisted interpretation.",
            "Ethical considerations, limitations, and potential biases are thoughtfully addressed, showing awareness of cultural sensitivities and responsible use of technology in archaeology.",
            "The educational and research applications are insightful and demonstrate the broader potential of the proposed system.",
            "The case study example effectively illustrates the practical application of the AI-VR system in a specific archaeological context.",
            "The overall response is well-structured, coherent, and demonstrates strong interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
