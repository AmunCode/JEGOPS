import json
from website import models


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
                 f_cracks=None, r_cracks=None, spotting=None, markings=None, grade=None, battery_life=0):
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
                f_cracks: str, optional
                    devices front has cracks (default is None)
                r_cracks: str, optional
                    device rear has cracks (default is None)
                spotting: str optional
                    device has spotting on the casing (default  is None)
                markings bool, optional
                    device has markings (default is None)
                grade: str, optional
                    the cosmetic grade attributed to the device (default is None)

                :return None
        """
        self.imei = imei  # serial number
        self.battery_condition = battery_life
        self.scratch_condition = scratches  # negligible, light, deep
        self.dent_condition = dents  # none, small, deep
        self.lcd_discolored = lcd_discoloration  # Boolean
        self.missing_parts = missing_parts  # Boolean
        self.f_cracked = f_cracks  # String
        self.r_cracked = r_cracks  # String
        self.spotting = spotting  # string
        self.marked = markings  # Boolean
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
            "front cracked": self.f_cracked,
            "rear cracked": self.r_cracked,
            "spotting":self.spotting,
            "markings": self.marked,
            "grade": self.grade
        }
        return phone_stats


class Obj:
    def __init__(self, dict1):
        self.__dict__.update(dict1)


def dict2obj(dict1):
    return json.loads(json.dumps(dict1), object_hook=Obj)


def sql_prep(test_result: dict):
    new_phone_entry = models.Result(
        Cos_tester_name=test_result['cos_tester'],
        Scratches=test_result['scratches'],
        Dents=test_result['dents'],
        LcdDiscoloration=test_result['lcd_discoloration'],
        ComponentsMissing=test_result['components_missing'],
        FrontCrack=test_result['front_cracks'],
        RearCrack=test_result['rear_cracks'],
        Markings=test_result['markings'],
        Spotting=test_result['spotting'],
        A4ReportLink=test_result['A4ReportLink'],
        A4Reports=test_result['A4Reports'],
        AppVersion=test_result['AppVersion'],
        AppleID=test_result['AppleID'],
        AvgBatteryTemperature=test_result['AvgBatteryTemperature'],
        BMic=test_result['BMic'],
        BatterChargeEnd=test_result['BatterChargeEnd'],
        BatteryChargeStart=test_result['BatteryChargeStart'],
        BatteryCurrentMaxCapacity=test_result['BatteryCurrentMaxCapacity'],
        BatteryCycle=test_result['BatteryCycle'],
        BatteryDesignMaxCapacity=test_result['BatteryDesignMaxCapacity'],
        BatteryDrain=test_result['BatteryDrain'],
        BatteryDrainDuration=test_result['BatteryDrainDuration'],
        BatteryDrainInfo=test_result['BatteryDrainInfo'],
        BatteryDrainType=test_result['BatteryDrainType'],
        BatteryHealthGrade=test_result['BatteryHealthGrade'],
        BatteryHealthPercentage=test_result['BatteryHealthPercentage'],
        BatteryModel=test_result['BatteryModel'],
        BatteryPercentage=test_result['BatteryPercentage'],
        BatteryResistance=test_result['BatteryResistance'],
        BatterySerial=test_result['BatterySerial'],
        BatterySource=test_result['BatterySource'],
        BatteryTemperature=test_result['BatteryTemperature'],
        BoxNo=test_result['BoxNo'],
        BuildNo=test_result['BoxNo'],
        Carrier=test_result['Carrier'],
        CarrierLockResponse=test_result['CarrierLockResponse'],
        CocoBatteryHealth=test_result['CocoBatteryHealth'],
        CocoCurrentCapacity=test_result['CocoCurrentCapacity'],
        CocoDesignCapacity=test_result['CocoDesignCapacity'],
        Color=test_result['Color'],
        CompatibleSim=test_result['CompatibleSim'],
        Cosmetics=test_result['Cosmetics'],
        CosmeticsFailed=test_result['CosmeticsFailed'],
        CosmeticsPassed=test_result['CosmeticsPassed'],
        CosmeticsPending=test_result['CosmeticsPending'],
        CosmeticsSettings=str(test_result['CosmeticsSettings']),
        CosmeticsWorking=test_result['CosmeticsWorking'],
        CountryOfOrigin=test_result['CountryOfOrigin'],
        CreatedAPITimeStamp=test_result['CreatedAPITimeStamp'],
        CreatedTimeStamp=test_result['CreatedTimeStamp'],
        Custom1=test_result['Custom1'],
        DecimalMEID=test_result['DecimalMEID'],
        DecimalMEID2=test_result['DecimalMEID2'],
        DefectsCode=test_result['DefectsCode'],
        DeviceCreatedDate=test_result['DeviceCreatedDate'],
        DeviceLock=test_result['DeviceLock'],
        DeviceState=test_result['DeviceState'],
        DeviceUpdatedDate=test_result['DeviceUpdatedDate'],
        EID=test_result['EID'],
        ESN=test_result['ESN'],
        ESNResponse=str(test_result['ESNResponse']),
        EndTime=test_result['EndTime'],
        Erased=test_result['Erased'],
        ErrorCode=test_result['ErrorCode'],
        FMic=test_result['FMic'],
        Failed=test_result['Failed'],
        Firmware=test_result['Firmware'],
        Grade=test_result['Grade'],
        GradingResults=test_result['GradingResults'],
        IFT_Codes=test_result['IFT_Codes'],
        IMEI=test_result['IMEI'],
        IMEI2=test_result['IMEI2'],
        InitialCarrier=test_result['InitialCarrier'],
        InvoiceNo=test_result['InvoiceNo'],
        Knox=test_result['Knox'],
        LPN=test_result['LPN'],
        LicenseIdentifier=test_result['LicenseIdentifier'],
        MDM=test_result['MDM'],
        MDMResponse=test_result['MDMResponse'],
        MEID=test_result['MEID'],
        MEID2=test_result['MEID2'],
        Make=test_result['Make'],
        ManualEntry=test_result['ManualEntry'],
        ManualFailure=test_result['ManualFailure'],
        MasterName=test_result['MasterName'],
        MaxBatteryTemperature=test_result['MaxBatteryTemperature'],
        Memory=test_result['Memory'],
        MinBatteryTemperature=test_result['MinBatteryTemperature'],
        Model=test_result['Model'],
        ModelNo=test_result['ModelNo'],
        Network=test_result['Network'],
        Network1=test_result['Network1'],
        Network2=test_result['Network2'],
        NotCompatibleSim=test_result['NotCompatibleSim'],
        Notes=test_result['Notes'],
        OEMBatteryHealth=test_result['OEMBatteryHealth'],
        OS=test_result['OS'],
        PESN=test_result['PESN'],
        PESN2=test_result['PESN2'],
        PackageName=test_result['PackageName'],
        Parts=test_result['Parts'],
        Passed=test_result['Passed'],
        Pending=test_result['Pending'],
        PortNumber=test_result['PortNumber'],
        ProductCode=test_result['ProductCode'],
        QTY=test_result['QTY'],
        Ram=test_result['Ram'],
        RegulatoryModelNumber=test_result['RegulatoryModelNumber'],
        RestoreCode=test_result['RestoreCode'],
        Rooted=test_result['Rooted'],
        SIM1MCC=test_result['SIM1MCC'],
        SIM1MNC=test_result['SIM1MNC'],
        SIM1Name=test_result['SIM1Name'],
        SIM2MCC=test_result['SIM2MCC'],
        SIM2MNC=test_result['SIM2MNC'],
        SIM2Name=test_result['SIM2Name'],
        SIMSERIAL=test_result['SIMSERIAL'],
        SIMSERIAL2=test_result['SIMSERIAL2'],
        SKUCode=test_result['SKUCode'],
        ScreenTime=test_result['ScreenTime'],
        Serial=test_result['Serial'],
        SimErased=test_result['SimErased'],
        SimHistory=test_result['SimHistory'],
        SimLock=test_result['SimLock'],
        SimLockResponse=test_result['SimLockResponse'],
        SimTechnology=test_result['SimTechnology'],
        StartTime=test_result['StartTime'],
        StationID=test_result['StationID'],
        TestPlanName=test_result['TestPlanName'],
        TesterName=test_result['TesterName'],
        TransactionID=test_result['TransactionID'],
        Type=test_result['Type'],
        UDID=test_result['UDID'],
        UnlockStatus=test_result['UnlockStatus'],
        UpdatedAPITimeStamp=test_result['UpdatedAPITimeStamp'],
        UpdatedTimeStamp=test_result['UpdatedTimeStamp'],
        VMic=test_result['VMic'],
        VendorName=test_result['VendorName'],
        Version=test_result['Version'],
        WareHouse=test_result['WareHouse'],
        WifiMacAddress=test_result['WifiMacAddress'],
        Working=test_result['Working'],
        androidCarrierId=test_result['androidCarrierId'],
        checkall=test_result['checkall'],
        deviceDisconnect=test_result['deviceDisconnect'],
        device_shutdown=test_result['device_shutdown'],
        eBayRefurbished=test_result['eBayRefurbished'],
        eBayRejection=test_result['eBayRejection'],
        endHeat=test_result['endHeat'],
        erasedNotes=test_result['erasedNotes'],
        erasedSD=test_result['erasedSD'],
        erasureReportLink=test_result['erasureReportLink'],
        esim_erased=test_result['esim_erased'],
        esim_present=test_result['esim_present'],
        final_price=test_result['final_price'],
        gradePerformed=test_result['gradePerformed'],
        grade_profile_id=test_result['grade_profile_id'],
        grade_route_id=test_result['grade_route_id'],
        iCloudInfo=test_result['iCloudInfo'],
        isCloudTransaction=test_result['isCloudTransaction'],
        isLabelPrint=test_result['isLabelPrint'],
        master_id=test_result['master_id'],
        startHeat=test_result['startHeat'],
        testerDeviceTime=test_result['testerDeviceTime'],
        transaction_type=test_result['transaction_type']
    )
    return new_phone_entry
