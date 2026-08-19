import json
import logging
import boto3
from botocore.exceptions import ClientError

# Configure logging to CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Python Lambda handler for SQS events.
    This function is triggered automatically when a message arrives in the SQS queue.
    """
    logger.info(f"Received event: {json.dumps(event)}")
    
    # SQS sends a list of records. We process them in a batch.
    for record in event['Records']:
        try:
            body = json.loads(record['body'])
            sku = body.get('sku')
            quantity = body.get('quantity')
            
            # Simulate database update logic
            logger.info(f"Processing inventory update: SKU={sku}, Qty={quantity}")
            
            # Simulate a blocker or error for demonstration
            if quantity < 0:
                raise ValueError("Invalid quantity: cannot be negative")
                
            logger.info(f"Successfully processed SKU {sku}")
            
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse JSON: {e}")
            raise e # Re-raise to trigger DLQ (Dead Letter Queue)
        except Exception as e:
            logger.error(f"Processing error: {e}")
            raise e

    return {
        'statusCode': 200,
        'body': json.dumps('Batch processed successfully')
    }
