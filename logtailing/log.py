import time
import random
import datetime

outString = {}
outString['out1'] = '{"obj":{"count":1,"message":{"eventdatetime":"2019-07-16T16:15:23.63918","logtype":"SHIM-F5-DATA","loglevel":"info","logsource":"iop-shim-web-kdc-irule-20p-build201 90626v1_HSL", "irulestate":"HTTP_RESPONSE_RELEASE", "sourcesite":"kdc", "sourcehost":"iop-shim-web-pro3.gcs.pitneybowes.com", "httpuri":"/webservice/Transaction.asmx", "localip":"10.53.  160.199","targetsystem":"GCS","partnerid":"","transactionid":"","metric":"shim-ebay-dispense","responsetime":45,"httpresponsecode":"200","soapfault":"","soaperrorcode":"","soaperrordesc ":"","hashkey":"684f9b7ba"}}}\n'
outString['out2'] = '{"obj":{"count":1,"message":{"eventdatetime":"2019-07-16T16:15:24.12124","logtype":"SHIM-F5-DATA","loglevel":"info", "logsource":"iop-shim-web-kdc-irule-20p-build20 190626v1_HSL","irulestate":"HTTP_RESPONSE_RELEASE", "sourcesite":"kdc","sourcehost":"iop-shim-web-pro3.gcs.pitneybowes.com", "httpuri":"/webservice/Error.asmx", "localip":"10.53.160.199 ","targetsystem":"GCS", "partnerid":"","transactionid":"", "metric":"shim-ebay-dispense", "responsetime":12, "httpresponsecode":"400", "soapfault":"", "soaperrorcode":"","soaperrordesc" :"", "hashkey":"684f9b7ba"}}}\n'
outString['out3'] = '{"obj":{"count":1,"message":{"eventdatetime":"2019-07-16T16:15:24.12133","logtype":"SHIM-F5-DATA","loglevel":"info", "logsource":"iop-shim-web-kdc-irule-20p-build20 190626v1_HSL","irulestate":"HTTP_RESPONSE_RELEASE", "sourcesite":"kdc","sourcehost":"iop-shim-web-pro3.gcs.pitneybowes.com", "httpuri":"/webservice/Cart.asmx", "localip":"10.53.160.199" ,"targetsystem":"GCS", "partnerid":"","transactionid":"", "metric":"shim-ebay-dispense", "responsetime":32, "httpresponsecode":"500", "soapfault":"", "soaperrorcode":"","soaperrordesc": "", "hashkey":"684f9b7ba"}}}\n'
outString['out4'] = '{"obj":{"count":1,"message":{"eventdatetime":"2019-07-16T16:15:24.12141","logtype":"SHIM-F5-DATA","loglevel":"info", "logsource":"iop-shim-web-kdc-irule-20p-build20 190626v1_HSL","irulestate":"HTTP_RESPONSE_RELEASE", "sourcesite":"kdc","sourcehost":"iop-shim-web-pro3.gcs.pitneybowes.com", "httpuri":"/webservice/OAuth.asmx", "localip":"10.53.160.199 ","targetsystem":"GCS", "partnerid":"","transactionid":"", "metric":"shim-ebay-dispense", "responsetime":87, "httpresponsecode":"204", "soapfault":"", "soaperrorcode":"","soaperrordesc" :"", "hashkey":"684f9b7ba"}}}\n'


while True:
    with open('test.log',mode='a') as f:
        output = outString['out'+str(random.randint(1,4))]
        d = datetime.datetime.utcnow()
        output2 = output[:46]+d.isoformat("T")+"Z"+output[71:]
        f.write(output2)
    time.sleep(0.1)
