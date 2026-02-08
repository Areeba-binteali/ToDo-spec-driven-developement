---
id: 1
title: "Update Constitution"
stage: "constitution"
date_iso: "2026-01-28"
surface: "agent"
model: "claude-opus-4-5-20251101"
feature: "none"
branch: "master"
user: "Wajiz.pk"
command: "/sp.constitution"
labels: ["constitution", "setup", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - ".specify/memory/constitution.md"
tests: []
---

# Prompt Text
```
/sp.constitution

Project: Phase II – Todo Full-Stack Web Application (Spec-Driven, Agentic Dev Stack)

Core principles:
- Spec-first development (no implementation without an approved spec)
- End-to-end consistency across frontend, backend, API, and database
- Strict user data isolation and security
- Zero manual coding (all code generated via Claude Code)
- Production-minded architecture (scalable, stateless, cloud-ready)

Key standards:
- All features must map directly to Spec-Kit specs under /specs/**
- Every implementation must reference relevant specs using @specs/ paths
- REST APIs must be fully JWT-protected (Authorization: Bearer <token>)
- Task data must always be filtered by authenticated user ID
- Backend must never trust client-provided user_id without JWT verification
- Database access must use SQLModel only (no raw SQL)
- Frontend must use a centralized API client for all backend calls
- Authentication handled exclusively via Better Auth + JWT (no custom auth logic)

Architecture rules:
- Monorepo structure enforced (frontend + backend in same repository)
- Frontend: Next.js 16+ (App Router, TypeScript, Tailwind)
- Backend: FastAPI (Python) with clear route separation
- Database: Neon Serverless PostgreSQL
- Auth flow: Better Auth (frontend) → JWT → FastAPI verification
- Shared JWT secret via environment variable: BETTER_AUTH_SECRET

API constraints:
- All endpoints under `/api/`
- No endpoint accessible without valid JWT
- User identity must be derived from JWT, not request body
- Task ownership enforced on every CRUD operation
- Proper HTTP status codes required (401, 403, 404, 422)

Development workflow:
- Step 1: Read and validate relevant specs
- Step 2: Generate implementation plan
- Step 3: Break plan into atomic tasks
- Step 4: Implement via Claude Code only
- Step 5: Review against acceptance criteria
- Step 6: Update specs if behavior changes

Quality gates:
- No feature considered complete without:
  - Matching spec acceptance criteria
  - Backend + frontend implementation
  - Aut
```

# Response Text
Updated the project constitution file (.specify/memory/constitution.md) to reflect the core principles for the Todo Full-Stack Web Application project, including spec-first development, end-to-end consistency, user data security, zero manual coding constraints, production-minded architecture, and JWT-protected API access. The constitution now includes detailed sections on additional constraints, technology stack requirements, API requirements, database requirements, development workflow stages, quality gates, and governance procedures.

# Outcome
Successfully created a comprehensive project constitution that captures all the specified principles and requirements for the Todo application development.