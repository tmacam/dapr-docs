---
type: docs
title: "A high level explanation of how to create a pluggable component"
linkTitle: "A high level explanation of how to create a pluggable component"
weight: 4500
description: "A high level explanation of how to create a pluggable component"
---

<!-- Doc Title. This doc should be titled something similar to "Developing pluggable components". The .NET docs titled the same will be changed -->

<!-- Another thing about this document: it should be programming language agnostic. This document should describe the step-by-step process of developing a pluggable component but completely bypassing any technology or language specific detail. -->


1. Mention that the proto files can be edited for different languages. I think this should touch on the following:
    * What these protobuff files are. You can add a HL answer and then just link to the official gRPC site if you'd like.
    * Why you need to do this
    * How to do it
    * ~~How much of the proto file needs to be edited~~ we don't have to edit those protos at all.
    * ~~Code snippet of a proto file completely edited for another language (maybe Java or another you're comfortable with that we support)~~ Again, protos are not modified at all.
2. How You can implement pluggable components in kubernetes.
3. Add a "Next Steps" Section that links to:
The other "developing pluggable components" doc for .NET
.NET sample marco will create (put in a placeholder for this)
