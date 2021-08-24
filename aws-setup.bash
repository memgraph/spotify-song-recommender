mkdir kafka
cd kafka
curl "https://downloads.apache.org/kafka/2.6.2/kafka_2.13-2.6.2.tgz" -o kafka.tgz
tar -xvzf kafka.tgz --strip 1
rm kafka.tgz
sudo apt-get update
sudo apt-get install zookeeperd vim
sudo adduser --system --no-create-home --disabled-password --disabled-login kafka
sudo vim /etc/systemd/system/zookeeper.service
sudo vim /etc/systemd/system/kafka.service
sudo systemctl daemon-reload
sudo mkdir /var/lib/kafka
sudo mkdir /var/lib/kafka/data
sudo echo "delete.topic.enable = true" >> config/server.properties
sudo echo "log.dirs=/var/lib/kafka/data" >> config/server.properties
sudo echo "listeners=PLAINTEXT://ec2-34-245-33-31.eu-west-1.compute.amazonaws.com:9092" >> config/server.properties
sudo echo "advertised.listeners=PLAINTEXT://ec2-34-245-33-31.eu-west-1.compute.amazonaws.com:9092" >> config/server.properties
sudo chown -R kafka:nogroup ~/kafka
sudo chown -R kafka:nogroup /var/lib/kafka
sudo ~/kafka/bin/kafka-server-start.sh ~/kafka/config/server.properties
~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic spotify
