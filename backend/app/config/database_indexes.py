import logging
from motor.motor_asyncio import AsyncIOMotorDatabase

logger = logging.getLogger(__name__)

async def create_log_view_indexes(database: AsyncIOMotorDatabase):
    """
    Membuat index untuk koleksi log_views di MongoDB.
    Index ini digunakan untuk mempercepat pencarian dan pengurutan data berdasarkan field tertentu.
    """
    try:
        # Index untuk timestamp-based queries (recent views, time-based analytics)
        await database.log_views.create_index([("timestamp", 1)])
        logger.info("Created index on timestamp field in log_views collection")

        # Compound index untuk query applier spesifik, sorted by time
        await database.log_views.create_index([("applier_id", 1), ("timestamp", -1)])
        logger.info("Created compound index on applier_id and timestamp fields in log_views collection")

        # Compound index untuk query job spesifik, sorted by time
        await database.log_views.create_index([("job_id", 1), ("timestamp", -1)])
        logger.info("Created compound index on job_id and timestamp fields in log_views collection")

        # Compound index untuk query applier dan job spesifik
        await database.log_views.create_index([("applier_id", 1), ("job_id", 1)])
        logger.info("Created compound index on applier_id and job_id fields in log_views collection")

        logger.info("All indexes created successfully for log_views collection")
    except Exception as e:
        logger.error(f"Error creating indexes for log_views collection: {str(e)}")
        raise