import json
import logging

def lambda_handler(event, context):
    # Set up a logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Get the custom message from the event
    custom_message = event["message"]

    # Write the custom message to the logs
    logger.info(custom_message)
    return {"message": f"{custom_message} written to CloudWatch Logs"}


## Lambda test event code

{
  "message": "Your custom message here"
}
