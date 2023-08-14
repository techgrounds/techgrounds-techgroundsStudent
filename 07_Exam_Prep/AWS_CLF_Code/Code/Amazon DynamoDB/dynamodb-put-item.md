aws dynamodb put-item --table-name Movies --item '{"Title": {"S": "The Godfather"}, "Year": {"S": "1972"}, "Rating": {"N": "9.2"}}'

aws dynamodb put-item --table-name Movies --item '{"Title": {"S": "The Dark Night"}, "Year": {"S": "2008"}, "Rating": {"N": "9.0"}}'

aws dynamodb put-item --table-name Movies --item '{"Title": {"S": "Pulp Fiction"}, "Year": {"S": "1994"}, "Rating": {"N": "8.8"}}'
                            
aws dynamodb put-item --table-name Movies --item '{"Title": {"S": "Top Gun: Maverick"}, "Year": {"S": "2022"}, "Rating": {"N": "8.2"}}'