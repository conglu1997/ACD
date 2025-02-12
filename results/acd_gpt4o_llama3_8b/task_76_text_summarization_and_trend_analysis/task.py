class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "In recent years, the technology sector has seen a significant shift towards cloud computing. Companies are increasingly moving their operations to cloud-based platforms to enhance scalability and reduce costs. Major players like Amazon, Google, and Microsoft have been at the forefront of this transformation, each offering a suite of cloud services. This trend is accompanied by a growing demand for cybersecurity measures to protect sensitive data stored in the cloud. Simultaneously, there has been an uptick in the development of artificial intelligence and machine learning technologies, which are being integrated into various cloud services to provide more advanced and automated solutions. The convergence of cloud computing and AI is paving the way for innovative applications in industries ranging from healthcare to finance.",
                "instructions": "Summarize the provided text and identify the key trends or patterns mentioned. Ensure that your summary is concise (50-100 words) and captures the main points accurately. Submit your summary and identified trends as a plain text string in the following format: \nSummary: [Your summary] \nTrends: [Identified trends]"
            },
            "2": {
                "data": "The renewable energy sector is experiencing rapid growth driven by global efforts to combat climate change. Solar and wind energy have emerged as the most popular renewable sources due to their decreasing costs and increasing efficiency. Governments worldwide are implementing policies and providing incentives to encourage the adoption of renewable energy. Additionally, technological advancements are leading to the development of more efficient energy storage solutions, which are critical for managing the intermittent nature of renewable energy sources. The push towards sustainability is also driving innovation in electric vehicles and smart grid technologies, which aim to create more efficient and environmentally friendly energy systems.",
                "instructions": "Summarize the provided text and identify the key trends or patterns mentioned. Ensure that your summary is concise (50-100 words) and captures the main points accurately. Submit your summary and identified trends as a plain text string in the following format: \nSummary: [Your summary] \nTrends: [Identified trends]"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Summarize the provided text and identify the key trends or patterns mentioned. Ensure that your summary is concise (50-100 words) and captures the main points accurately. Here is the text:\n\n{t['data']}\n\nSubmit your summary and identified trends as a plain text string in the following format:\nSummary: [Your summary] \nTrends: [Identified trends]\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The summary should be concise (50-100 words) and accurately capture the main points.",
            "The identified trends should be relevant to the provided text."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
