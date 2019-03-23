# The Docker-Minideb-Supervisor-Hug (DMSH) stack

In order to provide a working environment for an interconnected tool, and such turning it into an available microservice piece for a more complex structure, a segregated daemon is required. Applying this principle to current technologies provides us with the _API-in-a-Container template_. The **Docker-Minideb-Supervisor-Hug stack** is an application of this template.

## API-in-a-Container
- Container: [*docker*](https://github.com/docker) - "platform built for developers to build and run applications".
- System: [*minideb*](https://github.com/bitnami/minideb) - "small image based on Debian by bitnami".
- Manager: [*supervisor*](https://github.com/Supervisor/supervisor) - "process control system for UNIX".
- API: [*hug*](https://github.com/timothycrosley/hug) - "APIs, as simple as possible, but no simpler".
- *your code here*

## The Container level
Building the microservice inside an isolated and portable environment allows for:
- easier **integration** (isolating constraints and requirements)
- easier **delivery** (regarding distribution and transportability issues)

Note that any internal or intermediate infrastructure (e.g.: development environments, CI/CD toolchains) benefits from the same advantages as the final complex structure.

Aside from Docker, options for the Container level could go from fully-virtualized machines to segregated environment variables. Docker provides a good compromise between the learning curve and the features versus limitations ratio. Distribution infrastructure already exists through the Docker hub system. Same goes for containers management system, providing an eventual basis for the complex structure.

## The System level
Having a Container level alleviate the constraints on the service's underlying system through the segregation between the underlying structure and the microservice. Thus the system can be more easilly optimized, focused on a smaller set of limitations. As a default rule of thumb, the System level should provide a functionnal infosystem for the manager and the API while being minimal it is width and weight. Beyond that, relevant requierements can be added, from security to mobility.

One of the winning-side of the System level being (more or less) independant from the underlying structure is not only the microservice portability (being packed) but also the freedom of work for the microservice crafter. Providing a more friendly environment without most of its constraints on the underlying structure to crafters outside of the system field is a huge plus regarding democratic access to innovation, thus to the overall capabilities of complex structures.
