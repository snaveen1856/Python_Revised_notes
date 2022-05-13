
"""
##########  What is Micro-services ? ############

Micro-service:
=============
It is a way of breaking your big monolithic application into two or more Standalone and Independent applications 
that can be Run on different hardware or server instances. They can communicate each other over a REST API and 
works together to get functionality of an application or a product.

Each Micro-service goes separately in testing and deployed separately
Each Micro-service works separately or work together as part of user concern
If any Micro-service had issues, then that will not affect others.
Advantages:
----------
1. Deployment flexibility (which all goes separately)
2. Technology flexibility (we can write all in different languages, but they communicate through REST APIs)
3. Can be scaled up/down separately 
Disadvantage:
-------------
1. Deployment / architecture complexity(if 100 of micro-services)
2. Service discoverability (which goes to consume)

Finally Monolithic architecture and Micro-service architecture has their own advantages and Disadvantages

Orchestration layer in Microservice:
------------------------------------
Orchestration is the traditional way of handling interactions between different services in Service-Oriented 
Architecture (SOA). ... For example, if three services needed to be called in a particular order, the orchestrator 
makes a call to each one, waiting for a response before calling the next.

Zato:
----
Zato is an open source Python-based middleware platform and backend application server. 
It was designed as an agile ESB (Enterprise Service Bus) aimed at building systems of systems 
either on-premise or in the cloud. Zato provides SOA (Service Oriented Architecture), 
REST (Representational State Transfer), APIs and cloud integration, as well as back-end services 
exposure to front-end clients.
Zato is a powerful and scalable platform that not only assists in building and orchestrating integration services, but 
also enhances intercommunication across applications and data sources. It can keep in order all technical solutions your
business uses and open way for new opportunities and processes. Usage of a wide range of connectors, data formats and 
protocols allows Zato to avoid restricting architectural style or enforcing any other limitations.
"""

