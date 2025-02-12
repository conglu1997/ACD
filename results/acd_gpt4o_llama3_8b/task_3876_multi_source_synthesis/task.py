class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "Climate Change",
                "articles": [
                    "Climate change refers to significant changes in global temperatures and weather patterns over time. While climate change is a natural phenomenon, scientific evidence shows that human activities are currently driving an unprecedented rate of change. Burning fossil fuels, deforestation, and industrial processes are major contributors to the greenhouse gases that cause global warming.",
                    "The impacts of climate change are diverse and widespread. Rising sea levels, more frequent and severe weather events, and shifts in ecosystems and wildlife are just a few examples. Mitigation and adaptation strategies are essential to address these challenges. Renewable energy sources, reforestation, and sustainable agriculture are key approaches to reducing greenhouse gas emissions and building resilience.",
                    "Climate change policy involves both mitigation and adaptation strategies. Mitigation efforts focus on reducing greenhouse gas emissions, while adaptation strategies aim to minimize the impacts of climate change on society and the environment. International agreements, such as the Paris Agreement, play a crucial role in coordinating global efforts to address climate change.",
                    "Recent studies have shown that the Arctic is warming at a rate twice as fast as the rest of the world, leading to significant ice melt and permafrost thawing. This rapid change has profound implications for global sea levels and weather patterns, making it a critical area of focus for climate scientists and policymakers."
                ]
            },
            "2": {
                "topic": "Artificial Intelligence",
                "articles": [
                    "Artificial Intelligence (AI) is the simulation of human intelligence processes by machines, particularly computer systems. These processes include learning, reasoning, and self-correction. AI applications include expert systems, natural language processing, speech recognition, and machine vision.",
                    "The development of AI has raised significant ethical and societal concerns. Issues such as job displacement, privacy, and the potential for biased decision-making are critical areas of focus. Ensuring that AI systems are designed and used responsibly is essential for maximizing their benefits while minimizing risks.",
                    "AI has the potential to transform various industries, including healthcare, finance, and transportation. In healthcare, AI can assist in diagnosing diseases, personalizing treatments, and predicting patient outcomes. In finance, AI algorithms can analyze vast amounts of data to detect fraud and optimize investment strategies. In transportation, AI can enhance the efficiency and safety of autonomous vehicles.",
                    "One of the major challenges in AI development is ensuring transparency and accountability in decision-making processes. Researchers are working on creating explainable AI systems that can provide clear and understandable reasons for their decisions, which is crucial for gaining public trust and ensuring ethical compliance."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the following articles on the topic '{t['topic']}' and write a comprehensive summary that captures the key points from each source. Ensure that your summary is well-structured, coherent, and accurately reflects the information from the articles. Submit your summary as a plain text string in the following format:

Summary:
[Your summary here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should capture all key points from each article.",
            "The summary should be well-structured and coherent.",
            "The summary should accurately reflect the information from the articles."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
