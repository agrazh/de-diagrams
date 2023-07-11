

Console tools: `kafka-topics`, `kafka-console-producer`, `kafka-console-consumer` 


2. Create/delete topic with 3 partitions & RF = 2

```bash
$ /usr/bin/kafka-topics --create \
  --bootstrap-server kafka1:19092 \
  --replication-factor 2 --partitions 3 \
  --topic orders-w-bigtasty-eas011-ag

$ /usr/bin/kafka-topics --delete \
  --bootstrap-server kafka1:19092 \
  --topic orders-w-bigtasty-eas011-ag
```

3. Describe (check the ISR), send message

```bash
$ /usr/bin/kafka-topics --describe \
  --bootstrap-server kafka1:19092 \
  --topic orders-w-bigtasty-eas011-ag

# Push messages to the topic
$ /usr/bin/kafka-console-producer \
  --bootstrap-server kafka1:19092 \
  --topic orders-w-bigtasty-eas011-ag

# Simply pull all messages from the topic
$ /usr/bin/kafka-console-consumer \
  --bootstrap-server kafka1:19092 \
  --topic orders-w-bigtasty-eas011-ag \
  --from-beginning  # remove to get only new messages

# Pull message as a member of consumer group
/usr/bin/kafka-console-consumer \
  --bootstrap-server kafka1:19092 \
  --topic orders-w-bigtasty-eas011-ag \
  --from-beginning
  --group c_group_1
```

4. Organize message writing/reading with order messages keeping (fixed key or 1 partition)

```bash
$ /usr/bin/kafka-topics --create \
  --bootstrap-server kafka1:19092 \
  --replication-factor 2 --partitions 2 \
  --topic bigtasty-ol-eas011-ag

# The default partitioner will use the hash of the key to ensure that all messages for the same key
# go to same partition: Hash(Key) % Number of partitions -> Partition number

$ /usr/bin/kafka-console-producer \
  --bootstrap-server kafka1:19092 \
  --topic bigtasty-ol-eas011-ag \
  --property "parse.key=true" \
  --property "key.separator=:"
> 000:message1  # "000" key guarantees message delivery to partition_0
> 000:message2
> 001:message3  # goes to partition_1

$ /usr/bin/kafka-console-consumer \
  --bootstrap-server kafka1:19092 \
  --topic bigtasty-ol-eas011-ag \
  --partition 0 \
  --property "print.key=true" --property "key.separator=:"
```

5. Organize message writing/reading without order messages keeping and hash partitioning ()

```bash
$ /usr/bin/kafka-topics --create \
  --bootstrap-server kafka1:19092 \
  --replication-factor 2 --partitions 3 \
  --topic bigtasty-ul-eas011-ag

$ /usr/bin/kafka-console-producer \
  --bootstrap-server kafka1:19092 \
  --topic bigtasty-ul-eas011-ag
> message1
> message2
> message3

# Create two consumers in the same group
$ /usr/bin/kafka-console-consumer \
--bootstrap-server kafka1:19092 \
--topic bigtasty-ul-eas011-ag \
--group c-group-1
```

6. Organize message writing/reading without skew data (null key)

```bash
# This producer guarantees that keys are not NULL (?) 
$ /usr/bin/kafka-console-producer \
  --bootstrap-server kafka1:19092 \
  --topic bigtasty-ol-eas011-ag \
  --property "parse.key=true" \
  --property "key.separator=:"
```

7. Read messages from the start, end and offset (/usr/bin/kafka-console-consumer --help)

```bash
$ /usr/bin/kafka-consumer-groups \
  --bootstrap-server kafka1:19092 \
  --group c-group-1 \
  --describe

$ /usr/bin/kafka-consumer-groups \
  --bootstrap-server kafka1:19092 \
  --group c-group-1 \
  --topic bigtasty-ul-eas011-ag \
  --reset-offsets \ 
  --to-earliest \  # --to-lates , --to-offset 5
  --execute
```

8. Read topic with 2 partitions with 2 consumers in one consumer group and different consumer group

```bash
$ /usr/bin/kafka-topics --create \
  --bootstrap-server kafka1:19092 \
  --replication-factor 2 --partitions 3 \
  --topic bigtasty-ul-eas011-ag

$ /usr/bin/kafka-console-producer \
  --bootstrap-server kafka1:19092 \
  --topic bigtasty-ul-eas011-ag
> message1
> message2
> message3

# Create two consumers in the c-group-1
$ /usr/bin/kafka-console-consumer \
--bootstrap-server kafka1:19092 \
--topic bigtasty-ul-eas011-ag \
--group c-group-1

# Create one consumers in the c-group-2
$ /usr/bin/kafka-console-consumer \
--bootstrap-server kafka1:19092 \
--topic bigtasty-ul-eas011-ag \
--group c-group-2

# Or I didn't understand the question
```

9. Choose optimal number of consumers for reading topic with 4 partitions

```bash
4 consumers - one per partition (?)
```

10. Write messages with min latency

```bash
/usr/bin/kafka-console-producer \
  --bootstrap-server kafka1:19092 \
  --topic bigtasty-ul-eas011-ag \
  --compression-codec snappy 
```

11. Write messages with max compression max throughput

```bash
# we can increase the number of partitions
/usr/bin/kafka-topics --alter \
  --bootstrap-server kafka1:19092 \
  --partitions 3 \
  --topic bigtasty-ol-eas011-ag

/usr/bin/kafka-topics --describe \
  --bootstrap-server kafka1:19092 \
  --topic bigtasty-ol-eas011-ag

/usr/bin/kafka-console-producer \
  --bootstrap-server kafka1:19092 \
  --topic bigtasty-ul-eas011-ag \
  --compression-codec lz4
```
