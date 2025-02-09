from src.utils.config import load_farmers
from src.messaging.farmer_sms import send_farmer_sms
from src.models.yield_predictor import predict_yield
from src.utils.log_formatter import setup_pretty_logging
import logging

# Setup pretty logging
setup_pretty_logging()

def execute_sms_pipeline():
    """Execute the SMS pipeline to generate and send predictions to farmers."""
    logger = logging.getLogger(__name__)
    logger.info("Starting SMS pipeline execution")
    
    try:
        farmers = load_farmers()
        logger.info(f"Loaded {len(farmers)} farmers from database")
        
        successful_sends = 0
        failed_sends = 0
        
        for farmer in farmers:
            try:
                prediction = predict_yield(farmer)
                if prediction:
                    success = send_farmer_sms(
                        prediction=prediction,
                        area_hectares=farmer.area_hectares,
                        phone_number=farmer.phone_number
                    )
                    if success:
                        successful_sends += 1
                        logger.info(f"Successfully sent prediction for farm area {farmer.area_hectares} hectares")
                    else:
                        failed_sends += 1
                        logger.error(f"Failed to send prediction for farm area {farmer.area_hectares} hectares")
            except Exception as farm_error:
                logger.error(f"Error processing farm data: {str(farm_error)}")
                failed_sends += 1
                continue
                    
        logger.info(f"SMS Pipeline completed. Successful: {successful_sends}, Failed: {failed_sends}")
            
    except Exception as e:
        logger.error(f"Critical error in SMS pipeline: {str(e)}")
        raise

if __name__ == "__main__":
    execute_sms_pipeline()

    