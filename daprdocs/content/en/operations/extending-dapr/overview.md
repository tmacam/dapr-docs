---
type: docs
title: "gRPC Pluggable components overview"
linkTitle: "Overview"
weight: 4500
description: "Overview of gRPC pluggable components."
---

Dapr can be extended to use external components that are not naitively supported by the Dapr runtime [(supported Dapr components)](https://docs.dapr.io/operations/components/). This functionality is provided through gRPC pluggable components which are created external to the runtime, are developed differently from traditional Dapr components and can still be used with existing building block APIs. 

<img src="/images/concepts-building-blocks.png" width=400> 

Creating your own external gRPC pluggable components can be hepful for scenarios where writing a traditional Dapr component might not be feasible (e.g., unfamiliar with Go, remaining untethered to Dapr release cycle, not interested in contributing custom component to dapr project etc.). For those situations creating an external pluggable component could be a better option.


## External gRPC components vs. traditional components
Out of the box, Dapr building blocks come with integrations to a wide range of cloud providers and open source solutions. We call each of these individual integrations “components”. For instance, an input biding integration for MySql is a component and a state store integration for MySQL would be a different component.


|Component details |External gRPC Pluggable Components |Traditional Dapr Component| 
|--------------------|:--------|---------|
| **Language component is written in** | [Can be written in any gRPC-supported programming language](https://grpc.io/docs/what-is-grpc/introduction/#:~:text=Protocol%20buffer%20versions,-While%20protocol%20buffers&text=Proto3%20is%20currently%20available%20in,with%20more%20languages%20in%20development.)  | [Must be written in Go](https://github.com/dapr/components-contrib/blob/master/docs/developing-component.md) |
| **Where component runs** | Runs as distinct process, container or pod seperate from Dapr itself | Run as part of the same executable as Dapr itself   |
| **Integration with Dapr** | Integrates with Dapr using gRPC via Unix Domain Sockets  | Integrated directly with Dapr codebase|
| **Hosting and distribution**| Distributed and hosted independently from Dapr itself, in your own repository, following your own release cycle | Distributed and hosted with the rest of Dapr codebase | 


## External gRPC Pluggable Components

gRPC Pluggable Components as an alternative way of adding new integrations and functionality to Dapr. They differ from “traditional” or (embedded?) components in the following ways:
- They can be written in any gRPC-supported programming language.
- They run in a distinct process, container or pod than Dapr itself.
- They integrate with Dapr by means well defined SPI (Service Provider Interface) defined using gRPC through Unix Domain Sockets.
- They can be distributed indepe ndently from Dapr itself, on their own repository, with their own release cycle.

<img src="/images/pluggable-component-process.png" width=400>

Pluggable components are automatically discovered by creating sockets in a shared volume. The process is the following:
1. The Component listens to an [UDS](https://en.wikipedia.org/wiki/Unix_domain_socket) placed on the shared volume.
2. The Dapr runtime lists all [UDS](https://en.wikipedia.org/wiki/Unix_domain_socket) in the shared volume.
3. The Dapr runtime connects with the socket and uses gRPC reflection to discover all services that such component implements.

A single component can implement multiple [building blocks](http://localhost:1313/concepts/building-blocks-concept/) at once.
[gRPC-based](https://grpc.io/) Dapr components are typically run as containers or processes that communicate with the Dapr main process via [Unix Domain Sockets](https://en.wikipedia.org/wiki/Unix_domain_socket).

## Next Steps
- Developing gRPC Components
- Using gRPC components
