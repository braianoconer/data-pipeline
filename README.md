# data-pipeline

## Course: Kafka 101 (confluent)
https://developer.confluent.io/learn-kafka/apache-kafka


## Course: Kafka Connect 101 (confluent)
https://developer.confluent.io/learn-kafka/kafka-connect


## Course: Kafka Streams 101 (confluent)
https://developer.confluent.io/learn-kafka/kafka-streams


## Course: Building Data Pipelines with Apache Kafka (confluent)
https://developer.confluent.io/learn-kafka/data-pipelines


## Course: Kafka Connect Fundamentals (pluralsight)
https://app.pluralsight.com/library/courses/kafka-connect-fundamentals/table-of-contents


## Course: Building ETL Pipelines from Streaming Data with Kafka and ksqlDB (pluralsight)
https://app.pluralsight.com/library/courses/kafka-streams-ksql-fundamentals/table-of-contents

---

## Conference: Event-Driven Architectures Done Right, Apache Kafka • Tim Berglund • Devoxx Poland 2021 (youtube)
https://youtu.be/A_mstzRGfIE


## Conference: Processing Streaming Data with KSQL - Tim Berglund (youtube)
https://youtu.be/LM-aQQQes4Q


## Conference: Building Streaming Microservices with Apache Kafka - Tim Berglund (youtube)
https://youtu.be/Hlb-Ss3q3as


## Conference: Apache Kafka and KSQL in Action : Let’s Build a Streaming Data Pipeline! by Robin Moffatt (youtube)
https://youtu.be/Z8_O0wEIafw


## How to install Kafka Connect connector plugins (youtube)
https://youtu.be/18gDPSOH3wU


---


## Generalized Amazon S3 Source Connector

https://docs.confluent.io/kafka-connect-s3-source/current/generalized/overview.html


## S3 Source Connector Configuration Properties
https://docs.confluent.io/kafka-connect-s3-source/current/configuration_options.html#s3-source-configuration-options


## Streams Concepts
https://docs.confluent.io/platform/current/streams/concepts.html


## Kafka Connect Deep Dive – Converters and Serialization Explained
https://www.confluent.io/blog/kafka-connect-deep-dive-converters-serialization-explained/


## kafka-elasticsearch-connector-tutorial
https://www.confluent.io/blog/kafka-elasticsearch-connector-tutorial/


## Kafkacat > kcat
https://docs.confluent.io/platform/current/app-development/kafkacat-usage.html

https://github.com/edenhill/kcat

### produce messages from file
cat data.json | kcat -b kafka:29092 -t new_topic

### consume messages 
kcat -b kafka:29092 -t new_topic


---


## confluentinc examples repo
https://github.com/confluentinc/examples


## confluentinc demo-scene repo
https://github.com/confluentinc/demo-scene/blob/master/build-a-streaming-pipeline/docker-compose.yml


---

## S3 source connectors alternatives
https://dzone.com/articles/reading-aws-s3-file-content-to-kafka-topic

https://gist.github.com/mlazzarini/5a445bcd98af2ba7a285ec20ba086c95

https://github.com/adobe/kafka-connect-s3

https://github.com/instaclustr/kafka-connect-connectors

https://github.com/OneCricketeer/kafka-connect-sandbox/blob/master/sources/s3-minio-binary-backup.json
