# SPEC-0007 — Zeroth Post-Quantum Cryptographic Framework

- **Status:** Draft
- **Track:** Cryptography
- **Normative:** No
- **Version:** 0.1
- **Published:** 2026-09-11
- **Security sensitivity:** Public

## 1. Abstract

This specification defines the approved architecture-level post-quantum requirements for The Zeroth Protocol. The objective is not to lock a single production algorithm prematurely, but to make cryptographic agility, hybrid transition, downgrade resistance, key rotation, and eventual post-quantum migration first-class protocol properties.

This document intentionally avoids publishing exploit-sensitive implementation details or treating current research candidates as final production cryptography.

## 2. Security objective

Zeroth must remain capable of preserving authorization integrity, settlement integrity, governance integrity, and verification provenance as cryptographic assumptions evolve.

The protocol must therefore avoid designs in which a single immutable key type, signature encoding, or classical-only verification rule becomes permanently embedded into protocol state without a migration path.

## 3. Scope

Post-quantum resilience affects at least:

- agent identity and authorization;
- operator and service identities;
- validator, sequencer, or committee attestations where applicable;
- transaction and settlement authorization;
- governance proposals, approvals, and emergency actions;
- economic-memory access controls;
- cryptographic commitments and evidence bindings;
- release and software provenance;
- long-lived records whose authenticity may need to be verified after cryptographic migration;
- key generation, storage, rotation, revocation, and recovery;
- cross-version interoperability and downgrade resistance.

## 4. Design principles

### 4.1 Algorithm agility

Protocol objects that depend on cryptographic verification should identify the cryptographic suite or verification policy needed to interpret them. Implementations must not infer a permanent global algorithm from historical convention alone.

### 4.2 Hybrid transition capability

During migration periods, Zeroth may require authorization evidence that combines classical and post-quantum cryptographic evidence. Hybrid use is a migration and defense-in-depth mechanism, not a declaration that any current candidate suite is permanently selected for production.

### 4.3 No silent downgrade

A verifier must not silently reinterpret an object requiring stronger cryptographic policy under a weaker policy because one algorithm, key, or implementation path is unavailable.

Downgrade behavior must fail closed unless an explicitly authorized compatibility policy applies.

### 4.4 Explicit cryptographic policy binding

Signatures and attestations should be bound to sufficient context to prevent cross-domain or cross-version reuse. Context may include protocol domain, network or environment, object type, version, authority scope, and the hash or commitment of the authorized payload.

### 4.5 Rotation without identity loss

Long-lived agent or governance identity must not require permanent reuse of one signing key. Key rotation and revocation should preserve continuity through explicit authorization state rather than by equating identity with a single public key.

### 4.6 Historical verifiability

Migration must define how historical objects remain verifiable after algorithms or verification policies change. The protocol should distinguish historical validity under the policy active at creation from authorization to create new objects under a current policy.

## 5. Cryptographic suite identifiers

Public protocol formats should be capable of identifying:

- suite identifier;
- signature or attestation format version;
- public-key or credential format version;
- hash / commitment suite where relevant;
- verification-policy version where composite or hybrid validation is required.

Identifiers must be unambiguous and versioned. Unknown mandatory suites must fail closed.

## 6. Hybrid verification model

Where hybrid policy is active, a protocol object may carry more than one cryptographic proof over the same canonical authorization context.

The verification rule must explicitly define whether proofs are:

- conjunctive — all required proofs must verify;
- thresholded — a defined subset must verify;
- transitional — acceptance depends on an explicitly versioned migration epoch or policy.

The acceptance rule must never be inferred from proof ordering or presence alone.

## 7. Identity and authorization

Agent and operator identities should reference authorized key material through protocol state or credentials that support:

- multiple active keys where policy allows;
- key-purpose separation;
- rotation;
- revocation;
- expiry;
- recovery under explicitly governed conditions;
- migration from one cryptographic suite to another.

A reputation score, model confidence value, or historical identity association must not substitute for cryptographic authority.

## 8. Validator and protocol attestations

Where Zeroth components produce validator, sequencer, committee, oracle, verifier, or similar attestations, the signed context must identify the semantic object being authorized and its protocol version.

Migration to post-quantum-capable attestations must preserve replay resistance and must not permit a classical-only fallback unless that fallback is explicitly authorized by current protocol policy.

## 9. Settlement authorization

Settlement-sensitive signatures and proofs require stronger migration discipline because compromise may directly affect economic state.

Settlement authorization formats should therefore support:

- suite/version binding;
- explicit authority scope;
- chain or settlement-domain separation;
- replay protection;
- expiry or state-dependent validity where applicable;
- revocation and key rotation;
- cryptographic-policy migration without reinterpretation of historical authorization.

## 10. Governance authorization

Governance actions that change protocol rules, cryptographic policy, emergency state, upgrade authority, or settlement-critical parameters must be bound to an explicit governance domain and policy version.

A cryptographic migration must not allow a weaker legacy key path to override a newer stronger governance policy through ambiguous fallback semantics.

## 11. Economic Memory and access authorization

Where Zeroth maintains long-lived economic or protocol memory, cryptographic migration applies to both authenticity and access control.

The public architecture should favor storing commitments, digests, or protocol-relevant state rather than unnecessary private payloads. Access to protected material must support key rotation and policy migration independently from the historical integrity of the record.

## 12. Commitments and hashes

Post-quantum planning is not limited to digital signatures. The protocol must track cryptographic assumptions attached to commitments, Merkle structures, proofs, state roots, release manifests, and other long-lived digests.

If a commitment construction is superseded, migration rules must make the transition explicit rather than silently re-hashing historical state under a new scheme without provenance.

## 13. Key lifecycle requirements

Every production cryptographic role should define:

- key purpose;
- generation requirements;
- storage boundary;
- activation;
- rotation cadence or trigger;
- revocation path;
- compromise recovery;
- migration to a successor suite;
- audit/provenance evidence appropriate to that role.

Operational key custody details remain private.

## 14. Migration epochs

A future normative version of this specification may define explicit cryptographic migration epochs such as:

1. classical compatibility;
2. hybrid-required transition;
3. post-quantum-preferred operation;
4. post-quantum-required operation;
5. legacy verification only for historical artifacts.

The exact production sequence and algorithms remain subject to security review, interoperability testing, standards maturity, implementation readiness, and governance approval.

## 15. Test vectors and interoperability

Public cryptographic formats that become normative should have canonical positive and negative test vectors published through `zeroth-test-vectors`.

Vectors should cover, where applicable:

- canonical encoding;
- valid verification;
- malformed keys and signatures;
- wrong-domain signatures;
- wrong-version signatures;
- missing required hybrid proof;
- downgrade attempts;
- replay-context mismatch;
- rotated/revoked key handling.

Exploit-sensitive vectors may remain embargoed until the relevant vulnerability is remediated.

## 16. Production algorithm selection

This draft deliberately does **not** ratify a final production post-quantum signature algorithm, parameter set, threshold construction, or hybrid combination.

Research and qualification artifacts may evaluate concrete candidate algorithms. Candidate use in a prototype, audit target, or assurance snapshot does not by itself make that algorithm a permanent protocol standard.

Final selection requires a separate normative decision supported by security analysis, implementation evidence, interoperability vectors, migration analysis, and governance approval.

## 17. Relationship to other specifications

This framework is intended to constrain and inform:

- `SPEC-0001` — System Architecture
- `SPEC-0002` — Agent Identity and Authorization
- `SPEC-0005` — Settlement Interface
- `SPEC-0006` — Protected Ordering Interface
- `SPEC-0008` — Rollup / Appchain Evolution Architecture

Cryptographic requirements defined by those specifications must not contradict the downgrade-resistance and algorithm-agility principles defined here without an explicit superseding decision.

## 18. Status and change control

This is a **Draft, non-normative cryptographic architecture specification**. It establishes public design requirements while keeping production algorithm selection open.

Promotion to normative status requires independent cryptographic review, public interoperability vectors, migration analysis, and the applicable `ZEROTH-OSG-01` security/release gates.
