class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "title": "User Manual for a Smart Thermostat",
                "specifications": "The smart thermostat allows users to control the temperature of their home remotely via a mobile app. It has features like scheduling, geofencing, and energy usage reports. It supports both Fahrenheit and Celsius. The device can be integrated with smart home systems like Google Home and Amazon Alexa."
            },
            "2": {
                "title": "API Documentation for a Weather Data Service",
                "specifications": "The weather data service provides real-time weather updates and forecasts. It offers endpoints for current weather, 7-day forecast, and historical weather data. The API uses RESTful principles and supports JSON responses. Authentication is done through API keys. Rate limits are set to 1000 requests per day."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to produce technical documentation based on the following specifications:\n\nTitle: {t['title']}\n\nSpecifications: {t['specifications']}\n\nYour documentation should include the following elements:\n1. An introduction that provides an overview of the product or service.\n2. Detailed instructions or descriptions of key features and functionalities.\n3. Any necessary diagrams or examples to illustrate usage.\n4. A section on troubleshooting common issues.\n5. Clear and concise language throughout.\n\nProvide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The documentation should include an introduction.",
            "The documentation should provide detailed instructions or descriptions of key features and functionalities.",
            "The documentation should include diagrams or examples where necessary.",
            "The documentation should include a section on troubleshooting common issues.",
            "The language should be clear and concise."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
