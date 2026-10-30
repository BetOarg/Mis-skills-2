---
name: ads-campaign-builder
description: Build complete, ready-to-implement Google Ads and Meta Ads campaign plans, including structure, audience, creative, landing page, tracking, budgets, optimization, and reporting. Use for campaign planning or improving advertising performance; never publish campaigns or spend money without explicit approval.
---

# Ads Campaign Builder

## Goal
Deliver an implementable campaign, not just a list of marketing ideas. Separate confirmed business facts, assumptions, and data still needed. Tailor structure and language to the market, product, funnel, and budget.

## Rules
- Establish objective, offer, target market/geography, audience, conversion action, budget, timing, landing page, and available creative assets.
- If a critical detail is missing, ask one direct question. If work can proceed with stated assumptions, proceed and label them.
- Do not invent prices, discounts, availability, legal claims, customer testimonials, guarantees, conversion results, or platform capabilities.
- Verify current ad-platform policies and technical requirements when web research is available; cite current sources for changing rules.
- Keep Google Search, Performance Max, Meta prospecting, and retargeting roles distinct; recommend only campaign types justified by the goal, budget, tracking, and asset availability.
- Include negative keywords and exclusions where relevant, audience exclusions, geographic settings, language, schedule, and lead qualification.
- Specify a budget by platform/campaign and a test period. Do not promise results or use unsupported ROAS/CPL projections.
- Plan measurement before launch: events, UTMs, conversion definitions, consent/privacy, CRM or lead handling, deduplication, and test procedure.
- Ads, landing pages, and lead forms must accurately represent the offer and must not collect unnecessary personal data.
- Never publish, activate, change live budgets, or incur spend without explicit user approval.
- Do not claim a campaign is live or tracking works unless verified in the actual platform/account.

## Workflow
1. **Brief:** summarize objective, offer, geography, audience, funnel, budget, timing, and constraints.
2. **Fact table:** classify facts as CONFIRMED, ASSUMPTION, or PENDING. Highlight blockers that materially change campaign design.
3. **Strategy:** define conversion goal, proposition, funnel, channel roles, audience segments, exclusions, and expected learning.
4. **Campaign architecture:** provide campaign/ad set/ad group naming, objective, locations, languages, placements, bidding approach, budget, schedule, and targeting.
5. **Search build:** deliver keyword clusters by intent, match-type strategy, negative keywords, ad group themes, responsive search ad headlines/descriptions within current character limits, and extensions/assets.
6. **Meta build:** deliver campaign objective, ad set structure, audience/prospecting/retargeting plan, placements, creative concepts, primary text, headlines, descriptions, and CTA. Label unavailable audiences and prerequisites.
7. **Creative and landing page:** provide hooks, variants, proof points, visual direction, landing-page sections, form fields, FAQs, and trust/legal details. Never fabricate proof.
8. **Tracking QA:** define conversion events, UTMs, attribution assumptions, consent/privacy checks, test leads, deduplication, and how to confirm events.
9. **Budget and schedule:** give a phased plan (test, evaluate, scale/stop) and specify guardrails. If budget is unknown, offer a bounded proposed test and label it as a proposal.
10. **Optimization rules:** define review cadence and explicit pause/continue/scale thresholds using available data. Avoid false precision; thresholds must fit the budget and conversion volume.
11. **Launch checklist:** provide an implementation checklist and clearly separate items requiring account access or approval.
12. **Final deliverable:** ensure all ad copy, keywords, settings, tracking and optimization actions are present, or label each missing item and why it is pending.

## Required output
- Objective and conversion definition.
- Confirmed facts / assumptions / pending data.
- Campaign map and naming convention.
- Exact targeting and exclusions.
- Ready-to-use copy and creative briefs.
- Budget split and test duration.
- Tracking and landing-page QA.
- Optimization decision rules.
- Launch checklist and approval boundary.

## Examples

### Good example 1
User: “Build Google and Meta campaigns to sell residential lots to buyers in Uruguay.”
Action: clarify or label price/payment/delivery facts, define Uruguay-focused segments, build high-intent Search keywords and negatives, draft responsive search ads, create Meta creative/copy variants, specify budgets and test cadence, design lead form/landing page, and list tracking QA. Do not publish or invent prices.

### Good example 2
User: “Improve our lead campaign; CPL rose.”
Action: inspect the supplied performance window, spend, conversions, lead quality, audience and creative changes; identify evidence-supported hypotheses and a controlled test plan. If account data is unavailable, state that the diagnosis is provisional.

### Bad example
User: “Create an ad campaign.”
Bad action: claim an expected CPL, fabricate a discount, select a large budget without context, and activate the campaign immediately.
Why bad: unsupported claims and unapproved spend create commercial and compliance risk.

## Experiment design and measurement discipline
Before recommending optimization tests, define each experiment explicitly:
- **Hypothesis:** the specific audience, query intent, message, offer, placement, or landing-page change expected to affect a named metric, with a reason grounded in available evidence.
- **Variable and comparison:** change one primary variable where practical; state the control/baseline and avoid mixing unrelated changes in the same test.
- **Primary metric and guardrails:** define the conversion metric (for example qualified lead rate or cost per qualified lead) and guardrails such as lead quality, invalid-contact rate, frequency, spend, or policy risk.
- **Window and decision rule:** set a review window and minimum evidence requirement appropriate to spend and conversion volume. If volume is too low, report the result as inconclusive; do not declare a winner from noise or arbitrary small samples.
- **Stop/scale conditions:** define pause, continue, and scale criteria before launch. Never lower the success threshold after seeing results merely to call a test successful.
- **Attribution and data quality:** check event deduplication, consent, UTMs, CRM status mapping, offline conversion imports, and lead-source reconciliation before comparing campaigns.
- **Economics:** where inputs are supplied, calculate break-even cost per lead or acquisition from contribution margin and lead-to-sale rate; show the formula and assumptions. Do not invent margin, close rate, or lifetime value.
- Report actual platform results separately from modeled scenarios. A campaign plan, preview, or simulated benchmark is not evidence of live performance.
