# Validation record

Version: 0.1.0. Date: 2026-09-24.

Scope: original general workflow instructions, not jurisdiction-specific legal advice. No real project/customer data or private case material is included. External background references were checked during authoring: NIST AI 600-1 and Building Commission NSW security-of-payment guidance. No numerical legal deadline is hardcoded.

Structural validation: run scripts/validate.py. It checks the six required files, core sections, agent controls, document depth, balanced code fences and README local links. It is not a test of agent behaviour.

Editorial checks: the variation example computes 25 × $80 = $2,000; the payment example distinguishes $30,000 current movement, $10,000 earlier unpaid and $40,000 total outstanding; the dispute example computes 8 × $150 + $2,000 = $3,200. The delay example explicitly declines to infer completion impact from event duration. Meeting conditions and authority are preserved. Contract review requires the actual incorporated document set.

36 acceptance scenarios are specified (six per playbook). Agent execution status: NOT RUN. Model compatibility: NOT CLAIMED. Independent professional review: NOT PERFORMED. Before live use, the adopting organisation must validate the playbook in its actual agent environment, contract and approval system.

Release classification: PUBLIC PREVIEW — usable as a starting procedure with human review; not certified production automation.
