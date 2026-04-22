## 6. Scene: AI Jira Automation
**User Prompt:**
"Act as a Senior AI Integration Architect. Create a highly technical guide on how to integrate Large Language Models (LLMs) with Atlassian Jira to automate Agile workflows.
Structure the Markdown document with these exact sections:
1. THE AI-AGILE VISION: Briefly explain how AI transforms traditional backlog management from manual data entry to automated generation.
2. AUTO-GENERATING USER STORIES: Explain the workflow of feeding raw client requirements into an LLM, and having it output perfectly formatted Jira User Stories (including Title, Description, Acceptance Criteria, and Story Points).
3. EPIC DECOMPOSITION: Describe how an AI Agent can take a massive Epic (e.g., "Build a Payment Gateway") and automatically break it down into logical Developer Tasks and Sub-tasks using Jira's REST API.
4. RISK PREDICTION & QA: Explain how AI can analyze past resolved Jira tickets to predict bug-prone code areas and automatically generate QA Testing tasks for the new Sprint.
Output ONLY the raw Markdown document. Ensure the tone is cutting-edge and professional."

**Model Response:**
> [# The AI- Agile Vision

## Introduction
In traditional agile workflows, backlog management involves manual data entry of user stories into Jira. This process can be time-consuming and prone to errors.

With Large Language Models (LLMs), we automate this workflow by feeding raw client requirements directly into the LLM for outputting perfectly formatted Jira User Stories in a single step.
## Auto-Generating User Stories
### Workflow

1. **Input**: Raw Client Requirements - These can be text documents, emails or even voice recordings of user stories.

2. **Processing**:
    * The raw input is fed into the LLM for processing and understanding context.
3. **Output**: Jira User Story Template - This includes Title (e.g., "Payment Gateway Integration"), Description ("As a customer, I want to be able to make payments through our website."), Acceptance Criteria (e.g., "The payment gateway should support all major credit cards."), and Story Points.

### Example
```json
{
  "title": "Build Payment Gateway",
  "description": "Develop an integration with popular online payment platforms.",
  "acceptance_criteria": [
    {
      "criterion": "Support for Visa, Mastercard, American Express, PayPal."
    },
    ...
  ],
  "story_points": [5]
}
```
## Epic Decomposition
### Workflow

1. **Input**: Large Epic - For example: "Build a Payment Gateway"
2. **Processing**:
   * The LLM analyzes the epic and breaks it down into logical Developer Tasks.
3. **Output**: Jira Issues (Developer Tasks) with Sub-tasks.

### Example
```json
{
  "type": "task",
  "summary": "Implement Visa Integration",
  "description": "",
  "assignee": null,
  "issuetype": {
    "id": "10256"
  },
  "priority": {"name":"High"},
  "labels":[],
}
```
## Risk Prediction & QA
### Workflow

1. **Input**: Past Jira Tickets - These include resolved bugs, issues and feature requests.
2. **Processing**:
   * The LLM analyzes the past tickets to identify patterns in bug-prone code areas.

3. **Output**: New QA Testing Tasks for upcoming Sprints (e.g., "Test payment gateway integration with Visa").

### Example
```json
{
  "type": "task",
  "summary": "QA Test Payment Gateway Integration - Visa",
  "description": "",
  "assignee": null,
  "issuetype": {
    "id": "10256"
  },
}
```
## Conclusion

By integrating LLMs with Atlassian Jira, we can automate the backlog management process and enhance agility. This not only saves time but also reduces errors in data entry while providing valuable insights for risk prediction and QA tasks.
# References
* [Atlassian REST API](https://developer.atlassian.com/rest/)
* [Large Language Models (LLMs)](https://www.openai.com/blog/gpt-3/)]

---