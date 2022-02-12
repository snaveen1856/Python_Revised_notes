"""
What is Zato and why using Python makes sense? High-level overview
Zato is a highly scalable, Python-based integration platform for APIs, SOA and microservices. It is used to connect
distributed systems or data sources and to build API-first, backend applications. The platform is designed and built
specifically with Python users in mind.

Zato is used for enterprise, business integrations, data science, IoT and other scenarios that require integrations
of multiple systems.

Real-world, production Zato environments include:

A platform for processing payments from consumer devices
Systems for telecommunication operators integrating CRM, ERP, Charging Systems, Billing and other OSS/BSS applications
internal or external to the operators
A data science system for processing of information related to securities transactions (FIX)
A platform for public administration systems, helping achieve healthcare data interoperability through the integration
of independent data sources, databases and health information exchanges (HIE)
A global IoT platform integrating medical devices
A platform to process events produced by early warning systems
Backend e-commerce systems managing multiple suppliers, marketplaces and process flows
B2B platforms to accept and process multi-channel orders in cooperation with backend ERP and CRM systems
Platforms integrating real-estate applications, collecting data from independent data sources to present unified APIs to
internal and external applications
A system for the management of hardware resources of an enterprise cloud provider
Online auction sites
E-learning platforms
Zato offers connectors to all the popular technologies, such as REST, SOAP, AMQP, IBM MQ, SQL, Odoo, SAP, HL7, Redis,
MongoDB, WebSockets, S3 and many more.

Running on premises, in the cloud, or under Docker, Kubernetes and other container technologies, Zato services are
optimised for high performance - it is easily possible to run hundreds and thousands of services on typical server
instances as offered by Amazon, Google Cloud, Azure or other cloud providers.

Zato servers offer high availability and no-downtime deployment. Servers form clusters that are used to scale systems
both horizontally and vertically.

The software is 100% Open Source with commercial and community support available

A platform and language for interesting, reusable and atomic services
Zato promotes the design of, and helps you build, solutions composed of services which are interesting, reusable and
atomic (IRA):

I for Interesting - each service should make its clients want to use it more and more. People should immediately see the
value of using the service in their processes. An interesting service strikes everyone as immediately useful in wider
contexts, preferably with few or no conditions, prerequisites and obligations. An interesting service is aesthetically
pleasing, both in terms of its technical usage as well as its potential applicability in fields broader than originally
envisaged. If people check the service and say “I know, we will definitely use it” or “Why don’t we use it” you know
that the service is interesting. If they say “Oh no, not this one again” or “No, thanks, but no” then it is the
opposite.
R for Reusable - services can be used in different, independent business processes
A for Atomic - each service fullfils a single, atomic business need
Each service is deployed independently and, as a whole, they constitute an implementation of business processes taking
place in your company or organisation.

With Zato, developers use Python to focus on the business logic exclusively and the platform takes care of scalability,
availability, communication protocols, messaging, security or routing. This lets developers concentrate only on what is
the very core of systems integrations - making sure their services are IRA.

Python is the perfect choice for API integrations, SOA and microservices, because it hits the sweet spot under several
key headings:

It is a very high level language, with a syntax close to how grammar of various spoken languages works, which makes it
easy to translate business requirements into implementation
Yet, it is a solid, mainstream and full-featured, real programming language rather than a domain-specific one which
means that it offers to developers a great degree of flexibility and choice in expressing their needs
Many Python developers have a strong web programming / open source background which means that it is little effort to
take a step further, towards API integrations and backend servers. In turn, this means that it is easy to find good
people for API projects.
Many Python developers know multiple programming languages - this is very useful in the context of integration projects
where one is typically faced with dozens of technologies, vendors or integration methods and techniques.
Lower maintenance costs - thanks to the language’s unique design, Python programmers tend to produce code that is easy
to read and understand. From the perspective of multi-year maintenance, reading and analysing code, rather than writing
it, is what most programmers do most of the time, making sense to use a language that makes it easy to carry out the
most common tasks.
In short, Python can be construed as executable pseudo-code with many of its users already having roots in modern
server-side programming so Zato, both from a technical and strategic perspective, is a natural choice for complex and
sophisticated API solutions as a platform built in the language and designed for Python developers from day one.

More than services
Systems integrations commonly require two more features that Zato offers as well:

File transfer - allows you to move batch data between locations and to distribute it among systems and APIs
Single Sign-On (SSO) - a convenient REST interface lets you easily provide authentication and authorisation to users
across multiple systems
Next steps
Start the tutorial to learn more technical details about Zato, including its architecture, installation and usage. After
 completing it, you will have a multi-protocol service representing a sample scenario often seen in banking systems with
  several applications cooperating in providing a single, consistent API to its callers.
Visit the support page if you would like to discuss anything about Zato with its creators
Table of Contents
What is Zato and why using Python makes sense?
High-level overview
A platform and language for interesting, reusable and atomic services
More than services
Next steps
Quick search
 » Zato versions
3.2 (stable)
3.1 (previous)

"""