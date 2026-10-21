# How to Prime the Generative AI Kit (v1.0)
**Path:** `admin/policies/generative_ai_kit_howto.md`

To use the Generative AI Kit effectively, you must "ground" the AI in the reality of this course. If you ask a generic AI "Is my project good?", it will hallucinate a positive response. You must force the AI to read the **05_term_project_taxonomy.md** and **06_term_project_sourcing_guide.md** files before evaluating your ideas.

Below are the exact procedures for priming the five major platforms. 

**Instructor Recommendation:** 
*   Use **ChatGPT / M365 Copilot** or **Claude / Qwen** for general QA, architectural reasoning, and drafting. 
*   Use **Gemini** or **Perplexity** for sourcing, filtering, and ranking references interactively. This ensures you maintain *stakeholdership* in pre-vetting candidate datasets, cloud platforms, and toolchains before you commit to them.

---

### 1. ChatGPT or M365 Copilot
*Best for: General QA, methodology brainstorming, and robust Python code reasoning.*
*   **The Setup:** Open a new chat (GPT-4o or M365 Copilot). 
*   **Grounding:** Click the attachment (paperclip) icon. Upload both `05_term_project_taxonomy.md` and `06_term_project_sourcing_guide.md` as files.
*   **Priming:** Paste the `[SYSTEM INSTRUCTION]` block from the GenAI Kit into the chat box. Add: *"Read the two attached markdown files. Do not respond until you have fully ingested the course taxonomy and feasibility rubric. Once ready, ask me for my project category and dataset."*

### 2. Claude (Anthropic) or Qwen
*Best for: Deep context synthesis, strict adherence to formatting rubrics, and academic writing critique.*
*   **The Setup:** If using Claude, create a new "Project" (if on Pro) or a standard chat. 
*   **Grounding:** In a Claude Project, upload the `05` and `06` `.md` files to the "Project Knowledge" base. If using standard chat, attach the files directly.
*   **Priming:** Paste the `[SYSTEM INSTRUCTION]` into the "Custom Instructions" box of the Project, or as your first prompt. Claude is highly obedient to constraints; explicitly tell it: *"Act as a strict Socratic gatekeeper. Reject any proposed dataset that falls into Tier 3 of the sourcing guide."*

### 3. Gemini (Google)
*Best for: Massive context windows (Gemini 1.5 Pro) and interactive reference filtering.*
*   **The Setup:** Open Gemini Advanced (or Gemini 1.5 Pro via Google AI Studio).
*   **Grounding:** Use the `+` icon to upload the `05` and `06` `.md` files, or paste the raw text of both documents directly into the prompt if file uploads are restricted.
*   **Priming:** Paste the `[SYSTEM INSTRUCTION]` block. **Crucial:** Ask Gemini to actively rank and filter candidate datasets for your specific topic. *Example: "Based on the Tier 1/Tier 2 sourcing guide I provided, search for 3 candidate datasets for [My Topic] and rank them by how easily I can execute the 'Obtain' stage."*

### 4. Perplexity
*Best for: Live literature reviews, finding SOTA baselines, and discovering datasets with active links.*
*   **The Setup:** Open a new Perplexity Pro Search thread.
*   **Grounding:** Because Perplexity excels at web search but drops long context, use a condensed grounding. Attach the `06_term_project_sourcing_guide.md` file using the `Attach` button.
*   **Priming:** Use Perplexity specifically for the **Obtain** and **Literature** stages. *Prompt Example: "I am building a predictive model for CIS 531. Read the attached sourcing guidelines. Search Hugging Face and Kaggle for datasets matching [My Topic] that strictly meet the 'Tier 1 or Tier 2' requirements outlined in my document. Provide direct links."*

### 5. Grok (xAI)
*Best for: Real-time social data analysis, identifying trending topics, and rapid code generation.*
*   **The Setup:** Open a new Grok chat.
*   **Grounding:** Paste the raw text of the `05_term_project_taxonomy.md` directly into the prompt (Grok handles raw text pasting very well).
*   **Priming:** Combine the taxonomy with the system instruction. *Prompt Example: "Acting as the CIS 531 Research Design Coordinator, evaluate my idea for a [Insert Category] pipeline. Here is the course taxonomy: [Paste Taxonomy]."*

---

# M365 Copilot Version

Generated using this prompt:
```text
Ingest the following GenAI how-to and explain step-by-step, with citations of each platform's extant documentation, how to create a course project in each of the 5 main platforms listed using generative_ai_kit.md as project instructions. Emit output with the URLs inline in GitHub-flavored Markdown (GFM) format in a fenced box.


The kit (goes in instructions): https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/policies/generative_ai_kit.md 
The grounding documents to attach as files:
- https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/05_term_project_taxonomy.md 
- https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/06_term_project_sourcing_guide.md
```

# Creating a CIS 531/731 Course Project in Five Generative-AI Platforms

**Documentation status checked:** October 7, 2026

This guide explains how to create a persistent, course-grounded project workspace in each of the five platform families identified in `generative_ai_kit_howto.md`.

The intended configuration is:

- **Project instructions:** the complete contents of [`generative_ai_kit.md`](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/policies/generative_ai_kit.md)
- **Grounding document 1:** [`05_term_project_taxonomy.md`](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/05_term_project_taxonomy.md)
- **Grounding document 2:** [`06_term_project_sourcing_guide.md`](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/06_term_project_sourcing_guide.md)

The three files serve different purposes:

1. `generative_ai_kit.md` specifies the AI's role, evaluation procedure, constraints, and response format.
2. `05_term_project_taxonomy.md` defines the allowable analytical categories, media types, and OSEMN stages.
3. `06_term_project_sourcing_guide.md` defines source tiers, Obtain and Scrub feasibility requirements, persistent stage handoffs, and the PS4 acceptance checklist.

Do not substitute a link for an uploaded file unless the platform explicitly supports retrieving and persistently grounding on that link. The safest procedure is to download the Markdown files and upload the actual `.md` files.

## 0. Prepare the three course files

Before configuring any platform:

1. Open [`generative_ai_kit.md`](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/policies/generative_ai_kit.md).
2. Select **Raw**, then save the file as `generative_ai_kit.md`.
3. Repeat this process for:
   - [`05_term_project_taxonomy.md`](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/05_term_project_taxonomy.md)
   - [`06_term_project_sourcing_guide.md`](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/06_term_project_sourcing_guide.md)
4. Open each downloaded file once and verify that it contains Markdown text rather than a saved GitHub HTML page.
5. Keep the filenames unchanged so that prompts can refer to the documents unambiguously.

Use a project name such as:

`CIS 531-731 Term Project - Team Name - Fall 2026`

## 1. ChatGPT or Microsoft 365 Copilot

### 1A. ChatGPT Projects

ChatGPT Projects are designed to keep related chats, uploaded files, and project-specific instructions together. OpenAI documents project creation, file sources, and project instructions at [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

#### Create the project

1. Sign in at https://chatgpt.com/.
2. In the left sidebar, select **New project**.
3. Name the project:

   `CIS 531-731 Term Project - Team Name - Fall 2026`

4. Optionally choose an icon and color.
5. Open the project's `...` menu and select **Project settings**.
6. Open `generative_ai_kit.md` locally.
7. Copy its complete contents, including the `[SYSTEM INSTRUCTION]` block and all constraints.
8. Paste the complete contents into **Project instructions**.
9. Save the instructions.

OpenAI states that project instructions apply inside that project and override conflicting global custom instructions: [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

#### Add the grounding documents

1. Open the project.
2. Select **Add files**, **Add source**, or the attachment control presented in the project interface.
3. Upload:
   - `05_term_project_taxonomy.md`
   - `06_term_project_sourcing_guide.md`
4. Confirm that both files appear in the project's source list.
5. If desired, also upload `generative_ai_kit.md` as a reference copy, even though its contents have already been placed in Project instructions.

ChatGPT Projects support uploaded reference material and pasted text as project sources: [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

#### Start the validation chat

Create a new chat inside the project and submit:

> Read `05_term_project_taxonomy.md` and `06_term_project_sourcing_guide.md` before evaluating any project idea. Do not assume that a project is feasible merely because a model could be trained. First report:
>
> 1. the three analytical categories;
> 2. the five media types;
> 3. the five OSEMN stages;
> 4. the distinction among Tier 1, Tier 2, and Tier 3 sources; and
> 5. the minimum Obtain and Scrub evidence required for PS4.
>
> After reporting those items, ask me for my proposed category, media type, claimed OSEMN stages, exact data source, and minimal acquisition-test result.

#### Validate the configuration

The project is correctly grounded only if ChatGPT identifies:

- exactly one category from Prescriptive, Descriptive, or Predictive;
- exactly one of the five media types;
- Obtain, Scrub, Explore, Model, and iNterpret as the five stages;
- Tier 1 as the preferred golden path;
- Tier 2 as a deliberate real-world API or benchmark path;
- Tier 3 as requiring a bounded, technically justified feasibility plan;
- a reproducible source-to-Bronze path as an early acceptance requirement; and
- versioned persistent artifacts between OSEMN stages.

If a later chat does not retain these constraints, verify that it was started **inside the project**, not as an unrelated general chat.

### 1B. Microsoft 365 Copilot Notebooks

For Microsoft 365 Copilot, the closest persistent project equivalent is a **Copilot Notebook**. Microsoft describes Copilot Notebooks as scoped workspaces that ground responses in curated references and support notebook-specific instructions: [How Microsoft Copilot Notebooks works](https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works).

#### Create the notebook

1. Open the Microsoft 365 Copilot app at https://m365.cloud.microsoft/.
2. In the left navigation, select **Notebooks**.
3. If **Notebooks** is not visible, open the app launcher and select it there.
4. Select **All notebooks**.
5. Select **New notebook**.
6. Name the notebook:

   `CIS 531-731 Term Project - Team Name - Fall 2026`

Microsoft's current setup procedure is documented at [Get started with Microsoft Copilot Notebooks](https://support.microsoft.com/en-gb/microsoft-365-copilot/get-started-with-microsoft-365-copilot-notebooks).

#### Add the grounding references

1. Open the notebook.
2. Open the **Content** pane if it is not already visible.
3. Select **Add references**.
4. Select **Upload**.
5. Upload:
   - `05_term_project_taxonomy.md`
   - `06_term_project_sourcing_guide.md`
6. Optionally upload `generative_ai_kit.md` as a third reference.
7. Verify that all expected files appear in the References list.

Microsoft documents `.md` as a supported Copilot Notebook reference type. It also explains uploading, linking, searching, and adding OneDrive or SharePoint references at [Add references to your Microsoft Copilot Notebook](https://support.microsoft.com/en-us/microsoft-365-copilot/add-references-to-your-microsoft-365-copilot-notebook) and [Get answers and insights about your Microsoft Copilot Notebook](https://support.microsoft.com/en-us/microsoft-365-copilot/get-answers-and-insights-about-your-microsoft-365-copilot-notebook).

#### Add the project instructions

1. Open the notebook's instructions or personalization control.
2. Paste the complete contents of `generative_ai_kit.md`.
3. Save the instructions.
4. Keep the two course-grounding documents as separate references rather than pasting them into the instruction field.

Copilot Notebooks can personalize responses through notebook-specific instructions and ground answers in the notebook's selected references: [How Microsoft Copilot Notebooks works](https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works).

#### Run the validation prompt

Submit the same validation prompt used for ChatGPT:

> Read `05_term_project_taxonomy.md` and `06_term_project_sourcing_guide.md` before evaluating any project idea. Report the allowable analytical categories, media types, OSEMN stages, source tiers, and minimum Obtain and Scrub evidence. Then ask for my proposed project coordinates and exact data source.

If Copilot says it cannot find one of the documents, remove and re-add that reference. A file attached only to a separate Copilot chat is not necessarily a persistent notebook reference.

#### Fallback when Copilot Notebooks is unavailable

Microsoft states that Copilot Notebooks requires an eligible Copilot or Copilot Chat license together with a SharePoint or OneDrive service plan: [Get started with Microsoft Copilot Notebooks](https://support.microsoft.com/en-gb/microsoft-365-copilot/get-started-with-microsoft-365-copilot-notebooks).

If Notebooks is unavailable:

1. Start a new Copilot chat.
2. Select `+` and then **Add images or files**.
3. Attach both grounding `.md` files.
4. Paste the complete contents of `generative_ai_kit.md` as the first message.
5. Continue the entire project-evaluation session in that chat.

Microsoft's ordinary Copilot file-upload procedure and supported formats are documented at [File upload in Microsoft Copilot](https://support.microsoft.com/en-us/microsoft-365-copilot/file-upload-in-microsoft-copilot).

This fallback is session-oriented. It is less reliable than a Notebook for a project that will span multiple chats or weeks.

## 2. Claude or Qwen

### 2A. Claude Projects

Claude Projects provide a project knowledge base and project-level instructions. Anthropic documents project creation, uploaded knowledge, and saved instructions at [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

#### Create the project

1. Sign in at https://claude.ai/.
2. Select **Projects** in the left navigation, or open https://claude.ai/projects.
3. Select **+ New Project**.
4. Set the project name to:

   `CIS 531-731 Term Project - Team Name - Fall 2026`

5. Add a short description such as:

   `Course-grounded workspace for project selection, data-source feasibility, OSEMN planning, implementation review, and PS4 proposal development.`

6. Select the appropriate visibility if using a Team or Enterprise plan.
7. Create the project.

Anthropic notes that the project name and description organize the workspace but are not themselves project knowledge available to Claude. Substance needed in later chats should therefore be added to the knowledge base or instructions: [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

#### Add project knowledge

1. Locate the **Project knowledge** area.
2. Select the `+` control.
3. Upload:
   - `05_term_project_taxonomy.md`
   - `06_term_project_sourcing_guide.md`
4. Optionally upload `generative_ai_kit.md` as a reference copy.
5. Confirm that both grounding files are listed in Project knowledge.

Files placed in Project knowledge are available across chats in the project. A file attached only to an individual chat is not automatically shared with other project chats. Anthropic documents this distinction at [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects) and [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

#### Add project instructions

1. Select **Set project instructions**.
2. Paste the complete contents of `generative_ai_kit.md`.
3. Append the following course-specific enforcement paragraph if it is not already present in the kit:

> Act as a strict Socratic project-design gatekeeper. Do not approve a proposal until its category, media type, OSEMN ownership, exact source identifier, minimal Obtain test, Bronze destination, Silver schema, Scrub operations, data-quality assertions, baseline, and persistent stage handoffs are explicit. Treat Tier 3 sources as unapproved unless the team presents a bounded technical justification, demonstrated preprocessing feasibility, and a fallback source.

4. Select **Save instructions**.

Anthropic states that project instructions apply to all chats within the project: [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

#### Run the validation prompt

Start a new chat inside the project and submit:

> Before discussing my idea, construct a course-constraint ledger from the project knowledge. Include:
>
> - allowed analytical categories;
> - allowed media types;
> - OSEMN stages;
> - Tier 1, Tier 2, and Tier 3 decision rules;
> - required Obtain evidence;
> - required Scrub evidence;
> - persistent handoff requirements; and
> - the final acceptance decision rule.
>
> Cite the filename supporting each part. Do not evaluate an idea until this ledger is complete.

Claude is ready when it distinguishes knowledge from instructions and cites both course grounding files appropriately.

### 2B. Qwen through Alibaba Cloud Model Studio

A simple Qwen chat may accept documents, but the more reproducible project-like implementation is an **Agent Application** in Alibaba Cloud Model Studio with:

- the GenAI kit as the agent's system prompt; and
- the taxonomy and sourcing guide in a connected knowledge base.

Alibaba documents no-code agent applications, system prompts, tools, and knowledge-base connections at [Agent applications](https://help.aliyun.com/en/model-studio/single-agent-application).

#### Create the Qwen agent

1. Sign in to Alibaba Cloud Model Studio.
2. Open **Application Management**.
3. Select **Create Application**.
4. Select **Agent Application**.
5. Select **Create Now**.
6. Choose an appropriate Qwen model, such as the currently available Qwen Plus or Max model.
7. Name the application:

   `CIS 531-731 Term Project - Team Name - Fall 2026`

#### Configure the instructions and knowledge

1. Paste the complete contents of `generative_ai_kit.md` into the agent's **System prompt** or equivalent instruction field.
2. Create or select a knowledge base.
3. Upload:
   - `05_term_project_taxonomy.md`
   - `06_term_project_sourcing_guide.md`
4. Connect the knowledge base to the agent.
5. If the interface offers source display, retrieval testing, or answer-source controls, enable them.
6. Save the application.
7. Test it in the left-side chat window before publishing or sharing it.

Alibaba describes Model Studio agents as applications that combine an LLM, a system prompt, external tools, and RAG knowledge bases: [Agent applications](https://help.aliyun.com/en/model-studio/single-agent-application).

#### Validate retrieval

Ask:

> Retrieve from the connected course knowledge base and identify the exact proposal evidence required for Obtain and Scrub. Name the source document used. If the knowledge base does not contain the answer, say so rather than answering from general knowledge.

Do not proceed until the agent retrieves the correct checklist from `06_term_project_sourcing_guide.md`.

## 3. Google Gemini

As of October 7, 2026, a custom **Gem** is the current generally documented method for combining reusable instructions with uploaded knowledge files in Gemini. Google has announced a later transition from Gems to Skills, but the Gemini-app Skills rollout is scheduled to begin after this guide's documentation date. Use the interface actually available in your account.

Google's current Gem procedure is documented at https://support.google.com/gemini/answer/15146780?hl=en.

### Create the Gem

1. Open https://gemini.google.com/ in a web browser.
2. Open the menu.
3. Select **Settings and help**.
4. Select **Gems**.
5. Select **New Gem**.
6. Name the Gem:

   `CIS 531-731 Term Project Gatekeeper`

Google currently requires the web app to create, edit, or delete custom Gems, although created Gems can subsequently appear in supported mobile and Workspace surfaces: https://support.google.com/gemini/answer/15146780?hl=en.

### Add the project instructions

1. Open `generative_ai_kit.md`.
2. Copy its complete contents.
3. Paste the contents into the Gem's **Instructions** field.
4. Do not ask Gemini to rewrite or shorten the instructions unless you manually verify that all mandatory rules remain present.
5. Add this sentence if the kit does not already contain an equivalent rule:

> Treat the uploaded taxonomy and sourcing guide as authoritative course policy. Distinguish statements retrieved from those files from recommendations based on general knowledge or live web search.

### Add the grounding documents

1. Under **Knowledge**, select **Add files**.
2. Choose **Upload files**.
3. Upload:
   - `05_term_project_taxonomy.md`
   - `06_term_project_sourcing_guide.md`
4. Optionally upload `generative_ai_kit.md` as a reference copy.
5. Save the Gem.

Google documents adding files under the Gem's Knowledge section and adding files either from the device or Google Drive at https://support.google.com/gemini/answer/15146780?hl=en. Google also describes reference files as a means of anchoring Gems to project-specific material at [Upload Google Docs and other file types to Gem instructions](https://workspaceupdates.googleblog.com/2024/11/upload-google-docs-and-other-file-types-to-gems.html).

### Run a two-stage validation

First, validate course grounding:

> Use only the uploaded course knowledge for this response. State:
>
> 1. the three analytical categories;
> 2. the five media types;
> 3. the five OSEMN stages;
> 4. the preferred source ordering;
> 5. the Tier 3 exception rule; and
> 6. the required persistent artifact after each OSEMN stage.
>
> Identify the grounding filename for each answer.

Second, test Gemini's sourcing role:

> My tentative topic is `[TOPIC]`. Before recommending a model, identify three candidate Tier 1 or Tier 2 data sources. For each candidate, provide:
>
> - exact dataset, table, competition, or endpoint identifier;
> - direct source URL;
> - access and authentication method;
> - expected format and scale;
> - Bronze landing plan;
> - likely Scrub operations;
> - rate-limit, schema, licensing, or reproducibility risks;
> - whether it is Tier 1 or Tier 2 under the uploaded guide; and
> - a minimal acquisition test.
>
> Rank the candidates primarily by Obtain and Scrub feasibility, not by model novelty. Clearly separate facts found on the web from conclusions based on the course documents.

### Important Gemini transition note

Google has announced that Skills will eventually replace Gems and use a Markdown-based `SKILL.md` format. The transition schedule and account-dependent rollout are documented at [About the transition from Gems to skills](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/about-the-transition-to-skills).

If **Skills** is already available in the account when this guide is used:

1. Create a custom Skill.
2. Place the complete `generative_ai_kit.md` content in the Skill instructions, or adapt it to the required `SKILL.md` structure without weakening any constraints.
3. Attach or otherwise make the two grounding documents available to the conversation.
4. Run the same grounding validation before using the Skill for project evaluation.

## 4. Perplexity

For a persistent course project, use a **Perplexity Space** rather than an isolated search thread. A Space can hold custom instructions, files, links, and multiple research threads.

Perplexity's official enterprise walkthrough demonstrates creating a Space, adding custom instructions, connecting files, and choosing between web and file sources: [How to Set Custom Files and Links in Spaces](https://www.perplexity.ai/enterprise/videos/how-to-set-custom-files-and-links).

### Create the Space

1. Sign in at [https://www.perplexity.ai/](https://www.perplexity.ai/).
2. Open **Spaces** from the left navigation.
3. Select **Create a Space**.
4. Name it:

   `CIS 531-731 Term Project - Team Name - Fall 2026`

5. Add a description such as:

   `Course-grounded research space for data-source discovery, literature review, baseline identification, and PS4 feasibility review.`

### Add custom instructions

1. Locate the Space's **Custom instructions** or **Instructions** field.
2. Paste the complete contents of `generative_ai_kit.md`.
3. If the interface imposes an instruction-length limit, do not silently summarize the kit. Instead:
   - retain its role, non-hallucination rules, source-tier policy, evidence requirements, and output contract in Custom instructions; and
   - upload the complete `generative_ai_kit.md` as a Space file.
4. Append:

> When web search is enabled, use it to discover and verify sources, not to override the uploaded course policy. Classify candidate data sources using the uploaded sourcing guide. Reject or flag any result that cannot be reconciled with the course's Tier 1, Tier 2, or Tier 3 rules.

### Add the grounding documents

1. Open the Space's **Files** area.
2. Select the add button.
3. Upload:
   - `05_term_project_taxonomy.md`
   - `06_term_project_sourcing_guide.md`
4. If the full GenAI kit did not fit in Custom instructions, also upload:
   - `generative_ai_kit.md`
5. Confirm that the files are visible in the Space.

Perplexity documents adding local files, connector files, and links to a Space in [How to Set Custom Files and Links in Spaces](https://www.perplexity.ai/enterprise/videos/how-to-set-custom-files-and-links).

### Create separate research threads

Create at least three threads inside the Space:

1. `01 - Taxonomy and Feasibility`
2. `02 - Dataset and Platform Sourcing`
3. `03 - Literature and Baselines`

This keeps distinct research products separate while preserving the Space-level instructions and files.

### Validate course-only retrieval

In the first thread, disable ordinary web search if the interface permits it and enable **My Files** or the equivalent file-only source selection. Submit:

> From the uploaded course files only, list the proposal acceptance criteria involving data-source access, authentication, minimal acquisition testing, Bronze persistence, Silver schema, Scrub operations, data-quality assertions, baselines, OSEMN ownership, and persistent handoffs. Cite the uploaded filename and section for each criterion.

The output should cite the course files, not unrelated public websites.

### Run the dataset-sourcing task

In the second thread, enable both web search and the uploaded files. Submit:

> I am proposing a `[PRESCRIPTIVE, DESCRIPTIVE, OR PREDICTIVE]` project using `[MEDIA TYPE]` data about `[TOPIC]`.
>
> Find five candidate data sources. Search official dataset publishers, Hugging Face, Kaggle, Databricks documentation, and relevant government repositories as appropriate.
>
> For each source, provide:
>
> - exact source identifier;
> - direct URL;
> - publisher;
> - access and authentication requirements;
> - license or terms information;
> - update frequency or version;
> - target fields needed for the project;
> - expected size;
> - minimal acquisition test;
> - raw landing format;
> - Bronze destination;
> - three concrete Scrub transformations;
> - two data-quality assertions;
> - source-tier classification under the uploaded course guide; and
> - evidence supporting that classification.
>
> Exclude or clearly quarantine Tier 3 sources. Rank the remaining candidates by reproducibility and Obtain/Scrub feasibility.

### Run the literature and baseline task

In the third thread, submit:

> Find current and foundational literature for this proposed project. Separate:
>
> 1. task-defining papers;
> 2. dataset papers or dataset cards;
> 3. reproducible baseline implementations;
> 4. evaluation-metric references; and
> 5. recent state-of-the-art work.
>
> Provide direct links. Do not call a paper or implementation open access unless the full artifact is legally accessible without institutional authentication. Explain which baseline is simple enough to remain viable if the advanced model fails.

Perplexity is particularly useful here because search findings can be cited interactively, while the uploaded course guide remains the authority for feasibility classification.

## 5. Grok

Grok supports uploaded files in chats, and a Projects interface is available at [https://grok.com/project](https://grok.com/project). Because project availability and controls may vary by account, use a Grok Project when available and a single dedicated chat otherwise.

xAI documents Grok's general file-upload capability at [Welcome to Grok](https://docs.x.ai/grok/overview) and attachment handling at [Files and results](https://docs.x.ai/grok-bot/files-and-results).

### 5A. Preferred procedure: Grok Project

1. Sign in at [https://grok.com/](https://grok.com/).
2. Open **Projects**, or navigate to [https://grok.com/project](https://grok.com/project).
3. Select the control to create a new Project.
4. Name it:

   `CIS 531-731 Term Project - Team Name - Fall 2026`

5. If the Project interface offers custom or project instructions:
   - open `generative_ai_kit.md`;
   - copy its complete contents;
   - paste them into the Project instructions field; and
   - save the instructions.
6. Upload:
   - `05_term_project_taxonomy.md`
   - `06_term_project_sourcing_guide.md`
7. Optionally upload `generative_ai_kit.md` as a reference copy.
8. Start the first chat inside the Project.

### 5B. Fallback procedure: dedicated Grok chat

If the Project interface is unavailable:

1. Start a new Grok chat.
2. Upload all three files:
   - `generative_ai_kit.md`
   - `05_term_project_taxonomy.md`
   - `06_term_project_sourcing_guide.md`
3. Submit:

> Treat `generative_ai_kit.md` as the controlling instruction set for this entire conversation. Treat `05_term_project_taxonomy.md` and `06_term_project_sourcing_guide.md` as authoritative course policy. Before evaluating my project, demonstrate that you can retrieve the category, media, OSEMN, source-tier, Obtain, Scrub, and persistent-handoff requirements from the attached files.

xAI's documentation directs users to attach files through the attachment control or by dragging files into the composer and recommends explicitly telling Grok what each attachment contains and how it should be used: [Files and results](https://docs.x.ai/grok-bot/files-and-results).

### Validate the Grok configuration

Submit:

> Build a compliance matrix for a proposed CIS 531/731 term project. The rows must cover:
>
> - analytical category;
> - media type;
> - exact data source;
> - source tier;
> - access method;
> - authentication;
> - minimal acquisition test;
> - raw landing format;
> - Bronze destination;
> - Silver target schema;
> - null policy;
> - duplicate policy;
> - type normalization;
> - data-quality assertions;
> - baseline;
> - claimed OSEMN stages;
> - automated stages;
> - persistent handoffs; and
> - final interpretation artifact.
>
> For now, populate the requirement column from the attached course files and leave the team-evidence column blank. Do not invent missing course requirements.

### Use Grok for bounded topical discovery

Grok can then be asked to investigate current or social-media-driven topics, but an unbounded social-media collection is classified as a Tier 3 tarpit in the course sourcing guide. Therefore, use a prompt such as:

> Identify current discussions relevant to `[TOPIC]`, but do not recommend an unbounded live social-media collection as the primary project dataset. Prefer a static public corpus, bounded documented archive, official API with reproducible parameters, or another Tier 1 or Tier 2 source. Separate topic discovery from dataset approval.

If Grok proposes scraping, proprietary data, or unbounded social-media ingestion, require it to apply the Tier 3 controls before considering the idea feasible.

## 6. Common project-initiation prompt

After configuring any of the five platforms, begin substantive project work with this prompt:

> We are preparing a CIS 531/731 term project.
>
> Do not recommend a model yet. Conduct project intake in the following order:
>
> 1. Ask us to select exactly one analytical category: Prescriptive, Descriptive, or Predictive.
> 2. Ask us to select exactly one media type: Time-Series, Spatial, Text, Multimedia, or Structured/Relational.
> 3. Ask which one or two OSEMN stages each team member intends to claim.
> 4. Ask for the exact data-source identifier and URL.
> 5. Ask for the access and authentication method.
> 6. Ask for the result of a bounded minimal acquisition test.
> 7. Ask for the raw landing format and Bronze destination.
> 8. Ask for the intended Silver schema.
> 9. Ask for at least three concrete Scrub transformations.
> 10. Ask for the null, duplicate, and type-normalization policies.
> 11. Ask for at least two automated data-quality assertions.
> 12. Ask for a simple baseline that remains executable if the advanced method fails.
> 13. Ask what persistent artifact each OSEMN stage will hand to the next stage.
>
> After collecting these answers, classify the source as Tier 1, Tier 2, or Tier 3 under the course sourcing guide. Do not approve a Tier 3 source without a bounded feasibility demonstration, an instructor-approval plan, and a fallback source.
>
> Produce a findings-first review with:
>
> - blocking deficiencies;
> - non-blocking risks;
> - missing evidence;
> - the proposed 3x5x5 taxonomy coordinate;
> - source-tier classification and rationale;
> - Obtain readiness;
> - Scrub readiness;
> - baseline readiness;
> - recommended next acquisition test; and
> - a provisional decision of `READY`, `READY WITH CONDITIONS`, or `NOT YET READY`.

## 7. Cross-platform grounding test

Run this test before relying on any platform's evaluation:

> A team proposes to scrape an undocumented commercial website, has not tested the scraper, plans to keep the resulting CSV on one student's laptop, and wants to fine-tune a transformer before deciding on a Bronze or Silver schema. Evaluate the proposal strictly under the uploaded course documents.

A properly grounded platform should identify at least the following problems:

- the data source is likely Tier 3 because it depends on fragile scraping;
- there is no demonstrated minimal acquisition test;
- there is no documented access, terms, rate-limit, or fallback plan;
- a local laptop CSV is not an acceptable persistent stage handoff;
- the Bronze destination is missing;
- the Silver schema and concrete Scrub plan are missing;
- model selection has improperly preceded data acquisition and validation;
- reproducibility is insufficient; and
- the proposal is `NOT YET READY`.

If the platform instead praises the model idea or immediately recommends architectures, the project is not adequately grounded. Recheck the instruction field, file placement, and whether the current chat is actually inside the configured Project, Notebook, Gem, Space, or agent.

## 8. Recommended division of labor among platforms

- **ChatGPT Project or Microsoft Copilot Notebook:** general project QA, methodology, architecture, code reasoning, and ongoing team documentation.
- **Claude Project or Qwen agent:** strict rubric application, deep synthesis across the course documents, structured critique, and academic writing review.
- **Gemini Gem:** interactive candidate-dataset discovery, comparison, and filtering, with explicit separation between web evidence and course-policy classification.
- **Perplexity Space:** cited literature review, baseline discovery, dataset links, license checking, and current source verification.
- **Grok Project:** rapid topical discovery and exploratory code generation, while enforcing the course restriction against unbounded social-media collection.

No platform should be treated as the final authority on course acceptance. The uploaded course documents supply the governing criteria, and instructor review remains necessary for Tier 3 exceptions, unclear sourcing permissions, or unusually complex acquisition and preprocessing plans.

## 9. Documentation references

### Course files

- [Generative AI Kit](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/policies/generative_ai_kit.md)
- [CIS 531/731 Term Project Taxonomy](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/05_term_project_taxonomy.md)
- [CIS 531/731 Data Sourcing and OSEMN Execution Guide](https://github.com/kddresearch/cis531-731-2026_fall/blob/main/admin/syllabus/06_term_project_sourcing_guide.md)

### ChatGPT

- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)
- [Using projects in ChatGPT](https://openai.com/academy/projects/)

### Microsoft 365 Copilot

- [Get started with Microsoft Copilot Notebooks](https://support.microsoft.com/en-gb/microsoft-365-copilot/get-started-with-microsoft-365-copilot-notebooks)
- [How Microsoft Copilot Notebooks works](https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works)
- [Add references to your Microsoft Copilot Notebook](https://support.microsoft.com/en-us/microsoft-365-copilot/add-references-to-your-microsoft-365-copilot-notebook)
- [Get answers and insights about your Microsoft Copilot Notebook](https://support.microsoft.com/en-us/microsoft-365-copilot/get-answers-and-insights-about-your-microsoft-365-copilot-notebook)
- [File upload in Microsoft Copilot](https://support.microsoft.com/en-us/microsoft-365-copilot/file-upload-in-microsoft-copilot)

### Claude

- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
- [Introduction to projects](https://academy.claude.com/courses/claude-101/introduction-to-projects)

### Qwen and Alibaba Cloud Model Studio

- [Agent applications](https://help.aliyun.com/en/model-studio/single-agent-application)
- [What is Alibaba Cloud Model Studio?](https://help.aliyun.com/en/model-studio/what-is-model-studio)

### Gemini

- https://support.google.com/gemini/answer/15146780?hl=en
- [Get started with Gems in Gemini Apps](https://support.google.com/gemini/answer/15236321?hl=en)
- [Upload Google Docs and other file types to Gem instructions](https://workspaceupdates.googleblog.com/2024/11/upload-google-docs-and-other-file-types-to-gems.html)
- [About the transition from Gems to skills](https://knowledge.workspace.google.com/admin/generative-ai/gemini-app/about-the-transition-to-skills)

### Perplexity

- [How to Set Custom Files and Links in Spaces](https://www.perplexity.ai/enterprise/videos/how-to-set-custom-files-and-links)
- [Perplexity](https://www.perplexity.ai/)

### Grok

- [Grok Projects](https://grok.com/project)
- [Welcome to Grok](https://docs.x.ai/grok/overview)
- [Files and results](https://docs.x.ai/grok-bot/files-and-results)
