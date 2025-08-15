from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info('Starting to build pipeline..')
        loader = AnimeDataLoader('data/anime_with_synopsis.csv', 'data/anime_updated.csv')
        processed_csv = loader.load_and_process()
        logger.info('Data Loaded and processed')
        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_vectorstore()
        logger.info('Vector store build successfully')
        logger.info('Pipeline build successfully')

    except Exception as e:
        logger.error(f'Failed to execute pipeline {str(e)}')
        raise CustomException('Error during pipeline', e)



if __name__ == '__main__':
    main()