# SPEC-0008 — Zeroth Rollup and Appchain Evolution Architecture

- **Status:** Draft
- **Track:** Architecture / Settlement
- **Normative:** No
- **Version:** 0.1
- **Published:** 2026-09-11
- **Security sensitivity:** Public

## 1. Abstract

This specification records the approved architectural principle that The Zeroth Protocol should **earn blockchain sovereignty rather than assume it**.

Zeroth does not require a sovereign Layer 1 at genesis. The protocol is expected to evolve through increasingly dedicated execution and settlement environments only when measured protocol needs, security readiness, decentralization, economics, and operational maturity justify the transition.

## 2. Approved evolution path

The current approved directional sequence is:

1. **Ethereum settlement**
2. **Arbitrum execution**
3. **Dedicated Zeroth Rollup / appchain** when justified
4. **PQ-native Zeroth settlement** only if explicit sovereignty-readiness criteria are satisfied

This sequence is an architecture strategy, not a commitment that every stage must occur or that any stage has a fixed launch date.

## 3. Non-goals

This specification does not:

- declare a Zeroth sovereign L1 for genesis;
- identify a final rollup stack or data-availability provider;
- lock a production consensus algorithm;
- equate Proof of Verifiable Work with blockchain consensus;
- expose production validator topology or infrastructure;
- define token issuance, validator economics, or monetary constants;
- treat research prototypes or assurance candidates as production-ready chain software.

## 4. Why genesis should not require sovereignty

A new sovereign chain creates its own security, validator, networking, upgrade, incident-response, bridge, client-diversity, and economic-security obligations.

If Zeroth can satisfy its initial execution and settlement requirements using established infrastructure, assuming those obligations at genesis would add protocol risk without necessarily adding proportional user or agent value.

The initial objective is therefore to prove Zeroth's economic and verification model before requiring the ecosystem to trust a new settlement layer.

## 5. Stage A — Ethereum settlement

Ethereum provides the initial high-assurance settlement anchor in the approved architecture.

At this stage, Zeroth should minimize unnecessary divergence from the security and tooling assumptions of the settlement environment while maintaining its own explicit protocol semantics above it.

Zeroth-specific work verification, economic-state rules, agent identity, and authorization remain protocol concerns even when final settlement uses Ethereum.

## 6. Stage B — Arbitrum execution

The approved early execution strategy uses Arbitrum where appropriate rather than immediately creating a dedicated Zeroth execution chain.

The purpose of this stage is to obtain more suitable execution economics and throughput while retaining a mature rollup ecosystem and Ethereum settlement relationship.

Use of Arbitrum must not make Zeroth protocol semantics inseparable from one implementation-specific environment. Public interfaces and state-transition rules should preserve a migration path.

## 7. Stage C — Dedicated Zeroth Rollup / appchain

A dedicated execution environment becomes justified only when Zeroth has protocol-specific requirements that materially exceed what the shared environment can provide.

Potential justification categories include:

- sustained protocol workload requiring dedicated capacity;
- execution-policy requirements specific to autonomous economic agents;
- sequencing or ordering requirements that cannot be safely expressed in the current environment;
- protocol-specific fee-market or resource-accounting needs;
- deterministic execution or state-access constraints;
- governance or upgrade-isolation requirements;
- measurable economic benefits that exceed the additional operational/security burden;
- a need for tighter integration between Zeroth execution and independently specified protocol primitives.

A dedicated execution environment still does not automatically imply sovereign settlement.

## 8. Stage D — PQ-native Zeroth settlement

A sovereign Zeroth settlement layer is the highest-cost and highest-responsibility stage in the approved evolution path.

It should be pursued only if the protocol can demonstrate that sovereign settlement materially improves Zeroth's security, autonomy, cryptographic roadmap, economics, or protocol functionality relative to remaining anchored to an external settlement layer.

Post-quantum capability alone is not sufficient justification for sovereignty if equivalent security properties can be achieved safely through less risky architecture.

## 9. Sovereignty-readiness gates

A native settlement decision must evaluate at least the following gates.

### 9.1 Security maturity

- production threat model complete;
- consensus-critical implementation independently reviewed;
- material security findings remediated or formally accepted with explicit rationale;
- adversarial, fuzzing, recovery, and failure-mode testing complete for the release candidate;
- cryptographic migration model stable;
- no dependency on security-through-obscurity.

### 9.2 Consensus maturity

- consensus semantics are formally specified;
- safety and liveness assumptions are explicit;
- implementation evidence is consistent with the specification;
- fault assumptions and quorum rules are independently reviewable;
- deterministic replay and recovery are demonstrated;
- qualification prototypes are clearly distinguished from production consensus.

### 9.3 Decentralization readiness

- credible operator diversity;
- no single operational dependency whose failure defeats the claimed security model;
- validator/sequencer onboarding and removal rules are defined;
- governance capture risks are analyzed;
- emergency authority is bounded and auditable.

### 9.4 Operational readiness

- reproducible deployment and release process;
- observability and incident response;
- backup, recovery, and state-reconstruction procedures;
- key compromise and rotation procedures;
- upgrade rollback / halt semantics where applicable;
- production capacity and failure-domain analysis.

### 9.5 Economic-security readiness

- sustainable security budget;
- incentive compatibility reviewed;
- concentration and collusion risks analyzed;
- slashing or equivalent accountability mechanisms, if any, specified and tested;
- dependence on token price or external liquidity explicitly modeled rather than assumed.

### 9.6 Ecosystem necessity

- clear evidence that shared settlement/execution materially constrains Zeroth;
- measurable benefit to agents, developers, operators, or economic security;
- migration costs and fragmentation risks are justified by those benefits.

## 10. PoVW separation

Proof of Verifiable Work must remain distinct from blockchain consensus throughout every stage.

PoVW evaluates claims and evidence according to Zeroth verification rules. Blockchain consensus orders and finalizes protocol state. A future Zeroth-native settlement layer must not collapse these responsibilities merely because both are Zeroth components.

This separation allows PoVW to evolve as an economic-verification system without requiring every change to become a consensus-mechanism change.

## 11. Portability requirements

To preserve the ability to move between execution/settlement stages, Zeroth should keep the following concerns explicitly versioned where practical:

- protocol object schemas;
- state-transition semantics;
- identity and authorization formats;
- settlement request/outcome semantics;
- verification/PoVW outputs;
- cryptographic suite identifiers;
- replay and domain-separation rules;
- canonical test vectors.

Implementation-specific adapters may exist, but should not redefine the protocol implicitly.

## 12. Migration safety

Any migration to a more dedicated execution or settlement environment must define:

- source and target state commitments;
- migration cutoff or epoch semantics;
- replay protection;
- handling of pending obligations and disputes;
- identity/key continuity;
- cryptographic-policy continuity;
- rollback or failure handling;
- verification procedures that independent parties can reproduce.

Economic state must not be duplicated, silently dropped, or made valid on both environments without an explicitly defined bridge/migration rule.

## 13. Post-quantum considerations

Every stage should preserve the cryptographic agility requirements defined by `SPEC-0007`.

A transition to dedicated or sovereign infrastructure must not reduce downgrade resistance or make future post-quantum migration harder. If a future native settlement layer claims PQ-native properties, those properties must be defined at the protocol and verification levels rather than only as implementation branding.

## 14. Governance

Moving from one architectural stage to another is a protocol-level decision and should require:

- an explicit Zeroth Improvement Proposal;
- published rationale and alternatives;
- security and migration analysis;
- operational readiness evidence;
- implementation and interoperability evidence;
- governance approval under the policy active at that time.

No implementation team should be able to create de facto sovereignty merely by deploying infrastructure that protocol governance has not adopted.

## 15. Status and change control

This is a **Draft, non-normative architecture specification**. It records the approved strategic evolution path and readiness principles but does not authorize deployment of a dedicated rollup, appchain, or sovereign Zeroth settlement layer.

Promotion of any stage to a production target requires its own reviewable proposal and the applicable `ZEROTH-OSG-01` release gates.
