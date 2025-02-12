class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"texts": [
                "The industrial revolution, which took place from the 18th to 19th centuries, was a period during which predominantly agrarian, rural societies in Europe and America became industrial and urban. Prior to the Industrial Revolution, which began in Britain in the late 1700s, manufacturing was often done in people’s homes, using hand tools or basic machines. Industrialization marked a shift to powered, special-purpose machinery, factories and mass production.",
                "The iron and textile industries, along with the development of the steam engine, played central roles in the Industrial Revolution, which also saw improved systems of transportation, communication and banking. While industrialization brought about an increased volume and variety of manufactured goods and an improved standard of living for some, it also resulted in often grim employment and living conditions for the poor and working classes."
            ]},
            "2": {"texts": [
                "Climate change refers to long-term changes in temperature, precipitation, and other atmospheric conditions on Earth. These changes can be caused by natural processes such as volcanic eruptions, variations in solar radiation, and changes in Earth's orbit, as well as by human activities, particularly the burning of fossil fuels, deforestation, and industrial processes.",
                "The consequences of climate change include rising sea levels, more frequent and severe weather events, shifts in ecosystems and wildlife populations, and impacts on human health and agriculture. Addressing climate change requires global cooperation to reduce greenhouse gas emissions, adapt to changing conditions, and transition to sustainable energy sources."
            ]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return """Your task is to read the following texts and synthesize the information into a cohesive and insightful summary. Ensure that your summary is clear, concise, and captures the key points from both texts. Here are the texts:\n\n{texts}\n\nSubmit your summary in plain text format.""".format(texts='\n\n'.join(t['texts']))

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should be clear and concise.",
            "The summary should capture the key points from both texts.",
            "The summary should be cohesive and coherent.",
            "The summary should be insightful and relevant."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
