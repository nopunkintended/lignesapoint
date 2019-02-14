# The Docker-Minideb-Supervisor-Hug (DMSH) stack

In order to provide a working environment for an interconnected tool, and such turning it into an available microservice piece for a more complex structure, a segregated daemon is required. Applying this principle to current technologies provides us with the _API-in-a-Container template_. The **Docker-Minideb-Supervisor-Hug stack** is an application of this template.

## DMSH
- [**docker**](https://github.com/docker): platform built for developers to build and run applications.
- [**minideb**](https://github.com/bitnami/minideb): small image based on Debian by bitnami.
- [**supervisor**](https://github.com/Supervisor/supervisor): process control system for UNIX.
- [**hug**](https://github.com/timothycrosley/hug): APIs, as simple as possible, but no simpler.
