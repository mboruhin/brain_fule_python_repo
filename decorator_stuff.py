class ShippingContainer:

    next_serial = 1337

    @staticmethod
    def _generate_serial():
        result = ShippingContainer.next_serial
        ShippingContainer.next_serial += 1
        return result
    # or:
    # @classmethod
    # def _generate_serial(cls):
    #     result = cls.next_serial
    #     cls.next_serial += 1
    #     return result

    @classmethod
    def my_class_method(cls, message):
        cls.attr = message


