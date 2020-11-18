Example of how to use SmartAgent to tail logs:

The included `log/py` example will generate logs- make sure its put in the `/home/ubuntu/pblogs` directory

Add the following monitor stanza to your `/etc/signalfx/agent.yaml`

```
  - type: telegraf/tail
    files:
    - '/home/ubuntu/pblogs/test.log'
    watchMethod: poll
    telegrafParser:         
      dataFormat: "json" 
      JSONTagKeys: 
       - "httpresponsecode"
       - "httpuri"
       - "sourcehost"
      JSONQuery: "obj.message"
      JSONTimeKey: "eventdatetime"
      JSONTimeFormat: "2006-01-02T15:04:05.9Z"
      metricName: "pbdata"
```
