class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "product_description": "A smart thermostat that can be controlled via a mobile app, supports voice commands, and learns the user's schedule to optimize energy usage. It features a sleek touchscreen interface and provides real-time energy consumption data.",
                "task_type": "generate"
            },
            "2": {
                "technical_specification": "Product Name: EcoTherm Smart Thermostat\nDimensions: 3.5 x 3.5 x 1 inches\nWeight: 0.5 lbs\nConnectivity: Wi-Fi, Bluetooth\nCompatibility: iOS, Android\nVoice Assistants: Alexa, Google Assistant\nLearning Algorithm: Adaptive scheduling based on user behavior\nEnergy Savings: Up to 20% on heating and cooling bills\nDisplay: 4-inch touchscreen\nReal-time Data: Yes, provides real-time energy consumption data\nInstallation: DIY with step-by-step guide or professional installation available.",
                "task_type": "interpret"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generate":
            return f"""Generate a detailed technical specification for the following product description. Ensure that the specification includes key details such as dimensions, weight, connectivity, compatibility, features, display, and any other relevant technical information. Your specification should be clear, concise, and logically organized.

Product Description:
{t['product_description']}

Submit your technical specification as a plain text string in the following format:
'Technical Specification: [Your specification here]'"""
        elif t["task_type"] == "interpret":
            return f"""Interpret the following technical specification and describe the product in layman's terms. Ensure that your description captures the key features and functionalities of the product in a way that is easy for a general audience to understand.

Technical Specification:
{t['technical_specification']}

Submit your interpretation as a plain text string in the following format:
'Product Description: [Your description here]'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generate":
            validation_criteria = ["The technical specification should include key details such as dimensions, weight, connectivity, compatibility, features, display, and any other relevant technical information.", "The specification should be clear, concise, and logically organized."]
        elif t["task_type"] == "interpret":
            validation_criteria = ["The interpretation should capture the key features and functionalities of the product.", "The description should be easy for a general audience to understand."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
