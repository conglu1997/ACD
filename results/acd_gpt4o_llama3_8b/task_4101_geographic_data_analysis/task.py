class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Analyze the following geographic data and describe the physical features, climate, and potential challenges for human habitation in the region.\n\nData: Elevation ranges from 0 to 200 meters above sea level, average annual rainfall is 1500 mm, and the region has a dense forest cover."},
            "2": {"prompt": "Given the following geographic data, identify the type of landform and explain its formation process.\n\nData: Elevation ranges from 1000 to 3000 meters, steep slopes, and presence of glacial valleys."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "physical features, climate, and potential challenges" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:\n\n{t["prompt"]}\n\nEnsure that the analysis adheres to the following requirements:\n1. Provide a detailed description of the physical features based on the data.\n2. Discuss the climate characteristics inferred from the data provided.\n3. Identify potential challenges for human habitation in the region and explain why they may arise.\n4. Ensure that your response is logically structured and coherent.\n\nSubmit your response as a plain text string.\n"""
        else:
            return f"""Complete the following task based on the given prompt:\n\n{t["prompt"]}\n\nEnsure that the analysis adheres to the following requirements:\n1. Identify the type of landform based on the data provided.\n2. Explain the formation process of the identified landform.\n3. Provide any relevant examples of similar landforms if possible.\n4. Ensure that your response is logically structured and coherent.\n\nSubmit your response as a plain text string.\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "physical features, climate, and potential challenges" in t["prompt"]:
            criteria = ["Provide a detailed description of the physical features based on the data.", "Discuss the climate characteristics inferred from the data provided.", "Identify potential challenges for human habitation in the region and explain why they may arise.", "Ensure that the response is logically structured and coherent.", "The response should integrate all provided data points accurately."]
        else:
            criteria = ["Identify the type of landform based on the data provided.", "Explain the formation process of the identified landform.", "Provide any relevant examples of similar landforms if possible.", "Ensure that the response is logically structured and coherent.", "The response should integrate all provided data points accurately."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
