import json


class Phone:
    """
    A class used to represent a phone

    ...

    Attributes
    ----------
    imei : str
        serial number of the device
    scratches : str
        the degree of scratches on a device (default is None)
    dents : str
        the degree of dents on a device (default is None)
    lcd_discoloration: bool
        device lcd discolored (default is None)
    missing_parts: bool
        device is missing parts (default is None)
    cracks: bool
        devices has cracks (default is None)
    markings: bool
        device has markings (default is None)
    grade: str
        the cosmetic grade attributed to the device (default is None)

    Methods
    -------
    cosmetic_report(sound=None)
        Prints the cosmetic attributes of the phone
    """
    def __init__(self, imei, scratches=None, dents=None, lcd_discoloration=None, missing_parts=None,
                 cracks=None, markings=None, grade=None, battery_life=0):
        """
            Constructs all the necessary attributes for the phone object.

            Parameters
            ----------
                imei : str
                    serial number of the device
                battery_life: float
                    the battery life of the device
                scratches : str, optional
                    the degree of scratches on a device (default is None)
                dents : str, optional
                    the degree of dents on a device (default is None)
                lcd_discoloration: bool, optional
                    device lcd discolored (default is None)
                missing_parts: bool, optional
                    device is missing internal or external parts (default is None)
                cracks: bool, optional
                    devices has cracks (default is None)
                markings bool, optional
                    device has markings (default is None)
                grade: str, optional
                    the cosmetic grade attributed to the device (default is None)

                :return None
        """
        self.imei = imei                                  # serial number
        self.battery_condition = battery_life
        self.scratch_condition = scratches                # negligible, light, deep
        self.dent_condition = dents                       # none, small, deep
        self.lcd_discolored = lcd_discoloration           # Boolean
        self.missing_parts = missing_parts                # Boolean
        self.cracked = cracks                             # Boolean
        self.marked = markings                            # Boolean
        self.grade = grade

    def cosmetic_report(self):
        """
            fills a dictionary with phone attributes

        :return:
            phone_stats: dict
                a dictionary with phone's attributes
        """
        phone_stats = {
            "imei": self.imei,
            "battery": self.battery_condition,
            "scratches": self.scratch_condition,
            "dents": self.dent_condition,
            "lcd discolored": self.lcd_discolored,
            "components": self.missing_parts,
            "cracked": self.cracked,
            "markings": self.marked,
            "grade": self.grade
        }
        return phone_stats


class Obj:
    def __init__(self, dict1):
        self.__dict__.update(dict1)


def dict2obj(dict1):
    return json.loads(json.dumps(dict1), object_hook=Obj)
