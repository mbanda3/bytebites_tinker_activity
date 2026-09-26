# ByteBites Reference File

## About This Project
You are building the backend logic for a campus food ordering app called ByteBites
using Python classes and simple algorithms.

## Project Scope
Do not add authentication logic, a database layer, or any features not described 
in the spec.

## Behavioral Instructions
<!-- Write a short set of instructions guiding how your AI assistant should behave 
when helping with this project — for example, which classes to stay within, 
what complexity to avoid, or any preferences for how suggestions are structured. -->

- Only model these four classes: `Customer`, `MenuItem`, `Menu`, `Transaction`. Do not invent
  additional classes (e.g. no `Order`, `PaymentMethod`, `Restaurant`, `Address`, `Discount`)
  unless the feature request explicitly calls for them.
- Do not add authentication/login logic (no passwords, tokens, sessions) — "verify they are
  real users" refers only to checking `purchase_history`, not building a login system.
- Do not add a database, persistence, or API layer. This is in-memory class design only.
- Keep attributes limited to what the feature request states. Don't invent extra fields
  (e.g. no `id`, `email`, `status`) unless asked.
- Use the exact class and attribute names from the spec so the diagram stays traceable back
  to the feature request sentence it came from.
- In Mermaid class diagrams, use `-->` for "has a" associations and `--|>` only for genuine
  "is a" inheritance — don't reach for inheritance when composition/association fits.
- When producing a diagram, output only a single ```mermaid classDiagram``` code block —
  no extra prose explanation unless I ask for one.
- If a request seems to require a class or field outside this scope, ask before adding it
  instead of silently expanding the design.
