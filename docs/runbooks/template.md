# Alert name, exactly as it appears in the alerting tool

Copy this file to `docs/runbooks/<alert-name>.md`, replace the text under each heading, delete this paragraph, and add the new file to the index in `docs/README.md`. Write for the person who is on call and has never seen this alert: numbered steps, exact commands, and the result to expect.

## Symptom

What the on-call person sees: the text of the alert, the condition that fires it (metric, threshold, duration), and where to look at it (dashboard, log query).

## Impact

Who is affected and how badly while the alert is firing: which callers, which functions, whether data is lost or only delayed. State how urgent the alert is.

## Diagnosis

Numbered steps that lead from the symptom to the cause. For each step give the command or the link, what a healthy result looks like, and what each unhealthy result means. List the known causes, most likely first.

## Fix

For each cause from the diagnosis, the numbered steps that restore the service, and how to confirm that the alert has cleared. If the fix is a rollback, link to [rollback.md](rollback.md).

## Escalation

Who to contact when the steps above do not restore the service, how to reach them, and after how long. Name the next level after that.
