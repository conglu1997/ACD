class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"requirements": "Develop an urban planning proposal for a new residential neighborhood in a coastal city. The neighborhood should include residential areas, commercial zones, green spaces, and transportation infrastructure. Consider the following constraints: the area is prone to flooding, the population density should be moderate (around 5,000 people per square kilometer), the plan should promote sustainable living, and it should include at least one community center and two schools."},
            "2": {"requirements": "Create an urban planning proposal for revitalizing an old industrial district in a large metropolitan area. The proposal should include mixed-use developments, public amenities, transportation networks, and cultural spaces. Consider the following constraints: the area has a history of pollution, there is a need for affordable housing (at least 30% of the housing units should be affordable), the plan should enhance the local economy, and it should include at least one park and a community health center."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a detailed urban planning proposal based on the following requirements:

{t["requirements"]}

Your proposal should include the following sections:
1. Introduction: Provide an overview of the planning area, its characteristics, and key objectives.
2. Land Use Plan: Describe the allocation of residential, commercial, green, and public spaces.
3. Transportation Plan: Outline the transportation infrastructure, including roads, public transit, and pedestrian pathways.
4. Environmental Considerations: Address sustainability measures, flood mitigation, and pollution control.
5. Economic and Social Impact: Discuss the potential economic benefits and social impact of the proposal.

Ensure that your proposal is clear, comprehensive, and well-structured. Submit your response as a plain text string in the specified format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The proposal should include all required sections.", "The content should be clear, comprehensive, and well-structured.", "The land use and transportation plans should logically correspond to the given requirements and constraints.", "The environmental considerations should address sustainability, flood mitigation, and pollution control.", "The economic and social impact should be thoroughly discussed.", "The introduction should provide a clear overview and key objectives of the planning area."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
