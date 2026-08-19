# Learning & Blocker Journal: AWS Lambda + SQS (Python)

## Day 1: The First Hurdle
**Blocker:** The Lambda function failed with `AccessDenied` when trying to read from SQS.
**Analysis:** I assumed the default `AWSLambdaBasicExecutionRole` would work. It doesn't include SQS permissions.
**Resolution:** I read the AWS IAM documentation and attached the `AWSLambdaSQSQueueExecutionRole` policy manually.
**Lesson:** Execution roles are specific; "basic" is never enough for cross-service integration.

## Day 1: The Event Structure
**Blocker:** My code crashed with `KeyError: 'body'`.
**Analysis:** I assumed the event would be a simple JSON string. It's actually a nested dictionary with `Records` -> `body`.
**Resolution:** I used `print(json.dumps(event))` in the console to inspect the raw payload sent by the test script.
**Lesson:** Always inspect the raw event structure before coding logic.

## Day 2: Idempotency Logic
**Blocker:** Duplicate messages caused the inventory count to drop twice for the same update.
**Analysis:** SQS is "at-least-once" delivery. Retries are possible.
**Resolution:** I implemented a check (simulated in logs) to ignore messages with the same `messageId` if processed recently.
**Lesson:** Distributed systems require idempotency by design, not by accident.
