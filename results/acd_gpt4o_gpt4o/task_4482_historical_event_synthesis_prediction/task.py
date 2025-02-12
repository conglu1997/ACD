class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"events": [
                "The Industrial Revolution (1760-1840): A period of major industrialization that transformed processes and lifestyles.",
                "The Great Depression (1929-1939): A severe worldwide economic depression that took place during the 1930s.",
                "The Cold War (1947-1991): A period of geopolitical tension between the Soviet Union and the United States.",
                "The Information Age (1970s-present): The current period characterized by the rapid shift from traditional industry to an economy based on information technology."
            ], "scenario": "What if the internet was invented during the Industrial Revolution? Predict the plausible outcomes of such an event on society, economy, and global power dynamics."},
            "2": {"events": [
                "The Renaissance (14th-17th centuries): A period in Europe marked by a revival of art, culture, and knowledge.",
                "The French Revolution (1789-1799): A period of radical social and political change in France that had a profound impact on the country and the world.",
                "World War II (1939-1945): A global war that involved most of the world's nations and resulted in significant changes to global power structures.",
                "The Space Race (1957-1969): A 20th-century competition between the Soviet Union and the United States to achieve significant milestones in space exploration."
            ], "scenario": "What if Leonardo da Vinci had access to modern computing technology during the Renaissance? Predict the plausible outcomes of such an event on science, art, and technological development."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        events = "\n".join(t["events"])
        scenario = t["scenario"]
        instructions = f"""Your task is to synthesize information from the following historical events and predict the plausible outcomes based on the given hypothetical scenario.\n\nHistorical Events:\n{events}\n\nScenario:\n{scenario}\n\nIn your response, provide a detailed analysis that considers the social, economic, and global implications of the scenario. Ensure your predictions are logical and well-supported by historical context.\n\nResponse Format:\n- Introduction: Provide a brief introduction to the scenario and the historical context.\n- Analysis: Detail the social, economic, and global implications of the scenario. Each implication should be supported by specific historical references and logical reasoning.\n- Conclusion: Summarize your predictions and their significance.\n\nProvide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should provide a detailed analysis considering social, economic, and global implications.",
            "Each implication should be supported by specific historical references and logical reasoning.",
            "The predictions should be logical and well-supported by historical context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
