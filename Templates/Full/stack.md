```markdown
# Stack

## 1. Identification

- **Project:** [name]
- **Version:** [v1]
- **Status:** [draft | reviewing | approved]
- **Tech owner:** [name]
- **Base docs:** project.md
- **Created:** [dd/mm/yyyy] · **Updated:** [dd/mm/yyyy]

---

## 2. Document Scope

**In scope:** languages · frameworks · databases · main libraries · infrastructure · technical standards · choice criteria

**Out of scope:** entity modeling · module architecture · API endpoints · implementation tasks · execution plan

---

## 3. Technical Context

**Technical summary:** [type of system being built]

**Project nature:** [web app | backend api | admin panel | hybrid app | microservice | automation | internal system | SaaS | marketplace]

**Expected operation:** [low scale | medium scale | high scale | internal | public | real-time | async | transactional | analytical]

**Target platforms:** [web] · [mobile] · [api] · [admin] · [worker] · [cli]

**Context influencing the stack:** [deadline constraint] · [team constraint] · [cost constraint] · [team experience] · [speed need] · [scale need] · [existing legacy]

---

## 4. Choice Principles

**Guiding principles:** [e.g. operational simplicity] · [fast development] · [low initial cost] · [ease of maintenance] · [progressive scalability] · [strong ecosystem] · [team alignment]

**Higher priority in choices:** [describe]

**What will be technically avoided:** unnecessary complexity · hard-to-operate service dependencies · stack misaligned with the team · immature tools · overengineering

---

## 5. Official Stack

### 5.1 Languages
- **Primary:** [e.g. TypeScript]
- **Secondary:** [e.g. SQL, Bash]
- **Rationale:** [why these languages]

### 5.2 Frontend
- **Framework:** [e.g. Next.js]
- **Main libraries:** [e.g. React] · [TanStack Query] · [Zod] · [React Hook Form]
- **UI strategy:** [SSR | CSR | hybrid | reusable components | own design system]
- **Rationale:** [explain]

### 5.3 Backend
- **Framework:** [e.g. NestJS | Fastify | Express]
- **Responsibilities:** [auth] · [business rules] · [integrations] · [persistence] · [queue] · [files] · [notifications]
- **Rationale:** [explain]

### 5.4 Database
- **Primary:** [e.g. PostgreSQL]
- **Auxiliary:** [Redis] · [Elastic] · [other]
- **ORM / Query builder:** [e.g. Prisma | Drizzle | Knex | raw SQL]
- **Rationale:** [explain]

### 5.5 Infrastructure & Hosting
- **Primary environment:** [e.g. VPS | Docker | Vercel | Railway | AWS | GCP]
- **Planned services:** [app] · [database] · [cache] · [queue] · [storage] · [cdn] · [proxy] · [monitoring]
- **Rationale:** [explain]

### 5.6 Auth & Authorization
- **Strategy:** [JWT | session | OAuth | auth provider | RBAC | ACL]
- **Rationale:** [explain]

### 5.7 Communication & API
- **Primary pattern:** [REST | GraphQL | RPC | WebSocket | events]
- **Contract format:** [OpenAPI | contract-first | code-first | hybrid]
- **Rationale:** [explain]

### 5.8 Testing
- **Tools:** [e.g. Vitest | Jest] · [Playwright | Cypress] · [Supertest]
- **Strategy:** [unit | integration | contract | e2e]
- **Rationale:** [explain]

### 5.9 Observability & Logs
- **Strategy:** structured logs · monitoring · alerts · health checks · tracing
- **Planned tools:** [tool 1] · [tool 2]
- **Rationale:** [explain]

### 5.10 Dev Experience & Quality
- **Tools:** [ESLint] · [Prettier] · [TypeScript strict] · [Husky] · [lint-staged] · [commitlint] · [turbo | nx | pnpm workspace]
- **Rationale:** [explain]

---

## 6. Structural Technical Decisions

**Adopted technical standards:** strong typing · input validation · domain/infrastructure separation · reusable components · centralized contracts · standardized error handling · structured logs · environment-based config

**Mandatory conventions:** [convention 1] · [convention 2] · [convention 3]

**Relevant code directives:** [directive 1] · [directive 2] · [directive 3]

---

## 7. Considered Alternatives

### Alternative 1
- **Option:** [describe]
- **Advantages:** [advantage 1] · [advantage 2]
- **Disadvantages:** [disadvantage 1] · [disadvantage 2]
- **Reason not adopted:** [explain]

### Alternative 2
- **Option:** [describe]
- **Advantages:** [advantage 1] · [advantage 2]
- **Disadvantages:** [disadvantage 1] · [disadvantage 2]
- **Reason not adopted:** [explain]

---

## 8. Technical Constraints

**Constraints that impacted the stack:** [constraint 1] · [constraint 2] · [constraint 3]

**Consciously assumed limitations:** [limitation 1] · [limitation 2]

**Technical risks of the chosen stack:** [risk 1] · [risk 2]

**Initial mitigations:** [mitigation 1] · [mitigation 2]

---

## 9. Main Dependencies

**Critical dependencies:** [dependency 1] · [dependency 2] · [dependency 3]

**Planned external services:** [service 1] · [service 2]

**Dependencies with highest operational risk:** [dependency 1] · [dependency 2]

---

## 10. Environment Strategy

**Planned environments:** local · dev · staging · prod

**Relevant differences between environments:** [describe]

**Environment config directive:** [describe]

---

## 11. Directives for Next Documents

| Document | How the stack impacts it |
|----------|--------------------------|
| architecture.md | [stack decisions that impact architecture] |
| entities.md | [persistence and modeling constraints] |
| contract.yaml | [technical standards to reflect in the contract] |
| structure.md | [folder and layer organization influenced by the stack] |
| deploy.md | [operational constraints and needs from the stack] |
| plan.md | [stack impacts on execution order] |
| tasks.md | [technical areas that must become early tasks] |

---

## 12. Operational Summary for Dev & AI

- **Frontend:** [fill]
- **Backend:** [fill]
- **Database:** [fill]
- **Infrastructure:** [fill]
- **Testing:** [fill]
- **What motivated this stack:** [reason 1] · [reason 2] · [reason 3]
- **What must be respected:** [rule 1] · [rule 2] · [rule 3]
- **What must be avoided:** [mistake 1] · [mistake 2]
- **What may still change:** [point 1] · [point 2]

---

## 13. Approval

- **Status:** [pending | approved | reviewing]
- **Approved by:** [name]
- **Date:** [dd/mm/yyyy]
- **Notes:** [notes]
```