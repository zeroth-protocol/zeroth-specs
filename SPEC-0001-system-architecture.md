# SPEC-0001 — Zeroth System Architecture

- **Status:** Draft
- **Track:** Architecture
- **Normative:** No
- **Version:** 0.1
- **Published:** 2026-09-11
- **Security sensitivity:** Public

## 1. Abstract

The Zeroth Protocol is an economic operating layer for autonomous AI agents. This specification defines the approved high-level system architecture and the boundary between economic verification, execution, settlement, consensus, identity, cryptography, governance, and future chain sovereignty.

This document intentionally excludes production secrets, exploit-sensitive implementation details, validator operational topology, private infrastructure, and unresolved security findings.

## 2. Architectural objective

Zeroth is designed to let autonomous agents participate in economic activity under explicit, machine-verifiable rules. The protocol must make authority, commitments, evidence, verification, settlement, and state transitions independently inspectable rather than relying on opaque application trust.

## 3. Architectural principles

### 3.1 Open protocol, staged implementation disclosure

The protocol architecture, standards, stable interfaces, and interoperability material should be public. Consensus-critical implementation, exploit-sensitive security research, and production infrastructure remain private until the applicable `ZEROTH-OSG-01` release gates are satisfied.

### 3.2 Earn sovereignty rather than assume it

Zeroth does not launch a sovereign Layer 1 at genesis. Blockchain sovereignty is an earned architectural state that must be justified by security, economic, operational, decentralization, and ecosystem evidence.

### 3.3 PoVW is not blockchain consensus

Proof of Verifiable Work (PoVW) evaluates whether work claims are supported by verifiable evidence according to the relevant Zeroth rules. PoVW must remain conceptually and operationally distinct from the mechanism that orders and finalizes blockchain state.

### 3.4 Cryptographic agility is a protocol property

Identity, signatures, attestations, settlement authorization, governance authorization, commitments, and long-lived protocol records must be designed for cryptographic migration rather than tied permanently to one signature scheme or key format.

### 3.5 Authority must be explicit

Reputation, contextual trust, model confidence, or historical performance must not silently create protocol authority. Authority must derive from explicit grants, credentials, roles, capabilities, or protocol-defined state.

## 4. Logical layers

The Zeroth architecture is decomposed into the following logical layers. Implementations may combine components operationally, but must preserve the semantic boundaries.

### 4.1 Identity and Authorization

Responsible for representing agents, principals, delegated capabilities, credentials, key material, authority scope, expiry, revocation, and rotation.

### 4.2 Economic State and Commitments

Responsible for protocol-visible economic commitments, entitlements, obligations, holds, releases, reversals, and state-transition inputs.

### 4.3 Work Claims and Evidence

Responsible for expressing claims about completed work and binding those claims to evidence or evidence commitments.

### 4.4 Verification / PoVW

Responsible for evaluating work evidence according to protocol-defined verification rules. Verification produces protocol-consumable outcomes; it does not itself replace execution-layer consensus.

### 4.5 Settlement

Responsible for applying authorized economic outcomes to the selected settlement substrate, subject to dispute, hold, finality, and replay-protection rules.

### 4.6 Execution

Responsible for deterministic application of Zeroth protocol state transitions on the active execution environment.

### 4.7 Blockchain Consensus

Responsible for ordering and finalizing execution-layer state according to the rules of the selected blockchain substrate. This is separate from PoVW.

### 4.8 Governance

Responsible for controlled protocol evolution, parameter authority, emergency procedures, cryptographic migration, standards adoption, and release decisions.

## 5. Genesis deployment architecture

The approved genesis strategy is not a sovereign Zeroth L1.

The intended evolution path is:

1. **Ethereum settlement** for high-assurance anchoring and settlement compatibility.
2. **Arbitrum execution** for the initial execution environment where appropriate.
3. **Dedicated Zeroth Rollup / appchain** only when workload, economics, control, performance, or protocol-specific execution requirements justify it.
4. **PQ-native Zeroth settlement** only if and when explicit native-settlement readiness criteria are satisfied.

This path is directional architecture, not a promise that every stage must occur or that a specific date is committed.

## 6. Native-chain readiness principle

A native Zeroth settlement layer must not be launched merely because Zeroth can technically implement one. Sovereignty should be considered only when the protocol can demonstrate that the move materially improves Zeroth without creating unacceptable security or operational concentration.

Readiness evaluation must include at least:

- a defensible security model;
- mature and independently reviewed consensus software;
- credible validator / operator diversity;
- resilient networking and recovery procedures;
- stable cryptographic and post-quantum migration architecture;
- production-grade observability and incident response;
- sustainable economic security;
- deterministic state-transition and replay semantics;
- demonstrated need that cannot be met adequately by the existing settlement/execution stack;
- a migration path that preserves user and agent safety.

The existence of research prototypes or qualification evidence is insufficient by itself to satisfy these criteria.

## 7. Public vs private architecture surface

### Public by default when publication-reviewed

- protocol specifications;
- Zeroth Improvement Proposals (ZIPs);
- stable interface schemas;
- cryptographic formats suitable for public interoperability;
- public test vectors;
- stable SDK surfaces;
- documentation and examples;
- audit reports cleared for publication.

### Private until hardened or permanently operational

- unresolved exploit details;
- production credentials and secrets;
- privileged infrastructure topology;
- IAM internals;
- active incident-response evidence;
- unreleased security findings;
- consensus-critical implementation that has not passed its release gate;
- anti-gaming details whose premature disclosure would weaken an active security control.

## 8. Security and post-quantum requirements

Post-quantum resilience is a protocol-level design requirement affecting at least:

- agent and operator identity;
- keys and signatures;
- validator / sequencer attestations;
- settlement authorization;
- governance authorization;
- memory-access authorization;
- cryptographic commitments;
- key rotation;
- algorithm migration;
- downgrade resistance;
- long-lived protocol records.

`SPEC-0007` defines the public architecture-level framework for these requirements.

## 9. Relationship to other specifications

This specification provides the architectural context for:

- `SPEC-0002` — Agent Identity and Authorization
- `SPEC-0003` — Economic State Transition Model
- `SPEC-0004` — Proof of Verifiable Work Interfaces
- `SPEC-0005` — Settlement Interface
- `SPEC-0006` — Protected Ordering Interface
- `SPEC-0007` — Hybrid Post-Quantum Signature Framework
- `SPEC-0008` — Rollup / Appchain Evolution Architecture

Later specifications may refine these components but must not silently collapse the separation between PoVW and blockchain consensus or silently assume sovereign-chain deployment at genesis.

## 10. Status and change control

This is a **Draft, non-normative architecture specification**. It records approved architectural direction but does not constitute a production-release declaration.

Protocol-semantic changes should proceed through the Zeroth Improvement Proposal process. Promotion to a normative or release-bound status requires publication review and the applicable engineering/security gates.
