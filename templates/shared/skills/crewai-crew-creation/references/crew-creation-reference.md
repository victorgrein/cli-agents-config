# CrewAI Crew Creation - Full Reference

> Source: Official CrewAI Documentation

## Prerequisites

- CrewAI installed (`pip install crewai 'crewai[tools]'`)
- API keys configured (OPENAI_API_KEY, etc.)
- Clear understanding of the task to accomplish

## Validation Checklist

- [ ] All agents have clear roles, goals, backstories
- [ ] All tasks have clear descriptions and expected outputs
- [ ] Task dependencies are correctly defined
- [ ] Tools are assigned to appropriate agents
- [ ] Process type matches workflow complexity
- [ ] Verbose mode enabled for debugging
- [ ] Output files specified where needed
- [ ] Environment variables configured

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| Agent not using tools | Check tool assignment, improve tool descriptions |
| Task output unclear | Make expected_output more specific |
| Context not passing | Verify context list in task definition |
| Rate limits | Add max_rpm to agents or crew |
| Long execution | Enable caching, reduce max_iter |

## Common Agent Patterns

- Research → Analysis → Writing
- Data Collection → Processing → Reporting
- Planning → Execution → Review
