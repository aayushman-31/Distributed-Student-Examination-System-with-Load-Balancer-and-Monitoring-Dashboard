# Distributed-Student-Examination-System-with-Load-Balancer-and-Monitoring-Dashboard
This project is a distributed web-based examination system designed to demonstrate core concepts of distributed computing, load balancing, fault tolerance, and system monitoring. The system allows students to log in through a web interface, attempt an online exam consisting of multiple-choice questions, and receive an automatically evaluated score.


The architecture consists of a client-facing web application, a centralized load balancer, and two backend exam servers, all running on the same machine but on different ports and accessible over a local network. The web application handles user authentication and interacts with the load balancer, which is responsible for distributing incoming requests to the exam servers.

The load balancer implements a Round Robin scheduling algorithm, ensuring that requests are alternately routed between the two servers for efficient workload distribution. Additionally, it incorporates health monitoring and capacity-aware routing, meaning it continuously checks whether servers are active and whether they have available processing capacity before assigning requests. If one server becomes unavailable, the system automatically redirects all traffic to the remaining active server, ensuring uninterrupted service.
