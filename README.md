# Backend Hands on Exercise

## Instructions
We would like you to create a work logging server. The work logging server enables our team members to log what tasks they are working on and understand the efforts we invest in every task.
Users of the server can:

1. start log work – mark that work on a specific assignment has begun.
2. end log work – mark that current assignement is no longer being worked at
3. Report - generate report of all users and time invested in each task

### Sample requests:
- Start work: User: Bob, task: Sample assignment 1 Start work: User: John task: Sample assignment 2 End work: User: Bob
- End work: User: John
- Get report:
User bob:
Sample assignment 1: 2 hours User John:
Sample assignment 2: 3 hours
  
### Additional assumptions:
  - Users cannot start log when a previous task is already started by them.
  - Please write a RESTful API server which enables the tasks above.
  - Solution should include tests to validate your code. You can use your preferred programming language.
  - Please have the solution available as a zip or a github repo. Please also include instructions on how to run and test your code and of any assumptions you took as part of this exercise.