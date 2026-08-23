---
source_url: https://hamel.dev/blog/posts/evals/
author: Hamel Husain
published: 2024-03-29
captured: 2026-06-06
capture_method: WebFetch (clipped markdown copy)
---

# Your AI Product Needs Evals

**Author:** Hamel Husain  
**Published:** March 29, 2024

## Motivation

Hamel Husain draws from five years of experience building language model products, starting with CodeSearchNet at GitHub. He observes that unsuccessful AI products share a common failure: the lack of robust evaluation systems. As an independent consultant helping companies build domain-specific AI products, Husain advocates for systematic evaluation as the foundation of successful LLM applications.

## Iterating Quickly == Success

Success in AI products mirrors software engineering success: speed of iteration matters tremendously. Three critical activities enable rapid iteration:

1. Evaluating quality through tests
2. Debugging issues via logging and data inspection
3. Modifying system behavior through prompt engineering, fine-tuning, or code changes

"Many people focus exclusively on #3 above, which prevents them from improving their LLM products beyond a demo." This oversight prevents the virtuous cycle that distinguishes great AI products from mediocre ones.

## Case Study: Lucy, A Real Estate AI Assistant

Rechat's AI assistant Lucy serves real estate professionals through a conversational interface. Initial rapid progress via prompt engineering plateaued as Lucy's functionality expanded, manifesting as:

- Whack-a-mole failure modes (fixing one reveals another)
- Limited visibility into effectiveness across tasks
- Increasingly unwieldy, example-heavy prompts

The solution centered on systematic evaluation across three levels.

## The Types Of Evaluation

### Level 1: Unit Tests

Unit tests for LLMs are assertions that run fast and cheaply, executable on every code change. Unlike traditional unit tests, they organize for use beyond testing—including data cleaning and automatic inference retries using assertion errors.

**Step 1: Write Scoped Tests**

Break down LLM functionality into features and scenarios. For Lucy's listing finder feature:

| Scenario | Assertions |
|----------|-----------|
| Only one listing matches | `len(listing_array) == 1` |
| Multiple listings match | `len(listing_array) > 1` |
| No listings match | `len(listing_array) == 0` |

Generic tests also apply broadly. For example, a regex assertion ensures UUIDs don't appear in LLM responses when the prompt instructs against including them.

**Step 2: Create Test Cases**

Generate test inputs using LLMs. One prompt asks for 50 different instructions real estate agents might give to create and retrieve contacts, producing synthetic test cases like:

```json
[
  [
    "Create a contact for John Smith (johndoe@apple.com) with phone 123-456-7890",
    "What's the email address of John Smith?"
  ],
  [
    "Add Emily Johnson with phone 987-654-3210, email emilyj@email.com",
    "What's the phone number for Emily Johnson?"
  ]
]
```

Continuously update tests based on observed failures. "You don't need to wait for production data to test your system." Pass rates depend on acceptable failure tolerance—not all tests require 100% passing.

**Step 3: Run & Track Your Tests Regularly**

Use existing CI infrastructure (GitHub Actions, GitLab Pipelines) with minimal friction. Track results over time in analytics systems like Metabase to visualize progress. Rechat's dashboard shows error prevalence before and after fixes.

### Level 2: Human & Model Eval

**Logging Traces**

Traces logically group events—conversations with LLMs including user messages and AI responses. Tools like LangSmith provide human-readable trace visualization with interactive playgrounds for prompt iteration.

**Looking At Your Traces**

"You must remove all friction from the process of looking at data." Render traces in domain-specific ways, building custom tools when necessary. Rechat's evaluation tool displays:

- Tool/feature and scenario being evaluated
- Synthetic vs. real user input source
- Filters for navigation
- Links to CRM and trace logging systems

Lightweight frameworks like Gradio, Streamlit, or Shiny build these tools in under a day. Start with binary good/bad labels rather than granular ratings.

**How much data should you look at?**

Initially examine all test-case traces and user-generated traces. "You can never stop looking at data—no free lunch exists." Sample more over time, stopping when you stop learning.

**Automated Evaluation w/ LLMs**

Don't eliminate human evaluation entirely. Track correlation between model-based and human evaluation. Use human critiques to iterate on evaluator model prompts for alignment.

Spreadsheet-based iteration works effectively: collect model responses, model critiques, and binary outcomes alongside human evaluator judgments. Iterate on critique prompts to improve alignment.

Tips for model-based evaluation:
- Use the most powerful affordable model for critiquing
- Maintain a mini-evaluation system for the evaluator itself
- Monitor model-human agreement periodically

**Important Note on Using Agreement as a Metric:** Raw agreement fails with imbalanced datasets. Use precision and recall separately instead.

### Level 3: A/B Testing

A/B testing for LLM products resembles testing other product types. Defer this until sufficient confidence exists about product-market fit. More mature products benefit most from this validation level.

### Evaluating RAG

RAG evaluation exceeds this post's scope but Jason Liu's article explores this subject in detail.

## Eval Systems Unlock Superpowers For Free

### Fine-Tuning

"Fine-tuning is best for learning syntax, style, and rules, whereas techniques like RAG supply the model with context or up-to-date facts."

Ninety-nine percent of fine-tuning labor involves assembling high-quality data. A solid evaluation system provides this data generation and curation engine nearly automatically.

**Data Synthesis & Curation**

Generate synthetic fine-tuning data using LLMs with prompts similar to test case generation. Filter results through Level 1 and Level 2 tests. Use existing human evaluation tools to curate high-quality traces for fine-tuning datasets.

### Debugging

Robust evaluation systems provide debugging infrastructure:

- Searchable, filterable trace databases
- Assertion-based error flagging mechanisms
- Log navigation tools identifying root causes
- Rapid testing of fixes

Evaluation and debugging infrastructure substantially overlap.

## Conclusion

Evaluation systems create virtuous cycles enabling rapid iteration. Key takeaways:

- Remove all friction from data inspection
- Keep approaches simple; avoid expensive tools initially
- Examine substantial data volumes
- Build problem-specific evaluation systems, not generic frameworks
- Write numerous tests and update them frequently
- Use LLMs to generate test cases, assertions, synthetic data, and critiques
- Reuse evaluation infrastructure for debugging and fine-tuning

Husain welcomes feedback at `hamel@parlance-labs.com`.

---

*This article adapted from a Vanishing Gradients podcast conversation with Emil Sedgh and Hugo Browne-Anderson. Reviewers included Jeremy Howard, Eugene Yan, Shreya Shankar, Jeremy Lewi, and Joseph Gleasure.*
