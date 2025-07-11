FROM mongo

COPY participants.json /participants.json
COPY studies.json /studies.json
COPY users.json /users.json


CMD mongoimport --host mongo --db card_sorter --authenticationDatabase admin --username rest_api --password password --collection participants --type json --file /participants.json --jsonArray && mongoimport --host mongo --db card_sorter --authenticationDatabase admin --username rest_api --password password --collection studies --type json --file /studies.json --jsonArray && mongoimport --host mongo --db card_sorter --authenticationDatabase admin --username rest_api --password password --collection users --type json --file /users.json --jsonArray
