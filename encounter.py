import json

import psycopg2
from flask import request
from flask_httpauth import HTTPBasicAuth
from flask_restful import Resource
from errorcapture import mail
from datetime import datetime

from common.db_conn import con

auth = HTTPBasicAuth()
API_AUTH={"salesforce_auth":"ampersandhealth"}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return API_AUTH.get(username) == password

class Encounter(Resource):
    @auth.login_required
    def post(self):
        try:
            item = json.loads(request.data)
            for k,v in item.items():
                # print type(v)
                if type(v) == unicode:
                    # print v
                    v = str(v).replace("'","''")
                    item[k] = v
            print item["Id"]
            item["Type"] = item["attributes"]["type"]
            # select_query = "select * from sf_contact where \"Id\"='" + item["Id"] + "'";
            # delete_query = "delete from sf_contact where \"Id\"='" + item["Id"] + "'";SELECT                                                                                                                            "CreatedById", "CreatedDate", "Encounter_End_Date__c", "Encounter_Start_Date__c", "HealthCloudGA__Account__c", "HealthCloudGA__Class__c", "HealthCloudGA__Encounter__c", "HealthCloudGA__HospitalAdmitSourceLabel__c", "HealthCloudGA__HospitalizationOrigin__c", "HealthCloudGA__HospitalizationPreAdmissionId__c",                        "HealthCloudGA__HospitalizeAdmitSourceCode__c", "HealthCloudGA__HospitalizeAdmitSourceSystem__c", "HealthCloudGA__HospitalizeDestination__c", "HealthCloudGA__HospitalizeDietCode__c", "HealthCloudGA__HospitalizeDietLabel__c", "HealthCloudGA__HospitalizeDietSystem__c", "HealthCloudGA__HospitalizeDischargeDiagnosis__c", "HealthCloudGA__HospitalizeDischargeDispositionCode__c", "HealthCloudGA__HospitalizeDischargeDispositionSystem__c", "HealthCloudGA__HospitalizeDischargeDispostionLabel__c", "HealthCloudGA__HospitalizeOrigin__c", "HealthCloudGA__HospitalizePeriodEnd__c", "HealthCloudGA__HospitalizePeriodStart__c",                          "HealthCloudGA__HospitalizePreAdmissionId__c", "HealthCloudGA__HospitalizeReadmission__c", "HealthCloudGA__HospitalizeSpecialArrangementCode__c", "HealthCloudGA__HospitalizeSpecialArrangementLabel__c", "HealthCloudGA__HospitalizeSpecialArrangementSystem__c",            "HealthCloudGA__HospitalizeSpecialCourtesyCode__c", "HealthCloudGA__HospitalizeSpecialCourtesyLabel__c", "HealthCloudGA__HospitalizeSpecialCourtesySystem__c", "HealthCloudGA__Indication__c", "HealthCloudGA__IsRestricted__c", "HealthCloudGA__IsVisibleOnPatientCard__c",        "HealthCloudGA__LastEncounter__c", "HealthCloudGA__LengthUnit__c", "HealthCloudGA__LengthValue__c", "HealthCloudGA__Location1City__c", "HealthCloudGA__Location1Country__c", "HealthCloudGA__Location1Description__c", "HealthCloudGA__Location1EndDate__c", "HealthCloudGA__Location1Id__c",                     "HealthCloudGA__Location1Line1__c", "HealthCloudGA__Location1Line2__c", "HealthCloudGA__Location1Name__c", "HealthCloudGA__Location1PostalCode__c", "HealthCloudGA__Location1StartDate__c", "HealthCloudGA__Location1State__c", "HealthCloudGA__Location1TelecomPeriodEnd__c", "HealthCloudGA__Location1TelecomPeriodStart__c", "HealthCloudGA__Location1TelecomSystem__c", "HealthCloudGA__Location1TelecomUse__c", "HealthCloudGA__Location1TelecomValue__c", "HealthCloudGA__Location1Text__c",                           "HealthCloudGA__Location1TypeCode__c", "HealthCloudGA__Location1TypeLabel__c", "HealthCloudGA__Location1TypeSystem__c", "HealthCloudGA__Location1Type__c", "HealthCloudGA__Location1Use__c", "HealthCloudGA__Location2City__c", "HealthCloudGA__Location2Country__c", "HealthCloudGA__Location2Description__c", "HealthCloudGA__Location2EndDate__c", "HealthCloudGA__Location2Id__c", "HealthCloudGA__Location2Line1__c", "HealthCloudGA__Location2Line2__c",                             "HealthCloudGA__Location2Name__c", "HealthCloudGA__Location2PostalCode__c", "HealthCloudGA__Location2StartDate__c", "HealthCloudGA__Location2State__c", "HealthCloudGA__Location2TelecomPeriodEnd__c", "HealthCloudGA__Location2TelecomPeriodStart__c", "HealthCloudGA__Location2TelecomSystem__c", "HealthCloudGA__Location2TelecomUse__c", "HealthCloudGA__Location2TelecomValue__c", "HealthCloudGA__Location2Text__c", "HealthCloudGA__Location2TypeCode__c", "HealthCloudGA__Location2TypeLabel__c",                 "HealthCloudGA__Location2TypeSystem__c", "HealthCloudGA__Location2Type__c", "HealthCloudGA__Location2Use__c", "HealthCloudGA__Location3City__c", "HealthCloudGA__Location3Country__c", "HealthCloudGA__Location3Description__c", "HealthCloudGA__Location3EndDate__c", "HealthCloudGA__Location3Id__c", "HealthCloudGA__Location3Line1__c",                      "HealthCloudGA__Location3Line2__c", "HealthCloudGA__Location3Name__c", healthcloudga__location3postalcode__c, "HealthCloudGA__Location3StartDate__c", "HealthCloudGA__Location3State__c", "HealthCloudGA__Location3TelecomPeriodEnd__c", "HealthCloudGA__Location3TelecomPeriodStart__c", "HealthCloudGA__Location3TelecomSystem__c", "HealthCloudGA__Location3TelecomUse__c",                   "HealthCloudGA__Location3TelecomValue__c", "HealthCloudGA__Location3Text__c", "HealthCloudGA__Location3TypeCode__c", "HealthCloudGA__Location3TypeLabel__c", "HealthCloudGA__Location3TypeSystem__c", "HealthCloudGA__Location3Type__c", "HealthCloudGA__Location3Use__c", "HealthCloudGA__Location4City__c", "HealthCloudGA__Location4Country__c", "HealthCloudGA__Location4Description__c", "HealthCloudGA__Location4EndDate__c", "HealthCloudGA__Location4Id__c", "HealthCloudGA__Location4Line1__c",                         healthcloudga__location4line2__c, "HealthCloudGA__Location4Name__c", "HealthCloudGA__Location4PostalCode__c", "HealthCloudGA__Location4StartDate__c", "HealthCloudGA__Location4State__c", "HealthCloudGA__Location4TelecomPeriodEnd__c", "HealthCloudGA__Location4TelecomPeriodStart__c", "HealthCloudGA__Location4TelecomSystem__c",                        "HealthCloudGA__Location4TelecomUse__c", "HealthCloudGA__Location4TelecomValue__c", "HealthCloudGA__Location4Text__c", "HealthCloudGA__Location4TypeCode__c", "HealthCloudGA__Location4TypeLabel__c", "HealthCloudGA__Location4TypeSystem__c", "HealthCloudGA__Location4Type__c", "HealthCloudGA__Location4Use__c", "HealthCloudGA__Location5City__c", "HealthCloudGA__Location5Country__c", "HealthCloudGA__Location5Description__c", "HealthCloudGA__Location5EndDate__c", "HealthCloudGA__Location5Id__c", "HealthCloudGA__Location5Line1__c", "HealthCloudGA__Location5Line2__c",                            "HealthCloudGA__Location5Name__c", "HealthCloudGA__Location5PostalCode__c", "HealthCloudGA__Location5StartDate__c",           "HealthCloudGA__Location5TelecomPeriodStart__c", "HealthCloudGA__Location5TelecomSystem__c", "HealthCloudGA__Location5TelecomUse__c", "HealthCloudGA__Location5TelecomValue__c", "HealthCloudGA__Location5Text__c", "HealthCloudGA__Location5TypeCode__c", "HealthCloudGA__Location5TypeLabel__c", "HealthCloudGA__Location5TypeSystem__c", "HealthCloudGA__Location5Type__c",                  "HealthCloudGA__Location5Use__c", "HealthCloudGA__Patient__c", "HealthCloudGA__PeriodEnd__c", "HealthCloudGA__PeriodStart__c", "HealthCloudGA__PriorityCode__c", "HealthCloudGA__PriorityLabel__c", "HealthCloudGA__PrioritySystem__c", "HealthCloudGA__Priority__c",             "HealthCloudGA__ReasonCode__c", "HealthCloudGA__ReasonLabel__c", "HealthCloudGA__ReasonSystem__c", "HealthCloudGA__ServiceProvider__c", "HealthCloudGA__SourceSystemId__c", "HealthCloudGA__SourceSystemModified__c", "HealthCloudGA__SourceSystem__c",              "HealthCloudGA__Status__c", "HealthCloudGA__TypeCode__c", "HealthCloudGA__TypeLabel__c", "Id", "IsDeleted", "LastActivityDate", "LastModifiedById", "LastModifiedDate", "LastReferencedDate", "LastViewedDate", "Name", "OwnerId",                          "RecordTypeId", "SystemModstamp", "Care_Plan__c", "RecordTypeIdText__c", updated_date, "HealthCloudGA__TypeSystem__c", "HealthCloudGA__Location5State__c", "HealthCloudGA__Location5TelecomPeriodEnd__c"

            insert_query = "insert into \"sf_ehr_encounter\" select * from json_populate_record(null::\"sf_ehr_encounter\",'" + json.dumps(item) + "') ON CONFLICT ON CONSTRAINT ehr_encounter_pkey DO UPDATE SET( \"CreatedById\", \"CreatedDate\", \"Encounter_End_Date__c\", \"Encounter_Start_Date__c\", \"HealthCloudGA__Account__c\", \"HealthCloudGA__Class__c\", \"HealthCloudGA__Encounter__c\", \"HealthCloudGA__HospitalAdmitSourceLabel__c\", \"HealthCloudGA__HospitalizationOrigin__c\", \"HealthCloudGA__HospitalizationPreAdmissionId__c\", \"HealthCloudGA__HospitalizeAdmitSourceCode__c\", \"HealthCloudGA__HospitalizeAdmitSourceSystem__c\", \"HealthCloudGA__HospitalizeDestination__c\", \"HealthCloudGA__HospitalizeDietCode__c\", \"HealthCloudGA__HospitalizeDietLabel__c\", \"HealthCloudGA__HospitalizeDietSystem__c\", \"HealthCloudGA__HospitalizeDischargeDiagnosis__c\", \"HealthCloudGA__HospitalizeDischargeDispositionCode__c\", \"HealthCloudGA__HospitalizeDischargeDispositionSystem__c\", \"HealthCloudGA__HospitalizeDischargeDispostionLabel__c\", \"HealthCloudGA__HospitalizeOrigin__c\", \"HealthCloudGA__HospitalizePeriodEnd__c\", \"HealthCloudGA__HospitalizePeriodStart__c\", \"HealthCloudGA__HospitalizePreAdmissionId__c\", \"HealthCloudGA__HospitalizeReadmission__c\", \"HealthCloudGA__HospitalizeSpecialArrangementCode__c\", \"HealthCloudGA__HospitalizeSpecialArrangementLabel__c\", \"HealthCloudGA__HospitalizeSpecialArrangementSystem__c\", \"HealthCloudGA__HospitalizeSpecialCourtesyCode__c\", \"HealthCloudGA__HospitalizeSpecialCourtesyLabel__c\", \"HealthCloudGA__HospitalizeSpecialCourtesySystem__c\", \"HealthCloudGA__Indication__c\", \"HealthCloudGA__IsRestricted__c\", \"HealthCloudGA__IsVisibleOnPatientCard__c\", \"HealthCloudGA__LastEncounter__c\", \"HealthCloudGA__LengthUnit__c\", \"HealthCloudGA__LengthValue__c\", \"HealthCloudGA__Location1City__c\", \"HealthCloudGA__Location1Country__c\", \"HealthCloudGA__Location1Description__c\", \"HealthCloudGA__Location1EndDate__c\", \"HealthCloudGA__Location1Id__c\", \"HealthCloudGA__Location1Line1__c\", \"HealthCloudGA__Location1Line2__c\", \"HealthCloudGA__Location1Name__c\", \"HealthCloudGA__Location1PostalCode__c\", \"HealthCloudGA__Location1StartDate__c\", \"HealthCloudGA__Location1State__c\", \"HealthCloudGA__Location1TelecomPeriodEnd__c\", \"HealthCloudGA__Location1TelecomPeriodStart__c\", \"HealthCloudGA__Location1TelecomSystem__c\", \"HealthCloudGA__Location1TelecomUse__c\", \"HealthCloudGA__Location1TelecomValue__c\", \"HealthCloudGA__Location1Text__c\", \"HealthCloudGA__Location1TypeCode__c\", \"HealthCloudGA__Location1TypeLabel__c\", \"HealthCloudGA__Location1TypeSystem__c\", \"HealthCloudGA__Location1Type__c\", \"HealthCloudGA__Location1Use__c\", \"HealthCloudGA__Location2City__c\", \"HealthCloudGA__Location2Country__c\", \"HealthCloudGA__Location2Description__c\", \"HealthCloudGA__Location2EndDate__c\", \"HealthCloudGA__Location2Id__c\", \"HealthCloudGA__Location2Line1__c\", \"HealthCloudGA__Location2Line2__c\", \"HealthCloudGA__Location2Name__c\", \"HealthCloudGA__Location2PostalCode__c\", \"HealthCloudGA__Location2StartDate__c\", \"HealthCloudGA__Location2State__c\", \"HealthCloudGA__Location2TelecomPeriodEnd__c\", \"HealthCloudGA__Location2TelecomPeriodStart__c\", \"HealthCloudGA__Location2TelecomSystem__c\", \"HealthCloudGA__Location2TelecomUse__c\", \"HealthCloudGA__Location2TelecomValue__c\", \"HealthCloudGA__Location2Text__c\", \"HealthCloudGA__Location2TypeCode__c\", \"HealthCloudGA__Location2TypeLabel__c\", \"HealthCloudGA__Location2TypeSystem__c\", \"HealthCloudGA__Location2Type__c\", \"HealthCloudGA__Location2Use__c\", \"HealthCloudGA__Location3City__c\", \"HealthCloudGA__Location3Country__c\", \"HealthCloudGA__Location3Description__c\", \"HealthCloudGA__Location3EndDate__c\", \"HealthCloudGA__Location3Id__c\", \"HealthCloudGA__Location3Line1__c\", \"HealthCloudGA__Location3Line2__c\", \"HealthCloudGA__Location3Name__c\", \"healthcloudga__location3postalcode__c\", \"HealthCloudGA__Location3StartDate__c\", \"HealthCloudGA__Location3State__c\", \"HealthCloudGA__Location3TelecomPeriodEnd__c\", \"HealthCloudGA__Location3TelecomPeriodStart__c\", \"HealthCloudGA__Location3TelecomSystem__c\", \"HealthCloudGA__Location3TelecomUse__c\", \"HealthCloudGA__Location3TelecomValue__c\", \"HealthCloudGA__Location3Text__c\", \"HealthCloudGA__Location3TypeCode__c\", \"HealthCloudGA__Location3TypeLabel__c\", \"HealthCloudGA__Location3TypeSystem__c\", \"HealthCloudGA__Location3Type__c\", \"HealthCloudGA__Location3Use__c\", \"HealthCloudGA__Location4City__c\", \"HealthCloudGA__Location4Country__c\", \"HealthCloudGA__Location4Description__c\", \"HealthCloudGA__Location4EndDate__c\", \"HealthCloudGA__Location4Id__c\", \"HealthCloudGA__Location4Line1__c\", \"healthcloudga__location4line2__c\", \"HealthCloudGA__Location4Name__c\", \"HealthCloudGA__Location4PostalCode__c\", \"HealthCloudGA__Location4StartDate__c\", \"HealthCloudGA__Location4State__c\", \"HealthCloudGA__Location4TelecomPeriodEnd__c\", \"HealthCloudGA__Location4TelecomPeriodStart__c\", \"HealthCloudGA__Location4TelecomSystem__c\", \"HealthCloudGA__Location4TelecomUse__c\", \"HealthCloudGA__Location4TelecomValue__c\", \"HealthCloudGA__Location4Text__c\", \"HealthCloudGA__Location4TypeCode__c\", \"HealthCloudGA__Location4TypeLabel__c\", \"HealthCloudGA__Location4TypeSystem__c\", \"HealthCloudGA__Location4Type__c\", \"HealthCloudGA__Location4Use__c\", \"HealthCloudGA__Location5City__c\", \"HealthCloudGA__Location5Country__c\", \"HealthCloudGA__Location5Description__c\", \"HealthCloudGA__Location5EndDate__c\", \"HealthCloudGA__Location5Id__c\", \"HealthCloudGA__Location5Line1__c\", \"HealthCloudGA__Location5Line2__c\", \"HealthCloudGA__Location5Name__c\", \"HealthCloudGA__Location5PostalCode__c\", \"HealthCloudGA__Location5StartDate__c\", \"HealthCloudGA__Location5TelecomPeriodStart__c\", \"HealthCloudGA__Location5TelecomSystem__c\", \"HealthCloudGA__Location5TelecomUse__c\", \"HealthCloudGA__Location5TelecomValue__c\", \"HealthCloudGA__Location5Text__c\", \"HealthCloudGA__Location5TypeCode__c\", \"HealthCloudGA__Location5TypeLabel__c\", \"HealthCloudGA__Location5TypeSystem__c\", \"HealthCloudGA__Location5Type__c\", \"HealthCloudGA__Location5Use__c\", \"HealthCloudGA__Patient__c\", \"HealthCloudGA__PeriodEnd__c\", \"HealthCloudGA__PeriodStart__c\", \"HealthCloudGA__PriorityCode__c\", \"HealthCloudGA__PriorityLabel__c\", \"HealthCloudGA__PrioritySystem__c\", \"HealthCloudGA__Priority__c\", \"HealthCloudGA__ReasonCode__c\", \"HealthCloudGA__ReasonLabel__c\", \"HealthCloudGA__ReasonSystem__c\", \"HealthCloudGA__ServiceProvider__c\", \"HealthCloudGA__SourceSystemId__c\", \"HealthCloudGA__SourceSystemModified__c\", \"HealthCloudGA__SourceSystem__c\", \"HealthCloudGA__Status__c\", \"HealthCloudGA__TypeCode__c\", \"HealthCloudGA__TypeLabel__c\",\"healthcloudga__typesystem__c\", \"Id\", \"IsDeleted\", \"LastActivityDate\", \"LastModifiedById\", \"LastModifiedDate\", \"LastReferencedDate\", \"LastViewedDate\", \"Name\", \"OwnerId\", \"RecordTypeId\", \"SystemModstamp\", \"Care_Plan__c\", \"RecordTypeIdText__c\", \"HealthCloudGA__Location5State__c\", \"HealthCloudGA__Location5TelecomPeriodEnd__c\",\"updated_date\",\"corporate_visit_id\")=(select * from json_populate_record(null::\"sf_ehr_encounter\",'" + json.dumps(item) + "'))";
            cur = con.cursor()
            # cur.execute(select_query)
            # if (bool(cur.rowcount)):
            #     print "delete"
            #     print delete_query
            #     cur.execute(delete_query);
            #     con.commit()

            print insert_query
            cur.execute(insert_query);
            con.commit()
            Tablename = "sf_ehr_encounter"
            updated_date = datetime.now()

            moniter_query = """INSERT INTO "process_monitor" (table_name,updated_date) VALUES (%s,%s)
                        ON CONFLICT ON CONSTRAINT process_monitor_pkey DO UPDATE SET ("updated_date")=(EXCLUDED."updated_date");"""
            values = (Tablename, updated_date)

            cur = con.cursor()
            print values
            cur.execute(moniter_query, values)
            con.commit()
            return "success"


        except (Exception, psycopg2.DatabaseError) as error:
            mail(str(error.args))
            return error.args
#dynamoDb automatically checkes the id if that id is present then it automatically updates that item and if it is not present then it automatically create new item.