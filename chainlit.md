# Network Agent

An agentic AI assistant for managing a live **Open5GS 5G core network**.
The agent autonomously chains tool calls to diagnose issues, remediate faults,
and explain network behaviour — all visible as expandable steps in real time.

---

## Available Tools

| Tool | What it does |
|------|-------------|
| `system_health_snapshot` | One-shot health check of all NFs, MongoDB, and the TUN device |
| `nf_lifecycle` | Start, stop, restart, or query the status of any Open5GS NF |
| `tail_nf_logs` | Read and filter recent log entries from any NF log file |
| `list_ue_sessions` | List all active UE registrations and their PDU sessions |
| `subscriber_crud` | Create, read, update, or delete subscriber profiles in MongoDB |
| `read_nf_config` | Read parsed YAML config for any NF — explorable by subtree path |
| `trace` | Capture a live 5G call flow and render it as a sequence diagram |

---

## Demo Scenarios

Three quick-start buttons appear on every message:

1. **🏥 Health Snapshot** — Poll every network function and get an instant status
   table with 🟢🟡🔴 emojis.

2. **👀 Watch Subscriber Attach** — List all currently registered UEs and their
   active PDU sessions, including assigned IP addresses.

3. **🔍 Debug Attach Failure** — Triage the network with a health snapshot as the
   first step, then drill down into logs or configs as needed.

---

## Call Flow Diagrams

Ask the agent to trace or explain any 5G procedure and it will render a
**Mermaid sequence diagram** inline:

- `show me the 5G registration call flow`
- `draw the PDU session establishment procedure`
- `trace the last attach attempt`
- `what does the authentication flow look like between UE, AMF, and AUSF?`

---

## Example Queries

```
show subscriber imsi-999700000000001
tail amf logs for the last 10 minutes
restart the smf
what is the AMF SBI address?
create 5 subscribers starting from imsi-999700000000010
```
