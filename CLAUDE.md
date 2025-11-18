# CLAUDE.md - AI Assistant Guide for the OS Ecosystem Cartridge

**Last Updated:** 2025-11-18
**Repository:** OS Ecosystem Cartridge
**Current State:** Blueprint Phase - Structure Defined, Implementation Pending

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Repository State & Context](#repository-state--context)
3. [Architecture Overview](#architecture-overview)
4. [Directory Structure](#directory-structure)
5. [Development Workflows](#development-workflows)
6. [Git Conventions](#git-conventions)
7. [File Organization Principles](#file-organization-principles)
8. [Key Conventions for AI Assistants](#key-conventions-for-ai-assistants)
9. [Implementation Roadmap](#implementation-roadmap)

---

## Quick Start

### Current State Summary

This repository is in its **blueprint phase**. The comprehensive README.md defines a vision for a monorepo "cartridge" ecosystem, but **the actual directory structure has not been created yet**.

**What exists:**
- `README.md` - Comprehensive architectural vision and philosophy
- `.git/` - Version control
- **Current branch:** `claude/claude-md-mi3tqytwn862omwz-01EL8wqL4F4f8Vyo5phFhDWE`

**What doesn't exist yet:**
- None of the 7 main directories (`governance/`, `archive/`, `workspace/`, `containers/`, `environment/`, `cloud/`, `docs/`)
- No configuration files (.gitignore, .editorconfig, etc.)
- No actual project code or dependencies

### Historical Context

**Commit History:**
1. **1ccd324** (Oct 25, 2024) - Initial implementation of a Swarm Orchestration System with Python code
2. **f3eb39a** (Oct 25, 2024) - Complete pivot: deleted all implementation, replaced with OS Ecosystem Cartridge vision

**Key Insight:** This represents an architectural evolution from a specific tool (swarm orchestration) to a comprehensive ecosystem framework.

---

## Repository State & Context

### Philosophy

This repository embodies a **"cartridge"** philosophy - a self-contained, highly-structured monorepo that consolidates diverse software projects into a unified, reproducible, transparent development environment.

**Core Principles:**
- **Holistic lifecycle management** - Source, docs, governance, and archives as one coherent system
- **Separation of concerns** - Clear layering between mutable (workspace) and immutable (archive)
- **Reproducibility** - Consistent environments via containers
- **Transparency** - Everything tracked, everything documented

### Design Philosophy for AI Assistants

When working with this repository, understand that:

1. **It's a meta-repository** - Not just code, but governance, policy, and infrastructure
2. **Structure precedes implementation** - The architecture is deliberately designed before coding
3. **Everything has a place** - The 7-directory structure is intentional and comprehensive
4. **Local-cloud mapping** - The `cloud/` directory bridges local development to GitHub
5. **Immutability matters** - `archive/` is append-only; `workspace/` is mutable

---

## Architecture Overview

### The Seven Pillars

The cartridge is organized into seven top-level directories, each serving a distinct architectural role:

```
/
├── governance/      # The Rulebook - Policies, licenses, standards
├── archive/         # The Museum - Immutable historical snapshots
├── workspace/       # The Workshop - Active development zone
├── containers/      # The Factory - Dev container templates
├── environment/     # The Configuration Hub - Env vars & secrets
├── cloud/           # The Bridge - GitHub/cloud mapping metadata
└── docs/            # The Library - Ecosystem documentation
```

### Architectural Layers

```
┌─────────────────────────────────────────┐
│         GOVERNANCE LAYER                │  ← Rules, policies, standards
│  (governance/, docs/)                   │
├─────────────────────────────────────────┤
│         DEVELOPMENT LAYER               │  ← Active work
│  (workspace/, containers/, environment/)│
├─────────────────────────────────────────┤
│         PERSISTENCE LAYER               │  ← Historical record
│  (archive/)                             │
├─────────────────────────────────────────┤
│         INTEGRATION LAYER               │  ← Cloud synchronization
│  (cloud/)                               │
└─────────────────────────────────────────┘
```

---

## Directory Structure

### 1. `governance/` - The Rulebook

**Purpose:** Foundational policies, licenses, and standards that govern the entire ecosystem.

**Planned Structure:**
```
governance/
├── policies/
│   ├── SECURITY.md           # Security policy
│   ├── CODE_OF_CONDUCT.md    # Community standards
│   ├── CONTRIBUTING.md       # Contribution guidelines
│   └── PRIVACY.md            # Data handling policy
├── licenses/
│   ├── LICENSE               # Primary license
│   └── THIRD_PARTY_NOTICES   # Dependency licenses
├── standards/
│   ├── coding-standards.md   # Code style guides
│   ├── commit-conventions.md # Git commit format
│   └── review-process.md     # Code review requirements
└── templates/
    ├── issue-template.md
    └── pr-template.md
```

**Key Principle:** This directory defines the "rules of engagement" for all contributors and projects.

### 2. `archive/` - The Museum

**Purpose:** Immutable, long-term preservation of historical artifacts.

**Planned Structure:**
```
archive/
├── snapshots/
│   ├── 2024/
│   ├── 2025/
│   └── [yearly directories]
├── research/
│   ├── papers/               # Important research papers
│   └── references/           # Curated reference materials
├── releases/
│   ├── v1.0.0/
│   └── [version directories]
└── legacy/
    └── swarm-orchestration-system/  # Previous implementation
```

**Key Principle:** Write-once, read-many. Never delete from archive, only add.

### 3. `workspace/` - The Workshop

**Purpose:** The primary mutable zone for all active development.

**Planned Structure:**
```
workspace/
├── orgs/                     # Mirror of GitHub organizations
│   ├── CoreSystems/
│   ├── ResearchLab/
│   └── [other orgs]/
├── repos/                    # Personal forks and experiments
│   ├── sandbox/
│   └── experimental/
├── projects/                 # GitHub Projects mirrors
│   ├── project-board-1.csv
│   └── roadmap.md
├── caches/                   # Build caches (gitignored)
└── artifacts/                # Build outputs (gitignored)
```

**Key Principle:** This is where actual coding happens. It mirrors cloud structure.

### 4. `containers/` - The Factory

**Purpose:** Standardized development container templates for reproducibility.

**Planned Structure:**
```
containers/
├── base/
│   └── Dockerfile
├── python/
│   ├── Dockerfile
│   └── devcontainer.json
├── node/
│   ├── Dockerfile
│   └── devcontainer.json
├── rust/
│   ├── Dockerfile
│   └── devcontainer.json
└── templates/
    └── README.md
```

**Key Principle:** "It works on my machine" should never be a problem.

### 5. `environment/` - The Configuration Hub

**Purpose:** Centralized environment variable management and secrets policy.

**Planned Structure:**
```
environment/
├── catalog/
│   ├── env-variables.md      # Canonical list of all env vars
│   └── repo-mapping.csv      # Which repos use which vars
├── templates/
│   ├── .env.template
│   └── .env.example
├── docs/
│   └── secrets-policy.md     # How to handle secrets
└── schemas/
    └── env-schema.json       # Validation schema
```

**Key Principle:** Never commit secrets. Document everything else.

### 6. `cloud/` - The Bridge

**Purpose:** Metadata mapping local cartridge to GitHub/cloud services.

**Planned Structure:**
```
cloud/
├── github/
│   ├── organizations.yaml    # Org structure mapping
│   ├── repositories.yaml     # Repo metadata
│   └── projects.yaml         # Project boards mapping
├── remotes/
│   └── remote-config.yaml    # Git remote configurations
└── sync/
    ├── sync-policy.md        # Sync rules and procedures
    └── last-sync.json        # Sync state tracking
```

**Key Principle:** Single source of truth for local-to-cloud relationships.

### 7. `docs/` - The Library

**Purpose:** Cartridge-level documentation about the ecosystem itself.

**Planned Structure:**
```
docs/
├── architecture/
│   ├── overview.md
│   ├── layering.md
│   └── principles.md
├── guides/
│   ├── getting-started.md
│   ├── maintenance.md
│   └── troubleshooting.md
├── decisions/                # Architecture Decision Records (ADRs)
│   ├── 001-cartridge-structure.md
│   └── 002-monorepo-vs-polyrepo.md
└── diagrams/
    └── [visual documentation]
```

**Key Principle:** Explain the "why" behind the structure, not just the "what".

---

## Development Workflows

### For AI Assistants: Standard Development Flow

When asked to implement features or make changes:

1. **Assess Current State**
   - Check which directories exist vs. planned
   - Verify branch status (`git status`, `git branch`)
   - Review recent commits for context

2. **Plan Before Implementing**
   - Use TodoWrite tool for multi-step tasks
   - Consider which of the 7 pillars the work belongs to
   - Respect the architecture - don't create files outside the structure

3. **Implement with Structure**
   - Create necessary directories following the planned structure
   - Place files in their correct architectural layer
   - Follow naming conventions (see below)

4. **Document Changes**
   - Update relevant docs when adding new capabilities
   - Consider if CLAUDE.md needs updating
   - Add ADRs (Architecture Decision Records) for significant choices

5. **Commit and Push**
   - Follow git conventions (see below)
   - Commit to the correct branch
   - Push with `-u origin <branch-name>`

### Creating the Initial Structure

If asked to "initialize" or "create the structure":

```bash
# Create all 7 main directories with .gitkeep files
mkdir -p governance/policies governance/licenses governance/standards governance/templates
mkdir -p archive/snapshots archive/research archive/releases archive/legacy
mkdir -p workspace/orgs workspace/repos workspace/projects workspace/caches workspace/artifacts
mkdir -p containers/base containers/python containers/node containers/rust
mkdir -p environment/catalog environment/templates environment/docs environment/schemas
mkdir -p cloud/github cloud/remotes cloud/sync
mkdir -p docs/architecture docs/guides docs/decisions docs/diagrams

# Create .gitkeep files for empty directories
find governance archive containers environment cloud docs -type d -exec touch {}/.gitkeep \;

# Create .gitignore for ephemeral directories
echo "*" > workspace/caches/.gitignore
echo "!.gitignore" >> workspace/caches/.gitignore
echo "*" > workspace/artifacts/.gitignore
echo "!.gitignore" >> workspace/artifacts/.gitignore
```

### Project Domain Classification

When adding new projects to `workspace/orgs/`, classify them by domain:

- 🧠 **AI/LLMs/Agentic Tools** - AI models, LLM integration, agentic workflows
- 🧰 **Developer Tooling** - CI/CD, automation, code quality tools
- 🌐 **Web & Docs** - Documentation systems, web schemas, public content
- 🧪 **ML & Data Science** - ML frameworks, data pipelines
- 🎮 **Games & Creative** - Interactive experiences, browser-based projects
- 🔐 **Governance & Security** - Policy enforcement, security tools, reverse engineering
- 🧬 **Symbolic & Experimental** - Research projects, experimental namespaces

---

## Git Conventions

### Branch Naming

**Current Branch Format:** `claude/claude-md-<session-id>`

**Standard Patterns:**
- `feature/<description>` - New features
- `fix/<description>` - Bug fixes
- `docs/<description>` - Documentation updates
- `refactor/<description>` - Code refactoring
- `chore/<description>` - Maintenance tasks
- `claude/<session-id>` - AI-assisted development sessions

### Commit Messages

**Format:**
```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

**Types:**
- `feat` - New feature
- `fix` - Bug fix
- `docs` - Documentation changes
- `style` - Code style changes (formatting, etc.)
- `refactor` - Code refactoring
- `test` - Adding/updating tests
- `chore` - Maintenance tasks
- `archive` - Adding to archive
- `governance` - Policy/standard updates

**Examples:**
```
feat(workspace): Add initial project structure for CoreSystems org

docs(CLAUDE): Update AI assistant guide with git conventions

archive(legacy): Preserve swarm-orchestration-system implementation

governance(policies): Add security policy and code of conduct
```

### Pushing Changes

**Always use:**
```bash
git push -u origin <branch-name>
```

**For network failures:** Retry up to 4 times with exponential backoff (2s, 4s, 8s, 16s)

---

## File Organization Principles

### Naming Conventions

**Directories:**
- Use lowercase with hyphens: `coding-standards/`, `dev-containers/`
- Exceptions: Organization names (mirror GitHub exactly)

**Files:**
- Documentation: `UPPERCASE.md` for important files (README.md, CLAUDE.md, LICENSE)
- Code: Follow language conventions (Python: snake_case, JavaScript: camelCase)
- Config: Use standard names (.gitignore, .editorconfig, package.json)

### README Files

Every significant directory should have a README.md explaining:
- Purpose of the directory
- What belongs there vs. elsewhere
- Naming conventions for that area
- Examples of proper usage

### Configuration Files to Create

**Root Level:**
```
.gitignore           # Standard ignores + workspace/caches, workspace/artifacts
.editorconfig        # Editor consistency
CLAUDE.md            # This file
README.md            # Public-facing overview (exists)
```

**Per-Domain:**
- Python projects: `pyproject.toml`, `requirements.txt`
- Node projects: `package.json`, `.npmrc`
- Rust projects: `Cargo.toml`

---

## Key Conventions for AI Assistants

### 🎯 Critical Guidelines

1. **Respect the Architecture**
   - Never create files outside the 7-directory structure
   - Understand the purpose of each pillar before placing files
   - Ask if uncertain about placement

2. **Preserve Immutability**
   - `archive/` is append-only - never modify or delete
   - `governance/` changes require careful consideration
   - `workspace/` is the mutable zone

3. **Document Decisions**
   - Create ADRs for significant architectural choices
   - Update CLAUDE.md when workflows change
   - Keep README.md synchronized with reality

4. **Maintain Consistency**
   - Follow existing patterns and conventions
   - Use TodoWrite for tracking multi-step tasks
   - Keep git history clean and meaningful

5. **Think Holistically**
   - This is a meta-system, not just code
   - Consider governance, documentation, and archival
   - Balance immediate needs with long-term structure

### 🔍 Before Making Changes

**Always Check:**
- [ ] Current git branch and status
- [ ] Which directories exist vs. planned
- [ ] Recent commit history for context
- [ ] Whether change belongs in governance, workspace, or elsewhere
- [ ] If documentation needs updating

**Always Ask:**
- "Does this fit the architecture?"
- "Should this be in archive or workspace?"
- "Does this need a governance policy first?"
- "Will this need container support?"

### 🚀 When Implementing Features

**Standard Flow:**
1. Create TodoWrite tasks for tracking
2. Verify/create necessary directory structure
3. Implement following architecture principles
4. Update relevant documentation
5. Commit with conventional commit message
6. Push to appropriate branch

### 📦 Managing Dependencies

**Principles:**
- Document all environment variables in `environment/catalog/`
- Container definitions in `containers/`
- Actual project dependencies in `workspace/orgs/<org>/<repo>/`
- Never commit secrets or credentials

### 🔄 Synchronization with GitHub

**When working with cloud mapping:**
- Update `cloud/github/` metadata when org/repo structure changes
- Maintain `cloud/remotes/` for git remote configurations
- Document sync procedures in `cloud/sync/`

---

## Implementation Roadmap

### Phase 1: Foundation (Current Priority)

**Status:** 🟡 In Progress

- [x] Create comprehensive README.md
- [x] Create CLAUDE.md (this file)
- [ ] Create all 7 main directory structures
- [ ] Add .gitignore with proper rules
- [ ] Create initial governance documents
  - [ ] SECURITY.md
  - [ ] CODE_OF_CONDUCT.md
  - [ ] CONTRIBUTING.md

### Phase 2: Infrastructure

**Status:** 🔴 Not Started

- [ ] Set up base development containers
- [ ] Create environment variable catalog
- [ ] Establish cloud mapping metadata
- [ ] Write architecture documentation
- [ ] Create workspace organization structure

### Phase 3: Migration & Archival

**Status:** 🔴 Not Started

- [ ] Archive the deleted Swarm Orchestration System
  - Extract from commit 1ccd324
  - Place in `archive/legacy/swarm-orchestration-system/`
  - Document in `archive/legacy/README.md`
- [ ] Create first ecosystem snapshot
- [ ] Establish archival procedures

### Phase 4: Active Development

**Status:** 🔴 Not Started

- [ ] Populate workspace with actual projects
- [ ] Create project boards in `workspace/projects/`
- [ ] Set up CI/CD infrastructure
- [ ] Begin multi-domain development

---

## Project Domains & Use Cases

### 🧠 AI, LLMs, and Agentic Tools

**When adding AI projects:**
- Place in `workspace/orgs/AI/` or similar
- Document model dependencies in `environment/`
- Consider container requirements (GPU support, etc.)
- May need governance policies for AI ethics

### 🧰 Developer Tooling & Automation

**When adding dev tools:**
- May belong in `containers/` if it's an environment tool
- Otherwise in `workspace/orgs/DevTools/`
- Document in `docs/guides/` if it affects workflows

### 🌐 Web & Docs Infrastructure

**When adding web projects:**
- Public documentation may also go in `docs/`
- Web schemas and standards in `governance/standards/`
- Actual sites/apps in `workspace/orgs/Web/`

### 🔐 Governance, Security, and Reverse Engineering

**Sensitive by nature:**
- Security policies ALWAYS in `governance/policies/`
- Security tools in `workspace/` but document in `governance/`
- Never commit security findings without review

---

## Troubleshooting

### Common Issues

**Q: Where should I put this file?**
A: Ask yourself:
1. Is it a policy/standard? → `governance/`
2. Is it historical/immutable? → `archive/`
3. Is it active development? → `workspace/`
4. Is it container config? → `containers/`
5. Is it environment config? → `environment/`
6. Is it cloud metadata? → `cloud/`
7. Is it ecosystem documentation? → `docs/`

**Q: Can I modify archive/?**
A: Only to add new content, never to modify or delete.

**Q: How do I handle secrets?**
A:
- Never commit them
- Document them in `environment/catalog/` (without values)
- Use `.env` files (gitignored)
- Follow `environment/docs/secrets-policy.md`

**Q: Which branch should I use?**
A: Check the task context. For Claude sessions, use the provided `claude/*` branch.

---

## Version History

| Version | Date       | Changes                                    |
|---------|------------|--------------------------------------------|
| 1.0.0   | 2025-11-18 | Initial creation of comprehensive guide    |

---

## Additional Resources

### Related Files
- `README.md` - Public-facing overview and philosophy
- `governance/CONTRIBUTING.md` - (To be created) Contribution guidelines
- `docs/architecture/` - (To be created) Detailed architecture docs

### External References
- GitHub Organizations: (To be documented in `cloud/github/`)
- Container Registry: (To be documented)
- CI/CD Pipelines: (To be documented)

---

## Notes for Future AI Assistants

This repository represents an ambitious vision for a comprehensive software ecosystem. As of 2025-11-18, it's in the **blueprint phase** - the architecture is designed but not yet implemented.

**Your role:**
- Help implement this vision systematically
- Maintain architectural integrity
- Document everything
- Ask questions when the right path is unclear

**Remember:**
- Structure before code
- Documentation as code
- Governance as foundation
- Archival as history

**This is not just a codebase. It's an ecosystem.**

---

*Last updated: 2025-11-18*
*Maintained by: AI Assistants (Claude)*
*For questions or updates: Review git history and recent commits*
