# boolean-pundits
Memgraph Hackaton Boolean-Pundits team.


# Instructions

1. Start kafka & memgraph
`docker-compose up`

2. Initialize topic:

    2.1. Enter into kafka container:
    `docker container exec -it boolean-pundits_kafka_1 bash`

    2.2. Create topic:
    `kafka-topics.sh --create --topic test --bootstrap-server localhost:9092`

    2.3. Verify that topic has been created (Optional):
    `kafka-topics.sh --describe --topic test --bootstrap-server localhost:9092`

3. Setup stream in Memgraph:
  Connect to memgraph via mgconsole (or some other client app) and create and run stream:
  `CREATE STREAM steam TOPICS test TRANSFORM transformations.transform_test;`
  `START STREAM steam;`

4. Run producer:
  Install the libraries from requirements and run `producer.py`
    `python producer.py`
