from flask import current_app

class RedisRecord(object):
    KEY = 'GUSEST_LIST'
    EXPIRY = 48 * 60 * 60  # in seconds

    def __init__(self):
        self.redis_client = current_app.redis_client

    def _get_key_name(self):
        return self.KEY

    def is_sent(self, event, objectid):
        return self.redis_client.exists(
            self._get_key_name()
        )

    def get_value(self):
        try:
            return self.redis_client.get(self._get_key_name())
        except Exception as err:
            print ("Error {err} in connecting redis to get value".format(err=err))
            current_app.logger.error("Error {err} in connecting redis to get value".format(err=err))
            raise Exception()

    def set_value(self, value):
        try:
            self.redis_client.setex(
                self._get_key_name(),
                value, self.EXPIRY
            )
        except Exception as err:
            print ("Error {err} in connecting redis to set value".format(err=err))
            current_app.logger.error("Error {err} in connecting redis to set value".format(err=err))
            raise Exception()

    def clear_sent(self):
        self.redis_client.delete(
            self._get_key_name()
        )
